---
title: luogu  P1967 货车运输
date: 2018-10-30 07:45:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
AA国有n n座城市，编号从 $1$ 到 $n$，城市之间有 $m$条双向道路。每一条道路对车辆都有重量限制，简称限重。现在有 $q$ 辆货车在运输货物， 司机们想知道每辆车在不超过车辆限重的情况下，最多能运多重的货物。

输入输出格式
输入格式：
第一行有两个用一个空格隔开的整数 $n,m$，表示 AA 国有 $n$ 座城市和 $m$ 条道路。

接下来 $m$行每行 $3$个整数 $x, y, z$每两个整数之间用一个空格隔开，表示从 $x$号城市到 $y$号城市有一条限重为 $z$ 的道路。注意： $x$ 不等于 $y$，两座城市之间可能有多条道路 。

接下来一行有一个整数 $q$，表示有 $q$ 辆货车需要运货。

接下来 $q$ 行，每行两个整数 $x、y$，之间用一个空格隔开，表示一辆货车需要从 $x$ 城市运输货物到 $y$ 城市，注意： **$x$ 不等于 $y$** 。
# 输入样例
#  输入样例1
```
4 3
1 2 4
2 3 3
3 1 1
3
1 3
1 4
1 3
```
#  输出样例
```
3
-1
3
```
# 解答
这道题其实就是求两点之间的路径的权值尽可能大的最小值。那么思路就是
>1.kurskal构造一颗**最大生成树** 并把这颗树建图。
2.对于点$x$ 和点$y$，我们用并查集(1中已经把构成联通块的点加入了并查集)看一下是否在同一个块中。如果在，我们就倍增找LCA，如果不在，就说明这两个点不连通。
#  倍增找LCA
这个我还是不太熟悉，所以写一下

首先，有个二维数组：p和w。p[x][i]表示$x$点向上走$2^i$步所到达的点。w[x][i]表示点$x$向上走$2^i$步以后，两点间最大路径的权值最小。
我们用dep[x]表示$x$点的深度
那么怎么处理这两个数组呢？首先从一个点开始，做dfs，然后每次拓展子节点(设为t)的时候，就把p[t][0]修改为$x$,w[t][0]修改为连接着两个点的边权。因为$2^0=1$然后拓展，i从1开始，到21(或者到一个合适的地方，大小越是$log_2^N$)结束，然后拓展每一个点的p[t][i]和w[t][i].这样就求出了这两个倍增数组。
我们用以下代码实现(有些细节在代码里面)：
```cpp
    for(int i = 1;i<=n;i++){
        if(!vis[i]){
            dep[i] = 1;
            dfs(i);
            p[i][0] = i;//对于每一个联通块的根，它向上走无论多少步，都是它自己
            w[i][0] = INF;//对于每一个联通块的根来说，只有把它的w[i][0]的值改成INF才不会对答案造成影响，因为它根本没法向上走
        }
    }
    for(int i = 1;i<=21;i++){
        for(int j = 1;j<=n;j++){
            p[j][i] = p[p[j][i-1]][i-1];
            w[j][i] = min(w[p[j][i-1]][i-1],w[j][i-1]);//这里处理w数组，是向上跳i步的值小还是跳2i步
        }
    }
}
```
处理完之后，就是找两个点的LCA。(这里不妨设dep[x]>dep[y])。那么我们先使用以下代码将$x$和$y$走到同一深度
```cpp
for(int i = 20;i>=0;i--){
        if(dep[p[x][i]]>=dep[y]){
            ans = min(w[x][i],ans);//改的时候注意更新答案
            x = p[x][i];
        }
    }
```
$x$和$y$走到同一深度以后，先判断一下它们是不是已经走到LCA了。
```cpp
if(x==y)return ans;
```
然后$x$和$y$同时向上走，直到走到LCA。注意，当p[x][i]=p[y][i]时，x和y还要向上走一步才可以到达LCA，具体原因我不知道怎么叙述~~语文太差~~。
```cpp
for(int i = 21;i>=0;i--){
        if(p[x][i]!=p[y][i]){
            ans = min(ans,min(w[x][i],w[y][i]));
            x = p[x][i];
            y = p[y][i];
        }
    }
    ans = min(ans,min(w[x][0],w[y][0]));
    return ans;
```
最后，附上AC代码
```cpp
// luogu-judger-enable-o2
# include <cstdio>
# include <algorithm>
# include <cstring>

using namespace std;
const int MAXN = 100010;
const int MAXM = 500010;
struct edge{
    int f,t,w,next;
    bool operator<(const edge &e2)const{
        return w>e2.w;
    }
}map[MAXN],tree_map[MAXM];//原图和生成树的图
const int INF = 0x7f7f7f7f;
int head_tree[MAXN],head[MAXN];
int tree_top,top;
int w[MAXN][25];//w[x][i]表示x向上跳2^i个点以后，生成树中最小的边权
int p[MAXN][25];//p[x][i]表示x向上跳2^i个点以后，到达的点
int father[MAXN];
bool vis[MAXN];
int dep[MAXN];
int n,m;
inline int find(int x){return father[x]==x?x:find(father[x]);}
inline void unionn(int x,int y){father[find(y)] = father[find(x)];}
inline bool judge(int x,int y){return find(x)==find(y);}
inline void swap(int &x,int &y){x = x^y;y = y^x;x = x^y;}
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
    while(c>='0'&&c<='9'){x = x*10+c-'0';c = getchar();}
    return x*f;
}
void addMap(int f,int t,int w){
    map[++top].next = head[f];
    map[top].f = f;
    map[top].t = t;
    map[top].w = w;
    head[f] = top;
}
void addTree(int f,int t,int w){
    tree_map[++tree_top].next = head_tree[f];
    tree_map[tree_top].t = t;
    tree_map[tree_top].w = w;
    tree_map[tree_top].f = f;
    head_tree[f] = tree_top;
}
void kruskal(){
    for(int i = 1;i<=n;i++)father[i] = i;
    sort(map+1,map+2*m+1);//无向图
    int cnt = 0;
    for(int i = 1;i<=2*m;i++){
        if(!judge(map[i].f,map[i].t)){
            addTree(map[i].f,map[i].t,map[i].w);
            addTree(map[i].t,map[i].f,map[i].w);
            unionn(map[i].f,map[i].t);
            cnt++;
        }
        if(cnt==n-1)break;
    }
}
void dfs(int x){
    vis[x] = true;
    for(int i = head_tree[x];i!=0;i = tree_map[i].next){
        int t = tree_map[i].t;
        if(!vis[t]){
            p[t][0] = x;
            w[t][0] = tree_map[i].w;
            dep[t] = dep[x]+1;
            dfs(t);
        }
    }
}
void init(){
    for(int i = 1;i<=n;i++){
        if(!vis[i]){
            dep[i] = 1;
            dfs(i);
            p[i][0] = i;
            w[i][0] = INF;
        }
    }
    for(int i = 1;i<=21;i++){
        for(int j = 1;j<=n;j++){
            p[j][i] = p[p[j][i-1]][i-1];
            w[j][i] = min(w[p[j][i-1]][i-1],w[j][i-1]);
        }
    }
}
int lca(int x,int y){
    int ans = INF;
    if(!judge(x,y))return -1;
    if(dep[x]<dep[y])swap(x,y);//现在y的深度小于x
    for(int i = 20;i>=0;i--){
        if(dep[p[x][i]]>=dep[y]){
            ans = min(w[x][i],ans);
            x = p[x][i];
        }
    }
    if(x==y)return ans;
    for(int i = 21;i>=0;i--){
        if(p[x][i]!=p[y][i]){
            ans = min(ans,min(w[x][i],w[y][i]));
            x = p[x][i];
            y = p[y][i];
        }
    }
    ans = min(ans,min(w[x][0],w[y][0]));
    return ans;
}
int main(void){
    n = read();
    m = read();
    int f,t,we;
    for(int i = 1;i<=m;i++){
        f = read(),t = read(),we = read();
        addMap(f,t,we);
        addMap(t,f,we);
    }
    kruskal();
    init();
    int q = read();
    while(q--){
        f = read();
        t = read();
        printf("%d\n",lca(f,t));
    }
    return 0;
}
```