---
title: 【最短路 杂题】woj3841 双调路径
date: 2019-10-21 19:27:05 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
如今的道路收费发展很快。道路的密度越来越大，因此选择最佳路径是很现实的问题。城市的道路是双向的，每条道路有固定的旅行时间以及需要支付的费用。
路径是连续经过的道路组成的。总时间是各条道路旅行时间的和，总费用是各条道路所支付费用的总和。一条路径越快，或者费用越低，该路径就越好。严格地说，如果一条路径比别的路径更快，而且不需要支付更多费用，它就比较好。反过来也如此理解。如果没有一条路径比某路径更好，则该路径被称为最小路径。
这样的最小的路径有可能不止一条，或者根本不存在路径。
问题：读入网络，计算最小路径的总数。费用时间都相同的两条最小路径只算作一条。你只要输出不同种类的最小路径数即可。
#  输入
第一行有四个整数，城市总数 n，道路总数 m，起点和终点城市 s,e
接下来的 m 行每行描述了一条道路的信息，包括四个整数，两个端点 p,r ，费用 c，以及时间 t ；
两个城市之间可能有多条路径连接。
#  输出
仅一个数，表示最小路径的总数。
样例输入
```
4 5 1 4
2 1 2 1
3 4 3 1
2 3 1 2
3 1 1 4
2 4 2 4
```
#  样例输出
```
2
```
# 解答
屑题面，题目的意思是当一条路径时间最小，而代价不多于其他路径的的路径以及代价最小时间不多于其他路径的路径叫最有路径，如果一条时间小，一条代价小，那么不够成比较关系，都统计。然后就是带状态spfa，dis[i][j]表示阿紫j时间到达i节点的最小话费，直接转移就是了。
然后会发现被卡了，因为如果$i<i_1 j<j_1$那么dis[i][j]肯定比dis[i1][j1]劣，然后树状数组优化DP转移就OK了。
代码:
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
using namespace std;
const int MAXT = 10010;
const int MAXN = 110;
const int MAXM = 310;
typedef pair<int,int> pii;
inline char nc(){
	static char buf[100000],*p1=buf,*p2=buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
template<typename T>
void read(T &x){
	x = 0;T f = 1;
	char c =nc();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
	x*=f;
}
struct edge{int f,t,w,time,next;}edges[MAXM<<2];
int head[MAXN],top = 1;
void add(int f,int t,int w,int time){
	edges[++top].next = head[f];
	edges[top].w = w;
	edges[top].t = t;
	edges[top].time = time;
	head[f] = top;
}
int n,m,s,e;
int dis[MAXN][MAXT];
bool vis[MAXN][MAXT];
int sum[MAXN][MAXT];
inline int lowbit(int x){return x&-x;}
inline int query(int pos,int x){x++;int ret = 0x3f3f3f3f;while(x)ret=min(ret,sum[pos][x]),x-=lowbit(x);return ret;}
inline void modify(int pos,int x,int v){x++;while(x<MAXT)sum[pos][x]=min(sum[pos][x],v),x+=lowbit(x);}
queue<pii> q;
void spfa(int s){
	q.push(make_pair(s,0));
	memset(dis,0x3f,sizeof(dis));
	dis[s][0] = 0;
	vis[s][0] = true;
	modify(s,0,0);
	while(!q.empty()){
		int top = q.front().first;int time = q.front().second;
		q.pop();
		vis[top][time] = false;
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			if(time+edges[i].time<=10000&&query(t,time+edges[i].time)>dis[top][time]+edges[i].w){
				modify(t,time+edges[i].time,dis[top][time]+edges[i].w);
				dis[t][time+edges[i].time] = dis[top][time]+edges[i].w;
				if(!vis[t][time+edges[i].time]){
					q.push(make_pair(t,time+edges[i].time));
					vis[t][time+edges[i].time] = true;
				}
			}
		}			
	}
}
int main(){
	# ifdef BEYONDSTARS
		freopen("testdata.in","r",stdin);
	# endif
	read(n),read(m),read(s),read(e);
	int f,t,c,time;
	for(int i = 1;i<=m;i++){
		read(f),read(t),read(c),read(time);
		add(f,t,c,time);add(t,f,c,time);
	}
	memset(sum,0x3f,sizeof(sum));
	spfa(s);
	int mn = 0x3f3f3f3f,ans = 0;
	for(int i = 0;i<=10000;i++){//就是这里，题面很迷
		if(mn>dis[e][i]){
			mn = dis[e][i];ans++;
		}
	}
	cout<<ans;
	return 0;
}

```