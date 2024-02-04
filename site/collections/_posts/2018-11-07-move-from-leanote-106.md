---
title: luoguP3387 【模板】缩点
date: 2018-11-07 20:47:58 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
给定一个n个点m条边有向图，每个点有一个权值，求一条路径，使路径经过的点权值之和最大。你只需要求出这个权值和。
允许多次经过一条边或者一个点，但是，重复经过的点，权值只计算一次。
#  输入输出格式
#  输入格式：
第一行，n,m
第二行，n个整数，依次代表点权
第三至m+2行，每行两个整数u,v，表示u->v有一条有向边
#  输出格式：
共一行，最大的点权之和。
#  输入输出样例
#  输入样例# 1： 
```
2 2
1 1
1 2
2 1
```
#  输出样例# 1： 
```
2
```
说明
n<=10^4,m<=10^5,点权<=1000
算法：Tarjan缩点+DAGdp
# 解答
其实是一道水题，不知道怎么刷到蓝题了，水的一批。
首先看路径权值和最大？爆搜？当然不行啦(暴力：你看不起我？)那我们考虑换种方法，我们看到题中的`一个点可以被计算多次，但权值只计算一次`我们想一下，如果一个点的权值可以计算多次怎么办？当然是找环啦，这样就一直在环上绕圈圈，权值和直接$\infty$，那么，这就是我们的切入点！找环！因为找到一个环，然后再缩点，我们就可以忽略这个环上其他点对求解的干扰。缩点的同时，我们把被缩掉的点的权值加到缩了的点上。于是乎我们就找到了如下流程：
>tarjan找环->缩点->dfs搜索(记忆化搜索)

注意，也是为了提醒我自己：
tarjan求强联通分量还有一个数组记录一个点是否在栈里面，和tarjan找双连通分量与割点与桥不同
AC代码：
```cpp
# include<iostream>
# include<cstdio>
# include <cmath>
# include <cstring>
# include <queue>
# include <stack>
# include <algorithm>
# include <fstream>
# include <set>
using namespace std;
const int MAXN = 101000;
struct edge{int f,t,w,next;}edges[MAXN];
int fe[MAXN],te[MAXN];
int head[MAXN];
int w[MAXN];
int top;
int n;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar();}
    return x*f;
}
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].f = f;
    edges[top].w = w;
    head[f] = top;
}
stack<int> stk;
int dfn_cnt;
int dfn[MAXN],low[MAXN];
int wei[MAXN];
int color[MAXN];
int col_cnt;
bool instack[MAXN];
int dp[MAXN];
void tarjan(int x){
    dfn[x] = low[x] = ++dfn_cnt;
    stk.push(x);
    instack[x] = true;
    for(int i = head[x];i!=0; i =edges[i].next){
        int t = edges[i].t;
        if(!dfn[t]){
            tarjan(t);
            low[x] = min(low[x],low[t]);
        }else if(instack[t]){
            low[x] =  min(dfn[t],low[x]);
        }
    }
    if(dfn[x]==low[x]){
        color[x] = ++col_cnt;
        wei[col_cnt]+=w[x];
        while(stk.top()!=x){
            wei[col_cnt] += w[stk.top()];
            instack[stk.top()] =  false;
            color[stk.top()] = col_cnt;
            stk.pop();
        }
        instack[x] = false;
        stk.pop();
    }
}
void dfs(int x){
    if(dp[x])return;
    dp[x] = wei[x];
    int maxsum = 0;
    for(int i = head[x];i!=0;i = edges[i].next){
        if(!dp[edges[i].t])dfs(edges[i].t);
        maxsum=max(maxsum,dp[edges[i].t]);
    }
    dp[x]+=maxsum;
}
int main(void){
    int m ;
    n = read(),m = read();
    for(int i = 1;i<=n;i++)w[i] = read();
    int f,t;
    for(int i = 1;i<=m;i++){
        f = read(),t = read();
        fe[i] = f,te[i] =t;
        add(f,t,1);
    }
    for(int i = 1;i<=n;i++)if(!dfn[i])tarjan(i);
    memset(head,0, sizeof(head));
    top = 0;
    for(int i = 1;i<=m;i++){
        if(color[fe[i]]!=color[te[i]]){
            add(color[fe[i]],color[te[i]],1);
        }
    }
    int ans = 0;
    for(int i = 1;i<=col_cnt;i++){
        if(!dp[i]){
            dfs(i);
            ans = max(ans,dp[i]);
        }
    }
    printf("%d",ans);
    return 0;
}
```