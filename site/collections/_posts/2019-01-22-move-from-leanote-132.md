---
title: 最短路拓展
date: 2019-01-22 11:14:56 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 次短路
就是在维护最短路的时候，顺便维护一下次短路。维护方法如下(spfa)

 1. 如果最短路被更新，那么就把次短路更新为之前的最短路
 2. 如果当前次短路大于最短路，且最短路没被更新，那么尝试更新
 3. 如果最短路没被更新，那么就尝试更新次短路
 

dijkstra做法：
 
 1. 如果最短路可以更新，那么更新
 2. 如果次短路长度大于最短路且可以更新次短路，更新

例题[[USACO06NOV]路障Roadblocks](https://www.luogu.org/problemnew/show/P2865)
代码如下：(spfa)
```cpp
# include <cstdio>
# include <iostream>
# include <queue>
# include <algorithm>
# include <stdio.h>
# include <deque>
# include <cstring>
# define LL long long
using namespace std;
const int MAXN = (int)100100;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
struct edge{int next,t,w;}edges[MAXN<<1];
int top,head[MAXN];
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int dis1[MAXN],dis2[MAXN];
int vis[MAXN];
void spfa(){
    int s = 1;
    memset(vis,false, sizeof(vis)),memset(dis1,0x3f, sizeof(dis1)),memset(dis2,0x3f, sizeof(dis2));
    queue<int> q;
    vis[s] = true,dis1[s] = 0;
    q.push(s);
    while (!q.empty()){
        int top = q.front();q.pop();
        vis[top]  =false;
        for(int i = head[top];i;i = edges[i].next){
            int t = edges[i].t;
            if(dis1[t]>dis1[top]+edges[i].w){
                dis2[t] = dis1[t];
                dis1[t]=dis1[top]+edges[i].w;
                if(!vis[t]){vis[t] = true;q.push(t);}
            }
            if(dis2[t]>dis1[top]+edges[i].w&&dis1[t]<dis1[top]+edges[i].w){
                dis2[t]=dis1[top]+edges[i].w;if(!vis[t]){vis[t] = true;q.push(t);}
            }
            if(dis2[t]>dis2[top]+edges[i].w){
                dis2[t]=dis2[top]+edges[i].w;if(!vis[t]){vis[t] = true;q.push(t);}
            }
        }
    }
}
int main(){
    int n,m;
    n = read(),m = read();
    for(int i = 1;i<=m;i++){
        int f = read(),t = read(),w = read();
        add(f,t,w);
        add(t,f,w);
    }
    spfa();
    cout<<dis2[n];
    return 0;
}
```
dijkstra:
```cpp
# include<bits/stdc++.h>
using namespace std;
# define N 100000
struct node{
	int u,v,w;
}e[N<<1];//边目录
int first[N]={0},nxt[N<<1],cnt=0;//详见前向星
int n,m,st,ed;
int visited[N],dis[N],secdis[N];
void add(int u,int v,int w){
	e[++cnt].u=u;
	e[cnt].v=v;
	e[cnt].w=w;
	nxt[cnt]=first[u];
	first[u]=cnt;
} 
void init(){
	cin>>n>>m;
	for(int i=1;i<=m;i++){
		int u,v,w;
		cin>>u>>v>>w;
		add(u,v,w);
		add(v,u,w);
	}
}
typedef pair<int,int> T;
void dijkstra(int s){
	memset(visited,0,sizeof(visited));
	memset(dis,0x3f,sizeof(dis));
	memset(secdis,0x3f,sizeof(secdis));
	dis[s]=0;
	priority_queue<T,vector<T>,greater<T> > q;
	q.push(make_pair(dis[s],s));
	while(!q.empty()){
		pair<int,int>t=q.top();
		q.pop();
		int d=t.first,u=t.second;
		if(d>secdis[u]) continue;
		visited[u]=1;
		for(int i=first[u];i;i=nxt[i]){
			int v=e[i].v;
			if(d+e[i].w<dis[v]){
				dis[v]=d+e[i].w;
				q.push(make_pair(dis[v],v));
			}
			if(d+e[i].w<secdis[v]&&d+e[i].w>dis[v]){
				secdis[v]=d+e[i].w;
				q.push(make_pair(secdis[v],v));
			}
		}
	}
}
int main(){
	init();
	dijkstra(1);
	cout<<secdis[n];
}
```
# 最短路计数
其实就是在更新的时候记一下数(加法原理)，**spfa算法要用多一个数组表示被累加的数，并且更新完了以后要清零，防止重复计算~~spfa毛病多~~**
dijkstra做法：
>求最短路的条数只需要在dijkstra上面加一个数组sumt[]记录就行，
sumt[v] 表示从源点 s 出发到 v 的最短路条数， 
• 当 dist[v] > dist[u] + d[u][v] 时，更新sumt[v] 的值就是 sumt[u]； 
• 当 dist[v] == dist[u] + d[u][v] 时，sumt[v] += sumt[u]； 
• 判断是否存在无数条最短路，即看是否存在这样的一条边(u, v)，
边权为 0，并且其中一条最短路经过这条边，也就是 源点 s 到 u 
的最短距离 + v 到终点 t 的最短距离 == 最短路长度，因为边权为 
0 的话就可以来回无限次地走。所以需要两次最短路分别计算出
源点 s 到每个点的最短路、每个点到终点 t 的最短路，然后枚举
每条边，即可判断是否存在无数条最短路 
代码：(不知道为什么woj要T一个点)
```cpp
# include <cstdio>
# include <iostream>
# include <queue>
# include <algorithm>
# include <stdio.h>
# include <deque>
# include <cstring>
using namespace std;
const int MAXN = (int)1000100;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
struct edge{int next,f,t,w;}edges[MAXN<<1];
int top,head[MAXN];
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].f = f;
    edges[top].w = w;
    head[f] = top;
}
long long g[MAXN];
const int mod = 1000000009;
long long dis1[MAXN],dis2[MAXN];
void dijkstra(int s, long long *dis){
    priority_queue<pair<int,int> > q;
    dis[s] = 0;
    g[s] = 1;
    q.push(make_pair(0,s));
    while(!q.empty()){
        pair<int,int> top = q.top();
        q.pop();
        if(dis[top.second]<top.first)continue;
        for(int i = head[top.second];i;i = edges[i].next){
            int t = edges[i].t;
            if(dis[t]>dis[top.second]+edges[i].w){
                dis[t] = dis[top.second]+edges[i].w;
                g[t] = g[top.second];
                q.push(make_pair(dis[t],t));
            }else{
                if(dis[t]==dis[top.second]+edges[i].w)g[t] = g[t]+g[top.second]%mod;
            }
        }
    }
}
int n,m;
bool judge(){
    for(int i = 1;i<=m;i+=2){
        int f = edges[i].f,t = edges[i].t;
        if(edges[i].w ==0&&dis1[f]+dis2[t]==dis1[n])return true;
    }
    return false;
}
int main(){
    n = read(),m = read();
    memset(dis1,0x3f, sizeof(dis1));
    memset(dis2,0x3f, sizeof(dis2));
    int f,t,w;
    for(int i = 1;i<=m;i++){
        f = read(),t = read(),w = read();
        add(f,t,w);
        add(t,f,w);
    }
    dijkstra(n,dis2);
    memset(g,0, sizeof(g));
    dijkstra(1,dis1);
    if(!judge())printf("%lld",g[n]);else printf("-1");
    return 0;
}
```
spfa 做法
Spfa不能像dijkstra那样直接计算，需要做一定调整。
设定数组dlt[i]表示点i在队列中累加的路径数，然后这样做
```cpp
# include<iostream>
# include<algorithm>
# include<cstdio>
# include<cstring>
# define N 200505
# define M 200105
# define INF 0x7f7f7f7f
using namespace std;
int dis[N],fst[N];
bool inq[N];
int u[M],v[M],w[M],nst[M];
int dl[200001];
int n,m,s,e,cnt=0;
int anss[100100];
//fst、nst为邻接表，u、v、w分别是每一条边的起点、终点、权值，inq标记点是否在队列中
void spfa(int s){
	for(int i=1;i<=n;i++) dis[i]=INF;
    dl[1]=s; inq[s]=1; dis[s]=0;
    int h=0,t=1;
    while(h!=t){
        h++;
        if(h>10000) h=1;
        for(int k=fst[dl[h]];k;k=nst[k]){
        	if(dis[v[k]]==dis[u[k]]+w[k]&&w[k]!=0)
        		anss[v[k]]=anss[v[k]]+anss[u[k]];//可以更新就更新，传递信息
        		if(dis[v[k]]==dis[u[k]]+w[k]&&w[k]==0)
        		anss[v[k]]=-1;
            if(dis[v[k]]>dis[u[k]]+w[k]){
                dis[v[k]]=dis[u[k]]+w[k];anss[v[k]]=anss[u[k]];
                if(!inq[v[k]]){
                    t++;
                    if(t>10000) t=1;
                    dl[t]=v[k];
                    inq[v[k]]=1;
                }
            }
        }
        inq[dl[h]]=0;//注意清空
    }
}
int main(){
    int i,j;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    anss[i]=1;
    for(i=1;i<=m;i++) //双向存储
    {
        cnt++;
        scanf("%d%d%d",&u[cnt],&v[cnt],&w[cnt]);
        nst[cnt]=fst[u[cnt]];
        fst[u[cnt]]=cnt;
        cnt++;
        u[cnt]=v[cnt-1],v[cnt]=u[cnt-1],w[cnt]=w[cnt-1];
        nst[cnt]=fst[u[cnt]];
        fst[u[cnt]]=cnt;
    }
    spfa(1);
    printf("%d\n",anss[n]);
    return 0;
}
```
其实dj好做的多
# S-T最短路中，经过点A路径总数
做法：正反跑2次图，求出1-A的路径总数，在求出n-A的路径总数，乘起来，就完了。前提是A在最短路上。判断Ａ在最短路上方法如下
1-A的最短路距离+A-T的最短路距离==1-n的最短路距离，那么A在最短路上。答案=g[1][a] * g[a][n]
# 分层图
对于有些图上的问题，直接处理不好做，把图假想分层，再跑最短路，就方便多了
eg[[USACO09FEB]改造路Revamping Trails](https://www.luogu.org/problemnew/show/P2939)
就是枚举删每k条边，然后分别建立k张图。再跑dij~mdzz 这题卡spfa~~
代码如下：
```cpp
//
// Created by dhy on 19-1-21.
//
# include <iostream>
# include <cstring>
# include <queue>
# include <cstdio>
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const int MAXN = 220010;
const int MAXM = 4200010;
struct edge{
    int t,w,next;
}edges[MAXM];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int dis[MAXN];
bool vis[MAXN];
void spfa(){
    memset(dis,0x3f,sizeof(dis));
    memset(vis,false,sizeof(vis));
    queue<int> q;
    int s = 1;
    vis[s] = true;
    dis[s] = 0;
    q.push(s);
    while(!q.empty()){
        int top = q.front();
        q.pop();
        vis[top] = false;
        for(int i = head[top];i!=0;i = edges[i].next){
            int t = edges[i].t;
            if(dis[t]>dis[top]+edges[i].w){
                dis[t] = dis[top]+edges[i].w;
                if(!vis[t]){
                    vis[t] = true;
                    q.push(t);
                }
            }
        }
    }
}
struct node{
    int f,w;
    bool operator<(const node &n2)const{
        return w>n2.w;
    }
};
void dijkstra(){
    priority_queue<node> q;
    memset(dis,0x3f,sizeof(dis));
    memset(vis,false,sizeof(vis));
    node temp;
    temp.f = 1;
    dis[1] = 0;
    temp.w = 1;
    q.push(temp);
    while(!q.empty()){
        node top = q.top();
        q.pop();
        if(vis[top.f])continue;
        vis[top.f] = true;
        for(int i = head[top.f];i!=0;i = edges[i].next){
            int t = edges[i].t;
            if(dis[t]>dis[top.f]+edges[i].w){
                dis[t]=dis[top.f]+edges[i].w;
                temp.f = t;
                temp.w = dis[top.f]+edges[i].w;
                q.push(temp);
            }
        }
    }
}
int main(){
    int k;
    int n = read();int m = read();
    k = read();
    for(int i = 1;i<=m;i++){
        int f =read(),t = read(),w = read();
        add(f,t,w);
        add(t,f,w);//0层
        for(int j = 1;j<=k;j++){
            add(j*n+f,j*n+t,w);
            add(j*n+t,j*n+f,w);
            add((j-1)*n+f,j*n+t,0);
            add((j-1)*n+t,j*n+f,0);
        }
    }
//    spfa();
    dijkstra();
    int ans = 0x3f3f3f3f;
    for(int i = 0;i<=k;i++){
        ans = min(ans,dis[i*n+n]);
    }
    printf("%d",ans);
    return 0;
}
```
当然了，这道题也可以用类似于DP+最短路的算法。见梁老讲义。
