---
title: 【枚举+二分图】hdu 5727
date: 2019-08-13 20:13:55 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
n个阴珠子n个阳珠子间隔串成一串项链，给出m组信息u,v表示u号阳珠子放在v号阴珠子旁边会褪色。求一种排列使得褪色阳珠子的个数最少。
#  输入
第一行两个数字n,m
接下去m行每行两个数字u,v
#  输出
一个数字代表答案
#  样例输入
```
3 4
1 1
1 2
1 3
2 1
```
#  样例输出
```
1
```
提示
数据保证 30% n<=5
100% n<=9
# 解答
很好的一道思维题。
首先枚举每个阴珠子的位置，然后尝试在每个空隙中放入一个合法的阳珠子，然后在图上连出边来，最后尝试跑一遍匈牙利算法。枚举阴珠子的位置的全排列，取最小答案。
代码：
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
# include <queue>
# include <cmath>
# include <algorithm>
using namespace std;
const int MAXN = 1060;
const int MAXM = MAXN;
struct edge{int t,w,next;}edges[MAXM<<1];
int head[MAXN],top = 1;
void add(int f,int t,int w){
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].w = w;
	head[f] = top;
}
int S,T;
int n,m;
int match[MAXN],vis[MAXN],dfn;
bool map[10][10];
bool G[10][10];
int a[10];
bool dfs(int x){
	for(int i = 1;i<=n;i++){
		if(G[x][i]){
			int t = i;
			if(vis[t]==dfn)continue;
			vis[t] = dfn;
			if(match[t]==-1||dfs(match[t])){
				match[t] = x;return true;
			}
		}
	}
	return false;
}
int hungry(){
	int ans = 0;
	memset(match,-1,sizeof(match));
	for(int i = 1;i<=n;i++){
		++dfn;
		if(dfs(i))ans++;
	}
	return ans;
}
int main(){
	cin>>n>>m;
	int f,t;
	for(int i = 1;i<=m;i++){
		cin>>f>>t;
		map[f][t] =  true;
	}
	int ans = 0x3f3f3f3f;
	for(int i = 1;i<=n;i++)a[i] = i;
	do{
		memset(G,false,sizeof(G));
		int l,r;
		for(int i = 1;i<=n;i++){
			for(int j = 1;j<=n;j++){
				if(j==1){
					l = a[1],r = a[n];
				}else{
					r = a[j];
					l = a[j-1];
				}
				if(map[i][l]||map[i][r])continue;
				G[i][j] = true;
			}
		}
		ans = min(ans,n-hungry());
	}while(next_permutation(a+2,a+1+n));
	cout<<ans;
	return 0;
}

```