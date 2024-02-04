---
title: luogu P2943 [USACO09MAR]清理Cleaning Up
date: 2019-02-17 13:51:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有N头奶牛，每头那牛都有一个标号Pi，1 <= Pi <= M <= N <= 40000。现在Farmer John要把这些奶牛分成若干段，定义每段的不和谐度为：若这段里有k个不同的数，那不和谐度为k*k。那总的不和谐度就是所有段的不和谐度的总和。
#  输入
第一行：两个整数N，M
第2..N+1行：N个整数代表每个奶牛的编号
#  输出
一个整数，代表最小不和谐度
#  样例输入
```
13 4
1
2
1
3
2
2
3
4
3
4
3
1
4
```
#  样例输出
```
11
```
#  标签
usaco2009mar
# 解答
好难的一道dp啊！奇奇怪怪的做法
# 低分做法
$O(n^2)$的DP
# 骗分做法
直接unique然后输出unique之后的长度
# 满分做法
我们考虑最坏情况：最坏情况就是每个点都单独算，那么最多也就是$n*1^2=n$次也就是说，答案最多不超过n次。那么可以知道，如果一个区间里面，出现的数的个数超过了$\sqrt n$次的话，这个区间就没意义了。假如我们知道从当前点为结尾的不同颜色出现为j次的区间的开始的地方，我们就可以方便的转移了。假设`pos[j]`的含义为以当前点为结尾，出现不同颜色为$j$种的区间的起始点，那么，转移方程就写成了$$dp[i] = min(dp[i],dp[pos[j]-1]+j*j)j\in [1,\sqrt n]$$
那么，问题就转化为了怎么处理pos数组。我们维护一下几个信息：

 - pre[i]表示**与当前点的颜色相同**的点在前面出现的最近的地方
 - last[i]表示**颜色为$i$的点**出现的最后的地方
 - nxt[i]表示**与当前点的颜色相同**的点在后面出现的最近的地方
 - pos[i]表示以**当前点作为结尾**，出现**不同数字的个数为$i$**的区间**最远**的起点
 
那么曾么维护呢？我们考虑`pre` `last` `nxt`互相维护：
```cpp
for(int i = 1;i<=n;i++){
        cin>>a[i];
        pre[i] = last[a[i]];//读入
        nxt[last[a[i]]] = i;//当前颜色的点上一次出现的地方的后一次出现的地方为当前点
        last[a[i]] = i;//a[i]种颜色最后一次出现为i
        nxt[i] = n+1;//当前点如果后面在没出现过，那么就是n+1
        dp[i] = INF;
    }
```
然后维护`pos`的同时，转移状态
```cpp
 for(int i = 1;i<=n;i++)pos[i] = 1;//初始化为1，后面会调整。并且也为了方便第一次出现的点(pre 为0)的维护
    for(int i = 1;i<=n;i++){
        for(int j = 1;j*j<=n;j++){
            if(pre[i]<pos[j])cnt[j]++;//如果这个颜色的点的出现都在当前区间的前面了，说明当前区间需要多一种颜色了。
            if(cnt[j]>j){//如果当前区间的不同颜色的点都超过了j了，也就是说不满足pos[j]的含义了，需要修改
                cnt[j]--;//颜色少一个
                while(nxt[pos[j]]<i)pos[j]++;//一直向后跳，知道调到一个位置，使得当前区间少一个颜色
                pos[j]++;//当前pos[j]的位置是在当前区间出现过的某种颜色的最后一个点，还需要向后跳一个，把这个点跳过去
            }
            dp[i] = min(dp[i],dp[pos[j]-1]+j*j);//pos维护完了，就该转移了
        }
    }
```
我一开始有个疑问，就是`if(cnt[j]>j)`的时候`cnt[j]--`会不会导致`cnt[j]--`以后，它的值任然大于`j`呢？其实不会，因为`cnt[j]`每增加一次的时候，就会判断一次，刚刚超过的时候就修改了，所以不会.~~说白了就是我太弱了~~
AC代码如下：
```cpp
# include <cstdlib>
# include <iostream>
# include <vector>
# include <cmath>
# include <string>
# include <algorithm>
# include <cstdio>
using namespace std;
const int INF = 0x7f7f7f7f;
const int MAXN = 40010;
int a[MAXN],pre[MAXN],pos[MAXN],cnt[MAXN],last[MAXN],nxt[MAXN],dp[MAXN];
int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n,m;cin>>n>>m;
    for(int i = 1;i<=n;i++){
        cin>>a[i];
        pre[i] = last[a[i]];
        nxt[last[a[i]]] = i;
        last[a[i]] = i;
        nxt[i] = n+1;
        dp[i] = INF;
    }
    for(int i = 1;i<=n;i++)pos[i] = 1;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j*j<=n;j++){
            if(pre[i]<pos[j])cnt[j]++;
            if(cnt[j]>j){
                cnt[j]--;
                while(nxt[pos[j]]<i)pos[j]++;
                pos[j]++;
            }
            dp[i] = min(dp[i],dp[pos[j]-1]+j*j);
        }
    }
    cout<<dp[n];
    return 0;
}
```