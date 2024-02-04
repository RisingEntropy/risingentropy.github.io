---
title: 树链剖分
date: 2018-11-25 10:21:42 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# Introduction
>树链剖分，计算机术语，指一种对树进行划分的算法，它先通过轻重边剖分将树分为多条链，保证每个点属于且只属于一条链，然后再通过数据结构（树状数组、SBT、SPLAY、线段树等）来维护每一条链。                    ----百度百科

# Method
#  1.轻重边剖分
我们把树上的边分成两种：轻边和重边。以任意点为根，然后记size(u)为以u为根的子节点的节点个数，令v为u所有儿子中size值最大的一个儿子，则(u,v)为重边，v称为u的重儿子。u到其余儿子的边为轻边。
轻重边的性质：
1.如果(u,v)是轻边，那么size(v)$\leq$size(u)/2;
2.从根到某一点V的路径上的轻边的个数不多于$O(log\ n)$
3.某条路径称为重路径(链)，当且仅当它全部由重边组成(特殊的，一个点也算作一条重路径)。那么对于每个点到根的路径上都有不超过$O(log\ n)$条轻边和$O(log\ n)$条重路径。
证明参见一本通
画画图~~乱搞搞~~可以发现，一个点在且只在一条重路径上，而每条重路径一定是一条从根节点方向向叶节点方向延伸的深度递增的路径。对树进行轻重边剖分以后，操作所要处理的路径(u,v),我们可以分别处理u,v两个点到最近的公共祖先的路径。根据性质3，路径可以分解成最多$O(log\ n)$条重路径，和$O(log\ n)$条轻边，那么现在我们只考虑如何维护这两种对象。
对于重路径，他们此时相当于一个序列，因此我们只需要用线段树维护。对于轻边，我们可以直接跳过，访问下一条重路径，因为轻边的两端点一定在某条重路径上。这两种操作时间复杂度分别为$O(log^2\ n)$和最多$O(log\ n)$,所以总复杂度为$O(log^2\ n)$
剖分过程可以使用两次dfs实现，有时为了防止递归过深而导致栈溢出，也可以用bfs搞定。
计算一下7个值
father[x]x的父节点
dep[x]x的深度
size[x]x的子节点个数
son[x]x的重儿子，u->son[u]为重边
top[x]x所在重路径的顶部结点
seg[x]x在线段树中的位置
rev[x]线段树中第x个位置对应的树中的结点编号，即rev[seg[x]]=x;
第一遍dfs计算前4各值，第二遍dfs计算后三个。计算seg的时候，同一条路径上的点需要按顺序排在连续的一段位置，也就是一段区间。
[Good blog](http://www.cnblogs.com/chinhhh/p/7965433.html)
# Example
[luoguP3384](https://www.luogu.org/problemnew/show/P3384)
1.处理任意两点间路径上的点权和
2.处理一点及其子树的点权和
3.修改任意两点间路径上的点权
4.修改一点及其子树的点权
1、当我们要处理任意两点间路径时：
设所在链顶端的深度更深的那个点为x点

ans加上x点到x所在链顶端 这一段区间的点权和
把x跳到x所在链顶端的那个点的上面一个点
不停执行这两个步骤，直到两个点处于一条链上，这时再加上此时两个点的区间和即可
2、处理一点及其子树的点权和：
想到记录了每个非叶子节点的子树大小(含它自己)，并且每个子树的新编号都是连续的
于是直接线段树区间查询即可
时间复杂度为$O(\log n)$
代码：
```cpp
# include <cstdio>
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const int MAXN = 1e5+3;
struct edge{
    int t,w,next;
}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int dep[MAXN];
int father[MAXN];
int siz[MAXN];
int son[MAXN];
int tp[MAXN];
int w[MAXN],wei[MAXN];
int id[MAXN],cnt;
int n,m,r,mod;
void dfs1(int x,int fa){
    father[x] = fa;
    dep[x] = dep[fa]+1;
    siz[x] = 1;
    int maxSon = -999;
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(t==fa)continue;
        dfs1(t,x);
        siz[x]+=siz[t];
        if(siz[t]>maxSon)maxSon = siz[t],son[x] = t;
    }
}
void dfs2(int x,int tpp){
    tp[x] = tpp;
    id[x] = ++cnt;
    wei[id[x]] = w[x];
    if(!son[x])return;
    dfs2(son[x],tpp);
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(t==son[x]||t==father[x])continue;
        dfs2(t,t);//每个轻儿子都有一个从自己开始的重链 
    }
}
//---------Segment Tree----------------//
struct node{
    int val,laz;
}tree[MAXN<<2];
void build(int k,int l,int r){
    if(l==r){
        tree[k].val = wei[l];
        return;
    }
    int mid = l+r>>1;
    build(k<<1,l,mid);
    build((k<<1)+1,mid+1,r);
    tree[k].val = tree[k<<1].val+tree[(k<<1)+1].val%mod;
}
inline void add(int k,int l,int r,int v){
	tree[k].val+=v*(r-l+1);
	tree[k].val%=mod;
	tree[k].laz+=v;
	tree[k].laz%=mod;
}
void pushdown(int k,int l,int r){
    int mid = l+r>>1;
	add(k<<1,l,mid,tree[k].laz);
	add(k<<1|1,mid+1,r,tree[k].laz);
	tree[k].laz = 0;
}
void modify(int k,int l,int r,int x,int y,int val){
    if(l>=x&&r<=y){
        tree[k].val += val*(r-l+1);
        tree[k].laz +=val;
        tree[k].val%=mod;
        tree[k].laz%=mod;
		return;
    }
    if(r<x||l>y)return;
    int mid = l+r>>1;
    if(tree[k].laz)pushdown(k,l,r);
    if(x<=mid)modify(k*2,l,mid,x,y,val);
    if(y>mid)modify(k*2+1,mid+1,r,x,y,val);
    tree[k].val = tree[k<<1].val+tree[k<<1|1].val%mod;
}
int query(int k,int l,int r,int x,int y){
    if(l>=x&&r<=y){
        return tree[k].val;
    }
    if(l>y||r<x)return 0;
    if(tree[k].laz)pushdown(k,l,r);
    int mid = l+r>>1;
    int ans = 0;
    if(x<=mid)ans+=query(k<<1,l,mid,x,y);
    if(y>mid)ans+=query(k<<1|1,mid+1,r,x,y);
    ans%=mod;
    return ans;
}
void rModify(int x,int y,int k){
    k%=mod;
    while(tp[x]!=tp[y]){
        if(dep[tp[x]]<dep[tp[y]])swap(x,y);
        modify(1,1,n,id[tp[x]],id[x],k);
        x = father[tp[x]];
    }
    if(dep[x]>dep[y])swap(x,y);
    modify(1,1,n,id[x],id[y],k);
}
int queryRange(int x,int y){
    int ans = 0;
    while(tp[x]!=tp[y]){
        if(dep[tp[x]]<dep[tp[y]])swap(x,y);
        ans+=query(1,1,n,id[tp[x]],id[x]);
        ans%=mod;
        x = father[tp[x]];
    }
    if(dep[x]>dep[y])swap(x,y);
    ans+=query(1,1,n,id[x],id[y]);
    ans%=mod;
    return ans;
}
int querySon(int x){
    return query(1,1,n,id[x],id[x]+siz[x]-1);
}
void updateSon(int x,int k){
    modify(1,1,n,id[x],id[x]+siz[x]-1,k);
}
//------------------------/{/
int main(void){
    n = read(),m = read(),r = read(),mod = read();
    for(int i = 1;i<=n;i++){
        w[i] = read();
    }
    int f,t;
    for(int i = 1;i<n;i++){
        f = read(),t = read();
        add(f,t,1);
        add(t,f,1);
    }
    dep[r] = 1;
    dfs1(r,0);
    dfs2(r,r);
    build(1,1,n);
    while(m--){
        int k,x,y,z;
        k = read();
        if(k==1){
            x = read(),y = read(),z = read();
            rModify(x,y,z);
        }
        if(k==2){
            x = read(),y = read();
            printf("%d\n",queryRange(x,y));
        }
        if(k==3){
            x = read(),z = read();
            updateSon(x,z);
        }
        if(k==4){
            x = read();
            printf("%d\n",querySon(x));
        }
    }
    return 0;
}
```
总而言之，树链剖分就是通过把树砍了，做成区间问题。再用区间问题数据结构维护