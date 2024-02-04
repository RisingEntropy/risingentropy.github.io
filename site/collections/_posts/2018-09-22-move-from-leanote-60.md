---
title: 割点与桥
date: 2018-09-22 11:02:42 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 一些概念(bing搜的)
一、定义
>1.点连通度与边连通度:在一个**无向连通图**中，如果有个顶点集合V.副除顶点集合V以及与V中顶点相连(至少有一端在V中)的所有边后原图不连通，就称这个点集v为割点集合。
2.一个图的点连通度:最小割点集合中的顶点数。
如果有一个边集合 ，删除这个边集合以后.原图不连通.就称这 个点集为割边集合。
3.一个图的边连通度:最小割边集合中的边数。
4.双连通图、割点与桥:如果一个无向连通图的点连通度大于1，则称该图是点双连通的point hicomnected),简称双连通或重连通(即刪去任意一点原图仍然连通)。 一个图有割点，当且仅当这个图的点连通度为1时,割点集合的唯一元素被称为割点(cut point)(即删去制点原图不连通)一个图可能有多个割点。
**5.有割点的图不一定有割边**
6.割点集合的唯一元素被称为割点
如果一个无向连同图的边连同度大于1，则称该图是双边连同的，简称双联通或重连通。一个图有桥，当且仅当这个图的边连通度为1时，割边的唯一元素被称为桥。有割边的图也不一定有割点如图
![有割边却没有割点](https://cdn.risingentropy.top/images/posts/bb62a76ab644145bb003edf.png)

<font color="red">错误猜想：两个割点之间的边一定是割边。割边的两个端点一定是割点，如图：
</font>
![eg1](https://cdn.risingentropy.top/images/posts/bb62a76ab644145bb003edf.png)   ![eg2](https://cdn.risingentropy.top/images/posts/bb62a76ab644145bb003edf.png)

# 计算割点与桥
#  tarjan算法
流程与tarjan求强连通分量类似求low与dfn。但要加一个特判，根节点如果有两个及以上的儿子，那么他也是割点。
判定定理：
对于一个点 u，有以下两种情况：
如果 u 是根节点，那么当它有多于一个子树时，它就是割点
如果 u 不是根节点，并且 u 为 v 在搜索树中的父亲，当 dfn[ u ] ≤ low[ v ] 时，它就是割点
【割边】 
#  计算桥
其实很简单，一条无向边(u,v)是桥，当且仅当(u,v)是树枝变，且满足dfn[u]`<`low[v]。因为v想要到达u的父亲，必须经过(u,v)这条边，所以删除这条边以后，图不连同.
<font color="red">注意：因为前向星在存无向图的时候，把一条边拆分成2条边储存，所以判断(u,v)是否为后向边的时候注意判断是正边，反边，还是新的一条边</font>
找反边：edges[i]的反边是edges[i^1]//就是奇数减一，偶数加一
判定定理：
**如果一条搜索树上的边，连接着两个结点xy，且x是y的父亲，且满足low[y]>dfn[x]，那么就是割边了**
code:板子里面

# 双连通分量
>若一个无向图中的去掉任意一个节点（一条边）都不会改变此图的连通性，即不存在割点（桥），则称作点（边）双连通图。一个无向图中的每一个极大点（边）双连通子图称作此无向图的点（边）双连通分量。

---百度百科

#  边双连通分量
若一个无向图中的去掉任意一条边都不会改变此图的连通性，即不存在桥，则称作边双连通图。一个无向图中的每一个极大边双连通子图称作此无向图的边双连通分量。
#  点双连通分量
若一个无向图中的去掉任意一个节点都不会改变此图的连通性，即不存在割点，则称作点双连通图。一个无向图中的每一个极大点双连通子图称作此无向图的点双连通分量。

# 求取
找到一条树枝边或者后向边(非横叉边)，把这条边入栈。当u是一个个点时，同时把边从栈顶一个个取出，直到遇到边(u,v)为止。取出的这些边与其相连的点，组成一个点双联通分量
点：
```cpp
//tarjan find cut point
edge stack[10000];
int dfn[10000];
int low[10000];
int stop;
int dfn_cnt;
int bcc_num[1000];//哪个点属于哪个双连通分量 
int bcc_cnt;//有多少个双连通分量
vector<int> bcc[10000];//每个双连通分量有哪些点 
bool iscut[1000];
int root;
void tarjan(int x,int fa){
    low[x] = dfn[x] = ++dfn_cnt;
    int child = 0;
    for(int i = head[x];i!=0;i = edges[i].next){
    	int v = edges[i].t;
        if(!dfn[i]){//下一个点没有被访问过; 
        	stack[++stop] = edges[i];
            tarjan(edges[i].t,x);
            child++;
            low[x] = min(low[x],low[edges[i].t]);
            if(low[v]>dfn[x]){
            	iscut[x] = true;
            	++bcc_cnt;
            	bcc[bcc_cnt].clear();
            	while(true){
            		edge e = stack[stop--];
            		if(bcc_num[e.f]!=bcc_cnt){
            			bcc[bcc_cnt].push_back(e.f);
            			bcc_no[e.f] = bcc_cnt;
            		}
            		if(bcc_num[e.t]!=bcc_cnt){//取出这些边与其相邻的点，组成一个双连通分量 
            			bcc[bcc_cnt].push_back(e.t);
            			bcc_no[e.t] = bcc_cnt;
            		}
            		if(e.f == x&&e.t = v){
            			break;//直到取出边(u,v) 
            		}
            	}
            }
        }else{
        	if(dfn[x]>dfn[v]&&v!=fa){
        		stack[++top] = edges[i];
           		low[x] = min(low[x],dfn[edges[i].t]) ;
        	}
		}
		
    }
    if(fa<=&&child==1){
		iscut[x] = false; 
	}
}
void findbcc(int n){
	//初始化一些东西，如果全局变量的话不需要
	for(int i = 1;i<=n;i++){
		if(!dfn[i]){
			tarjan(i,-1);//-1应该是一个虚拟根节点 
		}
	} 
}
```
边：
边双连通分量的求解非常简单，因为边双连通分量之间没有公共边，而且桥不在任意一个边双连通分量中，所以算法十分简单，即先一次DFS找到所有桥，再一次DFS（排除了桥）找到边双连通分量。 
PS：当然可以用一次DFS实现。 
code:
```cpp
//tarjan find cut point
edge stack[10000];
int dfn[10000];
int low[10000];
int stop;
int dfn_cnt;
int bcc_num[1000];//哪个点属于哪个双连通分量 
int bcc_cnt;//有多少个双连通分量
vector<int> bcc[10000];//每个双连通分量有哪些点 
bool isbridge[1000];
int root;
void tarjan(int x,int fa){
    low[x] = dfn[x] = ++dfn_cnt;
    for(int i = head[x];i!=0;i = edges[i].next){
    	int v = edges[i].t;
        if(!dfn[i]){//下一个点没有被访问过; 
            tarjan(edges[i].t,x);
            low[x] = min(low[x],low[edges[i].t]);
            if(low[v]>dfn[x]){
            	isbridgs[i] = isbridge[i^1] = true;
            }
        }else{
        	if(dfn[x]>dfn[v]&&v!=fa){
        		stack[++top] = edges[i];
           		low[x] = min(low[x],dfn[edges[i].t]) ;
        	}
		}
		
    }
}
void dfs(int index){
	dfn[index] = true;
	bcc_num[index] = bcc_cnt;
	for(int i = head[index];i!=0;i = edges[i].next){
		int v = edges[i].t;
		if(isbridge[i])continue;
		if(!dfn[v]){
			dfs(v);
		}
	}
}
void find_ebcc(int n){
	//做一些初始化，把数组初始化了 
	for(int i = 1;i<=n;i++){
		if(!dfn[n]){
			tarjan(i,-1);
		}
	}
	memset(dfn,0,sizeof(dfn));
	for(int i = 1;i<=n;i++){
		if(!dfn[i]){
			bcc_cnt++;
			dfs(i);
		}
	} 
}
```
# 有桥连通图变双连通图
求出所有的桥，然后删除这些桥边，剩下的每一个都是双连通子图。把每个双连通子图收缩为一个顶点，再把桥边加回来，这个图一定是一棵树，边连同度为1.
统计出树中度为1的节点个数，即叶节点的个数，记为leaf,则至少在树上添加(leaf+1)/2条边，可使它连同.
所有结论：当叶子数=1时，将一个有桥图通过加边变成双连通图至少添加的边数为0，否则为(leaf+1)/2
