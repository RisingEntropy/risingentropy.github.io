---
title: 【区间DP】glod在奔跑中吃草
date: 2019-09-29 14:04:43 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
在一块又长又直的田里有N个草丛，可以将田看作是一个线性数轴，将草丛看作是数轴上的一个整数点。
Bessie从某个特殊的位置L (1 <= L <= 1,000,000)开始，可以沿着两个方向在穿越数轴（可以反向），到达所有的草丛并吃掉它。她移动的速度是一定的（一个单位时间移动一个单位距离），当她到达草丛时就立即吃掉它。
草丛变质后就不能吃了，我们称草丛的"变质期"就是从Bessie开始移动到吃掉该草丛前的这段时间。当所有的草丛都吃掉后，Bessie想让变质期尽可能地小。
找到在Bessie吃掉所有的草丛后，使得所有草丛的变质期之和最小。
#  输入
第1行：两个用空格隔开的整数：N（<=1000）和L
第2行至N+1行：每行包括一个整数P，表示草丛的位置(1 <= P <= 1,000,000)。
#  输出
1行：一个整数，表示Bessie在吃掉所有的草丛后，使得所有草丛的变质期之和最小。
#  样例输入
```
4 10
1
9
11
19
```
#  样例输出
```
44
```
# 提示
输入解释：
4个草丛的位置：1, 9, 11和19，Bessie开始的位置在10。
输出解释：
Bessie可以按下列路线：
开始在10的位置，时间为0
移动到9的位置，时间为1
移动到11的位置，时间为3
移动到19的位置，时间为11
移动到1的位置，时间为29
得到所有的草丛的变质期为1+3+11+29 = 44，也许还有另外的路线可以得到同样的答案，但不能使得它更小。
标签
usaco2006nov-glod
# 解答
区间DP+记忆化搜索，dp[l][r][0/1]表示已经吃完区间$[l,r]$之后，当前在左边/右边，给全局造成的变质期的和最小。
那么显然有如下转移方程式：
$$dp[l][r][0] = min(dp[l-1][r][0]+dis[l,l-1]*(n-(r-l+1)),dp[l][r+1][0]+dis[r,r+1]*(n-(r-l+1)))$$
代码：
```cpp
# include <iostream>
# include <algorithm>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 1010;
const int INF = 1e9;
int dp[MAXN][MAXN][2];
int pos[MAXN];
int n;
int dfs(int l,int r,int d){
	if(l==1&&r==n)return 0;
	if(dp[l][r][d]!=-1)return dp[l][r][d];
	int ret = INF;
	int p;
	if(d==0)p = l;else p = r;
	if(l!=1){
		ret = min(ret,dfs(l-1,r,0)+(pos[p]-pos[l-1])*(n-1-(r-l)));
	}
	if(r!=n){
		ret = min(ret,dfs(l,r+1,1)+(pos[r+1]-pos[p])*(n-1-(r-l)));
	}
	return dp[l][r][d] = ret;
}
int main(){
	int L;scanf("%d %d",&n,&L);
	for(int i = 1;i<=n;i++)scanf("%d",&pos[i]);
	pos[++n] = L;sort(pos+1,pos+1+n);
	int p;
	for(int i = 1;i<=n;i++)if(pos[i]==L){p = i;break;}
	memset(dp,-1,sizeof(dp));
	printf("%d",dfs(p,p,0));
	return 0;
}
```