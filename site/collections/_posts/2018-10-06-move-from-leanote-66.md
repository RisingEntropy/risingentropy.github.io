---
title: 反素数luogu P1463
date: 2018-10-06 10:28:52 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
对于任何正整数x，其约数的个数记作g(x)。例如g(1)=1、g(6)=4。
如果某个正整数x满足：g(x)>g(i) 0`<`i`<`x，则称x为反质数。例如，整数1，2，4，6等都是反质数。
现在给定一个数N，你能求出不超过N的最大的反质数么？
#  输入格式：
一个数N（1<=N<=2,000,000,000）。
#  输出格式：
不超过N的最大的反质数。
#  输入
```
1000
```
#  输出
```
840
```
# 解答
其实这是一个数学题。设答案为m,且$m=p_1^{c_1}\times p_2^{c_2}\times p_3^{c_3}...\times p_n^{c_n}$那么要使m的因数最大，那么必有$c_1\geq c_2\geq c_3...$原因是因为因数个数相同时，较小的质因数个数越多，那么对于这个数的值的贡献越小，这个数在范围内就越有可能大。证明的话，可以将ci从大到小排列$c_1\leq c_2 \leq..c_n$然后发现新的数的约数个数与m相等，那么，m'小于m，所以不成立。
因数个数公式：
$$\prod_{i=1}^{m}(c_i+1)(m为质因数个数)$$
# 代码
```cpp
# include <iostream>
# include <string>
# include <cstring>
using namespace std;
int primes[13]={0,2,3,5,7,11,13,17,19,23,29,31,37};//一共就这么几个素数，在题干中的范围内，不可能再有其他质因数了
long long ans = 0;
long long n;
int MAX = 0;
void dfs(int prime_cnt,long long now,int nums){//暴搜
	if(prime_cnt>=12)return;//如果因数个数大于12,那么不可能了，剪掉
	if(nums>MAX){//找到了因数多的数
		MAX = nums;
		ans = now;
	}
	if(MAX==nums&&ans>now){//如果当前数小于已找到的答案，且因数个数相同，那么我们取较小的那个，因为这样更可能获得更多的因数
	//当初自己迷惑这里，其实是不必要的，因为在范围内，找到因数个数更多的数是，在上面就已经更新了，这里就不会更新了，否则，因数个数相同，取较小的值
		ans = now;
	}
	for(int i = 1;i<=63;i++){
		if(primes[prime_cnt]*now>n)break;//如果超了,舍弃不要
		dfs(prime_cnt+1,now*=primes[prime_cnt],nums*(i+1));//根据一个数的因数个数公式
	}
	
}

int main(void){
	ios::sync_with_stdio(false);
	cin>>n;
	dfs(1,1,1);
	cout<<ans;
}
```