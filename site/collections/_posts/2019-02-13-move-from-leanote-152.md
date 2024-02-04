---
title: bzoj 2654 tree
date: 2019-02-13 19:14:23 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
给你一个无向带权连通图，每条边是黑色或白色。让你求一棵最小权的恰好有need条白色边的生成树。题目保证有解。
#  输入
第一行V,E,need分别表示点数，边数和需要的白色边数。
接下来E行,每行s,t,c,col表示这边的端点(点从0开始标号)，边权，颜色(0白色1黑色
#  输出
一行表示所求生成树的边权和。
V<=50000,E<=100000,所有数据边权为[1,100]中的正整数。
#  样例
#  样例输入
```
2 2 1
0 1 1 1
0 1 2 0
```
#  样例输出
```
2
```
# 解答
好怪异的一道题。贪心显然是不对的~~我就WA了好几次~~。怎么做呢？我们发现，如果白色边的边权整体大一点的话，那么最小生成树里面，白边就会少一点。如果白边边权少一点，那么白边就会多一点。再看看，我们发现有单调性(白边当且大小都满足不了$need$条边，那么再多一点肯定白边就更少了)所以我们可以二分。在$[-100,100]$范围内二分.注意，在整数域内二分的话，只能$mid=l+r>>1$而不能$mid = l+r/2$因为他们在整数域上含义，`/`是向0取整，`>>`是向下取整，用`/`的话会导致漏解。注意还以一个坑点**排序时，如果边权相同，那么需要把白边优先放到前面去**
```cpp
//
// Created by dhy on 19-2-12.
//
# include <iostream>
# include <algorithm>
using namespace std;
struct edge{int f,t,w,color;bool operator<(const edge&e2)const { return w==e2.w?color<e2.color:w<e2.w;}};
const int MAXN = 100010;
int V,E,need;
edge edges[MAXN];
int top;
int fa[MAXN];
inline int find(int x){return x==fa[x]?x:fa[x] = find(fa[x]);}
inline bool judge(int x,int y){return find(x)==find(y);}
inline void unionn(int x,int y){fa[find(y)]=find(x);}
void init(){for(int i = 1;i<=V;i++)fa[i] = i;}
int ans = 0;
bool check(int x){
    for(int i = 1;i<=top;i++)if(edges[i].color==0)edges[i].w+=x;
    init();
    int tot = 0,white = 0;
    sort(edges+1,edges+1+top);
    int MST = 0;
    for(int i = 1;i<=top;i++){
        if(judge(edges[i].f,edges[i].t))continue;
        unionn(edges[i].f,edges[i].t);
        white+=1-edges[i].color;
        tot++;
        MST+=edges[i].w;
        if(tot>=V-1){
            break;
        }
    }
    for(int i = 1;i<=top;i++)if(edges[i].color==0)edges[i].w-=x;
    ans = MST;
    return white>=need;
}
int main(){
    cin>>V>>E>>need;
    int f,t,w,color;
    for(int i = 1;i<=E;i++){
        cin>>f>>t>>w>>color;
        f++,t++;
        edges[++top].f = f;edges[top].t = t;edges[top].w = w;edges[top].color = color;
    }
    int l = -100,r = 100;
    while(l<r){
        int mid = l+r+1>>1;
        if(check(mid))l = mid;
        else r = mid-1;
    }
    check(l);
    cout<<ans-l*need;
    return 0;
}
```