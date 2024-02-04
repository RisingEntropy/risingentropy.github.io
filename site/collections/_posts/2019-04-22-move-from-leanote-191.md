---
title: Link-cut tree
date: 2019-04-22 15:05:39 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# link-cut tree
其实就是类似于树链剖分的思想，有类似于`preferred edge`,支持的操作如下

 1. access(x)，把x到根的路径设置为重链
 2. makeroot(x),通过类似于[文艺平衡树]的方法，把树翻转，从而把x变成树的根
 3. linke(x,y)x和y连接一条边
 4. cut(x,y)把x和y的连边剪断
 5. find(x)找出x所在的长链的根
 
其实就是通过多棵splay树来维护不同的重链：
板子：
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
const int MAXN = 3e5+100;
int tree[MAXN][2],fa[MAXN],sum[MAXN],val[MAXN],tag[MAXN];
int top,stk[MAXN];
int which(int x){return tree[fa[x]][1]==x;}
int read(){
	int x= 0,f = 1;
	char c = getchar();
	while(c<'0'||c>'9'){
		if(c=='-')f = -1;
		c = getchar();
	}
	while(c>='0'&&c<='9'){
		x = (x<<1)+(x<<3)+(c^48);
		c = getchar();
	}
	return x*f;
}
void pushdown(int x){
	if(!tag[x])return ;
	swap(tree[x][0],tree[x][1]);
	tag[tree[x][0]]^=1;
	tag[tree[x][1]]^=1;
	tag[x] = 0;
}
void pushup(int x){sum[x] = sum[tree[x][0]]^sum[tree[x][1]]^val[x];}
bool isroot(int x){return !fa[x]||(x!=tree[fa[x]][0]&&x!=tree[fa[x]][1]);}
void rotate(int x){
	int y = fa[x],z = fa[y],d = which(x);
	if(!isroot(y))tree[z][which(y)] = x;
	fa[x] = z;fa[y] = x;tree[y][d] = tree[x][d^1];
	tree[x][d^1] = y;fa[tree[y][d]] = y;
	pushup(y),pushup(x);
}
void splay(int x){
	top = 0;stk[++top] = x;
	for(int i = x;!isroot(i);i = fa[i])stk[++top] = fa[i];
	while(top)pushdown(stk[top--]);
	for(int y = fa[x];!isroot(x);rotate(x),y = fa[x]){
		if(!isroot(y))rotate(which(x)==which(y)?y:x);
	}
}
void access(int x){
	for(int y = 0;x;y = x,x = fa[x]){
		splay(x),tree[x][1] = y,pushup(x);
	}
}
void makeroot(int x){access(x),splay(x);tag[x]^=1;}
int find(int x){
	access(x);splay(x);
	while(tree[x][0])pushdown(x),x = tree[x][0];
	splay(x);return x;
}
void split(int x,int y){
	makeroot(x);access(y);splay(y);
}
void link(int x,int y){
	makeroot(x);fa[x] = y;pushup(y);
}
void cut(int x,int y){
	if(find(x)!=find(y))return ;
	split(x,y);
	if(fa[x]!=y||tree[x][1])return ;
	tree[y][0] = fa[x] = 0;pushup(y);
}
int query(int x,int y){
	split(x,y);return sum[y];
}
int n,m;
int main(){
	ios::sync_with_stdio(false);
	n = read(),m = read();
	for(int i = 1;i<=n;i++)val[i] = read();
	for(int i = 1;i<=m;i++){
		int op,x,y;op = read(),x = read(),y = read();
		if(op==0){
			printf("%d\n",query(x,y));
		}else if(op==1){
			if(find(x)!=find(y))link(x,y);
		}else if(op ==2){
			cut(x,y);
		}else{
			access(x);splay(x);val[x] = y;pushup(x);
		}
	}
	return 0;
}
```