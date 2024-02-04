---
title: oi-HAOI2008硬币购物
date: 2019-10-09 21:03:55 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
硬币购物一共有4种硬币。面值分别为c1,c2,c3,c4。某人去商店买东西，去了tot次。每次带di枚ci硬币，买si的价值的东西。请问每次有多少种付款方法。
#  输入
第一行 c1,c2,c3,c4,tot 下面tot行 d1,d2,d3,d4,s
#  输出
每次的方法数

#  样例输入
```
1 2 5 10 2
3 2 3 1 10
1000 2 2 2 900
```
#  样例输出
```
4
27
```
提示
di,s<=100000
tot<=1000
标签
HAOI2008
# 解答
很好的一道容斥原理的题。首先要知道一个结论，就是这个限制非常难以处理，如果没有限制就好了，那么答案直接跑一个完全背包。$dp[j] += dp[j-v[i]]$转移就好了，但是现在有限制啊，那到底怎么处理呢？然后我在某大佬的博客上看到如下式子，非常生动形象：
$$[2,+\infty)-(3,\infty)=[2,3]$$
于是乎我们计算出没有限制的答案，再减去限制+1到没有限制的答案就可以了，但是怎么同时把4个全部考虑上去呢？当然是枚举每个集合，然后使用容斥原理就可以考虑4个东西对此的影响了。但是要注意一点，就是枚举子集的时候，如果是奇数就-1，否则+1，因为我们计算的是减掉的那一坨，而不是容斥原理公式中对答案正贡献的一坨。
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# define int long long
using namespace std;
const int MAXN = (int)5e5+10;
inline char nc(){
	static char buf[100000],*p1 = buf,*p2 = buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
template<typename T>
void read(T &x){
	x = 0;
	char c = nc();
	while(c<'0'||c>'9')c = nc();
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
}
int c[5],d[5];
long long dp[100010];
signed main(){
	# ifdef BEYONDSTARS
		freopen("testdata.in","r",stdin);
	# endif
	read(c[1]);read(c[2]);read(c[3]);read(c[4]);
	register int tot;read(tot);int s;
	dp[0] = 1;
	for(register int i = 1;i<=4;i++)for(int j = c[i];j<=100000;j++)dp[j]+=dp[j-c[i]];
	while(tot--){
		read(d[1]);read(d[2]);read(d[3]);read(d[4]);read(s);
		long long res = 0;
		for(int i =0;i<=15;i++){
			long long now = s,k = 1;
			for(int j = 1;j<=4;j++){
				if(i&(1<<j-1))k*=-1,now-=(d[j]+1)*c[j];
			}
			if(now>=0)res+=k*dp[now];
		}
		printf("%lld\n",res);
	}
	return 0;
}
```