---
title: 【矩阵快速幂】SCOI2009迷路
date: 2019-08-23 10:27:04 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Windy 在有向图中迷路了。 该有向图有 N 个节点，Windy 从节点 0 出发，他必须恰好在 T 时刻到达节点 N−1
现在给出该有向图，你能告诉 Windy 总共有多少种不同的路径吗？
注意：Windy 不能在某个节点逗留，且通过某有向边的时间严格为给定的时间。
#  输入
第一行包含两个整数，N,T

接下来有 N 行，每行一个长度为 N 的字符串。第 i 行第 j 列为 0 表示从节点 i 到节点 j 没有边，为 1 到 9 表示从节点 i 到节点 j 需要耗费的时间。

#  输出
包含一个整数，可能的路径数，这个数可能很大，只需输出这个数除以 2009 的余数。

#  样例输入 
```
样例输入 1
2 2
11
00
样例输出 1
1
样例说明 1
0→0→1 

样例输入 2
5 30
12045
07105
47805
12024
12345
样例输出 2
852
```
# 解答
其实很简单的一道题，只需要你做过[牛继电器](https://www.luogu.org/problem/P2886)，发现边权不大，拆点就好了额。
解答一下下为什么可以用矩阵快速幂来代替floyd计算经过k条边的最短路？
首先假设我们有两个矩阵$A$和$B$分别表示经过$x$和$y$条边的最短路的长度。那么要得到经过$x+y$条边的最短路，显然是：$min\{A[i][k]+B[k][j]\}$，然后最开始我们可以轻易计算出经过1条边的最短路，那么是不是计算k次就可得到答案了呢？于是乎矩阵快速幂一下就好了。Orz
代码:
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# define clear(x) memset(x,0,sizeof(x))
using namespace std;
const int MAXN = 101;
const int mod = 2009;
int n;
struct matrix{
	int map[MAXN][MAXN];
	void clean(){
		clear(map);
		for(int i = 1;i<=n*9;i++)map[i][i] = 1;
	}
	matrix operator*(const matrix &m2){
		matrix res;clear(res.map);
		for(int i = 1;i<=n*9;i++){
			for(int j = 1;j<=n*9;j++){
				for(int k = 1;k<=n*9;k++){
					res.map[i][j]+=map[i][k]*m2.map[k][j];
				}
				res.map[i][j]%=mod;
			}
		}
		return res;
	}
};
matrix fp(matrix b,int p){
	matrix res;res.clean();
	while(p){
		if(p&1)res = res*b;
		b = b*b;
		p>>=1;
	}
	return res;
}
char s[MAXN];
matrix map;
int main(){
	int T;
	scanf("%d%d",&n,&T);
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=8;j++){
			map.map[i+j*n][i+(j-1)*n] = 1;
		}
	}
	int d;
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=n;j++){
			scanf("%1d",&d);
			map.map[i][j+(d-1)*n] = 1;
		}
	}
	matrix res = fp(map,T);
	printf("%d",res.map[1][n]);
	return 0;
}
```
