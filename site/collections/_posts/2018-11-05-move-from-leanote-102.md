---
title: topo排序HDU1285过不了
date: 2018-11-05 21:22:21 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# Problem Description
有N个比赛队（1<=N<=500），编号依次为1，2，3，。。。。，N进行比赛，比赛结束后，裁判委员会要将所有参赛队伍从前往后依次排名，但现在裁判委员会不能直接获得每个队的比赛成绩，只知道每场比赛的结果，即P1赢P2，用P1，P2表示，排名时P1在P2之前。现在请你编程序确定排名。
 

# Input
输入有若干组，每组中的第一行为二个数N（1<=N<=500），M；其中N表示队伍的个数，M表示接着有M行的输入数据。接下来的M行数据中，每行也有两个整数P1，P2表示即P1队赢了P2队。
 

# Output
给出一个符合要求的排名。输出时队伍号之间有空格，最后一名后面没有空格。

其他说明：符合条件的排名可能不是唯一的，此时要求输出时编号小的队伍在前；输入数据保证是正确的，即输入数据确保一定能有一个符合要求的排名。
 

#  Sample Input
```
4 3
1 2
2 3
4 3
```

#  Sample Output
```
1 2 4 3
```
# 解答
一道裸的拓扑排序板子题
代码：
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
const int MAXN = 510;
struct edge{
    int t,w,next;
}edges[MAXN*5];
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
queue<int> ans;
int indegree[MAXN];

void topo(){
	int id;
	for(int i = 1;i<=n;i++){
		for(int i = 1;i<=n;i++){
			if(indegree[i]==0){
				id = i;
				break;
			}
		}
		ans.push(id);indegree[id] = -1;
		for(int i = head[id];i!=0;i = edges[i].next){
			int  t = edges[i].t;
			indegree[t]--;
		}
	}
}
int main(){
	int m;
	while(scanf("%d %d",&n,&m)!=EOF){
		int p1,p2;
		for(int i = 1;i<=m;i++){
			p1 = read(),p2 = read();
			add(p1,p2,1);
			indegree[p2]++;
		}
		topo();
		while(!ans.empty()){
			printf("%d ",ans.front());
			ans.pop();
		}
		printf("\n");
	}	
	return 0;
}
```
