---
title: 【数论】3898 Sumdiv
date: 2019-08-22 20:49:53 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
求 $A^B$ 的所有约数之和 mod 9901。

# 输入
输入两个整数 A,B

# 输出
输出答案 mod 9901。

#  样例输入
```
2 3
```
#  样例输出
```
15
```
提示
样例说明
23=8，8的所有约数为 1,2,4,8，1+2+4+8=15,15 mod 9901=15，因此输出 15
数据范围与提示
对于全部数据，$0≤A,B≤5×10^7$
# 解答
唯一分解定理，把A分解为如下形式：$$\prod_j\sum\limits_{i = 0}^{ci} P_j^{i}$$
然后由于是$B$次方，所以每一个$c_i$都要扩大$B$倍，对于每一个$p_i$可以使用等比数列求和公式算出它的值为$$\frac{p_i^{n+1}-1}{1-p_i}$$对上面处理一个快速幂，对于下面处理了一个逆元。完事了。
代码:
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# define int long long
using namespace std;
const int mod = 9901;
int fp(int b,int p){
	int ans = 1;
	while(p){
		if(p&1)ans = ans*b%mod;
		b = b*b%mod;
		p>>=1;
	}
	return ans;
}
signed main(){
	int a,b;scanf("%d%d",&a,&b);
	int ans = 1;
	register int cnt = 0;
	for(register int i = 2;i<=a;i++){
		cnt = 0;
		while(a%i==0)cnt++,a/=i;
		if(cnt)ans = (ans*(((fp(i,cnt*b+1)-1+mod)%mod)*fp(i-1,mod-2)%mod))%mod;
		if(a==1)break;
	}
	printf("%d",ans);
	return 0;
}
```