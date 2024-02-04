---
title: woj3784 【模板】树链剖分换根
date: 2019-03-18 15:30:49 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给定一棵大小为 n 的有根点权树,支持以下操作:
• 换根
• 修改点权
• 查询子树最小值
# 输入
第一行两个整数 n, Q ,分别表示树的大小和操作数。接下来n行,每行两个整数f,v,第i+1行的两个数表示点i的父亲和点i的权。保证f < i。如 果f = 0,那么i为根。输入数据保证只有i = 1时,f = 0。接下来 m 行,为以下格式中的一种:
• V x y表示把点x的权改为y
• E x 表示把有根树的根改为点 x
• Q x 表示查询点 x 的子树最小值
# 输出
对于每个 Q ,输出子树最小值。
样例输入
```
3 7
0 1
1 2
1 3
Q 1
V 1 6
Q 1
V 2 5
Q 1
V 3 4
Q 1
```
样例输出
```
1
2
3
4
```
提示
对于 100% 的数据:n, Q ≤ 10^5。
# 解答
树链剖分的板子题。
换了根对原树的形态没有影响，所以可以按照1为根进行剖分。然后记录当前的根。
对于修改，直接线段树单点就行了
对于换根记录就行了。
对于查询，就比较麻烦了。考虑下面三种情况(记当前的根为root,查询的点为x)
如果x是root的子树，那么显然直接查询就可以了
如果x==root，直接查询整个子树
如果x是root的祖先，那么就找出x到root路径上的**最靠近**x的点y，查询整棵树中除了y的子树的其他树就好了，图解：
过几天再来补
代码：快读有问题，这份代码过不了，过几天去更新可以过的代码
```cpp
//
// Created by dhy on 19-3-17.
//
# include<bits/stdc++.h>
using namespace std;
struct IO
{
    streambuf *ib,*ob;
    int buf[50];
    inline void init()
    {
        ios::sync_with_stdio(false);
        cin.tie(NULL);cout.tie(NULL);
        ib=cin.rdbuf();ob=cout.rdbuf();
    }
    inline int read()
    {
        char ch=ib->sbumpc();int i=0,f=1;
        while(!isdigit(ch)){if(ch=='-')f=-1;ch=ib->sbumpc();}
        while(isdigit(ch)){i=(i<<1)+(i<<3)+ch-'0';ch=ib->sbumpc();}
        return i*f;
    }
    inline void W(int x)
    {
        if(!x){ob->sputc('0');return;}
        if(x<0){ob->sputc('-');x=-x;}
        while(x){buf[++buf[0]]=x%10,x/=10;}
        while(buf[0])ob->sputc(buf[buf[0]--]+'0');
    }
}io;
const int MAXN = 100010;
const int INF = 0x3f3f3f3f;
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
int w[MAXN];//former weight
int a[MAXN];
int root;
class SegmentTree{
private:
    struct node{int max,sum;}tree[MAXN<<2];
public:
    void build(int k,int l,int r){
        if(l==r){tree[k].sum = tree[k].max = a[l];return;}
        int mid = l+r>>1;
        build(k<<1,l,mid);build(k<<1|1,mid+1,r);
        tree[k].max = min(tree[k<<1].max,tree[k<<1|1].max);
        tree[k].sum = tree[k<<1].sum+tree[k<<1|1].sum;
    }
    void modify(int k,int l,int r,int pos,int v){
        if(l==r){
            tree[k].sum = tree[k].max = v;return;
        }
        int mid = l+r>>1;
        if(pos<=mid)modify(k<<1,l,mid,pos,v);
        else modify(k<<1|1,mid+1,r,pos,v);
        tree[k].max = min(tree[k<<1].max,tree[k<<1|1].max);
        tree[k].sum = tree[k<<1].sum+tree[k<<1|1].sum;
    }
    int querySum(int k,int l,int r,int x,int y){
        if(l>=x&&r<=y)return tree[k].sum;
        if(x>r||y<l)return 0;
        int mid = l+r>>1;
        int ret = 0;
        if(x<=mid)ret+=querySum(k<<1,l,mid,x,y);
        if(y>mid)ret+=querySum(k<<1|1,mid+1,r,x,y);
        return ret;
    }
    int queryMin(int k,int l,int r,int x,int y){
        if(l>=x&&r<=y)return tree[k].max;
        if(x>r||y<l)return INF;
        int mid = l+r>>1;
        int ret = INF;
        if(x<=mid)ret = min(ret,queryMin(k<<1,l,mid,x,y));
        if(y>mid)ret = min(ret,queryMin(k<<1|1,mid+1,r,x,y));
        return ret;
    }
};
SegmentTree segmentTree;
int father[MAXN],track[MAXN],dep[MAXN],size[MAXN];
int dfn,id[MAXN],heavyson[MAXN];
void dfs1(int x,int fa){
    dep[x] = dep[fa]+1;
    size[x] = 1;
    father[x] = fa;
    int sonSize = 0;
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(t==fa)continue;
        dfs1(t,x);
        size[x]+=size[t];
        if(size[t]>sonSize)sonSize = size[t],heavyson[x] = t;
    }
}
void dfs2(int x,int tpp){
    track[x] = tpp;
    id[x] = ++dfn;
    a[id[x]] = w[x];
    if(!heavyson[x])return;
    dfs2(heavyson[x],tpp);
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(t==father[x]||t==heavyson[x])continue;
        dfs2(t,t);
    }
}
int lca(int x,int y){
    while(track[x]!=track[y]){
        if(dep[track[x]]<dep[track[y]])swap(x,y);
        x = father[track[x]];
    }
    return dep[x]<dep[y]?x:y;
}
int find(int x,int y){
	while(track[x]!=track[y]){//保证最后调到一条重链上
		if(dep[x]<dep[y])swap(x,y);
		if(father[track[x]]==y)return track[x];
		x = father[track[x]];
	}
	if(dep[x]<dep[y])swap(x,y);
	return heavyson[y];返回深度更小的点的重儿子，因为都在一条重链上了
}
int main(){
	io.init();
    int n,Q;n = io.read(),Q = io.read();
    int f,t;
    for(int i = 1;i<=n;i++){
        f = io.read(),t = io.read();
        if(f!=0){
            add(f,i,1);
            w[i] = t;
        }else{
            root = i;w[i] = t;
        }
    }
    dfs1(root,root);dfs2(root,root);
    segmentTree.build(1,1,dfn);
    char opt[5];int x,y;
    while(Q--){
        scanf("%s",opt);
        if(opt[0]=='Q'){
            x = io.read();
            int LCA = lca(x,root);
            if(x==root)printf("%d\n",segmentTree.queryMin(1,1,dfn,1,dfn));
            else if(LCA!=x){
                printf("%d\n",segmentTree.queryMin(1,1,dfn,id[x],id[x]+size[x]-1));
            }else{//这里有问题，要找出x到root的路径中，最靠近x的那个点y再扣掉y的子树
            	int p = find(x,root);
                printf("%d\n",min(segmentTree.queryMin(1,1,dfn,1,id[p]-1),segmentTree.queryMin(1,1,dfn,id[p]+size[p],dfn)));
            }
        }else if(opt[0]=='E')root = io.read();
        else{
            x = io.read(),y = io.read();
            segmentTree.modify(1,1,dfn,id[x],y);
        }
    }
    return 0;
}
```