---
title: P1736 创意吃鱼法
date: 2019-01-05 23:01:05 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
回到家中的猫猫把三桶鱼全部转移到了她那长方形大池子中，然后开始思考：到底要以何种方法吃鱼呢（猫猫就是这么可爱，吃鱼也要想好吃法 ^_*）。她发现，把大池子视为01矩阵（0表示对应位置无鱼，1表示对应位置有鱼）有助于决定吃鱼策略。

在代表池子的01矩阵中，有很多的正方形子矩阵，如果某个正方形子矩阵的某条对角线上都有鱼，且此正方形子矩阵的其他地方无鱼，猫猫就可以从这个正方形子矩阵“对角线的一端”下口，只一吸，就能把对角线上的那一队鲜鱼吸入口中。

猫猫是个贪婪的家伙，所以她想一口吃掉尽量多的鱼。请你帮猫猫计算一下，她一口下去，最多可以吃掉多少条鱼？

#  输入输出格式
#  输入格式：
有多组输入数据，每组数据：

第一行有两个整数n和m（n,m≥1），描述池塘规模。接下来的n行，每行有m个数字（非“0”即“1”）。每两个数字之间用空格隔开。

对于30%的数据，有n,m≤100

对于60%的数据，有n,m≤1000

对于100%的数据，有n,m≤2500

#  输出格式：
只有一个整数——猫猫一口下去可以吃掉的鱼的数量，占一行，行末有回车。

#  输入输出样例
#  输入样例# 1： 
```
4 6
0 1 0 1 0 0
0 0 1 0 1 0
1 1 0 0 0 1
0 1 1 0 1 0
```
#  输出样例# 1： 
```
3
```
说明
右上角的
```
1 0 0
0 1 0
0 0 1
```
# 解答
其实有$O(n^2logN)$的做法的，就是二分+二维前缀和+暴力
然而，我们用dp
首先考虑状态如何转移
我们发现当且仅当f[i,j]=1并且i,j都有长度为len的某一点，才可能构成一个这样的方阵，并且，此时可以由f[i-1][j-1]转移过来，我们先打个表，col[i][j]表示(i,j)这个点在竖直方向上(包括这个点)，0的个数有几个，同样的row[i][j]表示水平方向上0有几个，那么转移方程就是(只考虑从左到右的情况)$$F[i][j] = min(F[i-1][j-1],min(col[i-1][j],row[i][j-1]))$$
为什么要$min(col[i-1][j],row[i][j-1])$呢？因为我们发现这个方阵长度是有限制的，其限制就是与它接上的上一个方阵的长度不能大过自己的限制条件(水平竖直方向上的连续的0的个数)，然后再从右到左做一遍就好了。
~~题解写的比较水，以后再来改吧，今天太晚了~~
代码：
```cpp
//
// Created by dhy on 19-1-5.
//
# include <iostream>
# include <cstring>
using namespace std;
const int MAXN = 2510;
int map[MAXN][MAXN];
int dp[MAXN][MAXN];
int row[MAXN][MAXN];
int col[MAXN][MAXN];
int n,m;
int main(){
    int n,m;
    ios::sync_with_stdio(false);
    int ans = 0;
    cin>>n>>m;
    for(int i = 1;i<=n;i++) {
        for (int j = 1; j <= m; j++){
            cin>>map[i][j];
            if(map[i][j]==0){
                col[i][j] = col[i-1][j]+1;
                row[i][j] = row[i][j-1]+1;
            }else{
                dp[i][j] = min(dp[i-1][j-1],min(row[i][j-1],col[i-1][j]))+1;

            }
            ans = max(ans,dp[i][j]);
        }
    }
    memset(dp,0, sizeof(dp));
    memset(row,0, sizeof(row));
    memset(col,0, sizeof(col));
    for(int i = 1;i<=n;i++)
        for(int j = m;j>=1;j--){
            if(map[i][j]==0){
                col[i][j] = col[i-1][j]+1;
                row[i][j] = row[i][j+1]+1;
            }else{
                dp[i][j] = min(dp[i-1][j+1],min(row[i][j+1],col[i-1][j]))+1;
            }
                ans = max(ans,dp[i][j]);
        }
        cout<<ans;

    return 0;
};

```