---
title: tarjan求割点and割边
date: 2018-09-24 15:42:56 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

tarjan 求割点
```cpp
//tarjan find cut point
int stack[10000];
int dfn[10000];
int low[10000];
int stop;
int dfn_cnt;
bool iscut[1000];
int root;
/*
割点判断定理：
对于一个点 u，有以下两种情况：
如果 u 是根节点，那么当它有多于一个子树时，它就是割点
如果 u 不是根节点，并且 u 为 v 在搜索树中的父亲，当 dfn[ u ] ≤ low[ v ] 时，它就是割点
【割点】 
*/
void tarjan(int x){
	low[x] = dfn[x] = ++dfn_cnt;
	stack[++top] = x;
	int child = 0;
	for(int i = head[x];i!=0;i = edges[i].next){
		if(!dfn[i]){//下一个点没有被访问过; 
			tarjan(edges[i].t);
			child++;
			low[x] = min(low[x],low[edges[i].t]);
			if(x==root&&child>1){//点x是树根节点并且有超过两个子树，那么它是割点 
				iscut[x] = true;
			}
			if(x!=root&&low[edges[i].t]>=dfn[x]){//如果x不是树根节点且dfn[u]<=low[v]那么它是割点，见割点判断定理 
				iscut[x] = true;
			}
		}else{
			low[x] = min(low[x],dfn[edges[i].t]) ;
		}
	}
}
//root 为每个搜索树的开始点 
//eg:
	for(int i = 1;i<=n;i++){
		if(!dfn[i]){//这个点没被访问过
			root = i;
			tarjan 
			
		}
	}
```

# 割边
```cpp
/*
判定定理：如果一条搜索树上的边，连接着两个结点xy，且x是y的父亲，且满足low[y]>dfn[x]，那么就是割边了
*/
//这个板子可能暂时有问题
void tarjan(int x,int fa){
	low[x] = dfn[x] = ++dfn_cnt;
	for(int i = head[x];i!=0;i = edges[i].next){
	    int v = edges[i].t;
	    if(!dfn[v]){
	        tarjan(v,x);
	        low[x]=min(low[v],low[x]);
	       if(low[v]>dfn[x]){
	        iscut[i]=iscut[i^1]=true;//判定定理
	       }
	    }else if(dfn[x]>dfn[v]&&v!=fa){
	       low[x] = min(dfn[v],low[x]);
	    }
	}
}
```