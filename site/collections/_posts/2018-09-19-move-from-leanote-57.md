---
title: kosaraju题解
date: 2018-09-19 17:22:48 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
using namespace std;
int st[10000];//可以用stl stack 代替 
int t = 0;//可以用stl stack 代替 
struct edge{ 
	int t,next;
}edges[100000],edges2[100000];
int head[10000];
int head2[10000];
int top2;
int top;
int visited[10000];
void add1(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
void add2(int f,int t){
	edges[++top2].next = head2[f];
	edges[top2].t = t;
	head2[f] = top2;
}
void dfs(int s){
	visited[s] = true;
	for(int i = head[s];i!=0;i = edges[i].next){
		if(!visited[edges[i].t]){
			dfs(edges[i].t);
		}
	}
	st[++t] = s;
}
void dfs2(int s){
	visited[visited[edges2[s].t] = true;
	for(int i = head[s];i!=0;i = edges2[i].next){
		dfs2(edges[2].t);//可以在此记录强连通分量的顶点 
	}
}
int kosaraju(){
	int sum = 0;
	for(int i = 1;i<=n;i++){
		if(!visited[i]){
			dfs(i);
		}
	}
	memset(visited,false,sizeof(visited));
	for(int i = n;i>=1;i--){//选择具有最晚访问完的顶点，对反图进行dfs 
		if(!visited[st[i]]){
			sum++;
			dfs2(st[i]);
		}
	}
	//强连通分量数 
	return sum;
}
```