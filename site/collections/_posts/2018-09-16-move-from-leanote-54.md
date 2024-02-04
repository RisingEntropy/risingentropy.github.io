---
title: Dijkstra+Heap
date: 2018-09-16 09:20:01 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# dijkstra+heap优化板子luoguP2384
```cpp
//
// Created by dhy on 18-9-15.
//
# include <queue>
# include <iostream>
# include <algorithm>
using namespace std;
int n,e;
struct edge{
    int t,w,next;
}edges[1000000];
int head[1000000];
int top = 0;
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
bool visited[1000000];
int dis[1000000];
int dijkstra(int s){
    priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > q;
    fill(dis,dis+n+1,0x3ffffff);
    dis[s] = 1;
    q.push(make_pair(1,s));
    while(!q.empty()){
        int f = q.top().second;
        q.pop();
        if(visited[f])continue;
        visited[f] = true;
        for(int i = head[f];i!=0;i = edges[i].next){
            if(dis[edges[i].t]>(dis[f]*edges[i].w)){
                dis[edges[i].t]=(dis[f]*edges[i].w)%9987;
                q.push(make_pair(dis[edges[i].t],edges[i].t));
            }
        }
    }
}
int main(void){
    ios::sync_with_stdio(false);
    cin>>n>>e;

    int f,t,w;
    for(int i = 1;i<=e;i++){
        cin>>f>>t>>w;
        add(f,t,w);
//        add(t,f,w);
    }
    dijkstra(1);
    cout<<dis[n];
    return 0;
}
```