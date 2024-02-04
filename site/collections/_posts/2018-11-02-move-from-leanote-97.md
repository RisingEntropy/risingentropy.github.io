---
title: luoguP2015 二叉苹果树
date: 2018-11-02 16:40:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有一棵苹果树，如果树枝有分叉，一定是分2叉（就是说没有只有1个儿子的结点）
这棵树共有N个结点（叶子点或者树枝分叉点），编号为1-N,树根编号一定是1。
我们用一根树枝两端连接的结点的编号来描述一根树枝的位置。下面是一颗有4个树枝的树
```
2   5
 \ / 
  3   4
   \ /
    1
```
现在这颗树枝条太多了，需要剪枝。但是一些树枝上长有苹果。

给定需要保留的树枝数量，求出最多能留住多少苹果。

# 输入输出格式
#  输入格式：
第1行2个数，N和Q(1`<`=Q`<`= N,1`<`N`<`=100)。

N表示树的结点数，Q表示要保留的树枝数量。接下来N-1行描述树枝的信息。

每行3个整数，前两个是它连接的结点的编号。第3个数是这根树枝上苹果的数量。

每根树枝上的苹果不超过30000个。

# 输出格式：
一个数，最多能留住的苹果的数量。

# 输入输出样例
#  输入样例# 1： 
```
5 2
1 3 1
1 4 10
2 3 20
3 5 20
```
#  输出样例# 1： 
```
21
```
# 解答
一道树形dp的入门题~~我还是不太会~~
我们假设dp[i][j]表示以i为根的树上保留j个节点的最大权值和。**注意因为本题是在一颗“苹果树上”剪，所以点f和它的子节点t直接的连边绝对不能剪！**那么我们进过思考，可以得到状态转移方程$$dp[i][j]=max\{dp[i][j],dp[i]j-k-1]+dp[t][j]+W[f][t]\}(0\leq j\leq min(q,edges[u]) 0\leq k\leq min(j-1,edges[t])$$
然后在dfs ~~大法师~~ 的时候就可以顺便计算了.注意，因为dp数组是在动态变化的，所以要向背包一样倒着搜，不然会重。AC代码：
```cpp
# include <iostream>
# include <cstdlib>
# include <cmath>
# include <time.h>
# include <cstdio>
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
const int MAXN = 101;
struct edge{
    int t,w,next;
}edges[MAXN*2+10];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int F[MAXN][MAXN],q,n,e[MAXN];
void dfs(int p,int f){
    for(int i = head[p];i!=0;i = edges[i].next){
        int t = edges[i].t;
        if(t==f)continue;
        dfs(t,p);
        e[p]+=e[t]+1;
        for(int j = min(q,e[p]);j>=1;j--){
            for(int k = min(e[p],j-1);k>=0;k--){
                F[p][j] = max(F[p][j],F[p][j-k-1]+F[t][k]+edges[i].w);
            }
        }
    }
}
int main() {
    n = read(),q = read();
    for(int i = 1;i<n;i++){
        int f,t,w;
        f = read(),t =read(),w = read();
        add(f,t,w);
        add(t,f,w);
    }
    dfs(1,0);
    printf("%d",F[1][q]);
    return 0;

}
```