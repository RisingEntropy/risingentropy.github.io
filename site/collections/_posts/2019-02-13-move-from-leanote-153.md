---
title: CF1114 D
date: 2019-02-13 22:22:50 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# CF1114D
# 题面
[Flood Fill](http://codeforces.com/contest/1114/problem/D)
# 一句话题意
给你一个序列，每次可以把连续的每个数组都相等的一部分变成任意数字，问多少次可以把这个序列变成数字完全相同的。
# 解答
我只会区间DP，不会那个神仙的回文$NlogN$做法。$dp[i][j]$表示把$[i,j]$这个区间全部改成一样的，需要多少次。首先初始状态肯定是$dp[i][i]=0$
dp[i][j]可以从2个地方转移过来$dp[i+1][j]$和$dp[i][j-1]$但是这里为了方便(后面就知道了)，我们从$dp[i][j]$转移到$dp[i-1][j]$和$dp[i][j+1]$.我们用$dp[i][j][0/1]$表示与这个区间最左边的一块颜色相同还是与最右边的一块颜色相同。这样就可以有如下转移方程式:$$dp[i-1][j][0] = min(dp[i-1][j][0],dp[i][j][0/1]+color!=a[i-1]);$$
$$dp[i][j+1][1] = min(dp[i][j+1][1],dp[i][j][0/1]+color!=a[j+1]$$
目标状态:$min(dp[1][n][1],dp[1][n][0])$
代码：
```cpp
//
// Created by dhy on 19-2-13.
//
# include <iostream>
# include <algorithm>
# include <cstring>
using namespace std;
const int MAXN = 5010;
int a[MAXN];
int dp[MAXN][MAXN][2];
int main(){
    iostream::sync_with_stdio(false);
    cin.tie(nullptr);cout.tie(nullptr);
    int n;cin>>n;
    for(int i = 1;i<=n;i++)cin>>a[i];
    n = unique(a+1,a+n+1)-a-1;
    memset(dp,0x3f,sizeof(dp));
    for(int i = 1;i<=n;i++)
        dp[i][i][0] = dp[i][i][1] = 0;
    for(int j = 1;j<=n;j++){
        for(int i = j;i>=1;i--){
            for(int col = 0;col<2;col++){
                int c = (col==0?a[i]:a[j]);
                if(i>1)dp[i-1][j][0] = min(dp[i-1][j][0],dp[i][j][col]+(c!=a[i-1]));
                if(j<n)dp[i][j+1][1] = min(dp[i][j+1][1],dp[i][j][col]+(c!=a[j+1]));
            }
        }
    }
    cout<<min(dp[1][n][0],dp[1][n][1]);
    return 0;
}
```