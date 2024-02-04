---
title: 差分约束luoguP3275 [SCOI2011]糖果
date: 2018-11-05 20:23:49 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
幼儿园里有N个小朋友，lxhgww老师现在想要给这些小朋友们分配糖果，要求每个小朋友都要分到糖果。但是小朋友们也有嫉妒心，总是会提出一些要求，比如小明不希望小红分到的糖果比他的多，于是在分配糖果的时候，lxhgww需要满足小朋友们的K个要求。幼儿园的糖果总是有限的，lxhgww想知道他至少需要准备多少个糖果，才能使得每个小朋友都能够分到糖果，并且满足小朋友们所有的要求。

#  输入输出格式
#  输入格式：
输入的第一行是两个整数N，K。接下来K行，表示这些点需要满足的关系，每行3个数字，X，A，B。如果X=1， 表示第A个小朋友分到的糖果必须和第B个小朋友分到的糖果一样多；如果X=2，  
表示第A个小朋友分到的糖果必须少于第B个小朋友分到的糖果；如果X=3，
表示第A个小朋友分到的糖果必须不少于第B个小朋友分到的糖果；如果X=4，
表示第A个小朋友分到的糖果必须多于第B个小朋友分到的糖果；如果X=5，
表示第A个小朋友分到的糖果必须不多于第B个小朋友分到的糖果；


#  输出格式：
输出一行，表示lxhgww老师至少需要准备的糖果数，如果不能满足小朋友们的所有要求，就输出-1。

# 输入输出样例
#  输入样例# 1： 
```
5 7
1 1 2
2 3 2
4 4 1
3 4 5
5 4 5
2 3 5
4 5 1
```
#  输出样例# 1： 
```
11
```
说明
【数据范围】
对于30%的数据，保证 N<=100
对于100%的数据，保证 N<=100000
对于所有的数据，保证 K<=100000，1<=X<=5，1<=A, B<=N
# 解答
一道非常裸的查封约束。对于差分约束：
如果$X_i-X_j\leq C_i$那么我们连一条从$X_j$出发到$X_i$长度为$C_i$的边，跑最短路
如果$X_i-X_j\geq C_i$那么我们连一条$X_j$连向$X_i$长度为$C_i$的边，跑最长路。
如果图中**有环则无解**！
差分约束主要是要找出题面中的**隐含条件**，要仔细考虑。如果无负环，则尽量跑dijkstra(它不支持最长路)，防止卡spfa。对于这道题
```cpp
	for(int i = 1;i<=n;i++){
		add(0,i,1);
	}
```
这里一定要倒着来，不然luogu上# 6点过不了，据说是与spfa的顺序有关，我太菜了，不懂。
然后就是AC代码：
```cpp
# include <cstdio>
# include <cstring>
# include <cmath>
# include <algorithm>
# include <queue>
using namespace std;
long long read(){
	long long x = 0,f = 1;
	static char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = (x<<1)+(x<<3)+c-'0';c = getchar();}
	return x*f;
}
const int MAXN = 100010;
struct edge{
    int t,w,next;
}edges[MAXN*10];
int head[MAXN];
int top;
int n;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int dis[MAXN];
int tot[MAXN];
bool vis[MAXN];
void spfa(){
	memset(vis,false,sizeof(vis));
	queue<int> q;
	int s = 0;
	vis[s] = true;
	dis[s] = 0;
	q.push(s);
	while(!q.empty()){
		int top = q.front();
		q.pop();
		vis[top] = false;
		if(tot[top]==n-1){
			printf("-1");
			exit(0);
		}
		tot[top]++;
		for(int i = head[top];i!=0;i = edges[i].next){
			int t = edges[i].t;
			if(dis[t]<dis[top]+edges[i].w){
				dis[t] = dis[top]+edges[i].w;
				if(!vis[t]){
					vis[t] = true;
					q.push(t);
				}
			}
		}
	}
}
int main(){
	int k;
	n = read();
	k = read();
	int x,a,b;
	for(int i = 1;i<=k;i++){
		x= read(),a = read(),b = read();
		if(x==1){
			add(a,b,0);
			add(b,a,0);
		}else if(x==2){
			if(a==b){
				printf("-1");
				return 0;
			}
			add(a,b,1);
		}else if(x==3){
			add(b,a,0);
		}else if(x==4){
			if(a==b){
				printf("-1");
				return 0;
			}
			add(b,a,1);
		}else{
			add(a,b,0);
		}
	}
	for(int i = 1;i<=n;i++){
		add(0,i,1);
	}
	spfa();
	long long ans = 0;
	for(int i = 1;i<=n;i++)ans+=dis[i];
	printf("%lld",ans);
	return 0;
}
```