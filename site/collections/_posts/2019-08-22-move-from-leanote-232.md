---
title: 【组合数学，计数】CQOI2014」数三角形
date: 2019-08-22 21:04:15 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给定一个 n×m 的网格，请计算三点都在格点上的三角形共有多少个。下图为 4×4 的网格上的一个三角形。
![图片标题](https://cdn.risingentropy.top/images/posts/d5e930fab644141fe007516.png)
注意：三角形的三点不能共线。
#  输入
输入一行，包含两个空格分隔的正整数 m 和 n

#  输出
输出一个正整数，为所求三角形数量。

#  样例输入
```
2 2
```
#  样例输出 
```
76
```
# 解答
正难则反的思想。统计三角形的数量不好统计，但是我们可以统计所有三点对的数量，减去在一条线上的三点对的数量。
对于所有三点对的数量就是$$m*n\choose 3$$
然后考虑如何统计在一条直线上的三点对的数量。
有一个结论：一条过$(0,0)$和$(x,y)$的直线经过的整数点的个数为$gcd(x,y)-1$,于是乎我们枚举每一条直线，统计出这条直线上的整数点的个数，由于我们已经枚举了两个端点。所以中间经过的整数点的个数就是对于这两个端点的不合法的情况，然后由于可以交换两个端点，所以答案要乘以2。
代码如下：
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
using namespace std;
const int MAXN = 1010;
int n,m;
long long gcd(long long a,long long b){return b==0?a:gcd(b,a%b);}
long long C(int n,int m){
	long long res = 1;
	for(long long i = 1;i<=m;i++){
		res = (res*(long long)(n-m+i))/i;
	}
	return res;
}
int main(){
	cin>>n>>m;m++,n++;
	long long ans = C(m*n,3);
	ans -= C(n,3)*m;ans-=C(m,3)*n;
	for(long long i = 2;i<n;i++){
		for(long long j = 2;j<m;j++){
			long long g = gcd(i,j)-1;
			ans-=(n-i)*(m-j)*2*g;
		}
	}
	cout<<ans;
	return 0;
}
```
# 解法2
感谢hzq大佬，教会了我如何正着统计答案。
首先我们首先可以肯定一个矩形里面可以围一些三角形。于是呼枚举每个矩形，考虑矩形内的三角形个数就行了。Orz
统计方法如下

 1. 有一个点在四个顶点，那么答案是(i-1)*(j-1)*4
 2. 有两个点在顶点上，这个有点烦。考虑在同一侧还是在对角线上。如果在同一侧答案就是:2*(i-1)+2*(j-1)，然后统计在对角线的情况。这个是真的烦。答案是(i-1)*(j-1)(好像是这么多吧？我没算过，反正大概就是三角形的面积那样子)。
 3. 统计三个点都在顶点的情况，最简单，直接是4
 
代码：
```cpp
咕咕咕咕
```