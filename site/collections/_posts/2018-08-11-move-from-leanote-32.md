---
title: SPFA慎用！！！！它已经死了！！！！
date: 2018-08-11 13:10:51 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
    int dis[N];
    bool exist[2001];
    memset(exist,false, sizeof(exist));
    memset(dis,0x7f, sizeof(dis));
    queue<int> q;
    dis[s] = 0;
    q.push(s);
    exist[s] = true;
    int u;
    while(!q.empty()){
        u = q.front();
        q.pop();
        exist[u] = false;
        for(int i = head[u];i!=0;i = edges[i].next){
            int v = edges[i].to;
            if(dis[v]>dis[u]+edges[i].w){
                dis[v] = dis[u]+edges[i].w;
                if(!exist[v]){
                    exist[v] = true;
                    q.push(v);
                    inQueueTimes[v]++;
                }
        }
    }
    return false;
}

```