---
title: BZOJ1016[JSOI2008]最小生成树计数
date: 2019-02-17 10:04:01 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
现在给出了一个简单无向加权图。你不满足于求出这个图的最小生成树，而希望知道这个图中有多少个不同的 最小生成树。（如果两颗最小生成树中至少有一条边不同，则这两个最小生成树就是不同的）。由于不同的最小生 成树可能很多，所以你只需要输出方案数对31011的模就可以了。

#  输入
第一行包含两个数，n和m，其中1<=n<=100;1<=m<=1000;表示该无向图的节点数和边数。每个节点用1~n的整数编号。接下来的m行，每行包含两个整数：a,b,c，表示节点a,b之间的边的权值为c，其中1<=c<=1,000,000,000。数据保证不会出现自回边和重边。注意：具有相同权值的边不会超过10条。

# 输出
输出不同的最小生成树有多少个。你只需要输出数量对31011的模就可以了。

#  样例输入
```
4 6
1 2 1
1 3 1
1 4 1
2 3 2
2 4 1
3 4 1
```
#  样例输出
```
8
```
# 解答
其实就是搜索。有一个结论：
>边不同的最小生成树中，边权相同的边个数量是相等的。

证明(复制于[taoran的博客](https://www.luogu.org/blog/taoran/solution-p4208))：
>一开始集合中为空，然后向集合中加边，先加最小的边，无论怎样都会加到不能再加，就相当于把边都加入后把环删除，此时凡是能用这种边连通的点都联通了，之后把相连通的点缩为一个点考虑，第二次同理加当前最小的边（整体第二小的边）......然后感性理解一下呗qwq

做法：
我们可以把边权相等的一些边放到一起作为一个集合，然后在每个集合里面枚举每一条边，看看是否可以放到最小生成树里面。注意并查集不可以路径压缩，因为这样会丢失树的形态的信息。
代码：
```cpp
# include <cstdlib>
# include <iostream>
# include <vector>
# include <cmath>
# include <string>
# include <algorithm>
# include <cstdio>
using namespace std;
const int MAXM = 1010;
const int MAXN = 110;
struct edge{int f,t;long long w;bool operator<(const edge &e2){return w<e2.w;}}edges[MAXM];
struct range{int l,r,cnt;}ranges[MAXM];
int range_cnt;
int fa[MAXN];
int n,m;
int find(int x){return x==fa[x]?x:find(fa[x]);}
inline void init(){for(int i = 1;i<=n;i++)fa[i] = i;}
bool kruskal(){
    sort(edges+1,edges+1+m);
    init();
    int cnt = 0;
    for(int i = 1;i<=m;i++){
        if(edges[i].w!=edges[i-1].w){ranges[++range_cnt].l = i;ranges[range_cnt-1].r = i - 1;}
        int fx = find(edges[i].f);int fy = find(edges[i].t);
        if(fx!=fy){
            cnt++;
            ranges[range_cnt].cnt++;
            fa[fx] = fy;
        }
    }
    ranges[range_cnt].r = m;
    return cnt==n-1;
}
int res;
void dfs(int x,int pos,int cnt){
    if(pos==ranges[x].r+1){
        if(cnt==ranges[x].cnt)res++;
        return ;
    }
    int fx = find(edges[pos].f);int fy = find(edges[pos].t);
    if(fx!=fy){
        fa[fx] = fy;
        dfs(x,pos+1,cnt+1);
        fa[fx] = fx;//记得把并查集还原
        fa[fy] = fy;
    }
    dfs(x,pos+1,cnt);
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin>>n>>m;
    int f,t;long long w;
    for(int i = 1;i<=m;i++){
        cin>>f>>t>>w;
        edges[i].f = f;edges[i].t = t;edges[i].w = w;
    }
    init();
    if(!kruskal()){
        cout<<0<<endl;
        return 0;
    }
    init();
    int ans = 1;int mod = 31011;
    for(int i = 1;i<=range_cnt;i++){
        res = 0;dfs(i,ranges[i].l,0);ans = ans*res%mod;
        for(int j = ranges[i].l;j<=ranges[i].r;j++){
            int f = edges[j].f;int t = edges[j].t;
            int fx = find(f),fy = find(t);
            if(fx!=fy){
                fa[fx] = fy;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
```