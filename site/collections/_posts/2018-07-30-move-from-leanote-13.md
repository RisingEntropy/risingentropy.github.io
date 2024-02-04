---
title: 洛谷P1629
date: 2018-07-30 15:38:20 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题目描述
有一个邮递员要送东西，邮局在节点1.他总共要送N-1样东西，其目的地分别是2~N。由于这个城市的交通比较繁忙，因此所有的道路都是单行的，共有M条道路，通过每条道路需要一定的时间。这个邮递员每次只能带一样东西。求送完这N-1样东西并且最终回到邮局最少需要多少时间。

# 输入输出格式
#  输入格式：
第一行包括两个整数N和M。

第2到第M+1行，每行三个数字U、V、W，表示从A到B有一条需要W时间的道路。 满足1<=U,V<=N,1<=W<=10000,输入保证任意两点都能互相到达。

#  【数据规模】

对于30%的数据，有1≤N≤200;

对于100%的数据，有1≤N≤1000,1≤M≤100000。

# 输出格式：
输出仅一行，包含一个整数，为最少需要的时间。

# 输入输出样例
#  输入样例# 1： 
```
5 10
2 3 5
1 5 5
3 5 6
1 2 8
1 3 8
5 3 4
4 1 8
4 5 3
3 5 6
5 4 2
```
#  输出样例# 1： 
```
83
```
# 解答
其实非常简单的一道题。因为道路是单向的，又要知道1到所有点的距离和所有点到1 的距离，所以直接建反向边就行了。这样只需要跑两次spfa。
代码:
```cpp
# include <cstdio>
# include <queue>
# include <cstring>
# include <iostream>
# include <vector>
using namespace std;
const int MAXN = 1010;
const int MAXM = 100010;
struct edge{
    int t,w,next;
}edges1[MAXM],edges2[MAXM];
int head1[MAXN],head2[MAXN];
int top1,top2;
int dis1[MAXN];
int dis2[MAXN];
bool vis1[MAXN];
bool vis2[MAXN];
typedef pair<int,int> p;
void add1(int f,int t,int w){
    edges1[++top1].next =  head1[f];
    edges1[top1].t = t;
    edges1[top1].w = w;
    head1[f] = top1;
}
void add2(int f,int t,int w){
    edges2[++top2].next = head2[f];
    edges2[top2].t = t;
    edges2[top2].w = w;
    head2[f] = top2;
}
void dijkstra1(){//正图
    memset(dis1,0x3f,sizeof(dis1));
    memset(vis1,false,sizeof(vis1));
    priority_queue<p,vector<p>,greater<p> > q;
    dis1[1] = 0;
    q.push(make_pair(0,1));
    while(!q.empty()){
        int top = q.top().second;
        q.pop();
        if(vis1[top])continue;
        vis1[top] = true;
        for(int i = head1[top];i!=0;i = edges1[i].next){
            int t = edges1[i].t;
            if(dis1[t]>dis1[top]+edges1[i].w){
                dis1[t]=dis1[top]+edges1[i].w;
                q.push(make_pair(dis1[t],t));
            }
        }
    }
}
void dijkstra2(){//反图
    memset(dis2,0x3f,sizeof(dis2));
    memset(vis2,false,sizeof(vis2));
    priority_queue<p,vector<p>,greater<p> > q;
    dis2[1] = 0;
    q.push(make_pair(0,1));
    while(!q.empty()){
        int top = q.top().second;
        q.pop();
        if(vis2[top])continue;
        vis2[top] = true;
        for(int i = head2[top];i!=0;i = edges2[i].next){
            int t = edges2[i].t;
            if(dis2[t]>dis2[top]+edges2[i].w){
                dis2[t]=dis2[top]+edges2[i].w;
                q.push(make_pair(dis2[t],t));
            }
        }
    }
}
int main(void){
    int n,m;
    cin>>n>>m;
    int f,t,w;
    for(int i = 1;i<=m;i++){
        cin>>f>>t>>w;
        add1(f,t,w);
        add2(t,f,w);
    }
    dijkstra1();
    dijkstra2();
    int ans = 0;
    for(int i =  2;i<=n;i++)ans+=dis1[i]+dis2[i];
    cout<<ans;
    return 0;
}
```
无脑压行版：
```cpp
# include <cstdio>
# include <queue>
# include <cstring>
# include <iostream>
# include <vector>
using namespace std;
const int MAXN = 1010;const int MAXM = 100010;struct edge{ int t,w,next; }edges1[MAXM],edges2[MAXM];
int head1[MAXN],head2[MAXN];int top1,top2;int dis1[MAXN];int dis2[MAXN];bool vis1[MAXN];bool vis2[MAXN];typedef pair<int,int> p;
void add1(int f,int t,int w){ edges1[++top1].next =  head1[f];edges1[top1].t = t;edges1[top1].w = w;head1[f] = top1; }
void add2(int f,int t,int w){edges2[++top2].next = head2[f];edges2[top2].t = t;edges2[top2].w = w;head2[f] = top2; }
void dijkstra1(){//正图
    memset(dis1,0x3f,sizeof(dis1));memset(vis1,false,sizeof(vis1));priority_queue<p,vector<p>,greater<p> > q;dis1[1] = 0;q.push(make_pair(0,1));
    while(!q.empty()){
        int top = q.top().second;q.pop();if(vis1[top])continue;vis1[top] = true;
        for(int i = head1[top];i!=0;i = edges1[i].next){
            int t = edges1[i].t;if(dis1[t]>dis1[top]+edges1[i].w)dis1[t]=dis1[top]+edges1[i].w,q.push(make_pair(dis1[t],t));
        }
    }
}
void dijkstra2(){//反图
    memset(dis2,0x3f,sizeof(dis2));memset(vis2,false,sizeof(vis2));priority_queue<p,vector<p>,greater<p> > q;dis2[1] = 0;q.push(make_pair(0,1));
    while(!q.empty()){
        int top = q.top().second;q.pop();if(vis2[top])continue;vis2[top] = true;
        for(int i = head2[top];i!=0;i = edges2[i].next){ int t = edges2[i].t;if(dis2[t]>dis2[top]+edges2[i].w)dis2[t]=dis2[top]+edges2[i].w,q.push(make_pair(dis2[t],t));
        }
    }
}
int main(void){
    int n,m;cin>>n>>m;int f,t,w;
    for(int i = 1;i<=m;i++)cin>>f>>t>>w;add1(f,t,w);add2(t,f,w);
    dijkstra1();dijkstra2();int ans = 0;for(int i =  2;i<=n;i++)ans+=dis1[i]+dis2[i];cout<<ans;
    return 0;
}
```