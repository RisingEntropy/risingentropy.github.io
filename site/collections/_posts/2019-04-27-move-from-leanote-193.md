---
title: 【lct，最小生成树】luoguP4172 [WC2006]水管局长
date: 2019-04-27 14:52:30 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
`SC` 省 `MY` 市有着庞大的地下水管网络，嘟嘟是 `MY` 市的水管局长（就是管水管的啦），嘟嘟作为水管局长的工作就是：每天供水公司可能要将一定量的水从 `x` 处送往 `y` 处，嘟嘟需要为供水公司找到一条从 `A` 至 `B` 的水管的路径，接着通过信息化的控制中心通知路径上的水管进入准备送水状态，等到路径上每一条水管都准备好了，供水公司就可以开始送水了。嘟嘟一次只能处理一项送水任务，等到当前的送水任务完成了，才能处理下一项。
在处理每项送水任务之前，路径上的水管都要进行一系列的准备操作，如清洗、消毒等等。嘟嘟在控制中心一声令下，这些水管的准备操作同时开始，但由于各条管道的长度、内径不同，进行准备操作需要的时间可能不同。供水公司总是希望嘟嘟能找到这样一条送水路径，路径上的所有管道全都准备就绪所需要的时间尽量短。嘟嘟希望你能帮助他完成这样的一个选择路径的系统，以满足供水公司的要求。另外，由于 `MY` 市的水管年代久远，一些水管会不时出现故障导致不能使用，你的程序必须考虑到这一点。
不妨将 `MY` 市的水管网络看作一幅简单无向图（即没有自环或重边）：水管是图中的边，水管的连接处为图中的结点。
#  输入
输入文件第一行为 3 个整数：N,M,Q 分别表示管道连接处（结点）的数目、目前水管（无向边）的数目，以及你的程序需要处理的任务数目（包括寻找一条满足要求的路径和接受某条水管坏掉的事实）。
以下 M行，每行 3 个整数x,y 和 t，描述一条对应的水管。x 和 y 表示水管两端结点的编号，t表示准备送水所需要的时间。我们不妨为结点从 1 至 N 编号，这样所有的 x 和 y 都在范围[1,N]内。
以下 Q 行，每行描述一项任务。其中第一个整数为 k：
若 k=1则后跟两个整数A和B，表示你需要为供水公司寻找一条满足要求的从 A 到 B 的水管路径；
若 k=2，则后跟两个整数x和 y，表示直接连接 x和y 的水管宣布报废（保证合法，即在此之前直接连接 x 和 y 尚未报废的水管一定存在）。
#  输出
按顺序对应输入文件中每一项 k=1的任务，你需要输出一个数字和一个回车/换行符。该数字表示：你寻找到的水管路径中所有管道全都完成准备工作所需要的时间（当然要求最短）。
#  样例输入
```
4 4 3
1 2 2
2 3 3
3 4 2
1 4 2
1 1 4
2 1 4
1 1 4
```
样例输出
```
2
3
```
提示
N≤10000
M≤1000000
Q≤100000
测试数据中宣布报废的水管不超过 5000条；且任何时候我们考虑的水管网络都是连通的，即从任一结点 A必有至少一条水管路径通往任一结点 B 。
# 解答
我们考虑货车运输的做法。就是树链上的最短路径，那么最小生成树一定是最优的(可以参考`kurskal`的证明)，然后由于是维护的边权，所以我们要拆边，建立虚点，边权转点权。注意一点，虚点的编号就是n+虚电代表的边的编号。然后lct维护的标记mx是最大点权的点的**编号**。考虑到有删边不好做，我们可以离线，这样删边就变成了加边，简单容易多了。这题有点考代码能力。~~对于我这种没啥代码能力的蒟蒻来说，只能看题解~~
代码
```cpp
# include <iostream>
# include <algorithm>
# include <cstdio>
# include <map>
# define mp make_pair
using namespace std;
const int MAXN = 100010+1000010;
int n,m;
int tree[MAXN][2],mx[MAXN],fa[MAXN],tag[MAXN],sum[MAXN],val[MAXN];
int top,stk[MAXN];
typedef pair<int, int> pii;
struct edge{int f,t,w;bool vis;bool operator<(const edge&e2)const{return w<e2.w;}}edges[1000010];
struct query{int op,x,y,id,ans;}querys[100010];
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}

int which(int x){return tree[fa[x]][1]==x;}
void pushup(int x){
    mx[x] = val[x];
    if(edges[mx[tree[x][0]]].w>edges[mx[x]].w)mx[x] = mx[tree[x][0]];
    if(edges[mx[tree[x][1]]].w>edges[mx[x]].w)mx[x] = mx[tree[x][1]];
}
void pushdown(int x){
    if(!tag[x])return ;
    swap(tree[x][0],tree[x][1]);
    tag[tree[x][0]]^=1;
    tag[tree[x][1]]^=1;
    tag[x] = 0;
}
bool isroot(int x){return !fa[x]||(x!=tree[fa[x]][0]&&x!=tree[fa[x]][1]);}
void rotate(int x){
    int y = fa[x],z = fa[y],d = which(x);
    if(!isroot(y))tree[z][which(y)] = x;
    fa[x] = z;fa[y] = x;tree[y][d] = tree[x][d^1];
    tree[x][d^1] = y;fa[tree[y][d]] = y;
    pushup(y),pushup(x);
}
void splay(int x){
    top = 0;stk[++top] = x;
    for(int i = x;!isroot(i);i = fa[i])stk[++top] = fa[i];
    while(top)pushdown(stk[top--]);
    for(int y = fa[x];!isroot(x);rotate(x),y = fa[x]){
        if(!isroot(y))rotate(which(x)==which(y)?y:x);
    }
}
void access(int x){
    for(int y = 0;x;y = x,x = fa[x]){
        splay(x),tree[x][1] = y,pushup(x);
    }
}
void makeroot(int x){access(x),splay(x);tag[x]^=1;}
int find(int x){
    access(x);splay(x);
    while(tree[x][0])pushdown(x),x = tree[x][0];
    splay(x);return x;
}
void split(int x,int y){
    makeroot(x);access(y);splay(y);
}
void link(int x,int y){
    makeroot(x);fa[x] = y;pushup(y);
}
void cut(int x,int y){
    if(find(x)!=find(y))return ;
    split(x,y);
    if(fa[x]!=y||tree[x][1])return ;
    tree[y][0] = fa[x] = 0;pushup(y);
}
void init(int x,int y){
    mx[x] = val[x] = y;
}
map<pii,int> ap;
int main(){
    int q;
    ios::sync_with_stdio(false);
    n = read(),m = read(),q = read();
    for(int i = 1;i<=m;i++){
        int f,t,w;f = read(),t = read(),w = read();
        if(f>t)swap(f,t);
        edges[i].f = f;edges[i].t = t;edges[i].w = w;
    }
    sort(edges+1,edges+1+m);
    for(int i = 1;i<=m;i++)ap[mp(edges[i].f,edges[i].t)] = i;
    for(int i = 1;i<=q;i++){
        int f,t,op;op = read(),f = read(),t = read();
        if(f>t)swap(f,t);
        querys[i].x = f;querys[i].y = t;
        querys[i].op = op;
        if(op==2){
            querys[i].id = ap[mp(f,t)];
            edges[querys[i].id].vis = true;
        }
    }
    int all = m+n;
    for(int i = 1;i<=all;i++)init(i,i<=n?0:(i-n));
    int sum = 0;
    for(int i = 1;i<=m;i++){
        if(!edges[i].vis){
            if(sum==n-1)break;
            if(find(edges[i].f)==find(edges[i].t))continue;
            link(edges[i].f,i+n);link(edges[i].t,i+n);
            sum++;
        }
    }
    for(int i = q;i>=1;i--){
        int f = querys[i].x,t = querys[i].y,op = querys[i].op;
        if(op==1){
            split(f,t);querys[i].ans = edges[mx[t]].w;
        } else{
            split(f,t);
            int id = querys[i].id,y = mx[t];
            if(edges[id].w<edges[y].w){
                cut(edges[y].f,y+n);cut(edges[y].t,y+n);
                link(f,id+n);link(t,id+n);
            }
        }
    }
    for(int i = 1;i<=q;i++)if(querys[i].op==1)printf("%d\n",querys[i].ans);
}
```