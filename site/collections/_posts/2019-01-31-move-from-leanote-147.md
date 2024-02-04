---
title: bzoj 2721 樱花
date: 2019-01-31 11:34:59 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
![enter image description here](https://cdn.risingentropy.top/images/posts/c526e01ab64412baf0004ac.png)
![enter image description here](https://cdn.risingentropy.top/images/posts/c526e01ab64412baf0004ac.png)
![enter image description here](https://cdn.risingentropy.top/images/posts/c526e01ab64412baf0004ac.png)
![enter image description here](https://cdn.risingentropy.top/images/posts/c526e01ab64412baf0004ac.png)
# 解答
瘤子题一道。我们考虑化简:
$$\frac{1}{x}+\frac{1}{y}=\frac{1}{n!}$$
~~显然~~$y$必须大于$n!$，不妨设$$y = n!+t$$
那么
$$\frac{1}{x}+\frac{1}{n!+t} = \frac{1}{n!}$$
通分化简
$$n!^2+tn!+xn! = x(n!+t)$$
约去$xn!$
$$n!^2+tn!=xt$$
同时约去t
$$\frac{n!^2}{t}+n!=x$$
所以，t是$n!^2$的因数。
根据因数计算计算公式：
$$F(x) = (p_1+1)(p_2+1)(p_3+1)(p_4+1)...(p_m+1)$$
所以做一个线筛，筛出所有质数。然后统计次幂就好了。
# 特别注意
我一开始写代码的时候，MAXN 设的值为1e+10，然后筛的时候也筛到了1e6+10;但是开1e6+10的数组最大下表为1e6+9，就溢出了一位，然鹅我的cnt计数变量恰好定义在筛的质数的后面，就被覆盖了，cnt就永远是0.但是在bzoj和luogu上能AC，因为这两个OJ的编译器是后定义的变量先储存。woj和loj就不一样了了，先定义的先储存于是WA声一片。
代码：
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
const int MAXN = (int)1e6+10;
bool not_prime[MAXN];
int primes[MAXN];int cnt;
int factors[MAXN];
int xxn;
int mn[MAXN];
void get_prime(){
	not_prime[1] = true;
	for(int i = 2;i<MAXN;i++){
		if(!not_prime[i]){
			primes[++cnt] = i;
			mn[i] = cnt;
		}
		for(int j = 1;j<=cnt&&i*primes[j]<MAXN;j++){
			not_prime[i*primes[j]] = true;
			mn[i*primes[j]] = j;
			if(i%primes[j]==0)break;
		}
	}
}
void cal(){
	for(int i = 2;i<=xxn;i++){
		int x = i;
		while(x!=1){
			factors[mn[x]]++;
			x/=primes[mn[x]];
		}
	}
}
const int mod = (int)1e9+7;
int main(){
	cin>>xxn;
	get_prime();
	cal();
	long long ans = 1;
	for(int i = 1;i<=xxn;i++){
		ans = ans * 1LL * (1+factors[i]*2)%mod;
	}
	cout<<ans;
	return 0;
	
}
```