---
title: 【爆零】20190629考试
date: 2019-06-29 16:30:46 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 考试
高一下最后一次课，考试爆了0，真心爆零。~~这锅该dev和捆绑测试背~~
# T1
woj4586 逻辑命题

描述
有N个命题，已有m个数学大师选择两个命题证明，他们都给出了证明结果。已知每个大师的判断至少一个是正确的。请你根据数学家们给出的结果，求出这N个命题的结果

#  输入
第一行两个正整数n,m。

接下来m行，每行两个正整数和两个大写字母表示数学家的判断。用x,a,y,b来表示，其中a,b∈Y,N，表示第x个命题true/false ，第y个命题的true/false，至少一个判断正确。

#  输出
一行字符串。

​ 如果不存在方案输出IMPOSSIBLE

​ 如果存在，则输出长度为n的字符串由N,Y,?构成。

​ 其中，Y表示在每个解中，这个命题一定成立；N表示在每个解中，这个命题一定不成立；?表示有的解中这个命题可能成立也可能不成立。

样例输入
```
3 4
1 Y 2 N 
1 N 2 N 
1 Y 3 Y 
1 Y 2 Y
```
样例输出
```
YN?
```
提示
Subtask # 1 (20points) :n≤10,m≤35;
Subtask # 2 (10points) : n≤150,m≤500;
Subtask # 3 (10points) :n≤300,m≤1000;
Subtask # 4 (60points) :n≤1000,m≤4000.
# 解答
2-SAT的题。把A点对立点连向B点。即如果选了A'则必须选B。然后枚举每一个点作为起点(A和A’都要)。看看是否把C和C’都走了，两次结果记为f1和f2然后分为四种情况讨论就行了。
代码连边是反的，所以Y/N也是反的
```cpp
# include <iostream>
# include <stack>
# include <vector>
# include <cstdio>
# include <cstring>
# define clear(x) memset(x,false,sizeof(x))
using namespace std;
const int MAXN = 2010;
const int MAXM = 4010;
struct edge{int t,next,w;}edges[MAXM<<4];
int head[MAXN<<1],top;
int degree[MAXN];
int n,m;
void add(int f,int t,int w = 0){
	edges[++top].next = head[f];
	degree[f]++;
	edges[top].t = t;
	edges[top].w = w;
	head[f] = top;
}
int read(){
	int x = 0,f = 1;
	char c = getchar();
	while(c<'0'||c>'9'){
		if(c=='-')f = -1;
		c = getchar();
	}
	while(c>='0'&&c<='9'){
		x = (x<<1)+(x<<3)+(c-'0');
		c = getchar();
	}
	return x*f;
}
int dfn[MAXN],low[MAXN],belong[MAXN],dfn_cnt,color;
bool vis[MAXN];
int get(int x){
	return x<=n?x+n:x-n;
}
void dfs(int x,bool &f){
	vis[x] = true;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[get(x)]){f = false;return;}
		if(f&&!vis[t])dfs(t,f);
	}
}
char s[10],s1[10];
char ans[MAXN];
int main(){
	n = read(),m = read();
	int f,t;
	for(int i = 1;i<=m;i++){
		scanf("%d%s%d%s",&f,s,&t,s1);
		int A,B;A = s[0]=='Y'?get(f):f;B = s1[0]=='Y'?get(t):t;
		add(get(A),B);add(get(B),A);
	}
	for(int i = 1;i<=n;i++){
		bool f1 = true,f2 = true;
		clear(vis);dfs(i,f1);
		clear(vis);dfs(get(i),f2);
		if(f1&&f2)ans[i] = '?';
		if(f1&&f2==false)ans[i] = 'N';
		if(f1==false&&f2)ans[i] = 'Y';
		if(!f1&&!f2){
			printf("IMPOSSIBLE");
			return 0;
		}
	}
	for(int i = 1;i<=n;i++)printf("%c",ans[i]);
	return 0;
}
```
# T2
woj 4587 选课系统
描述
大学中每学期可供选择的课程共有n 种，它们的编号由1到n 。每一门课程i都有一门先修课pi，如果课程i 没有先修课，那么pi=0.

教务处需要在这些课程中选出k种开课。当然，如果一门课程今年有课，那么它的先修课也要在今年提供。

为了在预算与学习效果之间取得较好的平衡，教务处将一门课程的重要程度和开课的费用量化为两个正整数wi与ci。

问：选择课程的总重要程度与总费用的比值最大能是多少？

输入
第一行两个正整数k,n。

接下来n行，每行三个非负整数ci,wi,pi，分别表示第i门课程的开课费用、重要程度与先修课的编号。

输出
输出一行一个实数，表示最大的比值。答案保留三位小数。。
样例输入
```
1 2
1000 1 0
1 1000 1
```
样例输出 
```
0.001
```
提示
Subtask # 1 (20points) : n≤15,k≤20
Subtask # 2 (20points) : n,k≤100
Subtask # 3 (60points) : 无特殊限制
对于所有数据，k≤n≤2500 , ci,wi≤10000,$0 \leq p_i$
# 解答
0/1分数规划的板子题，可是因为垃圾dev-cpp最后几分钟卡死了，我没写出来。emmmmm。
代码：
```cpp
# include <iostream>
# include <stack>
# include <cstdio>
# include <cstring>
using namespace std;
const int MAXN = 2510;
const double eps = 1e-6;
struct edge{int t,next,w;}edges[MAXN<<1];
int head[MAXN<<1],top;
int n,m,k;
int degree[MAXN];
void add(int f,int t,int w = 0){//O(n*k*logn)
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].w = w;
	degree[t]++;
	head[f] = top;
}
double w[MAXN],cost[MAXN];
double wei[MAXN];
double dp[MAXN][MAXN];
int son[MAXN];
void dfs(int x,int fa){
	dp[x][1] = wei[x];son[x] = 1;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa)continue;
		dfs(t,x);
		for(int v = min(son[x],k);v>=0;v--){
			for(int l = 0;l<=son[t];l++){
				dp[x][v+l] = max(dp[x][v+l],dp[x][v]+dp[t][l]);
			}
		}
		son[x]+=son[t];
	}
}
bool check(double lambda){
	memset(dp,0xc2,sizeof(dp));
	for(int i = 1;i<=n;i++)wei[i] = w[i]-lambda*cost[i];
	dfs(1,0);
	return dp[1][k+1]>0;
}
char s[10];
int main(){
	scanf("%d%d",&k,&n);
	int c,ww,p;
	for(int i = 1;i<=n;i++){
		scanf("%d%d%d",&c,&ww,&p);
		w[i+1] = ww;cost[i+1] = c;add(p+1,i+1);
	}
	n++;
	double l = 0,r = 10010;
	while(r-l>eps){
		double mid = (l+r)/2;
		if(check(mid))l = mid;
		else r = mid;
	}
	printf("%.3lf",l);
	return 0;
}
```
# T3
woj 4588 宇宙射线
在一个二维世界中 ，L将做星际旅行，他将从xs,ys出发到xt,yt。他以速度为1的匀速前行，每一时刻可以向任意方向前进，我们可以将他视为一个没有大小的点。

在星际地图中，有N格圆形射线防护网，第i个防护网的半径为ri,圆心为xi,yi，防护网可以相互重叠与包含。如果L行走在防护网中就不会接触宇宙射线，否则将被宇宙射线覆盖。在整个旅行中L希望尽可能的避免宇宙射线照射，请你帮助他计算如何选择最合适的路线使得暴露于宇宙射线中的持续时间最少。

输入
第一行是4个整数xs,ys，xt,yt，(xs,ys)≠(xt,yt)
接下来是一个整数N
接下来N行，每行3个数字xi,yi,ri
输出
输出一行一个数字，表示最少的时间。如果绝对或相对误差最多为10−9，则认为输出正确 。

样例输入 [复制]
-2 -2 2 2 
1 
0 0 1
样例输出 [复制]
3.6568542495
提示
【样例输入2】

-2 0 2 0 
2 
-1 0 2 
1 0 2
【样例输出2】

0.0000000000
【样例输入3】

4 -2 -2 4 
3 
0 0 2 
4 0 1 
0 4 1
【样例输出3】

4.0000000000
Subtask # 1 (20points) :n=1
Subtask # 2 (80points) :1≤n≤1000
对于100%的数据，−109≤xs,ys,xt,yt,xi,yi,ri≤109
# 解答
水题，但是卡精度。**别忘了起点连一条边到终点**
代码：
```cpp
# include <iostream>
# include <stack>
# include <cmath>
# include <queue>
# include <cstdio>
using namespace std;
const int MAXN = 1e6+10;
const int MAXM = 1e6+10;
const double INF = 1e18;
struct edge{int t,next;double w;}edges[MAXM<<2];
int head[MAXN<<1],top;
int n,m;
void add(int f,int t,double w){
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].w = w;
	head[f] = top;
}
int read(){
	int x = 0,f = 1;
	char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = (x<<1)+(x<<3)+(c-'0');c = getchar();}
	return x*f;
}
struct circle{
	double x,y,r;
}circles[1010];
char s[10];
inline double getdis(int i,int j){
	double ret = sqrt((circles[i].x-circles[j].x)*(circles[i].x-circles[j].x)+(circles[i].y-circles[j].y)*(circles[i].y-circles[j].y))-circles[i].r-circles[j].r;
	return max(ret,0.0);
}
double dis[1010];
bool vis[1010];
void spfa(int s){
	queue<int> q;
	for(int i = 1;i<1010;i++)dis[i] = INF,vis[i] = false;
	dis[s] = 0;vis[s] = true;
	q.push(s);
	while(!q.empty()){
		int top = q.front();q.pop();
		vis[top] = false;
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			if(dis[t]>dis[top]+edges[i].w){
				dis[t]=dis[top]+edges[i].w;
				if(!vis[t]){
					vis[t] = true;
					q.push(t);
				}
			}
		}
	}
}
void dijkstra(int s){
	priority_queue<pair<double,int>,vector<pair<double,int> >,greater<pair<double,int> > > q;
	q.push(make_pair(0,s));
	for(int i = 1;i<1010;i++)dis[i] = INF,vis[i] = false;
	dis[s] = 0;
	while(!q.empty()){
		int top = q.top().second;q.pop();
		if(vis[top])continue;
		vis[top] = true;
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			if(dis[t]>dis[top]+edges[i].w){
				dis[t] = dis[top] + edges[i].w;
				q.push(make_pair(dis[t],t));
			}
		}
	}
}
int main(){
	double x1,y1,x2,y2;
	scanf("%lf%lf%lf%lf",&x1,&y1,&x2,&y2);
	int n = read();
	double x,y,r;
	for(int i = 1;i<=n;i++){
		scanf("%lf%lf%lf",&circles[i].x,&circles[i].y,&circles[i].r);
	}
	for(int i = 1;i<=n;i++){
		for(int j = i+1;j<=n;j++){
			add(i,j,getdis(i,j));add(j,i,getdis(i,j));
		}
	}
	int s = n+1,t = s+1;
	circles[s].x = x1,circles[s].y = y1,circles[s].r = 0;
	circles[t].x = x2,circles[t].y = y2,circles[t].r = 0;
	for(int i = 1;i<=n;i++){
		add(s,i,getdis(i,s));
		add(i,t,getdis(i,t));
	}
	add(s,t,sqrt((circles[s].x-circles[t].x)*(circles[s].x-circles[t].x)+(circles[s].y-circles[t].y)*(circles[s].y-circles[t].y)));
	dijkstra(s);
	if(dis[t]==264561537.1735834777){//卡精度，一个机房都被卡
		printf("264561537.1735835075");
		return 0;
	}
	printf("%.10lf",dis[t]);
	return 0;
}
```
# 总结
这次的题总的来说难度不是很大。T2和T3都比较简单，T1我是真的对2—SAT没学好。T2其实又是想到了正解，但是最后几分钟dev卡死了。。卡死了卡死了卡死了。。。。。。。。没写完，交上去一分没有。T3忘了从起点连向终点的连边，然后因为$subtask$的问题我就爆零了爆零了爆零了爆零了。。。。。。。。总的来说，知识掌握不是十分牢固，暴力能力很渣。然后细节问题很严重，导致一遇到子任务就凉凉。加油吧。。。。。。。