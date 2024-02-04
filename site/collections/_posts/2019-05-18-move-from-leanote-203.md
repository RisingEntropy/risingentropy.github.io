---
title: 【点分治】woj 3968
date: 2019-05-18 17:03:12 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给一棵树,每条边有权.求一条路径,权值和等于K,且边的数量最小.

输入
第一行 两个整数 n, k

第二..n行 每行三个整数 表示一条无向边的两端和权值 (注意点的编号从0开始)

输出
一个整数 表示最小边数量 如果不存在这样的路径 输出-1

样例输入
```
4 3
0 1 1
1 2 2
1 3 4
```
样例输出 
```
2
```
提示
n≤2e5k≤1e6
# 解答
子树里面tmp[dis]表示走到距离为dis的路程时最少深度。然后动态更新。代码：
```cpp
# include <iostream>
# include <set>
# include <cstdio>
# include <cstring>
# include <cstdlib>
using namespace std;
const int MAXN = (int)3e5+10;
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
int size[MAXN],root,mi,ans = 0x3f3f3f3f,n,k;
int dis[MAXN],dep[MAXN*10],num;
int son[MAXN];
int sum;
int temp[MAXN*10];
bool vis[MAXN];
void getroot(int x,int fa){
	size[x] = 1;son[x] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa||vis[t])continue;
		getroot(t,x);
		size[x]+=size[t];son[x] = max(son[x],size[t]);
	}
	son[x] = max(son[x],sum-size[x]);
	if(son[x]<son[root])root = x;
}
int cal(int x,int fa){
	if(dis[x]<=k)ans= min(ans,temp[k-dis[x]]+dep[x]);
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa||vis[t])continue;
		dep[t] = dep[x]+1;dis[t] = dis[x]+edges[i].w;
		cal(t,x);
	}
}
void update(int x,int fa,int f){
	if(dis[x]<=k){
		if(f)temp[dis[x]] = min(temp[dis[x]],dep[x]);
		else temp[dis[x]] = 0x3f3f3f3f;
	}
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa||vis[t])continue;
		update(t,x,f);
	}
}
void dfs(int x){
	vis[x] = true;temp[0] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		dis[t] = edges[i].w;dep[t] = 1;
		cal(t,0);update(t,0,1);
	}
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(!vis[t])update(t,t,0);
	}
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		sum = size[t];root = 0;
		getroot(t,0);
		dfs(root);
	}
}
int main(){
	 int size=40<<20;//40M
    __asm__ ("movq %0,%%rsp\n"::"r"((char*)malloc(size)+size));
	cin>>n>>k;
	int f,t,w;
	memset(temp,0x3f,sizeof(temp));
	for(int i = 1;i<n;i++){
		cin>>f>>t>>w;f++,t++;
		add(f,t,w);add(t,f,w);
	}
	mi = n;
	sum = n;root = 0;son[0] = n;
	getroot(1,0);
	dfs(root);
	cout<<(ans==0x3f3f3f3f?-1:ans);
	exit(0);
}
```