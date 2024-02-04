---
title: bzoj 2118 墨墨的等式(好题)
date: 2019-02-12 20:57:19 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
墨墨突然对等式很感兴趣，他正在研究a1x1+a2y2+…+anxn=B存在非负整数解的条件，他要求你编写一个程序，给定N、{an}、以及B的取值范围，求出有多少B可以使等式存在非负整数解。
#  输入
输入的第一行包含3个正整数，分别表示N、BMin、BMax分别表示数列的长度、B的下界、B的上界。输入的第二行包含N个整数，即数列{an}的值。
#  输出
输出一个整数，表示有多少b可以使等式存在非负整数解。
#  样例
#  样例输入
```
2 5 10
3 5
```
#  样例输出
```
5
```
# 解答
我死活都想不到这TM和最短路有关系。大概弱是原罪吧！
# $15ptr$做法
爆搜。剪剪枝，其实也没多大用
```cpp
//
// Created by dhy on 19-2-11.
//
# include <iostream>
using namespace std;
int ans;
int n;
int num[14];
int re_sum[14];
void dfs(int pos,long long sum,long long maxx,long long minn){
    if(pos>n&&sum<=maxx&&sum>=minn){ans++;return; }
    if(sum+re_sum[pos+1]>=maxx){ans++; return;}
    else if(pos>n)return;
    for(int i = 0;i*num[pos]+sum<=maxx;i++){
        dfs(pos+1,sum+i*num[pos],maxx,minn);
    }
}
int main(){
    int bmax,bmin;
    cin>>n>>bmin>>bmax;
    for(int i = 1;i<=n;i++){
        cin>>num[i];
    }
    for(int i = n;i>=1;i--){
        re_sum[i] = num[i]+re_sum[i+1];
    }
    dfs(1,0,bmax,bmin);
    cout<<ans;
    return 0;
}
```
# $100ptr$做法
我们考虑对最后可以凑出来的数进行分类。对这个数进行对$min(a_i)$取模，分成$0-min(a_i)-1$类，对于每一类考虑有哪些可以由这一类拓展过来。如$v$可以被凑出来那么$v+m$(m代指$min(a_i)$)也可以被凑出来。也就是说，**只要我们找到一个最小的，在模m意义下等于p($p\in[1,m-1]$)的数，那么我们就可以算出所以在范围内的数**。要找出最小的那个数，我们发现这就是最短路模型，由i向i+a[j]%m连边。最后遍历dis[1-m-1]统计一下答案就行。至于存边的数组的大小，玄学，~~我懒得去算了~~开大点，不要爆空间就行。
代码：
```cpp
//
// Created by dhy on 19-2-11.
//
# include <iostream>
# include <queue>
# include <algorithm>
# include <cstring>
using namespace std;
int n;
int num[14];
const int MAXN = (int)5e5+10;
bool viss[MAXN];
long long dis[MAXN];
struct edge{
    long long t,w,next;
}edges[MAXN*20];
int head[MAXN];
int topp;
void add(int f,int t,int w) {
    edges[++topp].next = head[f];
    edges[topp].t = t;
    edges[topp].w = w;
    head[f] = topp;
}
void spfa(){
    memset(dis,0x6f,sizeof(dis));
    memset(viss,false,sizeof(viss));
    queue<long long> q;
    int s = 0;
    viss[s] = true;
    dis[s] = 0;
    q.push(s);
    while(!q.empty()){
        long long top = q.front();
        q.pop();
        viss[top] = false;
        for(long long i = head[top];i!=0;i = edges[i].next){
            long long t = edges[i].t;
            if(dis[t]>dis[top]+edges[i].w){
                dis[t] = dis[top]+edges[i].w;
                if(!viss[t]){
                    viss[t] = true;
                    q.push(t);
                }
            }
        }
    }
}

int main(){
    long long bmax,bmin;
    cin>>n>>bmin>>bmax;
    for(int i = 1;i<=n;i++)cin>>num[i];
    sort(num+1,num+1+n);
    int mn = num[1];
    for(int i = 0;i<mn;i++){
        for(int j = 2;j<=n;j++){
            add(i,(i+num[j])%mn,num[j]);
        }
    }
    spfa();
    long long ans = 0;
    for(int i = 0;i<mn;i++){
        if(dis[i]>bmax)continue;
        if(dis[i]>bmin){
            ans+=(bmax-dis[i])/mn+1;
        } else{
            ans+=(bmax-dis[i])/mn+1;
            ans-=(bmin-dis[i]+mn-1)/mn;
        }
    }
    cout<<ans;
    return 0;
}

```