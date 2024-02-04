---
title: 封闭集计数
date: 2019-01-23 15:03:00 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给定一张无向图，请支持以下操作：
插入一条无向边，输出当前有多少个“封闭集”
所谓“封闭集”，指的是一个边的非空子集 S，满足从任意一个点出发，都可以回到这个点（注意每个点可以经过多次，但是每条边需要经过一次。同时，一个孤立点视为可以回到自己。）
初始的时候图中没有边。
#  输入
第一行两个整数 N,M 表示这张图的点数以及要插入的边数。
接下来 M 行，每行两个整数，表示要插入的一条边的两端。注意保证没有自环，但是可能有重边
#  输出
M 行，每插入一条边，输出当前“封闭集”的数量，结果对 $100000009$ 取模。
#  样例输入
```
3 4
1 2
1 3
2 3
2 3
```
样例输出
```
0
0
1
3
```
提示
对于 30%：N, M <= 10
对于 60%：N, M <= 1000
对于 100%：N, M <= 200000
# 解答
很简单的一个水题，但是不好想。我们考虑两种边:在树上的边，和非树上的边。树上的边保证整个图连同，而非树上的边加一条进去，就多一个封闭集。考虑和集合子集一样，每一条非树边有选和不选两种情况。所以共有$2^n$种情况，但是呢？又不能一条都不选，所以是$2^n-1$
代码：
```cpp
# include <queue>
# include <cstdio>
# include <set>
# include <iostream>
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const long long mod = 100000009;
const int MAXN = 200010;
int fa[MAXN];
int n ,m;
inline void init(){for(int i = 1;i<=n;i++)fa[i] = i;}
inline int find(int x){return fa[x]==x?fa[x]:fa[x]=find(fa[x]);}
inline bool judge(int x,int y){return find(x)==find(y);}
inline void unionn(int x,int y){fa[find(y)] = find(x);}
long long quick(int p){
    long long ans = 1,bas = 2;
    while(p){
        if(p&1)ans = ans*bas%mod;
        bas = bas*bas%mod;
        p>>=1;
    }
    return ans;
}
int main(){
    n = read(),m = read();
    int not_tree_edge = 0;
    init();
    for(int i = 1;i<=m;i++){
        int f= read(),t = read();
        if(judge(f,t)){
            not_tree_edge++;
        } else{
            unionn(f,t);
        }
        printf("%lld\n",quick(not_tree_edge)-1);
    }
    return 0;
}
```