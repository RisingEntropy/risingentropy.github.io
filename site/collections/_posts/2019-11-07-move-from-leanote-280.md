---
title: unknown title
date: 2019-11-07 08:18:54 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
对于给出的n个询问，每次求有多少个数对(x,y)，满足a≤x≤b，c≤y≤d，且gcd(x,y) = k，gcd(x,y)函数为x和y的最大公约数。

#  输入
第一行一个整数n，接下来n行每行五个整数，分别表示a、b、c、d、k

#  输出
共n行，每行一个整数表示满足要求的数对(x,y)的个数

#  样例输入
```
2
2 5 1 5 1
1 5 1 5 2
```
#  样例输出
```
14
3
```
提示
100%的数据满足：1≤n≤50000，1≤a≤b≤50000，1≤c≤d≤50000，1≤k≤50000
# 解答
第一次自己把数学题的式子推出来Orz。
题目要求求：$\sum \limits_{i=1}^{n}\sum\limits_{j=1}^{m}[gcd(i,j)=k]$
$$
\sum\limits_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum\limits_{j=1}^{\lfloor\frac{m}{k}\rfloor}[gcd(i,j)=1]\\\sum\limits_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum\limits_{j=1}^{\lfloor\frac{m}{k}\rfloor}\sum_{d|gcd(i,j)}\mu(d)\\\sum\limits_{d=1}^{min(n,m)}\mu(d)\sum\limits_{i=1}^{\lfloor\frac{n}{kd}\rfloor}\sum\limits_{j=1}^{\lfloor\frac{m}{kd}\rfloor}1\\\sum\limits_{d=1}^{min(n,m)}\mu(d)\lfloor\frac{n}{kd}\rfloor\lfloor\frac{m}{kd}\rfloor
$$
对于后面下取整的式子可以整除分块，然后前面那一坨$\mu$可以做一个前缀和，在整除分块的时候同时计算了。
然后进行容斥，$ans(b,d)-ans(a,c-1)-ans(b-1,d)+ans(b-1,c-1)$
代码：
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 50010;
typedef long long LL;
inline char nc(){
	static char buf[100000],*p1=buf,*p2=buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
# define nc getchar
template<typename T>
inline void read(T &x){
	x = 0;T f = 1;
	char c = nc();
	while(c<'0'||c>'9'){if(c=='-')f =  -1;c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
	x*=f;
}
int prime[MAXN],mu[MAXN],cnt,sum[MAXN];
bool vis[MAXN];
void getprime(int n){
	mu[1] = 1;
	for(int i = 2;i<=n;i++){
		if(!vis[i]){prime[++cnt] = i;mu[i] = -1;}
		for(int j = 1;j<=cnt&&prime[j]*i<=n;j++){
			vis[i*prime[j]] = true;
			if(i%prime[j]==0)break;
			else mu[i*prime[j]]=-mu[i];
		}
	}
	for(int i = 1;i<=n;i++)sum[i] = sum[i-1]+mu[i];
}
int calc(int a,int b,int k){
	LL ans = 0;int limit = min(a,b);
	for(int l = 1,r;l<=limit;l = r+1){
		r = min(a/(a/l),b/(b/l));
		ans+=(a/(l*k))*(b/(l*k))*(sum[r]-sum[l-1]);
	}
	return ans;
}
int main(){
	getprime(50000);
	int T;read(T);
	int a,b,c,d,k;
	while(T--){
		read(a),read(b),read(c),read(d),read(k);
		printf("%d\n",calc(b,d,k)-calc(b,c-1,k)-calc(a-1,d,k)+calc(a-1,c-1,k));
	}
	return 0;
}

```