---
title: 【组合数学】bzoj3260跳
date: 2019-08-20 18:20:45 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
邪教喜欢在各种各样空间内跳。

现在，邪教来到了一个二维平面。在这个平面内，如果邪教当前跳到了(x,y)，那么他下一步可以选择跳到以下4个点：(x-1,y), (x+1,y), (x,y-1), (x,y+1)。

而每当邪教到达一个点，他需要耗费一些体力，假设到达(x,y)需要耗费的体力用C(x,y)表示。

对于C(x,y)，有以下几个性质：

1、若x=0或者y=0，则C(x,y)=1。

2、若x>0且y>0，则C(x,y)=C(x,y-1)+C(x-1,y)。

3、若x<0且y<0，则C(x,y)=无穷大。

现在，邪教想知道从(0,0)出发到(N,M)，最少花费多少体力（到达(0,0)点花费的体力也需要被算入）。

由于答案可能很大，只需要输出答案对10^9+7取模的结果。

#  输入
读入两个整数N，M，表示邪教想到达的点。

#  输出
输出仅一个整数，表示邪教需要花费的最小体力对10^9+7取模的结果。

#  样例输入
```
1 2
```
#  样例输出
```
6
```
提示
【数据说明】
对于10%的数据，满足N, M<=20；
对于30%的数据，满足N, M<=100；
对于60%的数据，满足min(N,M)<=100；
对于100%的数据，满足0<=N, M<=10^12，N*M<=10^12。
# 解答
把整个表格顺时针旋转45度就会发现这是一个杨辉三角。于是乎我们不妨设$n>m$，那么就有答案为：
$$N+\sum C_{N+i}^{i}$$
有因为有如下推论
$$\sum\limits_{i=0}^MC_{N+i}^{i} = C_{M+N+1}^{M}$$
然后就可以直接计算了
代码：
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
const long long mod = (int)1e9+7;
long long fp(long long b,long long p){
	int ans = 1;
	while(p){
		if(p&1)ans = ans*b%mod;
		b = b*b%mod;
		p>>=1;
	}
	return ans;
}
long long n,m;
int main(){
	scanf("%lld%lld",&n,&m);
	if(n<m)swap(n,m);
	n%=mod;
	long long ans = 1,ansb = 1;
	for(long long i = 1;i<=m;i++){
		ans = ans * ((n+m+2-i+mod)%mod)%mod;
		ansb = ansb*i%mod;
	}
	ans = ((ans*fp(ansb,mod-2)%mod+n)%mod+mod)%mod;
	printf("%lld",ans);
	return 0;
} 
```