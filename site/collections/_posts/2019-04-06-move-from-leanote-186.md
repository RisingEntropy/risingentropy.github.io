---
title: woj2378 架设电话线
date: 2019-04-06 14:40:28 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
最近，Farmer John的奶牛们越来越不满于牛棚里一塌糊涂的电话服务，于是，她们要求FJ把那些老旧的电话线换成性能更好的新电话线。新的电话线架设 在已有的N(2 <= N <=100,000)根电话线杆上，第i根电话线杆的高度为 height_i米(1 <= height_i <=100)。电话线总是从一根电话线杆的顶端被引到相邻的那根的顶端，如果这两根电话线杆的高度不同，那么FJ就必须为此支付 C*电话线杆高度差(1 <= C <=100)的费用。当然，你不能移动电话线杆，只能 按原有的顺序在相邻杆间架设电话线。Farmer John认为，加高某些电话线杆能减少架设电话线的总花费，尽管这项工作也需要支出一定的费用。更准确地，如果他把一根电话线杆加高X米的话 ，他得为此付出X^2的费用。请你帮Farmer John计算一下，如果合理地进行这两种工作，他最少要在这 个电话线改造工程上花多少钱。
#  输入
第1行: 2个用空格隔开的整数：N和C
第2..N+1行: 第i+1行仅有一个整数：height_i
#  输出
第1行: 输出Farmer John完成电话线改造工程所需要的最小花费
#  样例输入
```
5 2
2
3
5
1
4
```
#  样例输出
```
15
```
提示
输出说明:
最好的改造方法是：Farmer John把第一根电话线杆加高1米，把第四根加 高 2米，使得它们的高度依次为3，3，5，3，4米。这样花在加高电线杆上的钱是 5。此时，拉电话线的费用为2*(0+2+2+1) = 10，总花费为15。
# 解答
单调队列优化DP。我们很容易推出如下方程式：
$$dp[i][j] = (j-h[i])^2+min(dp[i-1][k]+c\times |i-k|)$$然后`hjy`讲过，去除这个讨厌的绝对值的办法就是分类讨论。
然后嘛：$$(j-h[i])^2+min\{ dp[i-1][k]-ck\}+cj j\ge k$$
$$(j-h[i])^2+min\{ dp[i-1][k]+ck\}-cj j\le k$$
然后就完了。
其实吧也没必要单独使用单调队列，直接遍历的时候就顺便更新了。
```cpp
// luogu-judger-enable-o2
# include<string.h>
# include <stdio.h>
# define MAXN 100005
const int INF = 0x3f3f3f3f;
int h[MAXN];
int dp[MAXN][201];
inline int read(){
    int x = 0,f = 1;
    char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}
inline int abs(int a){return a>0?a:-a;}
inline int min(int a,int b){return a<b?a:b;}
int main(void){
    int n = read(),c = read();
    for(int i = 1;i<=n;i++)h[i] = read();
    memset(dp,0x3f,sizeof(dp));
    for(int i = h[1];i<=100;i++) dp[1][i] = (h[1]-i)*(h[1]-i);
    for(int i = 2;i<=n;i++){
        int k = INF;
        for(int j = h[i-1];j<=100;j++){
            k = min(k,dp[i-1][j]-c*j);//找min括号里面的部分
            if(j>=h[i])dp[i][j] = k+c*j+(j-h[i])*(j-h[i]);//因为不能把电话杆变矮，使用必须大于h[i]
        }
        k = INF;
        for(int j = 100;j>=h[i-1];j--){//倒着来，并且只枚举到h[i]
        //因为如果h[i]<h[i-1]，对于h[i]可以枚举到，但是对于h[i-1]-h[i]之间的数就枚举不到了。
        //如果h[i]>h[i-1]，显然不影响，因为我们不能把它变矮
            k = min(k,dp[i-1][j]+c*j);
            dp[i][j] = min(k-c*j+(j-h[i])*(j-h[i]),dp[i][j]);
        }
    }
    int ans = 0x3f3f3f3f;
    for(int i = 1;i<=100;i++)ans = min(ans,dp[n][i]);
    printf("%d",ans);
    return 0;
}

```