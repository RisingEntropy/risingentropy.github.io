---
title: luogu P2341受欢迎的牛 
date: 2018-09-22 11:07:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
每头奶牛都梦想成为牛棚里的明星。被所有奶牛喜欢的奶牛就是一头明星奶牛。所有奶牛都是自恋狂，每头奶牛总是喜欢自己的。奶牛之间的“喜欢”是可以传递的——如果A喜欢B，B喜欢C，那么A也喜欢C。牛栏里共有N 头奶牛，给定一些奶牛之间的爱慕关系，请你算出有多少头奶牛可以当明星。
# 输入输出格式
#  输入格式：
第一行：两个用空格分开的整数：N和M
第二行到第M + 1行：每行两个用空格分开的整数：A和B，表示A喜欢B
#  输出格式：
第一行：单独一个整数，表示明星奶牛的数量
#  输入输出样例
输入样例# 1:
3 3
1 2
2 1
2 3
输出样例# 1:
1
# 解答
其实这道题应该不是特别难，就是简单的tarjan+缩点。缩点的话，就是用染色的思想，染上同一个颜色的点集，即可缩为一个点。
然后计算出度为0的点集，**注意，这里的点集是指缩点了以后的点集，既原来这里可能是一个强连通分量,因为如果在同一个强连通分量里面的奶牛，受欢迎程度是同样的，所以需要一个数组来记录每一个缩点后的点原来有多少个点~~有点绕~~**详见代码
```cpp
# include <iostream>
using namespace std;
const int maxn = 10005;
const int maxm = 50005;
struct edge{
	int f,t,next;
}edges[maxm];
int head[maxn];
int top;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].f = f;
	head[f] = top;
}//前向星存图 
int inline minn(int x,int y){return x>y?y:x;}
int stack[maxn];//tarjan需要的一个栈 
int dfn[maxn];
int low[maxn];
int dfn_sum;
int color[maxn];
int color_val;
int stop;
int col_cnt[maxn];//计算每个缩点后的点原来有几个点 
bool instack[maxn];//标记是否在栈中，方便找low 
void tarjan(int x){//求强连通分量 
	dfn[x]=low[x]=++dfn_sum;
	instack[x] = true;
	stack[++stop] = x;
	for(int i = head[x];i!=0;i = edges[i].next){
		int t = edges[i].t;
		if(!dfn[t]){
			tarjan(t);
			low[x] = minn(low[x],low[t]);
		}else if(instack[t]){
			low[x] = minn(low[x],dfn[t]);
		}
	}
	if(low[x]==dfn[x]){
		instack[x] = false;
		color[x] = ++color_val;
		col_cnt[color_val]++;//点x算一个点，所以要在这里给它加上去 
		while(stack[stop]!=x){
			color[stack[stop]]=color_val;//其实就是染色的思想缩点 
			instack[stack[stop--]] = false;
			col_cnt[color_val]++;
		}
		stop--;//在栈里又找到了x，要把它给删掉 
	}
}
int outdegree[maxn];//每个顶点(把同一个强连通分量里面的点缩点缩成一个点) 的出度 
int main(void){
	ios::sync_with_stdio(false);
	int n,m;
	cin>>n>>m;
	int tx,ty;
	for(int i = 1;i<=m;i++){
		cin>>tx>>ty;
		add(tx,ty);
	}
	for(int i = 1;i<=n;i++){
		if(!dfn[i]){
			tarjan(i);
		}
	}
	for(int i = 1;i<=n;i++){
		for(int j = head[i];j!=0;j = edges[j].next){
			int t = edges[j].t;
			if(color[i]!=color[t]){
				outdegree[color[i]]++;//每个点(缩点之后的点)的出度 
			}
		}	
	}
	int zero = 0;
	for(int i = 1;i<=color_val;i++){
		if(outdegree[i]==0){//出度为0则符合题意 
			if(zero!=0){//若有2个出度为0的点，则说明不存在最受欢迎的奶牛 
				cout<<0;
				return 0;
			}
			zero = i;
		}
	}
	cout<<col_cnt[zero];
	return 0;
}
```