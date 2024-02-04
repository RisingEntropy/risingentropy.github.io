---
title: NOIP 2009 最优贸易
date: 2019-01-31 12:05:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 描述
C 国有 n 个大城市和 m 条道路，每条道路连接这 n 个城市中的某两个城市。任意两个
城市之间最多只有一条道路直接相连。这 m 条道路中有一部分为单向通行的道路，一部分
为双向通行的道路，双向通行的道路在统计条数时也计为 1 条。
C 国幅员辽阔，各地的资源分布情况各不相同，这就导致了同一种商品在不同城市的价
格不一定相同。但是，同一种商品在同一个城市的买入价和卖出价始终是相同的。
商人阿龙来到 C 国旅游。当他得知同一种商品在不同城市的价格可能会不同这一信息
之后，便决定在旅游的同时，利用商品在不同城市中的差价赚回一点旅费。设 C 国 n 个城
市的标号从 1~ n，阿龙决定从 1 号城市出发，并最终在 n 号城市结束自己的旅行。在旅游的
过程中，任何城市可以重复经过多次，但不要求经过所有 n 个城市。阿龙通过这样的贸易方
式赚取旅费：他会选择一个经过的城市买入他最喜欢的商品――水晶球，并在之后经过的另
一个城市卖出这个水晶球，用赚取的差价当做旅费。由于阿龙主要是来 C 国旅游，他决定
这个贸易只进行最多一次，当然，在赚不到差价的情况下他就无需进行贸易。
假设 C 国有 5 个大城市，城市的编号和道路连接情况如下图，单向箭头表示这条道路
为单向通行，双向箭头表示这条道路为双向通行。
![enter image description here](https://cdn.risingentropy.top/images/posts/c52745bab64412db6000524.png)
假设 1~n 号城市的水晶球价格分别为 4，3，5，6，1。
阿龙可以选择如下一条线路：1->2->3->5，并在 2 号城市以 3 的价格买入水晶球，在 3
号城市以 5 的价格卖出水晶球，赚取的旅费数为 2。
阿龙也可以选择如下一条线路 1->4->5->4->5，并在第 1 次到达 5 号城市时以 1 的价格
买入水晶球，在第 2 次到达 4 号城市时以 6 的价格卖出水晶球，赚取的旅费数为 5。
现在给出 n 个城市的水晶球价格，m 条道路的信息（每条道路所连接的两个城市的编号
以及该条道路的通行情况）。请你告诉阿龙，他最多能赚取多少旅费。
#  输入
第一行包含 2 个正整数 n 和 m，中间用一个空格隔开，分别表示城市的数目和道路的数目。
第二行 n 个正整数，每两个整数之间用一个空格隔开，按标号顺序分别表示这 n 个城市的商品价格。
接下来 m 行，每行有 3 个正整数，x，y，z，每两个整数之间用一个空格隔开。如果 z=1，
表示这条道路是城市 x 到城市 y 之间的单向道路；如果 z=2，表示这条道路为城市 x 和城市y 之间的双向道路。

#  输出
包含 1 个整数，表示最多能赚取的旅费。如果没有进行贸易，
样例输入
```
5 5 
4 3 5 6 1 
1 2 1 
1 4 1 
2 3 2 
3 5 1 
4 5 2
```
样例输出
```
5
```
提示
【数据范围】
输入数据保证 1 号城市可以到达 n 号城市。
对于 10%的数据，1≤n≤6。
对于 30%的数据，1≤n≤100。
对于 50%的数据，不存在一条旅游路线，可以从一个城市出发，再回到这个城市。
对于 100%的数据，1≤n≤100000，1≤m≤500000，1≤x，y≤n，1≤z≤2，1≤各城市
水晶球价格≤100。
# 解答
超级水的一道题。正反~~两开花~~建图，然后正着从1号节点跑，跑出到当前节点买入最低价。再反着从n开始跑，跑出当前节点可到达的卖出最高价。然后减一下就好了。水的一批
```cpp
# include <iostream>
# include <queue>
# include <cstring>
# include <vector>
using namespace std;
const int MAXN = 100010;
vector<int> edges[MAXN];
vector<int> reedges[MAXN];
int mn[MAXN],mx[MAXN];
int vis[MAXN];
int price[MAXN];
int n,m;
void dfs1(int x,int minn){
	vis[x]++;
	mn[x] = min(minn,price[x]);
	for(int i = 0;i<edges[x].size();i++){
		int t = edges[x][i];
		if(vis[t]>3)continue;
		dfs1(t,mn[x]);
	}
} 
void dfs2(int x,int maxx){
	vis[x]++;
	mx[x] = max(price[x],maxx);
	for(int i = 0;i<reedges[x].size();i++){
		int t = reedges[x][i];
		if(vis[t]>3)continue;
		dfs2(t,mx[x]);
	}
}
int main(){
	cin>>n>>m;
	for(int i = 1;i<=n;i++)cin>>price[i];
	int x,y,z;
	for(int i = 1;i<=m;i++){
		cin>>x>>y>>z;
		if(z==1){
			edges[x].push_back(y);
			reedges[y].push_back(x);
		}else{
			edges[x].push_back(y),edges[y].push_back(x);
			reedges[x].push_back(y),reedges[y].push_back(x);
		}
	}
	dfs1(1,0x3f3f3f3f);
	memset(vis,0,sizeof(vis));
	dfs2(n,0);
	int ans = 0;
	for(int i = 1;i<=n;i++){
		if(mn[i]!=0&&mx[i]!=0){
			ans = max(ans,mx[i]-mn[i]);
		}
	}
	cout<<ans;
	return 0;
}
```