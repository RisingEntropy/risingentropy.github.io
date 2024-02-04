---
title: woj4376 种树
date: 2019-02-18 16:05:04 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有一个N个点M条边的无向图，每次选择一个点，并删除该点及其相邻的边，如果变成了一棵树，这这个点就是我们需要的。请找出满足条件的可能的点。
#  输入
第一行2个正整数N,M，表示N个点M条边，保证N>=2
接下来M行，每行2个整数U,V表示u，v有一条无向边，数据保证无自环与重边
#  输出
第一行是一个整数ans，表示一共有ans个可能的点
接下来一行输出ans个整数，用空格隔开，按从小到大输出可能的点（数据保证至少存在一个可能的点）
样例输入 
```
6 6
1 2
1 3
2 4
2 5
4 6
5 6
```
样例输出 
```
3
4 5 6
```
提示
对于 40%的数据：n，m<=1000；
另外存在 10%的数据：m=n-1；
另外存在 20%的数据：m=n；
对于 100%的数据：m n <100000
# 解答
其实考虑每个点可以被删掉的条件，必须有(m-n+2)条边连结着，不然没法构成树。然后删了以后图必须联通。所以直接跑割点，然后判断度就行了
```cpp
# include <cstdio>
# include <queue>
# include <iostream>
# include <algorithm>
# include <cstring>
# include <stack>
using namespace std;
const int MAXN = 100010;
const int MAXM = 100010;
int read(){
	int x = 0,f = 1;
	char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = (x<<1)+(x<<3)+(c-'0');c = getchar();}
	return x*f;
}
struct edge{int t,w,next;}edges[MAXM<<1];
int top,head[MAXN];
void add(int f,int t,int w){
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].w = w;
	head[f] = top;
}
int root;
int dfn[MAXN],low[MAXN];
int dfn_cnt;
bool iscut[MAXN];
void tarjan(int x){
	dfn[x] = low[x] = ++dfn_cnt;
	int children = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(!dfn[t]){
			tarjan(t);
			children++;
			low[x] = min(low[x],low[t]);
			if(children>1&&x==root){
				iscut[x] = true;
			}
			if(x!=root&&low[t]>=dfn[x]){
				iscut[x] = true;
			}
		}else {
			low[x] = min(low[x],dfn[t]);
		}
	}
}
int ans[MAXN],cnt;
int degree[MAXN];
int main(){
	int n = read(),m = read();
	for(int i = 1;i<=m;i++){
		int f = read(),t = read();
		add(f,t,1);add(t,f,1);
		degree[t]++;degree[f]++;
	}
	for(int i = 1;i<=n;i++){
		if(!dfn[i]){
			root = i;
			tarjan(i);
		}
	}
	for(int i = 1;i<=n;i++){
		if(!iscut[i]&&degree[i]==(m-n+2)){
			ans[++cnt] = i;
		}
	}
	printf("%d\n",cnt);
	for(int i = 1;i<=cnt;i++){
		printf("%d ",ans[i]);
	}
	return 0;
}
```