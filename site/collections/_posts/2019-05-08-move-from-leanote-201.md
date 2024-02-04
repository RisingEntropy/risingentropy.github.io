---
title: 【李超线段树】[JSOI2008]Blue Mary开公司 
date: 2019-05-08 17:03:33 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

[传送门](https://www.luogu.org/problemnew/show/P4254)
# 解答
抄自：http://www.cnblogs.com/NLDQY/p/10147594.html
李超线段树板子题。
什么是李超线段树呢？
李超线段树是用来解决二维直角坐标系上给定直线求最值的一类题目的线段树
这一类题目往往很难像传统线段树一样下传lazy_tag，所以就需要用到标记永久化
**标记永久化**作为预备知识，就不在此多做赘述了
说白了就是把函数的编号作为标记打上去。
然后注意一下修改：
若新插入的函数斜率比tag所记录的函数斜率更大
1.若新函数在mid上的y值也大于tag，那我们就可以直接把tag覆盖为新的函数，再用**原tag**去更新左区间。因为原tag对于右区间肯定是不会有贡献了的，但对于左区间却不一定，所以我们需要再次去进行更新，而原区间tag直接被覆盖，右区间则继续用新函数去尝试更新
图解：此处输入图片的描述
2.若新函数在mid上的y值小于tag，则再尝试用新函数去更新右区间，左区间就不用管了。
因为新函数在mid上已经比tag要小，则新函数对于左区间肯定不会再有贡献，而对于右区间却可能有贡献，所以还要再往右更新，基本原理跟之前差不多，就不再给出图解

若新插入的函数斜率比tag所记录的函数斜率更小
1.若新函数在mid上的值大于tag，我们就覆盖原tag，同时用原tag去更新右区间。由于斜率比原tag要小，则这种情况下，**原tag**对于左区间肯定是不会有贡献的，但对右区间却不一定,所以还需要去尝试更新右区间。
2.若原区间在mid的值小于tag，则在用新函数去尝试更新左区间，原理和以上大同小异
不知道怎么回事，我自己的代码总是WA，所以抄了别人的代码：
```cpp
# include<bits/stdc++.h>
# define N 1000020
using namespace std;
typedef double dl;
int n,t=1;
struct sgt_tag{
    # define ls q<<1
    # define rs q<<1|1
    int tot,tag[N*4];
    struct function{dl k,b;}fun[N*4];
    inline dl val(int x,int id){return fun[id].k*(x-1)+fun[id].b;}//因为起始点是1所以x要-1
    inline void ins(dl k,dl b){fun[++tot].k=k;fun[tot].b=b;change(1,1,N,tot);}
    inline void change(int q,int l,int r,int id){
        if(l==r){
            if(val(l,id)>val(l,tag[q]))tag[q]=id;
            return ;
        }
        int mid=(l+r)>>1;
        if(fun[id].k>fun[tag[q]].k){
            if(val(mid,id)>val(mid,tag[q]))change(ls,l,mid,tag[q]),tag[q]=id;
            else change(rs,mid+1,r,id);
        }else{
            if(val(mid,id)>val(mid,tag[q]))change(rs,mid+1,r,tag[q]),tag[q]=id;
            else change(ls,l,mid,id);
        }
    }
    inline dl query(int q,int l,int r,int x){
        if(l==r)return val(l,tag[q]);
        int mid=(l+r)>>1;dl ans=val(x,tag[q]);
        if(x<=mid)ans=max(ans,query(ls,l,mid,x));
        else ans=max(ans,query(rs,mid+1,r,x));
        return ans;
    }
}T;
inline int read(){
    int x=0,f=1;char ch=getchar();
    while(!isdigit(ch)){if(ch=='-')f=-f;ch=getchar();}
    while(isdigit(ch)){x=x*10+ch-48;ch=getchar();}
    return x*f;
}
int main(){
    n=read();
    begin:if(t>n)goto end;t++;
    char ch[10];scanf("%s",ch);
    if(ch[0]=='P'){dl k,b;scanf("%lf%lf",&b,&k);T.ins(k,b);}
    if(ch[0]=='Q'){int x=read();dl ans=T.query(1,1,N,x);printf("%d\n",(int)ans/100);}
    goto begin;
    end:return 0;
}
```
我自己的大暴力。维护区间最小值，如果当前函数最大值小于最小值，直接不管，否则向下更新~~测评机快的话可以过~~
```cpp
# include <cstdio>
# include <iostream>
using namespace std;
const int MAXT = 50010;
const int T = 50000;
struct node{double mn,mx;}tree[MAXT<<2];
void pushup(int k){tree[k].mn = min(tree[k<<1].mn,tree[k<<1|1].mn);tree[k].mx = max(tree[k<<1].mx,tree[k<<1|1].mx);}
void modify(int k,int l,int r,double first,double p){
    if(l==r){	
        tree[k].mn = tree[k].mx = max(tree[k].mx,first+p*double(r-1));
        return;
    }
    if(tree[k].mn>first+p*double(r-1))return;
    int mid = l+r>>1;
    modify(k<<1,l,mid,first,p);modify(k<<1|1,mid+1,r,first,p);
    pushup(k);
}
double query(int k,int l,int r,int pos){
    if(l==r){return tree[k].mx;}
    int mid = l+r>>1;
    if(pos<=mid)return query(k<<1,l,mid,pos);
    else return query(k<<1|1,mid+1,r,pos);
}
int main(){
    int n;scanf("%d",&n);
    char c[20];
    double S,P;
    int D;
    while(n--){
        scanf("%s",c);
        if(c[0]=='P'){
            scanf("%lf%lf",&S,&P);
            modify(1,1,T,S,P);
        }else{
            scanf("%d",&D);
            printf("%d\n",((int)(query(1,1,T,D)))/100);
        }
    }
}
```