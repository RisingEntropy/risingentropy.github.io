---
title: AHOI2009同类分布
date: 2019-03-16 09:51:06 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给出两个数$a,b$，求出$[a,b]$中各位数字之和能整除原数的数的个数。
# 输入格式：
一行，两个整数$a$和$b$
# 输出格式：
一个整数，表示答案
# 样例数据
#  输入样例
```
10 19
```
#  输出样例
```
3
```
# 解答
众所周知，题目越短，题越恶心。
这题不好想啊，但是题的名称给了提示，就是数学上的剩余系分类。我们枚举最后的数的和，这样我们就可方便转移了。
定义dp[pos][sum][mod]的含义为第pos位，前面所有数的和为sum，当前的剩余系位mod的方案数，转移嘛，就是dp[pos][sum][mod]->dp[pos-1][sum+i][(mod*10+1)%MOD]其中MOD是枚举的最后的数字的和。
关键问题是：我太菜了，想不到枚举MOD这种做法啊？~~实在不行打个表？~~
代码：
```cpp
# include <iostream>
# include <cstring>
using namespace std;
long long dp[20][200][200];
int num[20],cnt;
int MOD;
long long dfs(int pos,int sum,int mod,bool limit){
	if(pos==0)return mod==0&&sum==MOD;
	if(!limit&&dp[pos][sum][mod]!=-1)return dp[pos][sum][mod];
	int mx = limit?num[pos]:9;
	long long ans = 0;
	for(int i = 0;i<=mx;i++){
		ans+=dfs(pos-1,sum+i,(mod*10+i)%MOD,(i==mx)&&limit);
	}
	if(!limit)dp[pos][sum][mod] = ans;
	return ans;
}
long long work(long long x){
	cnt = 0;
	while(x){
		num[++cnt] = x%10;x/=10;
	}
	long long ans = 0;
	for(int i = 1;i<=9*cnt;i++){
		memset(dp,-1,sizeof(dp));
		MOD = i;
		ans += dfs(cnt,0,0,true);
	}
	return ans;
}
int main(){
	memset(dp,-1,sizeof(dp));
	long long x,y;cin>>x>>y;
	cout<<work(y)-work(x-1);
	return 0;
}
```