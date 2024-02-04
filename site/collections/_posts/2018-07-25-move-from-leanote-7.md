---
title: 最小环问题
date: 2018-07-25 22:01:34 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 最小环问题说白了就是暴力Floyed算法————沃·兹基·硕德
emm，上代码
```cpp
for(int k = 1;k<=n;k++)
    for(int i = 1;i<=k-1;i++){
        for(int j = i+1;k<=k-1;j++){
            answer = min(ans,dis[i][j]+g[j][k]+g[k][i]);
        }
        for(int i = 1;i<=n;i++)
            for(int j = 1;j<=n;j++){
                dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);//老套路
            }
    }
```
# 强连通分量
(1)kosaraju算法：

 1. 第一次对图进行DFS遍历，并在遍历的过程中，记录每一个点的退出顺序，
 2. 倒转每一条边的方向，构造出一个反图G’，然后按照退出顺序对反图进行第二次DFS遍历
 参见一本通P494