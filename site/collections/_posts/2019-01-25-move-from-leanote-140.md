---
title: bzoj1059 ZJOI2007矩阵游戏
date: 2019-01-25 14:13:42 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
小Q是一个非常聪明的孩子，除了国际象棋，他还很喜欢玩一个电脑益智游戏——矩阵游戏。矩阵游戏在一个N
*N黑白方阵进行（如同国际象棋一般，只是颜色是随意的）。每次可以对该矩阵进行两种操作：行交换操作：选择
矩阵的任意两行，交换这两行（即交换对应格子的颜色）列交换操作：选择矩阵的任意行列，交换这两列（即交换
对应格子的颜色）游戏的目标，即通过若干次操作，使得方阵的主对角线(左上角到右下角的连线)上的格子均为黑
色。对于某些关卡，小Q百思不得其解，以致他开始怀疑这些关卡是不是根本就是无解的！！于是小Q决定写一个程
序来判断这些关卡是否有解。
#  Input
　　第一行包含一个整数T，表示数据的组数。接下来包含T组数据，每组数据第一行为一个整数N，表示方阵的大
小；接下来N行为一个N*N的01矩阵（0表示白色，1表示黑色）。
#  Output
　　输出文件应包含T行。对于每一组数据，如果该关卡有解，输出一行Yes；否则输出一行No。

#  Sample Input
```
2
2
0 0
0 1
3
0 0 1
0 1 0
1 0 0
```
Sample Output
```
No
Yes
```
#  数据规模
对于100%的数据，N ≤ 200
# 解答
对于这种题，套路！横纵坐标连边。然后我们发现，如果一种情况能够移动过去，当且仅当任意一行和一列中1的个数为1.如下图所示
![title](https://cdn.risingentropy.top/images/posts/5c4aa9a7ab644106f500063c.png)
那么x和y连边了以后，做匹配。匹配出n组，则有解。为什么呢？因为对于一个$y$它只能与一个$x$连接。如果某个$y$与多个$x$连接了以后，必定有个$x$找不到$y$~~女朋友~~，所以匹配数一定为$n$
代码：
```cpp
# include <cstdio>
# include <algorithm>
# include <iostream>
# include <cstring>
using namespace std;
const int MAXN = 401000;
const int INF = 0x3f3f3f3f;
struct edge{int t,f,w,next;bool operator<(const edge &e2)const {return w>e2.w;}}edges[MAXN<<2];
int head[MAXN],top;
int map[43][43];
int n ,m;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int vis[1000];
int match[1000];
int dfn;
bool dfs(int x){
    for(int i = head[x];i;i = edges[i].next){
        int t  = edges[i].t;
        if(vis[t]==dfn)continue;
        vis[t] = dfn;
        if(match[t]==0||dfs(match[t])){
            match[t] = x;
            return true;
        }
    }
    return false;
}
char c;
int main(){
    int Q = read();
    while(Q--){
        n = read();
        memset(head,0, sizeof(head));
        memset(match,0, sizeof(match));
        memset(vis,0, sizeof(vis));
        top = 0;
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=n;j++){
                cin>>c;
                if(c=='1')add(i,j,1);
            }
        }
        for(int i = 1;i<=n;i++){
            ++dfn;
            if(!dfs(i)){
                printf("No\n");
                break;
            }
            if(i==n){
                printf("Yes\n");
            }
        }
    }
    return 0;
}

```