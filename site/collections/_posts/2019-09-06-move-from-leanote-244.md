---
title: 【拓扑排序】woj3969 球的序列
date: 2019-09-06 19:54:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
有n个球，编号1-n，现在知道一些重量关系，请你给每个球赋一个重量，使得所有的球的重量满足约束，任意两个球的重量不能相同，且重量也是1-n。
#  输入
第一行是2个整数N,M，表示一共N个球，M个约束
接下来M行，每行2个整数u，v，表示u比v轻
#  输出
如果不可以给每个球成功赋值，则输出NO；否则输出YES，并在第二行输出每个球的重量，要求第i个球的重量尽可能的小（即在满足条件情况下第一个球的重量尽量最轻，第二个球尽可能轻。。。）

#  样例输入
```
【输入样例】
4 1
3 2
【输出样例】
YES
1 3 2 4
【输入样例2】
4 2
1 2
2 1
【输出样例2】
NO
```
# 解答
神仙题。不难想到一个最弱智的做法，就是小的向大的连边，然后把拓扑排序中的堆换成队列，但是这样子是错的。仔细考虑为什么这样子是错的，发现是因为每条链中会被最小的点所限制，如果能够抛弃这个限制就好了，所以我们考虑大的向小的连边，然后从大的开始了赋值，这样子就不用考虑那么多问题了。Orz想不到啊%%%
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# include <vector>
using namespace std;
const int MAXN = 10010;
struct edeg{int t,next;}edges[MAXN<<1];
int head[MAXN],top,deg[MAXN],n;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	deg[t]++;
	head[f] = top;
}
int w[MAXN],cnt;
void topo(){
	priority_queue<int> q;
	cnt = n;
	for(int i = 1;i<=n;i++)if(!deg[i])q.push(i);
	while(!q.empty()){
		int top = q.top();q.pop();
		w[top] = --cnt;
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			if((--deg[t])==0){
				q.push(t);
			}
		}
	}
	if(cnt)printf("NO");
	else {
		puts("YES");
		for(int i = 1;i<=n;i++){
			printf("%d ",w[i]+1);
		}
	}
}
int main(){
	int m;
	cin>>n>>m;
	int f,t;
	for(int i = 1;i<=m;i++){
		cin>>f>>t;
		add(t,f);
	}
	topo();
	return 0;
}
```