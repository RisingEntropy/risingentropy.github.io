---
title: 【数论】bzoj1209
date: 2019-08-20 16:56:08 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有一个密码箱，0到n-1中的某些整数是它的密码，且满足。如果a和b都是它的密码，那么（a+b）%n也是它的密码（a，b）可以相等。%表示整除取余。某人试了k次密码，前k-1次都失败了，最后一次成功了 问该密码箱最多有多少不同的密码
#  输入
第一行2个整数表示n，k 第二行为k个空格隔开的非负整数。表示每次式的密码 数据保证有合法解
#  输出
一个数，表示结果
#  样例输入
```
42 5
28 31 18 38 24
```
#  样例输出
```
14
```
提示
10%数据n<=10000,k<=100 10%数据n<=10^9,n<=100; 前60%数据k<=1000 100%数据 1<=k<=250 000 ,k<=n<=10^14
标签
数学一本通
# 解答
首先有几个显然的结论

 1. 如果$x$是答案，那么$kx\ mod\ n$也是答案即$kx-tn$也一定是答案
 2. 由裴蜀定理有$kx+tn=gcd(x,n)$一定存在正整数$k$和$t$使得式子成立，所以$gcd(x,n)$一定是密码，反之若$x$不是密码，那么$gcd(x,n)$一定不是密码
 
于是有了上述结论就可以开始计算了。首先计算出每一个数与$n$的$gcd$记为$a[i]$，然后枚举$a[k]$的因数，若存在$x$不为其他$a$的项的因数，那么$x$及其倍数就是答案。有一点细节在代码里面
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <algorithm>
using namespace std;
const int MAXN = 250100; 
long long gcd(long long a,long long b){return b==0?a:gcd(b,a%b);}
long long a[MAXN];
int tot;
bool check(int x){
	for(int i = 1;i<=tot;i++)
		if(a[i]%x==0)
			return false;
	return true;
}
int main(){
	long long n,k;
	scanf("%lld%lld",&n,&k);
	for(int i = 1;i<=k;i++)scanf("%lld",&a[i]);
	for(int i = 1;i<=k;i++)a[i] = gcd(a[i],n);
	sort(a+1,a+k);tot = unique(a+1,a+k)-a-1;
	long long ans = 0;
	for(long long i = 1;i*i<=a[k];i++){
		if(a[k]%i==0){
			if(check(i)){
				ans = n/i;
				break;
			}
			else if(check(a[k]/i))ans = n/a[k]*i;
		}
	}
	printf("%lld",ans);
	return 0;
}
```