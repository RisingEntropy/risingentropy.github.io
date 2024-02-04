---
title: 【经过k条边的最短路】bzoj1706
date: 2019-08-19 21:11:10 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Description
FJ的N(2 <= N <= 1,000,000)头奶牛选择了接力跑作为她们的日常锻炼项目。至于进行接力跑的地点 自然是在牧场中现有的T(2 <= T <= 100)条跑道上。 农场上的跑道有一些交汇点，每条跑道都连结了两个不同的交汇点 I1_i和I2_i(1 <= I1_i <= 1,000; 1 <= I2_i <= 1,000)。每个交汇点都是至少两条跑道的端点。 奶牛们知道每条跑道的长度length_i(1 <= length_i <= 1,000)，以及每条跑道连结的交汇点的编号 并且，没有哪两个交汇点由两条不同的跑道直接相连。你可以认为这些交汇点和跑道构成了一张图。 为了完成一场接力跑，所有N头奶牛在跑步开始之前都要站在某个交汇点上（有些交汇点上可能站着不只1头奶牛）。当然，她们的站位要保证她们能够将接力棒顺次传递，并且最后持棒的奶牛要停在预设的终点。 你的任务是，写一个程序，计算在接力跑的起点(S)和终点(E)确定的情况下，奶牛们跑步路径可能的最小总长度。显然，这条路径必须恰好经过N条跑道。
#  Input
* 第1行: 4个用空格隔开的整数：N，T，S，以及E

* 第2..T+1行: 第i+1为3个以空格隔开的整数：length_i，I1_i，以及I2_i， 描述了第i条跑道。

#  Output
* 第1行: 输出1个正整数，表示起点为S、终点为E，并且恰好经过N条跑道的路 径的最小长度

#  Sample Input
```
2 6 6 4
11 4 6
4 4 8
8 4 9
6 6 8
2 6 9
3 8 9
```
#  Sample Output
```
10
```
# 解答
骚题，反正我是想不到，尤其是教练把它放在图论专题。。。。明明是线代的内容嘛。。。。
我们可以发现矩阵乘法和floyd很像，于是乎我们~~不难发现~~可以把矩阵的乘法换成floyd，(其实想想也是有道理的)，然后乘个n次就好了。。。。~~我太菜了~~
代码：
```cpp
# include <cstring>
# include <cstdio>
# include <iostream>
# include <algorithm>
using namespace std;
const int MAXN = 210;
int HASH[MAXN*MAXN],tot;
struct matrix{
	int a[MAXN][MAXN];
	matrix(){
		memset(a,0x3f,sizeof(a));
	}
};
matrix operator*(const matrix &m1,const matrix &m2){
	matrix ret;
	for(int k = 1;k<=tot;k++){
		for(int i = 1;i<=tot;i++){
			for(int j = 1;j<=tot;j++){
				ret.a[i][j] = min(ret.a[i][j],m1.a[i][k]+m2.a[k][j]);
			}
		}
	}
	return ret;
}
matrix qp(matrix a,int p){
	matrix res = a;
	while(p){
		if(p&1)res = res*a;
		a = a*a;
		p>>=1;
	}
	return res;
}
int main(){
	int n,m,S,E;
	scanf("%d%d%d%d",&n,&m,&S,&E);
	int f,t,w;
	matrix b;
	for(int i = 1;i<=m;i++){
		scanf("%d%d%d",&w,&f,&t);
		if(!HASH[f])HASH[f] = ++tot;
		if(!HASH[t])HASH[t] = ++tot;
		f = HASH[f],t = HASH[t];
		b.a[f][t] = b.a[t][f] = w;
	}
	matrix res = qp(b,n-1);
	printf("%d\n",res.a[HASH[S]][HASH[E]]);
	return 0;
}
```