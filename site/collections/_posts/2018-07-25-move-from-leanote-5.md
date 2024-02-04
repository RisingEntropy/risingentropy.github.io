---
title: SPFA算法解析洛谷P3371
date: 2018-07-25 20:07:13 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
# include <cstring>
# include <queue>
using namespace std;
struct edge{
    int next,diss ,to;
}Edges[500001];
int head[10001];
int edge_top = 0;//++edge_top
void addEdge(int from,int to,int weight){
  Edges[++edge_top].next = head[from];//head是保存上一个以该点为起点的节点
  Edges[edge_top].to = to;
  Edges[edge_top].diss = weight;
  head[from] = edge_top;//把上一个节点的位置换成这一个节点，这样才可以方便的形成链表式的结构，即链式前向星
}
int main() {
    int N,M,S;
    ios::sync_with_stdio(false);
    cin>>N>>M>>S;
    for(int i = 1;i<=M;i++){
        int Fi,Gi,Wi;
        cin>>Fi>>Gi>>Wi;
        addEdge(Fi,Gi,Wi);
    }//读入、建链表
    int dis[10001];
    for(int i = 1;i<=N;i++)dis[i] = 2147483647;
    bool visited[10005]{false};
    dis[S] = 0;//前面内容和dijkstra
    queue<int> q;
    q.push(S);
    visited[S] = true;
    while(!q.empty()){//类似于bfs，先将第一个点入队
        int u = q.front();//第一个点弹出队列
        int v;
        q.pop();
        visited[u] = false;//标记不在队列
        for(int i = head[u];i;i = Edges[i].next){//枚举该节点的每一个点
            v = Edges[i].to;//下一个节点
            if(dis[v]>dis[u]+Edges[i].diss){//若下一个点没有遍历过或者找到更短的路径，更新
                dis[v] = dis[u]+Edges[i].diss;
                if(!visited[v]){
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
    }
    for(int i = 1;i<=N;i++){
        cout<<dis[i]<<' ';
    }
    return 0;
}



```