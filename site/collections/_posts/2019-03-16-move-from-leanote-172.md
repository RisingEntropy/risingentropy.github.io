---
title: woj1505 美丽数
date: 2019-03-16 11:25:57 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
美丽数是指能被它的每一位非0的数字整除的正整数。

#  输入
包含若干组数据，每组数据一行两个数n,m，表示求[n,m]之间的美丽数的个数。

#  输出
对于每组数据输出一个答案，各占一行。

#  样例输入
```
1 9
12 15
```
#  样例输出
```
9
2
```
提示
$0 < n , m < 10^{18}$ 测试数据不超过100组
# 解答
![图片标题](https://cdn.risingentropy.top/images/posts/c8c6e50ab6441227e005693.png)
可以参见`zxy`神仙的博客：[【NOIP训练】美丽数（数位DP）](https://blog.csdn.net/zxyoi_dreamer/article/details/82892239)
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
//orz zxy sto
long long dp[20][50][2523];
int num[20],cnt;
int idx[2523];
inline int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
inline int lcm(int a,int b){return a*b/gcd(a,b);}
int ptr;
void pre(int n,int l){
	if(!idx[l])idx[l] = ++ptr;
	if(n>=10)return;
	pre(n+1,lcm(l,n));
	pre(n+1,l);
}
long long dfs(int pos,int lc,int remain,bool limit){
	if(pos==0)return remain%lc==0;
	if(!limit&&dp[pos][idx[lc]][remain]!=-1)return dp[pos][idx[lc]][remain];
	long long ans = 0;int mx = limit?num[pos]:9;
	for(int i = 0;i<=mx;i++){
		int nxt;
		if(i!=0){
			nxt = lcm(lc,i);
		}else{
			nxt = lc;
		}
		ans+=dfs(pos-1,nxt,(remain*10+i)%2520,limit&&(i==mx));
	}
	if(!limit)dp[pos][idx[lc]][remain] = ans;
	return ans;
}
long long work(long long x){
	cnt = 0;
	while(x){
		num[++cnt] = x%10;x/=10;
	}
	return dfs(cnt,1,0,true);
}
int main(){
	memset(dp,-1,sizeof(dp));
	pre(2,1);
	long long x,y;
	while(scanf("%lld %lld",&x,&y)!=EOF)
	cout<<work(y)-work(x-1)<<endl;
	return 0;
}
```