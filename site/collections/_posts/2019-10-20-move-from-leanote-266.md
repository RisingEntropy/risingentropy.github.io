---
title: hxy的图论总结
date: 2019-10-20 11:23:44 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

图论の汇总
==
--------------
#  最短路
- [] Floyd $O(n^3)$     用于处理任意两点间最短路
好题：[奶牛接力](http://oi.cdshishi.net:8000/problempage.php?problem_id=2379) Floyd矩阵快速幂（什么JB玩意）
也可以求传递闭包（可是我不会）
- [] Dijkstra $O((n+m)log(m))$
- [] Bellman-Ford 不会啊
- [] SPFA ···$O(不能过)$
#  最短路拓展
- [] 输出最短路路径（数）
- [] k短路
#  tarjan
#  无向图
- [] 割点（点双联通）
- [] 割边（边双联通）
#  有向图
- [] 强连通分量
#  拓扑排序
- [] 好题：[球的序列（【HNOI2015】菜肴制作）](http://oi.cdshishi.net:8000/problempage.php?problem_id=3969)
>注意此题是让编号小的球拓扑序尽量靠前（轻），不是让靠前的球编号尽量小……
但是可以把问题转化成让靠后的球编号尽量大（这个确实很玄）那么就建一个反图，大根堆实现
#  差分约束系统
 重点在于找出尽可能多的限制，SPFA判负环。

- [] [奶牛的站位Layout](http://oi.cdshishi.net:8000/problempage.php?problem_id=2239)
> 比较板子题了
朋友关系就是$dis[v]<=dis[u]+w$
敌对关系就是$dis[v]>=dis[u]+w$,转化成$dis[u]<=dis[v]-w$
(差分约束只能处理<=)
编号小的靠前：$dis[i-1]<=dis[i]$

- [] [出纳员问题](http://oi.cdshishi.net:8000/problempage.php?problem_id=3844) 有点毒
>求解$sum[i]$：知道$i$时间段内所需人数总和，答案即为$sum[24]$
但是在写限制的时候，0-7小时的情况很麻烦：$sum[24]-sum[i+16]$$+sum[i]>=R[i]$出现了三个变量
但我们求$sum[24]$，不妨二分它，然后判断是否合法即可
#  二分图
- [] km算法 复杂度$O(nm)$（雾）
以后复习，先贴代码
```
int tot,vis[N],match[N];
bool find(int u){
	for(int i=first[u],v;i;i=e[i].nxt){
		v=e[i].v;if(vis[v]!=tot){
			vis[v]=tot;
			if(match[v]==-1||find(match[v])){
				match[v]=u;return 1;
			}
		}
	}
	return 0;
}
int km(){
	int ret=0;memset(match,-1,sizeof(match));
	for(int i=0;i<n;i++){
		tot++;
		ret+=find(i);
	}
	return ret;
}
```

可以解决：

- [] 最大匹配
- [] 最小点覆盖：最大匹配
- [] 最小边覆盖：2n-最大匹配
- [] 最大独立集：2n-最大匹配
- [] 无向图最小边覆盖：只可意会不可证明
- [] DAG：嗯？？

例题也甩这了

 1. [] [矩阵游戏](http://oi.cdshishi.net:8000/problempage.php?problem_id=1744)：行列间建边，要求匹配数为n
 2. [] [glod小行星群](http://oi.cdshishi.net:8000/problempage.php?problem_id=2081) 建边同上
 3. [] [POJ - 2446 Chessboard]()
#  生成树
#  普通生成树
 4. [] prim：不会啊
 5. [] kruskal
[mst](http://oi.cdshishi.net:8000/problempage.php?problem_id=4323):生成树+树剖

>相当于是每条非树边都对kruskal上与之所成环的边都有一个贡献，一条树边所受最小的贡献就是答案。把边权存在点上，树剖解决

#  高级东西
 6. [] 基环树：不会啊
[]()
 7. [] kruskal重构树
这玩意的两点间lca就是两点间最小瓶颈路（or最大路，取决于sort）但重点不在于这个，而在于它的一些奇妙性质。
[[NOI2018]归程（return）](http://oi.cdshishi.net:8000/problempage.php?problem_id=3673)

> 对边权从大到小排序后kruskal，得到一个类似小根堆的重构树，lca为最小瓶颈。
这个时候它就有一个奇妙的性质：点权$>$水位线$p$的点的子树内可以随意走动，代价为$0$。
那么问题转化成两个子问题：求$u$点的深度最小的权值$>p$的祖先；求它子树内的所有点中，到1号节点的最短路最小是多少
问题一倍增解决，问题二dfs时解决，复杂度$O(dij)+O(kruskal)+O(n)+O(q*log(n))$

- [] 最短路树
[安全出行Safe Travel](http://oi.cdshishi.net:8000/problempage.php?problem_id=2423)
毒瘤题

> 跑出最短路生成树，对于每条非树边，会对$u$到$lca_{u,v}$，$v$到$lca_{u,v}$造成贡献（不包括$lca$）
继续分析：对于任意一个节点$x$，它的$ans$等于
$$min(dep_{lca}+w_i+dep_u+dep_v-2*dep_{lca}-(dep_x-dep_{lca}))$$
也就是说$ans_x=min(dep_u+dep_v+w_i)-dep_x$
其中$i$满足$x \not=lca_{u,v}$且$x\in lca_{u,v}$的子树
此时直接上树剖是$O(mlog^2(n))$的，也就是$O($卡常$)$,所以我们用到了**贪心**
把所有的$dep_u+dep_v+w_i$从小到大排序，所以取出来的$u,v$一定更新剩下未被更新的$u$到$lca$，$v$到$lca$上的点，同时为了优化这一过程，我们用**并查集**压缩被更新的点，复杂度做到$O(n+m)$

- [] dfs生成树
[【2019CSP-S测试1012】困难的图](http://oi.cdshishi.net:8000/problempage.php?problem_id=4749)

>记住无向图dfs生成树有个性质：没有横叉边，只有返祖边
因此这道题就是求：返祖边所覆盖的边与其他返祖边没有交集的所有返祖边。
所以直接在返祖边的$u,v$处打-1,和1的标记，dfs $O(n)$跑一边前缀和，然后$O(n+m)$直接枚举返祖边验证每个环是否合法（$sum\not=1$就不合法，直接跳出来，因此是$O(n)$的）

#  网络流
以防万一还是贴个板子吧
```
inline bool bfs(){
	queue<int>q;q.push(S);
	memset(dis,-1,sizeof(dis));dis[S]=0;
	while(!q.empty()){
		int u=q.front();q.pop();
		for(int i=first[u],v;i;i=e[i].nxt){
			v=e[i].v;
			if(e[i].w&&dis[v]==-1){
				dis[v]=dis[u]+1;
				if(v==T)return 1;
				q.push(v);
			}
		}
	}
	return 0;
}
int dfs(int u,int f){
	if(!f||u==T)return f;
	int used=0;
	for(int &i=cur[u],v;i;i=e[i].nxt){//当前弧
		v=e[i].v;
		if(e[i].w&&dis[v]==dis[u]+1){
			int w=dfs(v,min(f,e[i].w));
			if(!w)continue;
			f-=w;used+=w;
			e[i].w-=w;e[i^1].w+=w;
			if(!f)break;
		}
	}
	return used;
}
inline int dinic(){
	int ret=0;
	while(bfs()){
		for(int i=0;i<=T;i++)cur[i]=first[i];
		ret+=dfs(S,0x7fffffff);
	}
	return ret;
}
```
- [] 最大流
[危桥](http://oi.cdshishi.net:8000/problempage.php?problem_id=2766)
好题一道、

>直接建图跑最大流会有个问题：a流向b或者b流向a，如图
![其中红色为危桥](https://cdn.risingentropy.top/images/posts/dac3d33ab64412e1f00066f.png)
其中红色为危桥,but流量可以为无限大
这个时候我们让S连向b2，T连向b1，若这样仍满足，那方案一定合法

- [] 最小割
[zjoi2009狼与羊的故事](http://oi.cdshishi.net:8000/problempage.php?problem_id=1759)

> 既然要把两个东西分开，就$考^{ti}虑^{jie}$最小割
分开两个方格的代价为1，于是羊->狼连、羊->空地、空地->空地、空地->狼连边权为1的边。注意边不要连重了

[「网络流 24 题」太空飞行计划SPJ](http://oi.cdshishi.net:8000/problempage.php?problem_id=2309)
真正的好题

>观察到对于一个实验$i$，要不得到$val_i-\sum_j^{j\in i}cost_j$的贡献，要不得到$0$的贡献
所以~~根据题解~~可将题目转化成$$ans=sumval-\sum_{i=1}^n min(\sum_j^{j\in i}cost_j,val_i)$$
其中$\sum_{i=1}^n min(\sum_j^{j\in i}cost_j,val_i)$就是求个最小割
方案输出只需要判断是否出现在增广路中（$dis\not=-1$）（待填坑）

#  2-SAT

#  分层图

#  杂（七杂八的知识都考了的）题
这块实在是太杂了……

- [] [连通代价](http://oi.cdshishi.net:8000/problempage.php?problem_id=3668)

>直接暴力建边是$O(n^2)$的，但是有用的边只会在$x,y,z$的一维中连续的$a_i,a_{i+1}$相连，所以对三维排序后连续的点之间连边，复杂度$O(3nlog(n)+3n+kruskal)$

[双调路径](http://oi.cdshishi.net:8000/problempage.php?problem_id=3841)

> 

[【ARC084D】Small Multiple](http://oi.cdshishi.net:8000/problempage.php?problem_id=4260)
[墨墨的等式](http://oi.cdshishi.net:8000/problempage.php?problem_id=3993)
[HDU - 4370 0 or 1](https://vjudge.net/problem/HDU-4370)
[【ARC61E】Snuke's Subway Trip](http://oi.cdshishi.net:8000/problempage.php?problem_id=4194)
[黑白图](http://oi.cdshishi.net:8000/problempage.php?problem_id=3742)