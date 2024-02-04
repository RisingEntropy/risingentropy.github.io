---
title: luogu P1608 路径统计
date: 2018-11-01 21:46:48 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
“RP餐厅”的员工素质就是不一般，在齐刷刷的算出同一个电话号码之后，就准备让HZH,TZY去送快餐了，他们将自己居住的城市画了一张地图，已知在他们的地图上，有N个地方，而且他们目前处在标注为“1”的小镇上，而送餐的地点在标注为“N”的小镇。（有点废话）除此之外还知道这些道路都是单向的，从小镇I到J需要花费D[I,J]的时间，为了更高效快捷的将快餐送到顾客手中，
他们想走一条从小镇1到小镇N花费最少的一条路，但是他们临出发前，撞到因为在路上堵车而生气的FYY，深受启发，不能仅知道一条路线，万一。。。，于是，他们邀请FYY一起来研究起了下一个问题：这个最少花费的路径有多少条？
# 输入输出格式
# 输入格式：
输入文件第一行为两个空格隔开的数N，E，表示这张地图里有多少个小镇及有多少边的信息。
下面E行，每行三个数I、J、C，表示从I小镇到J小镇有道路相连且花费为C.（注意，数据提供的边信息可能会重复，不过保证I<>J,1<=I,J<=n）。
# 输出格式：
输出文件包含两个数，分别是最少花费和花费最少的路径的总数.
两个不同的最短路方案要求：路径长度相同（均为最短路长度）且至少有一条边不重合。
若城市N无法到达则只输出一个(‘No answer’);
# 输入输出样例
#  输入样例# 1： 
```
5 4
1 5 4
1 2 2
2 5 2
4 1 1
```
#  输出样例# 1： 
```
4 2
```
说明
对于30%的数据 N<=20;
对于100%的数据 1<=N<=2000,0<=E<=N*(N-1), 1<=C<=10.
# 解答
这道题正解大家都会~~不会的看楼上楼下的题解~~。我今天来交大家一种骗分算法:A\*!又名A star。是一种 **启发式搜索** 以下是定义
>A*算法，A*（A-Star)算法是一种静态路网中求解最短路径最有效的直接搜索方法，也是解决许多搜索问题的有效算法。算法中的距离估算值与实际值越接近，最终搜索速度越快。   -----百度百科

看了这个你也很懵~~mengbier~~对吧？其实这些都是废话。我现在给你举个例子：如果你从昆明到北京，现在你到了成都，已经走了500KM了，然后你有多条路可以走，每条路都有一个路牌，分别写着据北京700KM 750KM 800KM。那么你要走最短的路到北京，你肯定会优先选择700KM的一条而不是其他的路对吧。~~狗吃骨头都知道跑最短路~~ A\* 的思想意识一样的，它分为两个部分：走到当前点的权值和(花费)$h(x)$和估计到达目的地的花费(就是所谓的估计函数)$g(x)$。然后我们优先拓展可能权值和(所谓可能权值和就是$h(x)+g(x)$)最小/最大 的点，这样就可以避免拓展无用的状态，减少时间开销。

这道题我们用A\*来做，那就很简单了。首先建立一个反图(用于求取每一个点到n点的最短距离)和正图(后面的A\* 遍历用)，然后用~~spfa他死了~~ dijkstra跑一次最短路以获得每个点到n的最短距离，作为我们的估计函数，这样我们就获得了一个十分准确的估价函数。然后通过bfs每次选取可能花费最小的拓展，如果走到目标点，我们就记录一下(选取花费最小的点需要把bfs里面的队列换成优先队列，即**小根堆**)。

这样做固然可以，但是会T掉很多点，为什么呢？因为虽然用了启发式搜索，还是拓展了一些不可能在最短路上的点，所以我们需要另一利器：剪枝！没错，在bfs上剪枝！那么剪枝条件呢？我们只需要考虑可行性剪枝即可，因为最短路上起点到任意一点的距离加上这个点到终点的距离一点等于最短路权值和(废话)！如果堆顶的点的可能权值(这里的权值其实是确定的，因为我们的估计函数是精确的)都已经大于了最短路了，堆里面的其他元素都不可能在最短路上了那么我们直接返回就行了。关于A\* 可以看看我的另一篇题解：[P4467 [SCOI2007]k短路](http://denghaoyu.leanote.com/post/luoguP4467-%5BSCOI2007%5Dk%E7%9F%AD%E8%B7%AF) 推荐做一下[P4467](https://www.luogu.org/problemnew/show/P1608).原谅我的博客里借鉴了P4467一位大佬写的题解里面的图

注意A\*算法对内存要求比较大，出题人也会卡A\* （不然谁去写正解啊）所以在写A*时我推荐使用`algorithm` 库里面的`push_heap`和`pop_heap` 函数或者手打堆，而不要使用`priority_queue` 因为`priority_queue`内存用的多，不吸氧会T掉，吸氧会MLE。

最后由于A\* 不是正解，所以不可避免被卡掉几个点，所以我用了~~面向数据编程~~把这道题A了。不然也有80分

![ ](https://cdn.risingentropy.top/images/posts/bdba0cfab64410c0d001348.png)

以下是80分代码:
```cpp
# include <fstream>
# include <cstring>
# include <stdlib.h>
# include <algorithm>
# include <cstdio>
# include <queue>
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
const int MAXN = 2010;
int map1[MAXN][MAXN];
int map2[MAXN][MAXN];
int n,m;
inline void add(int f,int t,int w){
    map1[f][t] = w;
}
inline void add2(int f,int t,int w){
    map2[f][t] = w;
}
int dis[MAXN];
int vis[MAXN];
void spfa(){
    memset(dis,0x3f, sizeof(dis));
    memset(vis,false, sizeof(vis));
    queue<int> q;
    dis[n] = 0;
    vis[n] = true;
    q.push(n);
    while(!q.empty()){
        int top = q.front();
        q.pop();
        vis[top] = false;
        for(int i = 1;i<=n;i=-~i){
            if(map1[top][i]!=1061109567) {//联通的
                if (dis[i] > dis[top] + map1[top][i]) {
                    dis[i] = dis[top] + map1[top][i];
                    if (!vis[i]) {
                        vis[i] = true;
                        q.push(i);
                    }
                }
            }
        }
    }
}
struct node{
    int f,w;
    bool operator<(const node& n2)const{
        return w+dis[f]>n2.w+dis[n2.f];
    }
};
int ans;
node nodes[MAXN*MAXN];
int cnt;
void init(){
    make_heap(nodes+1,nodes+MAXN);
}
inline void push(const node &n){
    nodes[++cnt] = n;
    push_heap(nodes+1,nodes+cnt+1);
}
inline node pop(){
    pop_heap(nodes+1,nodes+cnt+1);
    return nodes[cnt--];
}
inline node qtop(){
    return nodes[1];
}
void AStar(){
    node s ={1,0};
    push(s);
    while(cnt){
        node top = qtop();
        pop();
        if(top.w>dis[1])return;
        if(top.w==dis[1]){
            if(top.f==n){
                ans++;
                continue;
            } else{
                return;
            }
        }
        for(int i = 1;i<=n;i=-~i){
            if(map2[top.f][i]!=1061109567) {
                node to = top;
                to.f = i;
                to.w += map2[top.f][i];
                push(to);
            }
        }
    }
}
int main(void){
    memset(map1,0x3f, sizeof(map1));
    memset(map2,0x3f, sizeof(map2));
    n = read(),m = read();
    int f,t,w;
    for(int i = 1;i<=m;i++){
        f = read(),t = read(),w = read();
        add(t,f,w);
        add2(f,t,w);
    }
    spfa();
    init();
    if(dis[1]==1061109567){
        printf("No answer\n");
    }else{
        AStar();
        printf("%d %d",dis[1],ans);
    }
    return 0;

}
```
最后，祝NOIP2018 rp++，各位大佬AK NOIP rp++，报送t大或者p大！共勉！