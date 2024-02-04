---
title: Splay
date: 2019-02-18 13:48:53 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# Splay
~~Splay可牛逼了，可以处理区间问题~~
splay说白了就是转着玩。每个点轮流转到根节点
文艺平衡树
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
const int MAXN = 100010;
int a[MAXN];
int root;
inline void swap(int &x,int &y){x = x^y;y = y^x;x = x^y;}
int tree[MAXN][2];int sze[MAXN];int cnt[MAXN];
int val[MAXN];int lzy[MAXN];int tot;int fa[MAXN];
int n;
inline void pushup(int x){sze[x] = sze[tree[x][0]]+sze[tree[x][1]]+cnt[x];}
int which(int x){return tree[fa[x]][1]==x;}
void rotate(int x){
	int y = fa[x];int z = fa[y],d = which(x),w = tree[x][d^1];
	tree[y][d] = w;fa[w] = y;
	tree[z][which(y)] = x;fa[x] = z;
	tree[x][d^1] = y;fa[y] = x;
	pushup(y);pushup(x);
}
void splay(int x,int tar = 0){
	while(fa[x]!=tar){
		int y = fa[x];int z = fa[y];
		if(z!=tar){
			if(which(x)==which(y))rotate(y);
			else rotate(x);
		}
		rotate(x);
	}
	if(!tar)root = x;
}
void pushdown(int x){
	if(lzy[x]){
		swap(tree[x][1],tree[x][0]);
		lzy[tree[x][0]]^= 1;lzy[tree[x][1]]^=1;
		lzy[x] = 0;
	}
}
int kth(int rank){
	int curr = root;
	while(1){
		pushdown(curr);
		if(tree[curr][0]&&rank<=sze[tree[curr][0]]){
			curr = tree[curr][0];
		}else if(rank>sze[tree[curr][0]]+cnt[curr]){
			rank-=sze[tree[curr][0]]+cnt[curr];
			curr = tree[curr][1];
		}else return curr;
	}
}
void insert(int x){
	int curr = root;int p = 0;
	while(curr&&val[curr]!=x){
		if(x>val[curr])p = curr,curr = tree[curr][1];else p = curr,curr = tree[curr][0];
	}
	if(curr){
		cnt[curr]++;
	}else{
		curr = ++tot;
		if(p)tree[p][x>val[p]] = curr;
		tree[curr][0] = tree[curr][1] = 0;
		fa[curr] = p;val[curr] = x;
		cnt[curr] = sze[curr] = 1;
	}
	splay(curr);
}
void find(int x){
	int curr = root;
	while(tree[curr][x>val[curr]]&&val[curr]!=x){
		curr = tree[curr][x>val[curr]];
	}
	splay(curr);
}
void reverse(int l,int r){
	int x = kth(l), y =kth(r+2);
	splay(x);
	splay(y,x);
	lzy[tree[y][0]]^=1;
}
int pre(int x){
	find(x);
	if(val[root]<x)return root;
	int curr = tree[root][0];
	while(tree[curr][1])curr = tree[curr][1];
	return curr;
}
int succ(int x){
	find(x);
	if(val[root]>x)return root;
	int curr = tree[root][1];
	while(tree[curr][0])curr = tree[curr][0];
	return curr;
}
void output(int x){
	pushdown(x);
	if(tree[x][0])output(tree[x][0]);
	if(val[x]&&val[x]<=n)printf("%d ",val[x]);
	if(tree[x][1])output(tree[x][1]);
}
int main(){
	int m;
	scanf("%d%d",&n,&m);
	int x,y;
	for(int i = 0;i<=n+1;i++)insert(i);
	while(m--){
		scanf("%d%d",&x,&y);
		reverse(x,y);
	}
	output(root);
	return 0;
}

```