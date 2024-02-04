---
title: 【斜率优化】luogu P4072 [SDOI2016]征途
date: 2019-09-07 13:53:29 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Pine 开始了从 S到 T 地的征途。
从 S 地到 T地的路可以划分成 n 段，相邻两段路的分界点设有休息站。
Pine 计划用 m 天到达 T 地。除第 m 天外，每一天晚上 Pine 都必须在休息站过夜。所以，一段路必须在同一天中走完。
Pine 希望每一天走的路长度尽可能相近，所以他希望每一天走的路的长度的方差尽可能小。
帮助 Pine 求出最小方差是多少。
设方差是 v ，可以证明，v×m^2 是一个整数。为了避免精度误差，输出结果时输出 v×m^2
#  输入
第一行两个数 n、 m。 第二行 n 个数，表示 n 段路的长度。

#  输出
一个数，最小方差乘以 m^2 后的值。

#  样例输入
```
5 2
1 2 5 8 6
```
样例输出
```
36
```
提示
对于 30% 的数据，1≤n≤10 对于 60% 的数据，1≤n≤100 对于 100% 的数据，1≤n≤3000
保证从S 到T 的总路程不超过 30000
# 解答
首先摆出方差的计算公式
$S^2 = \frac{\sum(x-{ x'})^2}{m}$
但是由于题面求得是$S^2m^2$所以题面可以化为:$S^2m^2 = m*\sum(x-x')^2$
化简得
$$\begin{aligned}
v &= \frac{\sum_{i=1}^{m}(\overline r - r_i)^2}{m}\\
  &= \frac{\sum_{i=1}^{m}r_i^2 + m * (\overline r)^2 - 2 * (\overline r) * \sum_{i=1}^{m}r_i}{m}\\
  &= \frac{\sum_{i=1}^{m}r_i^2 + m * (\frac{\sum_{i=1}^{m}r_i}{m})^2 - 2 * \frac{(\sum_{i=1}^{m}r_i)^2}{m}}{m}\\
  &=- \frac{(\sum_{i=1}^{m}r_i)^2}{m ^ 2} + \frac{\sum_{i=1}^{m}r_i^2}{m}
\end{aligned}
\begin{aligned}
v * m ^ 2 &= m * \sum_{i=1}^{m}r_i^2 - (\sum_{i=1}^{m}r_i) ^ 2\\
\end{aligned}$$
后面是一个定值，所以只要求前面最大就好了。
老套路dp
$f[i][k] = min(f[i][k], f[j][k - 1] + (sum[j] - sum[i])^2)$
然后画柿子
$\begin{aligned}
f[t][k - 1] + (sum[t] - sum[i])^2 &< f[j][k - 1] + (sum[j] - sum[i]) ^ 2\\
(f[t][k - 1] + sum[t] ^ 2) - (f[j][k - 1] + sum[j] ^ 2) &< 2 * sum[i] * (sum[t] - sum[j])\\
\frac{(f[t][k - 1] + sum[t] ^ 2) - (f[j][k - 1] + sum[j] ^ 2)}{2 * (sum[t] - sum[j])} &< sum[i]
\end{aligned}$
斜率优化就好了
这篇题解因为我太懒了，所以直接把这篇博客的公式抄了下来：
[博客](https://www.cnblogs.com/ztlztl/p/10623347.html)
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# define int long long
using namespace std;
const int MAXN = 3010;
int read(){
    int data=0;int w=1; char ch=0;
    ch=getchar();
    while(ch!='-' && (ch<'0' || ch>'9')) ch=getchar();
    if(ch=='-') w=-1,ch=getchar();
    while(ch>='0' && ch<='9') data=(data<<3)+(data<<1)+ch-'0',ch=getchar();
    return data*w;
}
int q[MAXN],head,tail;
int dp[MAXN][MAXN];
int sum[MAXN];
int n,m,sn;
inline int S(int x){return x*x;}
double slope(int d,int j,int k){
	return double(dp[j][d]+S(sum[j])-dp[k][d]-S(sum[k]))/double((sum[j]-sum[k]));
}
signed main(){
	n = read(),m = read();
	memset(dp,0x3f,sizeof(dp));
	for(int i = 1;i<=n;i++)sum[i] = sum[i-1]+read();
	for(int i = 1;i<=n;i++)dp[i][1] = S(sum[i]);
	for(int i = 2;i<=m;i++){
		head = tail = 1;tail--;
		for(int j = 1;j<=n;j++){
			while(head<tail&&slope(i-1,q[head],q[head+1])<2.0*sum[j])head++;
			int k = q[head];
			dp[j][i] = dp[k][i-1]+S(sum[j]-sum[k]);
			while(head<tail&&slope(i-1,j,q[tail])<slope(i-1,q[tail],q[tail-1]))tail--;
			q[++tail] = j;
		}
	}
	cout<<m*dp[n][m]-S(sum[n]);
	return 0;
} 
```
