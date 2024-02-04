---
title: unknown title
date: 2019-03-16 09:30:05 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
求给定区间 [X,Y][X,Y] 中满足下列条件的整数个数：这个数恰好等于 KK 个互不相等的 BB 的整数次幂之和。例如，设 X=15,Y=20,K=2,B=2X=15,Y=20,K=2,B=2，则有且仅有下列三个数满足题意：
$17 = 2^4+2^0$
$18 = 2^4+2^1$
$20 = 2^4+2^2$
# 样例输入
#  输入样例
```
15 20
2
2
```
#  输出样例
```
3
```
# 解答
很经典的一道数位DP的题。看一眼应该就知道这道题要化成B进制，然后在B进制下来每一位填数，继续观察发下现，既然只能填1或0，那么直接转二进制就可以了。所以我就愉快的WA了，看了博客知道，不能简单的化二进制，要**从高位向下找，找到第一个大于1的数，把之后的每一位都填1**，因为如果当前B进制下为大于1的数，那么后面随便乱填01都可以。代码：
```cpp
# include <iostream>
# include <cstring>
using namespace std;
const int MAXN = 35;
long long dp[MAXN][MAXN];
int num[MAXN];
int ct,K,B;
int dfs(int pos,int cnt,bool limit){
	if(pos==0)return cnt==K;
	if(!limit&&dp[pos][cnt]!=-1)return dp[pos][cnt];
	int mx = limit?num[pos]:1;
	long long ans = 0;
	for(int i = 0;i<=mx;i++){
		ans+=dfs(pos-1,cnt+i,(i==mx)&&limit);
	}
	if(!limit)dp[pos][cnt] = ans;
	return ans;
}
long long work(long long x){
	if(x==0)return 0;
	ct = 0;
	while(x){
		num[++ct] = x%B;
		x/=B;
	}
	for(int i = ct;i>=1;i--){//就是这里注意了，一开始我没想到，调了一晚♂上
		if(num[i]>1){
			for(int j = 1;j<=i;j++)num[j] = 1;
		    break;
		}
	}
	return dfs(ct,0,true);
}
int main(){
	memset(dp,-1,sizeof(dp));
	long long x,y;cin>>x>>y>>K>>B;
	cout<<work(y)-work(x-1);
	return 0;
}
```