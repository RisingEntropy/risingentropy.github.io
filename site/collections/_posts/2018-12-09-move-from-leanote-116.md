---
title: POJ3585
date: 2018-12-09 10:45:49 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
#  Description
有一个树形的水系，由 N-1 条河道和 N 个交叉点组成。我们可以把交叉点看作树中的节点，编号为1~N，河道则
看作树中的无向边。每条河道都有一个容量，连接 x 与 y 的河道的容量记为 c(x,y)。河道中单位时间流过的水
量不能超过河道的容量。有一个节点是整个水系的发源地，可以源源不断地流出水，我们称之为源点。除了源点之
外，树中所有度数为1的节点都是入海口，可以吸收无限多的水，我们称之为汇点。也就是说，水系中的水从源点
出发，沿着每条河道，最终流向各个汇点。在整个水系稳定时，每条河道中的水都以单位时间固定的水量流向固定
的方向。除源点和汇点之外，其余各点不贮存水，也就是流入该点的河道水量之和等于从该点流出的河道水量之和
。整个水系的流量就定义为源点单位时间发出的水量。在流量不超过河道容量的前提下，求哪个点作为源点时，整
个水系的流量最大，输出这个最大值。N≤2*〖10〗^5。
#  Input
The first line of the input is an integer T which indicates the number of test cases. 
The first line of each test case is a positive integer n. 
Each of the following n - 1 lines contains three integers x, y, z separated by spaces, 
representing there is an edge between node x and node y, and the capacity of the edge is z. 
Nodes are numbered from 1 to n.
All the elements are nonnegative integers no more than 200000. 
You may assume that the test data are all tree metrics.
#  Output
For each test case, output the result on a single line. 
#  Sample Input
```
1
5
1 2 11
1 4 13
3 4 5
4 5 10
```
#  Sample Output
```
26
```
# 解答
1.暴力做法
其实可以枚举每一个点作为起始点，然后跑dp，复杂度$O(n)$
2.满分做法
我们假设d[x]表示x作为源点，**在x的子树中流过的水量最大**，那么对于解法1，答案就是所有节点中,d[x]最大的一个。但是我们考虑能不能把这个信息用起来。我们使用F[x]表示以x作为根节点，在**整个图中的最大流量**，那么怎么通过现有信息维护出F数组呢？
我们y是x的子树，且F[x]已经求出。则$min(d[y],c(x,y))$就是x流向y的最大流量。那么x流向其他地方的流量就是$d[x]-min(d[y],c(x,y))$,现在我们以y作为根节点，那么F[y]包含两部分

 1. y流向y为根的子树的流量，保存在d[y]重
 2. y流向x进而流向其他节点的流量
 
又很容易想到F[y] = d[y]+y流向x进而流向其他节点的流量。那么就推出$F[y] = d[y] + min(F[x] - min(d[y],c(x,y)),c(x,y))$ 
对于入度为1的点单独考虑，那么总的状态转移方程就是如下
$$
F[y] = d[y] + min(F[x] - min(d[y],c(x,y)),c(x,y)) x度数大于1\\ c(x,y) x度数等于1
$$
代码如下(poj挂了，没提交)：
```cpp
//
// Created by dhy on 18-12-9.
//
# include <cmath>
# include <cstring>
# include <iostream>
using namespace std;
const int MAXN = (int)3e5;
struct edge{
    int t,w,next;
}edges[MAXN<<1];
int head[MAXN];
int top;
int degree[MAXN];
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int d[MAXN],F[MAXN];
bool vis[MAXN];
inline int min(int a,int b){return a<b?a:b;}
void dp(int x){
    vis[x] = true;
    d[x] = 0;
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(vis[t])continue;
        dp(t);
        if(degree[t]==1){
            d[x] += edges[i].w;
        }else{
            d[x] += min(d[t],edges[i].w);
        }
    }
}
void dfs(int x){
    vis[x] = true;
    for(int i = head[x];i;i = edges[i].next){
        int t = edges[i].t;
        if(vis[t])continue;
        if(degree[x]==1)F[t] = d[t] + edges[i].w;
        else F[t] = d[t] + min(F[x]-min(d[t],edges[i].w),edges[i].w);
        dfs(t);
    }
}
int main(void){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        memset(d,0, sizeof(d));
        memset(F,0, sizeof(F));
        for(int i = 1;i<n;i++){
            int x,y,z;

            cin>>x>>y>>z;
            degree[x]++,degree[y]++;
            add(x,y,z),add(y,x,z);
        }
        dp(1);
        memset(vis,false, sizeof(vis));
        F[1] = d[1];
        dfs(1);
        int ans = 0;
        for(int i = 1;i<=n;i++)ans = -min(-ans,-F[i]);
        cout<<ans<<endl;
    }
    return 0;
}
```
不知道怎么回事，反正就是RE