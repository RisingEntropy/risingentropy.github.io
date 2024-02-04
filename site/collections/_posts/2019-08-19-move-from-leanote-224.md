---
title: 【最小方差生成树】bzoj3754
date: 2019-08-19 21:15:06 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Wayne在玩儿一个很有趣的游戏。在游戏中，Wayne建造了N个城市，现在他想在这些城市间修一些公路，当然并不是任意两个城市间都能修，为了道路系统的美观，一共只有M对城市间能修公路，即有若干三元组 (Ui,Vi,Ci)表示Ui和Vi间有一条长度为Ci的双向道路。当然，游戏保证了，若所有道路都修建，那么任意两城市可以互相到达。Wayne拥有恰好N-1支修建队，每支队伍能且仅能修一条道路。当然，修建长度越大，修建的劳累度也越高，游戏设定是修建长度为C的公路就会有C的劳累度。当所有的队伍完工后，整个城市群必须连通，而这些修建队伍们会看看其他队伍的劳累情况，若劳累情况差异过大，可能就会引发骚动，不利于社会和谐发展。Wayne对这个问题非常头疼，于是他想知道，这N1支队伍劳累度的标准差最小能有多少。
标准差的定为：设有N个数，分别为ai,它们的平均数为![图片标题](https://cdn.risingentropy.top/images/posts/d5aa133ab64410bb4003232.png),那么标准差就是

![图片标题](https://cdn.risingentropy.top/images/posts/d5aa133ab64410bb4003232.png)

Input
第一行两个正整数N,M
接下来M行，每行三个正整数Ui,Vi,Ci
Output
输出最小的标准差，保留四位小数。
#  Sample Input
```
3 3
1 2 1
2 3 2
3 1 3
```
#  Sample Output
```
0.5000
```
Hint
N<=100,M<=2000,Ci<=100
# 解答
想到枚举方差还是比较好想，但是要想到如何快速计算有点困难。我们发现如果$a,b$的平均数的$a'$那么我们取值在$[a,a']$和$[b,b']$中是没有区别的。于是我们以0.25为步长，枚举就行了，只需要从0.25枚举到100，因为$100^2=-10000$
~~这题woj数据是真的水，我计算mst的时候忘了合并都有40分Orz~~
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <algorithm>
# include <cmath>
using namespace std;
const int MAXM = 2010;
const int MAXN = 110;
struct edge{int f,t,c;double w;bool operator<(const edge &e1)const {return w<e1.w;}}edges[MAXM];
int fa[MAXN];
int n,m; 
int find(int x){return fa[x] == x?x:fa[x] = find(fa[x]);}
void unite(int x,int y){fa[find(x)] = find(y);}
bool judge(int x,int y){return find(x) == find(y);}
void init(){for(int i = 1;i<=n;i++)fa[i] = i;}
double work(double mid){
	init();
	for(int i = 1;i<=m;i++)edges[i].w = (1.0*edges[i].c-mid)*(1.0*edges[i].c-mid);
	sort(edges+1,edges+m+1);
	int mst = 0,sqs = 0;
	int cnt = 0;
	for(int i = 1;i<=m;i++){
		int fx = find(edges[i].f),fy = find(edges[i].t);
		if(fx==fy)continue;
		mst+=edges[i].c;
		sqs+=edges[i].c*edges[i].c;
		cnt++;
		unite(fx,fy);
		if(cnt == n-1)break;
	}
	double avg = 1.0*mst/(n-1);
	double res = sqrt((1.0*sqs+(n-1)*avg*avg-2.0*mst*avg)/(n-1));
	return res;
} 
int main(){
	scanf("%d%d",&n,&m);
	int f,t,w;
	double ans = 1e18;
	for(int i = 1;i<=m;i++){
		scanf("%d%d%d",&f,&t,&w);
		edges[i].f = f;edges[i].t = t;
		edges[i].c = w;
	}
	for(double i = 0.25;i<=100.0;i+=0.5){
		ans = min(ans,work(i));
	}
	printf("%.4lf",ans);
	return 0;
}
```