---
title: P1273 有线电视网
date: 2019-01-12 22:44:59 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
某收费有线电视网计划转播一场重要的足球比赛。他们的转播网和用户终端构成一棵树状结构，这棵树的根结点位于足球比赛的现场，树叶为各个用户终端，其他中转站为该树的内部节点。

从转播站到转播站以及从转播站到所有用户终端的信号传输费用都是已知的，一场转播的总费用等于传输信号的费用总和。

现在每个用户都准备了一笔费用想观看这场精彩的足球比赛，有线电视网有权决定给哪些用户提供信号而不给哪些用户提供信号。

写一个程序找出一个方案使得有线电视网在不亏本的情况下使观看转播的用户尽可能多。

#  输入输出格式
#  输入格式：
输入文件的第一行包含两个用空格隔开的整数N和M，其中2≤N≤3000，1≤M≤N-1，N为整个有线电视网的结点总数，M为用户终端的数量。

第一个转播站即树的根结点编号为1，其他的转播站编号为2到N-M，用户终端编号为N-M+1到N。

接下来的N-M行每行表示—个转播站的数据，第i+1行表示第i个转播站的数据，其格式如下：

K A1 C1 A2 C2 … Ak Ck

K表示该转播站下接K个结点(转播站或用户)，每个结点对应一对整数A与C，A表示结点编号，C表示从当前转播站传输信号到结点A的费用。最后一行依次表示所有用户为观看比赛而准备支付的钱数。

# 输出格式：
输出文件仅一行，包含一个整数，表示上述问题所要求的最大用户数。

#  输入输出样例
#  输入样例# 1： 
```
5 3
2 2 2 5 3
2 3 2 4 3
3 4 2
```
#  输出样例# 1： 
```
2
```
说明

说明
样例解释
【样例解释】
![enter image description here](https://cdn.risingentropy.top/images/posts/c39fe3bab64416ed80019e1.png)
如图所示，共有五个结点。结点①为根结点，即现场直播站，②为一个中转站，③④⑤为用户端，共M个，编号从N-M+1到N，他们为观看比 赛分别准备的钱数为3、4、2，从结点①可以传送信号到结点②，费用为2，也可以传送信号到结点⑤，费用为3（第二行数据所示），从结点②可以传输信号到结点③，费用为2。也可传输信号到结点④，费用为3（第三行数据所示），如果要让所有用户（③④⑤）都能看上比赛，则信号传输的总费用为： 2+3+2+3=10，大于用户愿意支付的总费用3+4+2=9，有线电视网就亏本了，而只让③④两个用户看比赛就不亏本了。
# 解答
骚题一道。我们从答案可行性角度来想。我们用`dp[i][j]`表示从`i`个节点开始，选择`j`个节点获得的最大利润。这个利润是什么意思呢？就是总价值减去成本。那么状态转移方程式就是$$dp[i][j] = max(dp[i][j],dp[i][j-k]+dp[t][k]-w[edge])$$
代码
```cpp

# include <iostream>
# include <cstring>
using namespace std;
const int MAXN = 3010;
const int MAXM = 3010<<1;
struct edge{
    int t,w,next;
}edges[MAXM];
int head[MAXN];
int top;
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int dp[MAXN][MAXN];
int son[MAXN];
int n,m;
int cost[MAXN];
void dfs(int f,int fa){
    dp[f][0] = 0;
    if(f>=n-m+1){son[f] = 1;dp[f][1] = cost[f];return;}
    son[f] = 0;
    for(int i = head[f];i!=0;i = edges[i].next){
        int t = edges[i].t;
        if(t==fa)continue;
        dfs(t,f);son[f]+=son[t];
        for(int j = son[f];j>=0;j--){
            for(int k = son[t];k>=0;k--){
                dp[f][j] = max(dp[f][j],dp[f][j-k]+dp[t][k]-edges[i].w);
            }
        }

    }
}
int main(){
    cin>>n>>m;
    int k,a,c;
    for(int i = 1;i<=n-m;i++){
        cin>>k;
        for(int j = 1;j<=k;j++){
            cin>>a>>c;
            add(i,a,c);
        }
    }
    for(int i = n-m+1;i<=n;i++){
        cin>>cost[i];
    }
    memset(dp,0xc0, sizeof(dp));
    dfs(1,0);
    int ans = 0;
    for(int i = 1;i<=m;i++){
        if(dp[1][i]>=0){
            ans = i;
        }
    }
    cout<<ans;
    return 0;
};

```