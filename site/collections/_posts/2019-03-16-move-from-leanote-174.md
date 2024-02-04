---
title: 主席树
date: 2019-03-16 14:39:13 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
# include <algorithm>
# include <cstdio>
using namespace std;
const int MAXM = (int)1e6+10;
const int MAXN = (int)1e6+10;
int top;
int val[MAXN<<2],tree[MAXN<<2][2];
int a[MAXN];
int rt[MAXN];
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
void build(int &k,int l,int r){
	k = ++top;
	if(l==r){
		val[k] = a[l];
		return;
	}
	int mid = l+r>>1;
	build(tree[k][0],l,mid);build(tree[k][1],mid+1,r);
}
void ins(int &k,int pre,int l,int r,int pos,int v){
	k = ++top;
	tree[k][0] = tree[pre][0];
	tree[k][1] = tree[pre][1];
	val[k] = val[pre];
	if(l==r){val[k] = v;return;}
	int mid = l+r>>1;
	if(pos<=mid)ins(tree[k][0],tree[pre][0],l,mid,pos,v);
	else ins(tree[k][1],tree[pre][1],mid+1,r,pos,v);
}
int query(int k,int l,int r,int pos){
	if(l==r)return val[k];
	int mid = l+r>>1;
	if(pos<=mid)return query(tree[k][0],l,mid,pos);
	else return query(tree[k][1],mid+1,r,pos);
}
int main(){
	int n = read(),m = read();
	for(int i = 1;i<=n;i++)a[i] = read();
	build(rt[0],1,n);
	int vi,opt,loci,valuei;
	for(int i = 1;i<=m;i++){
		vi = read(),opt = read();
		if(opt==1){
			loci = read(),valuei = read();
			ins(rt[i],rt[vi],1,n,loci,valuei);
		}else{
			loci = read();
			printf("%d \n",query(rt[vi],1,n,loci));rt[i] = rt[vi];
		}
	}
}
```