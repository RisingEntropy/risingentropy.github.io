---
title: 【lct】【国家集训队】 tree II
date: 2019-04-21 16:00:41 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

#  题面
一棵n个点的树，每个点的初始权值为1。对于这棵树有q个操作，每个操作为以下四种操作之一：

+ u v c：将u到v的路径上的点的权值都加上自然数c；

- u1 v1 u2 v2：将树中原有的边(u1,v1)删除，加入一条新边(u2,v2)，保证操作完之后仍然是一棵树；

\* u v c：将u到v的路径上的点的权值都乘上自然数c；

/ u v：询问u到v的路径上的点的权值和，求出答案对于51061的余数。

输入输出格式
输入格式：
第一行两个整数n，q

接下来n-1行每行两个正整数u，v，描述这棵树

接下来q行，每行描述一个操作

输出格式：
对于每个/对应的答案输出一行

输入输出样例
输入样例# 1： 
3 2
1 2
2 3
* 1 3 4
/ 1 1
输出样例# 1： 
4
说明
10%的数据保证，1<=n，q<=2000

另外15%的数据保证，1<=n，q<=5*10^4，没有-操作，并且初始树为一条链

另外35%的数据保证，1<=n，q<=5*10^4，没有-操作

100%的数据保证，1<=n，q<=10^5，0<=c<=10^4
#  解答
lct板子题。就是打标记~~不就是打标记嘛，我就是打不出来。。。。~~注意，因为乘法优先级高于加法，所有先处理乘法标记，处理加法，这样才不会因为加法标记而影响乘法。
```cpp
# include <iostream>
# include <cstdio>
# define YL 51061
# define lc c[x][0]
# define rc c[x][1]
# define mul(x) x*=c;x%=YL
# define add(x,c) x+=c;x%=YL
using namespace std;
const int MAXN = 100010;
const long long mod = 51061;
long long tree[MAXN][2],sze[MAXN],sum[MAXN],tag[MAXN],add[MAXN],mul[MAXN],fa[MAXN],val[MAXN];
int top,stk[MAXN];
bool isroot(int x){return !fa[x]||(x!=tree[fa[x]][1]&&x!=tree[fa[x]][0]);}
int which(int x){return tree[fa[x]][1]==x;}
void pushup(int x){sum[x]=sum[tree[x][1]]+sum[tree[x][0]]+val[x]%mod;sze[x]=sze[tree[x][1]]+sze[tree[x][0]]+1;}

void pushdownadd(int x,long long v){
    sum[x] = sum[x]+sze[x]*v%mod;
    val[x] = val[x]+v%mod;
    add[x] = add[x]+v%mod;
}
void pushdownmul(int x,long long v){
    sum[x] = sum[x]*v%mod;
    val[x] = val[x]*v%mod;
    mul[x] = mul[x]*v%mod;
    add[x] = add[x]*v%mod;
}
void pushdown(int x){
    if(mul[x]!=1)pushdownmul(tree[x][1],mul[x]),pushdownmul(tree[x][0],mul[x]),mul[x] = 1ll;
    if(add[x])pushdownadd(tree[x][1],add[x]),pushdownadd(tree[x][0],add[x]),add[x] = 0;
    if(tag[x]){
        swap(tree[x][1],tree[x][0]);
        tag[tree[x][0]]^=1;tag[tree[x][1]]^=1;
        tag[x] = 0;
    }
}
void rotate(int x){
    int y = fa[x],z = fa[y],d = which(x),w = tree[x][d^1];
    if(!isroot(y))tree[z][which(y)] = x;
    fa[x] = z;fa[y] = x;
    tree[y][d] = w;
    tree[x][d^1] = y;fa[w] = y;
    pushup(y);pushup(x);
}
 void splay(int x){
     top = 0;stk[++top] = x;
     for(int y = x;!isroot(y);y = fa[y])stk[++top] = fa[y];
     while(top)pushdown(stk[top--]);
     while(!isroot(x)){
        int y = fa[x];
        if(!isroot(y)){
            if(which(x)==which(y))rotate(y);else rotate(x);
        }
        rotate(x);
     }
     pushup(x);
 }
 void access(int x){
     for(int y = 0;x;y = x,x = fa[x]){
         splay(x);tree[x][1] = y;pushup(x);
     }
 }
 void makeroot(int x){
     access(x);splay(x);tag[x]^=1;
 }
 int find(int x){
     access(x);splay(x);
     while(tree[x][0])pushdown(x),x = tree[x][0];
     splay(x);return x;
 }
 void split(int x,int y){
     makeroot(x);access(y);splay(y);
 }
 void link(int x,int y){
     makeroot(x);fa[x] = y;
 }
 void cut(int x,int y){
     if(find(x)!=find(y))return;
     split(x,y);
     if(fa[x]!=y||tree[x][1])return;
     tree[y][0] = fa[x] = 0;pushup(y);
 }
 int main(){
     int n,q;cin>>n>>q;
     int f,t;
    for(int i = 1;i<=n;i++)val[i] = sum[i] = mul[i] = 1;
     for(int i = 1;i<n;i++){
        cin>>f>>t;
        link(f,t);
     }
     char c[5];
     long long op,u1,u2,u3,u4;
     for(int i = 1;i<=q;i++){
        scanf("%s",c);
        if(c[0]=='+'){
            cin>>u1>>u2>>u3;
            u3%=mod;
            split(u1,u2);pushdownadd(u2,u3);
        }else if(c[0]=='-'){
            cin>>u1>>u2>>u3>>u4;
            cut(u1,u2);link(u3,u4);
        }else if(c[0]=='*'){
            cin>>u1>>u2>>u3;
            u3%=mod;
            split(u1,u2);pushdownmul(u2,u3);
        }else if(c[0]=='/'){
            cin>>u1>>u2;
            split(u1,u2);
            cout<<sum[u2]%mod<<endl;
        }
     }
     return 0;
 }
```
就是我现在还不知道为什么link的时候pushup就挂了，不pushup就切了