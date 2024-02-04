---
title: 20191023_blog
date: 2019-10-23 19:05:22 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 定时练习+图论
- [] floyd 求最小环，在计算的时候枚举中转点，然后记录ij是由哪个中转点转移过来的，然后递归地求上去。[例题](http://192.168.110.251/problempage.php?problem_id=2238) 对于有向图最小环，可以枚举起点1-n，然后以s为起点，跑dijkstra，s入队，更新相连的点，以后，把dis[s]设为INF，当dis被第二次入队以后，就是s为起点的最小环。
- [] 经过k条边的最短路：矩阵快速幂
- [] [ZYH的泼水节](http://192.168.110.251/problempage.php?problem_id=3526# )最小生成树 考虑kruskal合并的时候，两个并查集集合里面的点都需要向对方集合的点连边，一共需要连(sze[x]*sze[y]-1)(-1是因为x和y之前已经有一条边了)条边，边全一定是W(E(x,y))+1，因为要保证最小生成树形态不变.