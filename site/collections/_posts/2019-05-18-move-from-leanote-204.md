---
title: 【线段树+每一位处理】woj 3763 线段树
date: 2019-05-18 17:03:33 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
请你维护一个线段树
支持一下操作

A x l r 区间 and x

O x l r区间 Or x

X x l r 区间 Xor x

S l r 区间求和

输入
一个数 T表示数据组数 一个数n表示初始序列长 m表示查询 随后n个整数 接下来m次询问 如上

输出
所以S次询问的答案

样例输入
```
1
4 1
1 2 4 7
S 0 2
```
样例输出
```
7
```
提示
为防止min-max剪枝 n=1e6 m=1e5 Ai<15 T<=3
# 解答
把每一位全部拆掉，拆成31位，然后31棵线段树维护区间和。
注意到一下性质：

 1. 或运算：或0等于不操作，或1等于全部置1
 2. 与运算：与1相当于不变，与1相当于置0
 3. 异或：异或0相当于不变，异或1相当于交换0,1个数
 
注意学会打标记
```cpp
# include<iostream>
# include <cstring>
# include <cstdio>
# define lc k<<1
# define rc k<<1|1
using namespace std;
const int MAXN = 1000005;
int a[MAXN];
struct node{int l,r,sum,covtag,revtag;};
struct segTree{
	node tree[MAXN<<2];
	void clear(){
		memset(tree,0,sizeof(tree));
	}
	void pushup(int k){tree[k].sum = tree[k<<1].sum+tree[k<<1|1].sum;}
	void build(int k,int l,int r,int bit){
		tree[k].covtag = -1;
		tree[k].l = l;tree[k].r = r;
		if(l==r){
			tree[k].sum = (a[l]&(1<<bit))?1:0;
			return ;
		}
		int mid = l+r>>1;
		build(k<<1,l,mid,bit);build(k<<1|1,mid+1,r,bit);
		pushup(k);
	}
	void pushcov(int k,int num){
		tree[k].covtag = num;
		tree[k].revtag = 0;
		tree[k].sum = (tree[k].r-tree[k].l+1)*num;
	}
	void pushrev(int k){
		tree[k].revtag^=1;
		tree[k].sum = tree[k].r-tree[k].l+1-tree[k].sum;
	}
	void pushdown(int k){
		if(tree[k].covtag!=-1)pushcov(lc,tree[k].covtag),pushcov(rc,tree[k].covtag);
		if(tree[k].revtag!=0)pushrev(lc),pushrev(rc);
		tree[k].covtag = -1;tree[k].revtag = 0;
	}
	void reverse(int k,int l,int r,int x,int y){
		if(l>=x&&r<=y){return pushrev(k);}
		pushdown(k);
		int mid = l+r>>1;
		if(x<=mid)reverse(lc,l,mid,x,y);
		if(y>mid)reverse(rc,mid+1,r,x,y);
		pushup(k);
	}
	void reset(int k,int l,int r,int x,int y,int num){
		if(l>=x&&r<=y){return pushcov(k,num);}
		pushdown(k);
		int mid = l+r>>1;
		if(x<=mid)reset(lc,l,mid,x,y,num);
		if(y>mid)reset(rc,mid+1,r,x,y,num);
		pushup(k);
	}
	int query(int k,int l,int r,int x,int y){
		if(l>=x&&r<=y){return tree[k].sum;}
		pushdown(k);
		int ret = 0;
		int mid = l+r>>1;
		if(x<=mid)ret+=query(lc,l,mid,x,y);
		if(y>mid)ret+=query(rc,mid+1,r,x,y);
		return ret;
	}
};
segTree t[4];
int main(){
	int T;scanf("%d",&T);
	while(T--){
		for(int i = 0;i<=3;i++)t[i].clear();
		int n,m;scanf("%d%d",&n,&m);
		for(int i = 1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		for(int j = 0;j<=3;j++)
			t[j].build(1,1,n,j);
		while(m--){
			char c[5];
		scanf("%s",c);
		int l,r,x;
		if(c[0]=='A'){
			scanf("%d%d%d",&x,&l,&r);
			for(int i = 0;i<=3;i++){
				if(!(x&(1<<i)))t[i].reset(1,1,n,l+1,r+1,0);
			}
		}
		if(c[0]=='O'){
			scanf("%d%d%d",&x,&l,&r);
			for(int i = 0;i<=3;i++){
				if(x&(1<<i))t[i].reset(1,1,n,l+1,r+1,1);
			}
		}
		if(c[0]=='X'){
			scanf("%d%d%d",&x,&l,&r);
			for(int i = 0;i<=3;i++){
				if(x&(1<<i))t[i].reverse(1,1,n,l+1,r+1);
			}
		}
			if(c[0]=='S'){
				scanf("%d%d",&l,&r);
				long long ans = 0;
				for(int i = 0;i<=3;i++){
					ans+=t[i].query(1,1,n,l+1,r+1)<<i;
				}
				printf("%lld\n",ans);
			}
		}
	}
	return 0;
}
```