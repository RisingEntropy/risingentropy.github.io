---
title: 强连通分量
date: 2018-09-19 16:15:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# Kosaraju
基于两次dfs有向图强连通。
1.第一步：对原有的有向图G进行DFS，记录节点访问完的顺序，d[i],d[i]表示第i个访问完的结点是d[i]
1.第二部，选择具有最晚访问完的顶点，对反向图GT进行DFS，删除能够变力道的顶点，构成一个强连通分量。记录一下
3.如果还有顶点没有删除，继续第二部，否则算法结束。
```cpp
# include <iostream>
using namespace std;
int st[10000];//可以用stl stack 代替 
int t = 0;//可以用stl stack 代替 
struct edge{ 
	int t,next;
}edges[100000],edges2[100000];
int head[10000];
int head2[10000];
int top2;
int top;
int visited[10000];
void add1(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
void add2(int f,int t){
	edges[++top2].next = head2[f];
	edges[top2].t = t;
	head2[f] = top2;
}
void dfs(int s){
	visited[s] = true;
	for(int i = head[s];i!=0;i = edges[i].next){
		if(!visited[edges[i].t]){
			dfs(edges[i].t);
		}
	}
	st[++t] = s;
}
void dfs2(int s){
	visited[visited[edges2[s].t] = true;
	for(int i = head[s];i!=0;i = edges2[i].next){
		dfs2(edges[2].t);//可以在此记录强连通分量的顶点 
	}
}
int kosaraju(){
	int sum = 0;
	for(int i = 1;i<=n;i++){
		if(!visited[i]){
			dfs(i);
		}
	}
	memset(visited,false,sizeof(visited));
	for(int i = n;i>=1;i--){//选择具有最晚访问完的顶点，对反图进行dfs 
		if(!visited[st[i]]){
			sum++;
			dfs2(st[i]);
		}
	}
	//强连通分量数 
	return sum;
}
```
# tarjan
Tarjan算法是基于对图深度优先搜索的算法，每个强连通分量为搜索树中的一棵子树。搜索时，把当前搜索树中未处理的节点加入一个堆栈，回溯时可以判断栈顶到栈中的节点是否为一个强连通分量。
再Tarjan算法中，有如下定义。
DFN[ i ] : 在DFS中该节点被搜索的次序(时间戳)
**LOW[ i ] : 为i或i的子树能够追溯到的最早的栈中节点的次序号**
当DFN[i]==LOW[i]时，为i或i的子树可以构成一个强连通分量。
详细解析见[详细的tarjan讲解](http://www.cnblogs.com/shadowland/p/5872257.html)
代码：
```cpp
# include <iostream>
using namespace std;
struct edge{
	int t,next;
}edges[10000];
int head[10000];
int top;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
bool visited[1000];//某个节点是否在栈中
int dfn[1000];
int low[1000];
int dfn_sum;
int stack[10000];
int stop;
int color[10000];//哪个点染什么色，颜色一样的点属于同一个强连通分量 
int color_val = 0;
inline int minn(int x,int y){return x>y?y:x;}
void tarjan(int x){
	dfn[x] = ++dfn_sum;
	low[x] = dfn_sum;
	visited[x] = true;
	stack[++stop] = x;
	for(int i = head[x];i!=0;i = edges[i].next){
		int v = edges[i].t;
		if(dfn[v]==0){
			tarjan(v);
			low[x] = minn(low[x],low[v]);
		}else if(visited[v]){
			low[x] = minn(low[x],dfn[v]);//是回溯到的节点靠前，还是本来已经找到的节点靠前 
		}
	}
	if(dfn[x]==low[x]){
		visited[x] = false;
		color[x] = ++color_val;
		while(stack[top]!=x){
			color[stack[top]] = color_val;
			visited[stack[top--]] = false;
		}
		top--;//点x已经在栈中，并且已经找到了一个强连通分量，上一个在栈中的点x出栈 
	}
} 
```

# 缩点






