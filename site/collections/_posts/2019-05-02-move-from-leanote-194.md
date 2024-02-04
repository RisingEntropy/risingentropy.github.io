---
title: 【lct】bzoj 2959 长跑 (LCT 动态维护边双连通分量)
date: 2019-05-02 23:19:47 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
某校开展了同学们喜闻乐见的阳光长跑活动。为了能“为祖国健康工作五十年”，同学们纷纷离开寝室，离开教室，离开实验室，到操场参加3000米长跑运动。一时间操场上熙熙攘攘，摩肩接踵，盛况空前。
为了让同学们更好地监督自己，学校推行了刷卡机制。
学校中有n个地点，用1到n的整数表示，每个地点设有若干个刷卡机。
有以下三类事件：
1、修建了一条连接A地点和B地点的跑道。
2、A点的刷卡机台数变为了B。
3、进行了一次长跑。问一个同学从A出发，最后到达B最多可以刷卡多少次。具体的要求如下：
当同学到达一个地点时，他可以在这里的每一台刷卡机上都刷卡。但每台刷卡机只能刷卡一次，即使多次到达同一地点也不能多次刷卡。
为了安全起见，每条跑道都需要设定一个方向，这条跑道只能按照这个方向单向通行。最多的刷卡次数即为在任意设定跑道方向，按照任意路径从A地点到B地点能刷卡的最多次数。
#  输入
输入的第一行包含两个正整数n,m，表示地点的个数和操作的个数。
第二行包含n个非负整数，其中第i个数为第个地点最开始刷卡机的台数。
接下来有m行，每行包含三个非负整数P,A,B，P为事件类型，A,B为事件的两个参数。
最初所有地点之间都没有跑道。
每行相邻的两个数之间均用一个空格隔开。表示地点编号的数均在1到n之间，每个地点的刷卡机台数始终不超过10000，P=1,2,3。
#  输出
输出的行数等于第3类事件的个数，每行表示一个第3类事件。如果该情况下存在一种设定跑道方向的方案和路径的方案，可以到达，则输出最多可以刷卡的次数。如果A不能到达B，则输出-1。

#  样例输入
```
9 31
10 20 30 40 50 60 70 80 90
3 1 2
1 1 3
1 1 2
1 8 9
1 2 4
1 2 5
1 4 6
1 4 7
3 1 8
3 8 8
1 8 9
3 8 8
3 7 5
3 7 3
1 4 1
3 7 5
3 7 3
1 5 7
3 6 5
3 3 6
1 2 4
1 5 5
3 3 6
2 8 180
3 8 8
2 9 190
3 9 9
2 5 150
3 3 6
2 1 210
3 3 6
```
#  样例输出
```
-1
-1
80
170
180
170
190
170
250
280
280
270
370
380
580
```
提示
对于100%的数据，m<=5n，任意时刻，每个地点的刷卡机台数不超过10000。N<=1.5×105
# 解答
两个并查集维护，第一个维护某个点在哪个边双联通分量(下文写作：联通分量)里面，第二个维护两个联通分量是否联通，然后直接用LCT维护**联通分量**就行了。注意一点，因为一开始每个点是独立的，要对每个点操作，那么它的父亲就不是简单的`fa[x]`，而一个是`fidf(fa[x])`(维护点在联通分量的并查集的根)。包括rotate和splay等等操作里面都要这样。~~(学校破测评机卡cin)~~
代码：
```cpp
//
// Created by dhy on 19-5-2.
//
# include <iostream>
# include <cstdio>
# pragma GCC optimize(3)
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}
const int MAXN = (int)1.5e5+100;
int tree[MAXN][2],val[MAXN],sum[MAXN],fa[MAXN],tag[MAXN];
int f[MAXN],g[MAXN];
int v[MAXN];
int top,stk[MAXN];
int fidf(int x){return x==f[x]?x:f[x] = fidf(f[x]);}
void pushup(int x){sum[x] = sum[tree[x][1]]+sum[tree[x][0]]+val[x];}
void pushdown(int x){
    if(!tag[x])return;
    swap(tree[x][1],tree[x][0]);
    tag[tree[x][1]]^=1;tag[tree[x][0]]^=1;
    tag[x] = 0;
}
int which(int x){return tree[fidf(fa[x])][1] == x;}
bool isroot(int x){return (x!=tree[fidf(fa[x])][1]&&x!=tree[fidf(fa[x])][0]);}
void rotate(int x){
    int y = fidf(fa[x]),z = fidf(fa[y]),d = which(x),w = tree[x][d^1];
    if(!isroot(y))tree[z][which(y)] = x;
    fa[x] = z;fa[y] = x;
    tree[y][d] = w;
    tree[x][d^1] = y;fa[w] = y;
    pushup(y);pushup(x);
}
void splay(int x){
    top = 0;stk[++top] = x;
    for(int i = x;!isroot(i);i = fidf(fa[i]))stk[++top] = fidf(fa[i]);
    while(top)pushdown(stk[top--]);
    while(!isroot(x)){
        int y = fidf(fa[x]);
        if(!isroot(y)){
            if(which(x)==which(y))rotate(y);else rotate(x);
        }
        rotate(x);
    }
    pushup(x);
}
void access(int x){
    for(int y = 0;x;y = x,x = fidf(fa[x])){
        splay(x);tree[x][1] = y;pushup(x);
    }
}
void makeroot(int x){
    access(x);splay(x);tag[x]^=1;
}
void split(int x,int y){
    makeroot(x);access(y);splay(y);
}
void link(int x,int y){
    makeroot(x);fa[x] = y;
}
void dfs(int x,int root){
    f[x] = root;
    if(tree[x][0])dfs(tree[x][0],root);
    if(tree[x][1])dfs(tree[x][1],root);
}
int fidg(int x){return x==g[x]?x:g[x] = fidg(g[x]);}
int main(){
    int n,m;
    n = read(),m = read();
    for(int i = 1;i<=n;i++){
        v[i] = read();f[i] = i;g[i] = i;
        val[i] = sum[i] = v[i];
    }
    int p,a,b;
    while(m--){
        p = read(),a = read(),b = read();
        int fx = fidf(a),fy = fidf(b);
        if(p==1){
            if(fx!=fy){
                if(fidg(fx)!=fidg(fy)){
                    link(fx,fy);
                    g[g[fx]] = g[fy];
                }else{
                    split(fx,fy);
                    val[fy] = sum[fy];
                    dfs(fy,fy);
                    tree[fy][0] = 0;
                }
            }
        }else if(p==2){
            splay(fx);
            val[fx]+=b-v[a];
            sum[fx]+=b-v[a];
            v[a] = b;
        }else{
            if(fidg(fx)!=fidg(fy)){
                printf("-1\n");
            }else{
                split(fx,fy);
                printf("%d\n",sum[fy]);
            }
        }
    }
    return 0;
}
```