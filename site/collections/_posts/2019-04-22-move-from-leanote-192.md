---
title: 【lct】[HNOI2010]BOUNCE 弹飞绵羊
date: 2019-04-22 15:09:51 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
某天，Lostmonkey发明了一种超级弹力装置，为了在他的绵羊朋友面前显摆，他邀请小绵羊一起玩个游戏。游戏一开始，Lostmonkey在地上沿着一条直线摆上n个装置，每个装置设定初始弹力系数ki，当绵羊达到第i个装置时，它会往后弹ki步，达到第i+ki个装置，若不存在第i+ki个装置，则绵羊被弹飞。绵羊想知道当它从第i个装置起步时，被弹几次后会被弹飞。为了使得游戏更有趣，Lostmonkey可以修改某个弹力装置的弹力系数，任何时候弹力系数均为正整数。
#  输入
第一行包含一个整数n，表示地上有n个装置，装置的编号从0到n-1,接下来一行有n个正整数，依次为那n个装置的初始弹力系数。第三行有一个正整数m，接下来m行每行至少有两个数i、j，若i=1，你要输出从j出发被弹几次后被弹飞，若i=2则还会再输入一个正整数k，表示第j个弹力装置的系数被修改成k。对于20%的数据n,m<=10000，对于100%的数据n<=200000,m<=100000
输出

对于每个i=1的情况，你都要输出一个需要的步数，占一行。
#  样例输入
```
4
1 2 1 1
3
1 1
2 1 1
1 1
```
#  样例输出
```
2
3
```
标签
HNOI2010
# 解答
轻量化版的lct，设置一个虚点n+1,然后每个点向每个点可以跳到的点连边，如果跳出的点超过了n，就连向n+1,最后lct维护就行了。由于整棵树的根是不变的，所以不需要`access`和`isroot`/`makeroot`等操作。代码：
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
const int MAXN = 200010;
int tree[MAXN][2],val[MAXN],fa[MAXN];
int top,stk[MAXN];
int which(int x){return tree[fa[x]][1] ==x;}
void pushup(int x){val[x] = val[tree[x][1]]+val[tree[x][0]]+1;}
bool isroot(int x){return !fa[x]||(x!=tree[fa[x]][1]&&x!=tree[fa[x]][0]);}
void rotate(int x){
	int y = fa[x],z = fa[y],d = which(x),w = tree[x][d^1];
	if(!isroot(y))tree[z][which(y)]=x;
	fa[x] = z;tree[y][d] = w;fa[w] = y;
	tree[x][d^1] = y;fa[y] = x;
	pushup(y);pushup(x);
}
void splay(int x){
	while(!isroot(x)){
		int y = fa[x];
		if(!isroot(y)){
			if(which(y)==which(x))rotate(y);else rotate(x);
		}
		rotate(x);
	}
}
void access(int x){
	for(int y = 0;x;y = x,x = fa[x]){
		splay(x);tree[x][1] = y;pushup(x);
	}
}
int main(){
	int n;cin>>n;
	for(int i = 1;i<=n;i++){
		int v;cin>>v;
		val[i] = 1;
		if(i+v<=n)fa[i] = i+v;
	}
	int m;cin>>m;
	for(int i = 1;i<=m;i++){
		int op,x,y;
		cin>>op;
		if(op==1){
			cin>>x;x++;
			access(x);splay(x);
			cout<<val[x]<<endl;
		}else{
			cin>>x>>y;
			x++;access(x);splay(x);
			tree[x][0] = fa[tree[x][0]] = 0;
			if(x+y<=n)fa[x] = x+y;
		}
	}
}
```