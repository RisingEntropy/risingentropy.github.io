---
title: 拓扑排序WOJ# 2576 小咸鱼，大梦想
date: 2018-11-06 10:41:50 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
#  描述
有N条咸鱼，每条咸鱼都有自己的能力值A[i]，现在你要给这些咸鱼送饭，当然咸鱼也有梦想，他们会暗中较劲，所以你给每个咸鱼送饭的时候要保证对于相邻的两条咸鱼，能力值大的咸鱼得到的饭要比咸鱼值少的多，请问最少送多少饭就能满足条件？
#  输入
一开始是一个数字T，表示数据组数 接下来T行，每行是一个数N ，表示咸鱼的数量 接下来一行有n个数，表示每个咸鱼的能力值
#  输出
对于每组数据，输出答案
#  样例输入
```
2
3
1 2 3
4
3 1 2 2
```
#  样例输出 
```
6
6
```
#  提示
样例解释：
第一个样例中第1个咸鱼送1份饭,第2个咸鱼送2份饭,第三个咸鱼送3份饭.
第二个样例中第1个咸鱼送2份饭,第2个咸鱼送1份饭,第三个咸鱼送2份饭.最后一个咸鱼送一份饭,因为最后两个咸鱼的能力值不是严格大于.
数据范围：
30 % 的数据保证T <= 10 , N <= 1000
100 % 的数据保证T<=10 , N <= 100000
100 % 的数据保证0 <= A[i] <= 10^9
# 解答
其实就是裸的拓扑排序，我们比较相邻的两个咸鱼，如果a[i]>a[i-1]那么从i-1连一条道i的边，如果a[i-1]>a[i]，那么连一条从i-1到i的边。
注意，在一开始找入度为0的点的时候，要把所有入度为0的点都找完才行！！！。还要注意初始化f数组(f[i]表示i条咸鱼送多少饭，入度为0的咸鱼送1份饭)
AC代码：
```cpp
# include <cstdio>
# include <cstring>
# include <cmath>
# include <algorithm>
# include <set>
# include <queue>
# include <iostream>
# include <stack>

# pragma GCC optimize("Ofast")
using namespace std;
const int MAXN = 100010;
struct edge{ int t,w,next; }edges[MAXN];
int head[MAXN];
int top;
int indegree[MAXN];
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    indegree[t]++;
    head[f] = top;
}
int f[MAXN];
int n;
int a[MAXN];

void topo(){
    queue<int> q;
    for(int i = 1;i<=n;i++){
        if(indegree[i]==0){
            q.push(i);
            f[i] = 1;
        }
    }

    while(!q.empty()){
        int top = q.front();
        q.pop();
        for(int i = head[top];i!=0;i = edges[i].next){
            int t = edges[i].t;
            indegree[t]--;
            if(indegree[t]==0){
                f[t] = max(f[t],f[top]+1);
                q.push(t);
            }
        }
    }
}

int main(){
    int T;
    cin>>T;
    while(T--) {
        memset(f,0, sizeof(f));
        memset(head,0, sizeof(head));
        top = 0;
        cin >> n;
        for (int i = 1; i <= n; i++)cin >> a[i];
        for(int i = 2;i<=n;i++){
            if(a[i]>a[i-1])add(i-1,i,1);
            if(a[i]<a[i-1])add(i,i-1,i);
        }
        topo();
        long long ans = 0;
        for(int i = 1;i<=n;i++)ans+=f[i];
        cout<<ans<<endl;
    }
    return 0;
}
```