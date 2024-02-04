---
title: 【斜率优化】特别行动队】
date: 2019-08-25 20:40:23 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
因为懒得调格式问题，直接丢传送门吧。[传送门](https://www.luogu.org/problem/P3628)
# 解答
一道斜率优化的题，话说斜率优化里面的平方都是来恶心人的额。
我们考虑写出一个朴素的dp式子:$$dp[i] = max\{dp[j]+a(s_i-s_j)^2+b(s_i-s_j)+c\}$$
然后丢掉max符号，拆开括号得到$$dp[i] = dp[j]+a\times s_i^2-2as_is_j+as_j^2+bs_i-bs_j+c$$
若决策$j$优于$k$，那么用j-k可以的到以下式子:
$$dp[j]-dp[k]-2a_is_is_j+2as_is_k+as_j^2-as_k^2-bs_j+bs_k>0$$
进一步化简，移项得到$$\frac{dp[j]+as_j^2-bs_j-dp[k]-as_k^2+bs_k}{s_j-s_k}>2as_i$$
然后使用单调队列$O(1)$的维护以下就好了。特别注意一点，由于$a<0$所以我们维护的是一个上凸壳。所以要在取出队首的时候斜率的大小比较需要相反。代码如下：
```cpp
# include <iostream>
# include <cstring> 
# include <cstdio>
using namespace std;
const int MAXN = 1000100;
int read(){
	int x = 0,f = 1;
	char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = getchar();}
	return x*f;
}
long long dp[MAXN];
long long sum[MAXN];
long long a,b,c;
double slope(int j,int k){
	return double(dp[j]+a*(sum[j])*(sum[j])-b*sum[j]-dp[k]-a*(sum[k])*(sum[k])+b*sum[k])/double(sum[j]-sum[k]);
}
int q[MAXN],head,tail;
int n;
int main(){
	n = read(),a = read(),b = read(),c = read();
	long long v;
	for(int i = 1;i<=n;i++){v = read();sum[i] = sum[i-1]+v;}
	head = tail = 1;
	for(int i = 1;i<=n;i++){
		while(head<tail&&slope(q[head],q[head+1])>=2*a*sum[i])head++;//尤其注意这里的斜率比较问题
		int j = q[head];
		dp[i] = dp[j]+a*(sum[i]-sum[j])*(sum[i]-sum[j])+b*(sum[i]-sum[j])+c;
		while(head<tail&&slope(i,q[tail])>slope(q[tail],q[tail-1]))tail--;
		q[++tail] = i;
	}
	printf("%lld\n",dp[n]);
	return 0;
}
```