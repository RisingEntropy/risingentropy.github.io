---
title: dhy的图论总结
date: 2019-10-20 19:01:00 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 图论  

----------


#  目录
- [] 最短路(次短路，最短路计数，分层图)
- [] 最小生成树
- [] 树的直径和LCA
- [] 基环树*
- [] 差分约束，负环
- [] tarjan与有向图
- [] tarjan与无向图
- [] 2-SAT
- [] 记忆化搜索
- [] 二分图相关的一坨
- [] 基础网络流建图
- [] 其他一些杂七杂八的东西(结论题)

# 最短路
常用算法：dijkstra,spfa,floyd.

 1. dijkstra: 复杂度稳定，不好卡
 2. spfa: 稀疏图随机图表现优秀，会把卡到$O(NE)$
 3. floyd: 与矩阵快速幂结合，传递闭包，计算最小可重边覆盖。
 
经过k条边的最短路。floyd+矩阵快速幂~~蛤？~~[奶牛接力](http://oi.cdshishi.net:8000/problempage.php?problem_id=2379)
[k短路](http://192.168.110.251/problempage.php?problem_id=3056)A*爆搜

#  最短路经典题
[墨墨的等式](http://oi.cdshishi.net:8000/problempage.php?problem_id=3993)
[hdu 4370 0 or 1](https://vjudge.net/problem/HDU-4370)每行每列选取一个点作为这行这列的代表点，如果一个点选择了，那么那个点下面的点就不能选，然后连边，合法的情况当且仅当有一条1-n的路径，从1出去到1有最短的环，从n出去再回来也如此。(有点忘了)
#  次短路
[NOIP2017逛公园](http://oi.cdshishi.net:8000/problempage.php?problem_id=2749)部分分
#  最短路计数
[NOIP2017逛公园](http://oi.cdshishi.net:8000/problempage.php?problem_id=2749)部分分
#  分层图
[改造路](http://oi.cdshishi.net:8000/problempage.php?problem_id=2415)
[孤岛营救问题](http://oi.cdshishi.net:8000/problempage.php?problem_id=3408)有些遗忘
# 最小生成树
[最小生成树计数](http://oi.cdshishi.net:8000/problempage.php?problem_id=3502)有些遗忘
[次小生成树](http://oi.cdshishi.net:8000/problempage.php?problem_id=3775)当时没调出来
[mst](http://oi.cdshishi.net:8000/problempage.php?problem_id=4323)和线段树结合
[比特战争](http://oi.cdshishi.net:8000/problempage.php?problem_id=4122)并查集维护信息
[tree bzoj3754](http://oi.cdshishi.net:8000/problempage.php?problem_id=1182)最小方差生成树
[tree bzoj2654](http://oi.cdshishi.net:8000/problempage.php?problem_id=3696)二分
# 树的直径、中心、重心
树的重心和中心背下板子
[集合](http://oi.cdshishi.net:8000/problempage.php?problem_id=4698)直径上二分
#  LCA
这个只是个工具，好多东西都要用
# 基环树
就是为了把题搞得恶心一点的东西，把环跑出来，然后考虑每颗根在环上的子树，然后再单独处理环。
[IOI2008 island](http://oi.cdshishi.net:8000/problempage.php?problem_id=3629)
# 差分约束
[天平](http://oi.cdshishi.net:8000/problempage.php?problem_id=1255)floyd+差分约束+上下界处理
# tarjan与有向图
[消息传递](http://oi.cdshishi.net:8000/problempage.php?problem_id=2558)
[受欢迎的牛](http://oi.cdshishi.net:8000/problempage.php?problem_id=1091)比较水了
# tarjan与无向图
[困难的图](http://oi.cdshishi.net:8000/problempage.php?problem_id=4749)
[network](https://vjudge.net/problem/POJ-3694)边双缩点以后就变成了一颗树，桥就是树上的连边，直接暴力维护uv之间的点到父亲的连边的是否是桥就行了
# 2-SAT
[poj 3207](http://poj.org/problem?id=3207)
注意，还是去了解一下与 或 异或的 2SAT问题。
# 记忆化搜索
[NOIP2017 逛公园](http://192.168.110.251/problempage.php?problem_id=2749)
# 二分图*
[glod小行星群](http://oi.cdshishi.net:8000/problempage.php?problem_id=2081# )
[poj2446](http://poj.org/problem?id=2446)较板
最小点覆盖：最少的点（即覆盖数）＝最大匹配数 M
最大独立集：二分图的最大独立集数=节点数(n)-最大匹配数
最小边覆盖 = 最大独立集 = n - 最大匹配
二分图最小边覆盖 = 两边顶点数 - 最大匹配数
无向图的最小边覆盖 = (二分图两边顶点数 - 二分图的最大匹配数)/2
DAG最小路径覆盖分为不相交路径、可相交路径
 
>不相交：把原图的每个点V拆成 Vx和 Vy两个点，如果有一条有向边A->B，那么就加
边Ax−>By。这样就得到了一个二分图。那么最小路径覆盖=原图的结点数-新图的最
大匹配数。
可相交：先用floyd求出原图的传递闭包。然后就转化成了最小不相交路径覆盖问题。
# 网络流
[危桥](http://oi.cdshishi.net:8000/problempage.php?problem_id=2766)巧妙建图，因为a流向b的可能也流向c了，然后就是起点连向另一个的终点，交换连，如果依然满足，就行了。
[蜥蜴](http://oi.cdshishi.net:8000/problempage.php?problem_id=1243)
# 最短路树
[安全路径](http://192.168.110.251/problempage.php?problem_id=2423# ) 通俗的讲，就是一个点不能走，只能从下面或其他地方绕过去，然后一条非树边的影响仅限于lca(u,v)以下，然后暴力更新影响就行了Orz，每个点第一次被更新的时候就是最小值
# 拓扑排序
[车站分级](http://oi.cdshishi.net:8000/problempage.php?problem_id=1804)
[上网](http://oi.cdshishi.net:8000/problempage.php?problem_id=4751)线段树优化建图+拓扑排序
[球的序列](http://oi.cdshishi.net:8000/problempage.php?problem_id=3969)玄学题？正着做可能会导致一条链中编号偏大的点被赋予了小的值，不行，但是倒着做，转化为大的点编号尽量大，就可以做了。Orz 神仙思维。

原来OI还有这么多不明白，OI真是休闲养生的益智类游戏呢/雾
