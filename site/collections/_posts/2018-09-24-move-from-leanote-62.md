---
title: tarjan缩点
date: 2018-09-24 13:06:37 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
using namespace std;
struct edge{int t,next;}edges[10000];
int head[10000];
int top;
void add(int f,int t){
    edges[++top].next = head[f];
    edges[top].t = t;
    head[f] = top;
}
bool visited[1000];//某个节点是否在栈中
int dfn[1000];
int low[1000];
int dfn_sum;
int stack[10000];
int stop;
int color[10000];//哪个点染什么色，颜色一样的点属于同一个强连通分量 
int color_val = 0;
inline int minn(int x,int y){return x>y?y:x;}
void tarjan(int x){
    dfn[x] = ++dfn_sum;
    low[x] = dfn_sum;
    visited[x] = true;
    stack[++stop] = x;
    for(int i = head[x];i!=0;i = edges[i].next){
        int v = edges[i].t;
        if(dfn[v]==0){
            tarjan(v);
            low[x] = minn(low[x],low[v]);
        }else if(visited[v]){
            low[x] = minn(low[x],dfn[v]);//是回溯到的节点靠前，还是本来已经找到的节点靠前 
        }
    }
    if(dfn[x]==low[x]){
        visited[x] = false;
        color[x] = ++color_val;
        while(stack[stop]!=x){
            color[stack[stop]] = color_val;
            visited[stack[stop--]] = false;
        }
        stop--;//点x已经在栈中，并且已经找到了一个强连通分量，上一个在栈中的点x出栈 
    }
} 
```