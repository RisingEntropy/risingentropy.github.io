---
title: 【线段树】hyc的序列
date: 2019-05-04 13:42:43 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

sdzx的OIer们都已经熟练掌握了for循环（除了Kinnuch），自然区间求和什么的不在话下

现在有一个长度为n的神奇的数列

要求支持三种操作

1.区间求和

2.单点修改

3.区间取模

这里的区间取模指给定区间左端点l，右端点r，模数 mod ，将区间l到r内所有数取模 mod

输入
第一行 两个整数 n,m表示n个数，m个操作

接下来一行n个数 第i个表示数ai

接下来m行

每一行首先一个数 t

如果t==1 接下来两个数l，r，表示求和区间l到r

t==2 接下来两个数 x，v 表示将ax更改为v

t==3 接下来三个数 l,r,mod 意义同题面

输出
对于t==1的情况，输出区间的和

样例输入
5 5
10 9 8 7 6
1 3 5
3 2 4 4
3 1 5 2
2 4 2
1 1 4
样例输出 
21
3
提示
30% 数据 n<=1000 ， m<=1000，ai<=100

100% 数据 n<=1e5 ， m<=1e5，ai<=1e9

这是一个小铺垫

标签
mogician原创
# 解答
线段树区间取模。维护一个最大值，如果最大值都小于当前取模的值，那么直接不管，否则暴力修改~~(这TM都行?我把自己的做法(维护一个lazytag，如果大于上一次取模，就不管，小于直接暴力改))写炸了~~
```cpp
# include <iostream>
using namespace std;
const int INF = (int)1e9+7;
const int MAXN = (int)1e5+100;
struct node{long long sum,maxx;}tree[MAXN*4];
void pushup(int x){tree[x].sum = tree[x<<1].sum+tree[x<<1|1].sum;tree[x].maxx = max(tree[x<<1].maxx,tree[x<<1|1].maxx);}
int a[MAXN];
void build(int k,int l,int r){
    if(l==r){
        tree[k].sum = tree[k].maxx = a[l];
        return;
    }
    int mid = l+r>>1;
    build(k<<1,l,mid);build(k<<1|1,mid+1,r);
    pushup(k);
}
void modifyAdd(int k,int l,int r,int pos,int v){
    if(l==r){
        tree[k].sum = tree[k].maxx = v;return;
    }
    int mid = l+r>>1;
    if(pos<=mid)modifyAdd(k<<1,l,mid,pos,v);else modifyAdd(k<<1|1,mid+1,r,pos,v);
    pushup(k);
}
void modifyMod(int k,int l,int r,int x,int y,int v){
	if(tree[k].maxx<v)return;
    if(l==r){
    	tree[k].sum%=v; tree[k].maxx = tree[k].sum;
    	return;
    }
    int mid = l+r>>1;
    if(x<=mid)modifyMod(k<<1,l,mid,x,y,v);
    if(y>mid)modifyMod(k<<1|1,mid+1,r,x,y,v);
    pushup(k);
}
long long query(int k,int l,int r,int x,int y){
    if(l>=x&&r<=y){
        return tree[k].sum;
    }
    int mid = l+r>>1;
    long long ret = 0;
    if(x<=mid)ret+=query(k<<1,l,mid,x,y);
    if(y>mid)ret+=query(k<<1|1,mid+1,r,x,y);
    return ret;
}
int n,m;
int main(){
    cin>>n>>m;
    for(int i = 1;i<=n;i++)cin>>a[i];
    build(1,1,n);
    int opt,x,y,mod;
    for(int i = 1;i<=m;i++){
        cin>>opt>>x>>y;
        if(opt==1){
            cout<<query(1,1,n,x,y)<<endl;
        }else if(opt==2){
            modifyAdd(1,1,n,x,y);
        }else{
            cin>>mod;
            modifyMod(1,1,n,x,y,mod);
        }
    }
    return 0;
}
```