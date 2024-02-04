---
title: 【概率期望】CF398B Painting The Wall
date: 2019-10-11 20:18:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有一个 $n \times n$的网格，其中 $m$ 个格子上涂了色。每次随机选择一个格子（有可能是涂过色的格子）涂色，求让网格每一行每一列都至少有一个格子涂了色的操作次数期望。
输入输出样例
输入
```
5 2
2 3
4 1
```
输出
```
11.7669491886
```
# 解答
一类非常经典的概率DP问题，由于许多概率dp是倒着推得，所以我们用dp[i][j]表示还剩i行j列的的期望步数，那么显然有$dp[0][0] = 0.0$，然后考虑转移，有如下四类转移

 1. 从dp[i-1][j-1]转移，那么~~显然~~有：$dp[i][j]+=dp[i-1][j-1]*\frac{i*j}{n*n}$
 2. 从dp[i-1][j]转移，那么有：$dp[i][j]+=dp[i-1][j]*\frac{i*(n-j)}{n*n}$
 3. 从dp[i][j-1]转移，那么有：$dp[i][j]+=dp[i][j-1]*\frac{(n-i)*j}{n*n}$
 4. 从dp[i-1][j-1]转移，那么有：$dp[i][j]+=dp[i][j]*\frac{(n-i)*(n-j)}{n*n}$
 5. 加起来，化简得:$$dp[i][j] = \frac{(n*n +dp[i-1][j-1]*i*j+dp[i][j-1]*j*(n-i)+dp[i-1][j]*i*(n-j))}{(n*n-(n-i)*(n-j))}$$
代码：
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 2010;
int markx[MAXN],marky[MAXN];
double dp[MAXN][MAXN];
int n;
int main(){
	double n,m;cin>>n>>m;double row = n,col = n;
	int x,y;
	for(int i = 1;i<=m;i++){
		cin>>x>>y;
		if(!markx[x])markx[x] = true,row--;
		if(!marky[y])marky[y] = true,col--;
	}
	dp[0][0] = 0.0;
	for(int i = 1;i<=n;i++){
		dp[i][0] = dp[i-1][0]+double(n/i);
		dp[0][i] = dp[0][i-1]+double(n/i);
	}
	for(int i = 1;i<=row;i++){
		for(int j = 1;j<=col;j++){
			dp[int(i)][int(j)] = n*n+dp[i-1][j-1]*1.0*i*j+dp[i-1][j]*1.0*i*(n-j)+dp[i][j-1]*1.0*j*(n-i);
			dp[int(i)][int(j)]/=1.0*(n*n-(n-i)*(n-j));
		}
	}
	cout<<dp[int(row)][int(col)];
	return 0;
}
```