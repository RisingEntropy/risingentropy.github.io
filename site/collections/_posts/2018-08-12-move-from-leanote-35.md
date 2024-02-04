---
title: LCA
date: 2018-08-12 15:29:09 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
void dfs(int u,int fa){
    dep[u] = dep[fa]+1;
    for(int i = 0;i<=19;i++){
        f[u][i+1]=f[f[u][i]][i];//处理一下父节点
        for(int i = head[u];i!=0;i=next[i]){
            int v = i.nextl
            if(v==fa)continue;//很重要
            f[v][0]=u;//向上跳2^0==1，就是u
            dfs(v,u);
        }
    }
}

int LCA(int x,int y){
    if(dep[x]<dep[y])swap(x,y);
    for(int i = 20;i>0;i--){
        if(dep[x][i]>dep[y]x=f[x][i];
        if(x==y)return x;
    }
    for(int i = 20;i>=0;i--){
        if(f[x][i]!=f[y][i]){//注意这一行
            x=f[x][i];
            y=f[y][i];
        }
    }
    return f[x][0];
}
```