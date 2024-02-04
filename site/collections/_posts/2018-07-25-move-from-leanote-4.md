---
title: dijkstra算法解析洛谷P3371
date: 2018-07-25 19:50:08 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
# include <cstring>
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
    dis[S] = 0;//初始化，标记
    for(int i = 1;i<=N;i++){
        int minnl = 214748364;//不多说
        int k = 0;
        for(int j = 1;j<=N;j++){
            if(!visited[j]&&dis[j]<minnl){
                minnl = dis[j];
                k = j;
            }//寻找路径最短的点（一开始是自己，其他点全都没有遍历过）
        }
        if(k==0)break;
        visited[k] = true;
        for(int j = head[k];j;j = Edges[j].next){//dijkstra算法的核心
            if(!visited[Edges[j].to]//下一个点没被访问
               &&dis[Edges[j].to]>Edges[j].diss+dis[k]){//并且到下一个点的距离小于连接这条边的距离+到当前点的距离
                dis[Edges[j].to]=Edges[j].diss+dis[k];//update
            }
        }
    }
    for(int i = 1;i<=N;i++){
        cout<<dis[i]<<' ';
    }
    return 0;
}




```