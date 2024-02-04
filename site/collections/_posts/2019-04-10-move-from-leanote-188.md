---
title: 【期望】绿豆蛙的归宿
date: 2019-04-10 17:02:00 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给出一个有向无环图，起点为1终点为N，每条边都有一个长度，并且从起点出发能够到达所有的点，所有的点也都能够到达终点。绿豆蛙从起点出发，走向终点。
到达每一个顶点时，如果有K条离开该点的道路，绿豆蛙可以选择任意一条道路离开该点，并且走向每条路的概率为 1/K 。 现在绿豆蛙想知道，从起点走到终点的所经过的路径总长度期望是多少？
#  输入
第一行: 两个整数 N M，代表图中有N个点、M条边
第二行到第 1+M 行: 每行3个整数 a b c，代表从a到b有一条长度为c的有向边
#  输出
从起点到终点路径总长度的期望值，四舍五入保留两位小数
#  样例输入 
```
4 4 
1 2 1 
1 3 2 
2 3 3 
3 4 4
```
#  样例输出 
```
7.00
```
提示
对于20%的数据 N<=100
对于40%的数据 N<=1000
对于60%的数据 N<=10000
对于100%的数据 N<=100000，M<=2*N
# 解答
dp[i] 表示到i的期望，显然，n号点的期望长度为0,dp[i] = (dp[j]+w(i,j))/p,倒着拓扑排序，完事。
```cpp
# include <iostream>
# include <queue>
# include <iomanip>
using namespace std;
const int MAXN = 100010;
struct edge{
    int t,w,next;
}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int degree[MAXN];
double k[MAXN];
double dp[MAXN];
int n,m;
void topo(){
	queue<int> q;
	q.push(n);
	while(!q.empty()){
		int top = q.front();q.pop();
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			degree[t]--;
			dp[t] += (dp[top]+double(edges[i].w))/k[t];
			if(degree[t]==0)q.push(t);
		}
	}
}
int main(){
	cin>>n>>m;
	int a,b,c;
	for(int i = 1;i<=m;i++){
		cin>>a>>b>>c;
		add(b,a,c);
		degree[a]++;
		k[a]+=1.0;
	}
	topo();
	cout.setf(ios::fixed);
	cout<<setprecision(2)<<dp[1];
}
```