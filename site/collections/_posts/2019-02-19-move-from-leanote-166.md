---
title: DFS序
date: 2019-02-19 09:34:38 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# DFS序
dfs序比较重要的性质：一棵子树的所有节点在dfs序里是连续一段，主要就是利用这个性质来解题。
跑出dfs序，然后数据结构维护
# 经典问题
#  T1单点修改，子树查询
对某个点X权值加上一个数W，查询某个子树X里所有点权值和
解：列出dfs序，实现修改一个数，查询一段序列的和，显然这个序列可以用树状数组维护。
代码:
```cpp
# include <iostream>
using namespace std;
const int MAXN = 100010;
struct edge{int t,w,next;}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int tot;int dfn;
int a[MAXN];int st[MAXN];int ed[MAXN];
inline int lowbit(int x){return x&-x;}
void modify(int x,int v){
	while(x<=tot){
		a[x]+=v;
		x+=lowbit(x);
	}
}
int query(int x){int ans = 0;while(x>=1){ans+=a[x];x-=lowbit(x);}return ans;}
bool vis[MAXN];
void dfs(int x){
	vis[x] = true;
	st[x] = ++dfn;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		dfs(t);
	}
	ed[x] = dfn;
}
int main(){
	ios::sync_with_stdio(false);
	int n;cin>>n;
	int f,t;
	for(int i = 1;i<n;i++){cin>>f>>t;add(f,t,1),add(t,f,1);}
	int Q;cin>>Q;
	dfs(1);tot = dfn;
	char op;int x;
	for(int i = 1;i<=n;i++)
		modify(i,1);
	while(Q--){
		cin>>op>>x;
		if(op=='Q'){
			cout<<query(ed[x])-query(st[x]-1)<<endl;
		}else{
			if(query(st[x])-query(st[x]-1)==1)modify(st[x],-1);else modify(st[x],1);
		}
	}
}
```
#  T2树上路径修改，单点查询
• 对X到Y的最短路上所有点权值加上一个数W，查询某个点的权值。
对x—》y的路径修改等价于：

 - x->root 加v
 - y->root 加v
 - lca(x,y) -v
 - fa[lca(x,y)] -v
 

为什么呢？因为是统计x到y的最短路加v，lca(x,y)也在路径上，所以需要加v，但是因为x和y分别到root 的时候，都加了个v，lca被加了2次，所以需要减一次，而fa[lca(x,y)]不在路径上，所以需要减一次(前面lca(x,y))已经减了一次了。然后求lca，在树状数组维护就行了。这种问题，要把它分成几个问题来理解。树状数组是实现单点查询/修改的，其他是满足修改的方法的，不要绞一起来思考。
```cpp
# include <cstdio>
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
# define in read()
const int MAXN = 100010;
struct edge{int t,w,next;}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
inline int swap(int &x,int &y){x = x^y;y = y ^x;x = x^y;}
int fa[MAXN][20];
int dep[MAXN];
int st[MAXN],ed[MAXN];
bool vis[MAXN];
int a[MAXN];
int n;
int dfn;
inline int lowbit(int x){return x&-x;}
int query(int x){
	int ans = 0;
	while(x>0){ans+=a[x];x-=lowbit(x);}
	return ans;
}
int modify(int x,int v){
	while(x<=n){
		a[x]+=v;
		x+=lowbit(x);
	}
}
void dfs(int x,int f){
	vis[x] = true;
	fa[x][0] = f;
	dep[x] = dep[f]+1;
	st[x] = ++dfn;
	for(int i = 1;i<=19;i++)fa[x][i] = fa[fa[x][i-1]][i-1];
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		dfs(t,x);
	}
	ed[x] = dfn;
}
int lca(int x,int y){
	if(dep[x]<dep[y])swap(x,y);
	for(int i = 19;i>=0;i--)if(dep[fa[x][i]]>=dep[y])x = fa[x][i];
	if(x==y)return x;
	for(int i = 19;i>=0;i--){
		if(fa[x][i]!=fa[y][i]){
			x = fa[x][i],y = fa[y][i];
		}
	}
	return fa[x][0];
}
int main(){
	n = read();
	int f,t;
	for(int i = 1;i<n;i++){
		f  = in;t =in;add(f,t,1);add(t,f,1);
	}
	int Q;Q = in;
	int op,x,y,v;
	dfs(1,0);
	while(Q--){
		op = in;
		if(op==1){
			x = in;y = in;v= in;
			int lc = lca(x,y);
			modify(st[x],v);modify(st[y],v);
			modify(st[lc],-v);
			if(lc!=1)modify(st[fa[lc][0]],-v);
		}else{
			x = in;
			printf("%d \n",query(ed[x])-query(st[x]-1));
		}
	}
	return 0;
}
```
# T3树上路径修改，子树查询2231
从X到Y的点加上或者减去一个W，求某个点子树内的所有点的权值和.
解答：我们考虑对于每个修改的影响，如果x是y的子树，那么对y这棵树的影响是$w(x)*(dep[x]-dep[y]+1)$，那么我们把它拆开$w(x)*(dep[x]+1]-dep[y]*w(x))$，然后考虑T2的差分的做法，那么我们直接维护到根，然后减去(lca到根+lca的父节点到根)就行了(参见T2的理解或者做一下T4)。两个树状数组维护$w(x)$和$w(x)*(dep[x]-1)$就行了。代码如下：
```cpp
# include <bits/stdc++.h>
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
struct edge{int t,w,next;}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int fa[MAXN][20];
int dep[MAXN];
int st[MAXN],ed[MAXN];
bool vis[MAXN];
int a[MAXN];
int n;
int dfn;
inline int lowbit(int x){return x&-x;}
class tree{//I LOVE OOP
private:
	int a[MAXN];
public:
	int query(int x){
		int ans = 0;
		while(x>0){ans+=a[x];x-=lowbit(x);}
		return ans;
	}
	int modify(int x,int v){
		while(x<=n){
			a[x]+=v;
			x+=lowbit(x);
		}
	}
};
void dfs(int x,int f){
	vis[x] = true;
	fa[x][0] = f;
	dep[x] = dep[f]+1;
	st[x] = ++dfn;
	for(int i = 1;i<=19;i++)fa[x][i] = fa[fa[x][i-1]][i-1];
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		dfs(t,x);
	}
	ed[x] = dfn;
}
int lca(int x,int y){
	if(dep[x]<dep[y])swap(x,y);
	int delta = dep[x]-dep[y];
	for(int i = 19;i>=0;i--)if(dep[fa[x][i]]>=dep[y])x = fa[x][i];
	if(x==y)return x;
	for(int i = 19;i>=0;i--){
		if(fa[x][i]!=fa[y][i]){
			x = fa[x][i],y = fa[y][i];
		}
	}
	return fa[x][0];
}
tree t1,t2;
int main(){
	io.init();
	n = io.read();
	int f,t;
	for(int i = 1;i<n;i++){
		f = io.read(),t = io.read();add(f,t,1);add(t,f,1);
	}
	int Q;Q = io.read();
	int op,x,y,z;
	dfs(1,0);
	while(Q--){
		op = io.read();
		if(op==1){
			x = io.read(),y = io.read(), z = io.read();
			int lc = lca(x,y);
			t1.modify(st[x],z);
			t1.modify(st[y],z);
			t2.modify(st[x],z*(dep[x]+1));
			t2.modify(st[y],z*(dep[y]+1));
			t1.modify(st[lc],-z);
			t2.modify(st[lc],-z*(dep[lc]+1));
			if(lc!=1){
				t1.modify(st[fa[lc][0]],-z);
				t2.modify(st[fa[lc][0]],-z*(dep[fa[lc][0]]+1));
			}
		}else{
			x = io.read();
			printf("%d\n",t2.query(ed[x])-t2.query(st[x]-1)-dep[x]*(t1.query(ed[x])-t1.query(st[x]-1)));
		}
	}
	return 0;
}
```
# T4单点修改，路径询问2232
最简单的一个问题，直接x到根+y到根-lca到根-lca的父节点到根的点权和就完事了。树状数组超级好维护
```cpp
# include <bits/stdc++.h>
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
struct edge{int t,w,next;}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int fa[MAXN][20];
int dep[MAXN];
int st[MAXN],ed[MAXN];
bool vis[MAXN];
int a[MAXN];
int n;
int dfn;
inline int lowbit(int x){return x&-x;}
class tree{//I LOVE OOP
private:
	int a[MAXN];
public:
	int query(int x){
		int ans = 0;
		while(x>0){ans+=a[x];x-=lowbit(x);}
		return ans;
	}
	int modify(int x,int v){
		while(x<=n){
			a[x]+=v;
			x+=lowbit(x);
		}
	}
};
void dfs(int x,int f){
	vis[x] = true;
	fa[x][0] = f;
	dep[x] = dep[f]+1;
	st[x] = ++dfn;
	for(int i = 1;i<=19;i++)fa[x][i] = fa[fa[x][i-1]][i-1];
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		dfs(t,x);
	}
	ed[x] = dfn;
}
int lca(int x,int y){
	if(dep[x]<dep[y])swap(x,y);
	int delta = dep[x]-dep[y];
	for(int i = 19;i>=0;i--)if(dep[fa[x][i]]>=dep[y])x = fa[x][i];
	if(x==y)return x;
	for(int i = 19;i>=0;i--){
		if(fa[x][i]!=fa[y][i]){
			x = fa[x][i],y = fa[y][i];
		}
	}
	return fa[x][0];
}
tree t1;
int wei[MAXN];
int main(){
	io.init();
	n = io.read();
	int f,t;
	for(int i = 1;i<=n;i++)wei[i] = io.read();
	for(int i = 1;i<n;i++){
		f = io.read(),t = io.read();add(f,t,1);add(t,f,1);
	}
	int Q;Q = io.read();
	int op,x,y,z;
	dfs(1,0);
	for(int i = 1;i<=n;i++)t1.modify(st[i],wei[i]),t1.modify(ed[i]+1,-wei[i]);
	while(Q--){
		op = io.read();
		if(op==1){
			x = io.read();z = io.read();
			t1.modify(st[x],z);t1.modify(ed[x]+1,-z);
		}else{
			x = io.read();y = io.read();
			int lc = lca(x,y);
			int ans = t1.query(st[x])+t1.query(st[y])-t1.query(st[fa[lc][0]]) - t1.query(st[lc]);
			printf("%d\n",ans);
		}
	}
	return 0;
}
```
# T5T6T7
更简单了，不过涉及到一些树状数组不好维护的东西~~超级树状数组~~，就直接换线段树，或者其他数据结构就完事了。
题型五：子树修改，单点查询
问题六：子树修改，子树查询
问题七：子树修改，路径查询