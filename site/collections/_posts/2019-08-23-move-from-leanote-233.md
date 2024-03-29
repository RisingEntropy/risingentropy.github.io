---
title: 【数学数论】 [NOI2002]荒岛野人
date: 2019-08-23 19:54:47 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
克里特岛以野人群居而著称。岛上有排列成环行的M个山洞。这些山洞顺时针编号为1,2,…,M。岛上住着N个野人，一开始依次住在山洞C1,C2,…,CN中，以后每年，第i个野人会沿顺时针向前走Pi个洞住下来。
每个野人i有一个寿命值Li，即生存的年数。
下面四幅图描述了一个有6个山洞，住有三个野人的岛上前四年的情况。三个野人初始的洞穴编号依次为1，2，3；每年要走过的洞穴数依次为3，7，2；寿命值依次为4，3，1。
![图片标题](https://cdn.risingentropy.top/images/posts/d5fd440ab64417884002f10.png)

奇怪的是，虽然野人有很多，但没有任何两个野人在有生之年处在同一个山洞中，使得小岛一直保持和平与宁静，这让科学家们很是惊奇。他们想知道，至少有多少个山洞，才能维持岛上的和平呢？
输入格式
第1行为一个整数N(1<=N<=15)，即野人的数目。

第2行到第N+1每行为三个整数Ci, Pi, Li (1<=Ci,Pi<=100, 0<=Li<=106 )，表示每个野人所住的初始洞穴编号，每年走过的洞穴数及寿命值。

输出格式
仅包含一个数M，即最少可能的山洞数。输入数据保证有解，且M不大于10^6。

输入输出样例
输入
```
3
1 3 4
2 7 3
3 2 1
```
输出
```
6
```
说明/提示
对于50% 的数据：$N $的范围是$[1…1,000]$。

对于另外50% 的数据：$N$ 的范围是$[1…100,000]$。

对于100% 的数据：$C $的范围是$[1…1,000,000,000]$，$N$ 个整数中每个数的范围是：$[0…1,000,000,000]$。
# 解答
还是比较好想的一道数论的题。
由于n不是很大，所以我们可以$n^2$枚举任意两对野人。然后考虑枚举$M$由于M不会大于1e6，所以可以过，注意一点就是枚举的M需要从野人初始位置的最大开始枚举，不然一开始可能就有矛盾。
不难列出如下方程：
$C_i+xP_i\equiv C_j+xP_j(mod\ M)$
然后`exgcd`求就好了。
代码：(注意求得时候的符号问题)
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 20;
int p[MAXN],L[MAXN],C[MAXN];
int n;
int gcd(int a,int b,int &x,int &y){
	if(b==0){
		x = 1,y = 0;
		return a;
	}else{
		int d = gcd(b,a%b,x,y);
		int t = x;
		x = y;
		y = t-(a/b)*y;
		return d;
	}
}
bool judge(int M){
	int x,y;
	for(int i = 1;i<=n;i++){
		for(int j = i+1;j<=n;j++){
			int a = p[i]-p[j],b = M,c = C[j]-C[i];
			int g = gcd(a,b,x,y);
			if(c%g)continue;
			a/=g,b/=g,c/=g;
			if(b<0)b*=-1;
			x = (x*c%b+b)%b;
			if(x<=L[i]&&x<=L[j])return false;
		}
	}
	return true;
}
int main(){
	cin>>n;
	int mx = 0;
	for(int i = 1;i<=n;i++)cin>>C[i]>>p[i]>>L[i],mx = max(mx,C[i]);
	int i = mx;
	for(;i;i++)if(judge(i))return 0*printf("%d",i);
	return 0;
}
```