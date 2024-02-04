---
title: 【2-SAT】poj 3207Ikki's Story IV - Panda's Trick
date: 2019-06-09 12:03:37 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Description

liympanda, one of Ikki’s friend, likes playing games with Ikki. Today after minesweeping with Ikki and winning so many times, he is tired of such easy games and wants to play another game with Ikki.

liympanda has a magic circle and he puts it on a plane, there are n points on its boundary in circular border: 0, 1, 2, …, n − 1. Evil panda claims that he is connecting m pairs of points. To connect two points, liympanda either places the link entirely inside the circle or entirely outside the circle. Now liympanda tells Ikki no two links touch inside/outside the circle, except on the boundary. He wants Ikki to figure out whether this is possible…

Despaired at the minesweeping game just played, Ikki is totally at a loss, so he decides to write a program to help him.

Input

The input contains exactly one test case.

In the test case there will be a line consisting of of two integers: n and m (n ≤ 1,000, m ≤ 500). The following m lines each contain two integers ai and bi, which denote the endpoints of the ith wire. Every point will have at most one link.

Output

Output a line, either “panda is telling the truth...” or “the evil panda is lying again”.

Sample Input
```
4 2
0 1
3 2
```
Sample Output
```
panda is telling the truth...
```
# 解答
把每一个线段当做点，然后想~~yy~~出这可以看做是2-SAT跑异或。因为不妨设外面为1，里面为0。当且仅当异或值为1的时候没有相交，然后跑2-SAT就行了。~~完美口胡~~
```cpp
# include <iostream>
# include <vector>
# include <cstring>
# include <stack>
# include <cstdio>
using namespace std;
const int MAXN = 2010;
vector<int> G[MAXN];
stack<int> stk;
void add(int f,int t){G[f].push_back(t);}
int dfn[MAXN],low[MAXN],dfn_cnt,color_cnt,color[MAXN];
bool vis[MAXN];
int n,m;
int st[MAXN],ed[MAXN];
void tarjan(int x){
	low[x] = dfn[x] = ++dfn_cnt;stk.push(x);
	vis[x] = true;
	for(int i = 0;i<G[x].size();i++){
		int t = G[x][i];
		if(!dfn[t]){
			tarjan(t);low[x] = min(low[t],low[x]);
		}else if(vis[t])low[x] = min(low[x],dfn[t]);
	}
	if(dfn[x]==low[x]){
		++color_cnt;
		while(true){
			int t = stk.top();stk.pop();
			color[t] = color_cnt;vis[t] = false;
			if(t==x)break;
		}
	}
}
inline int oppo(int x){return x&1?x+1:x-1;}
bool check(){
	for(int i = 1;i<=m;i++){
		if(color[i]==color[i+m])return false;
	}
	return true;
}
void build(){
	for(int i = 1;i<=m;i++){
		for(int j = 1;j<i;j++){
			if((st[i]<=st[j]&&ed[i]<=ed[j]&&st[j]<=ed[i])||(st[j]<=st[i]&&ed[j]>=st[i]&&ed[j]<=ed[i])){
				add(i,j+m);add(j,i+m);
				add(i+m,j);add(j+m,i);//异或的连边方法
			}
		}
	}
}
int main(){
	cin>>n>>m;
	for(int i = 1;i<=m;i++){
		cin>>st[i]>>ed[i];
		if(st[i]>ed[i])swap(st[i],ed[i]);
	}
	build();
	for(int i = 1;i<=n+m;i++)if(!dfn[i])tarjan(i);
	if(check())cout<<"panda is telling the truth...";
	else cout<<"the evil panda is lying again";
	return 0;
}
```