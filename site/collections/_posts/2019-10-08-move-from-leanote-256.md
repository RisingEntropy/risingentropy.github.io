---
title: 容斥原理小记
date: 2019-10-08 07:57:23 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 容斥原理
公式
$|\bigcup\limits_{i = 1}^na_i| = \sum\limits_{k = 1}^{n}(-1)^{k-1}\times\sum\limits_{1\leq i_1\le i_2\le i_3...i_k\leq n}|\bigcap\limits_{i = 1}^k a_{i_k}|$
# 例题
woj2592 cost 数：
“给你一个有n个正整数的数列{an}。一个正整数x若满足在数列{an}中存在一个正整数ai，使x≡17（mod ai），那么x就是一个‘cost数’。请问1到m的正整数中，有多少个‘cost数’？”

# 解答
考虑$n==3$的情况，若要计算$[1,m]$中对$a_i$取模为17的数的个数，直接$(m-17)/a_i$就好了若要计算对A和B取模同时为17的数的个数，直接$(m-17)/lcm(A,B)$
同样的，对于更多的数也是如此。
然后这道题就是个比较显然的容斥原理，枚举每个数选还是不选，如果选的数的个数为偶数个，则乘上-1的系数。注意剪枝，因为如果搜索的过程中，lcm已经大于m了，直接`return`，然后从大的开始搜。
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 40;
inline char nc(){
	static char buf[100000],*p1 = buf,*p2 = buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
template<typename T>
void read(T &x){
	x = 0;T f = 1;
	char c = nc();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
}
long long a[MAXN];
inline long long gcd(long long a,long long b){return b==0?a:gcd(b,a%b);}
inline long long getlcm(long long a,long long b){return a*b/gcd(a,b);}
int res = 0;
long long n,m;
bool cmp(long long a,long long b){return a>b;}
void dfs(int step,int cnt,long long lcm){
	if(lcm>m)return;
	if(step==n+1){if(lcm!=1)res+=cnt*(m-17)/lcm;return;}
	dfs(step+1,cnt,lcm);
	dfs(step+1,cnt*-1,getlcm(lcm,a[step]));
}
int main(){
	# ifdef BEYONDSTARS
		freopen("testdata.in","r",stdin);
	# endif
	read(n);read(m);
	for(int i = 1;i<=n;i++)read(a[i]);
	sort(a+1,a+1+n,cmp);
	dfs(2,1,a[1]);dfs(2,-1,1);
	printf("%d",res+1);
	return 0;
}
```