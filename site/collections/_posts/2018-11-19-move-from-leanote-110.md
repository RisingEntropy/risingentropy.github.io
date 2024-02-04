---
title: 欧拉回路
date: 2018-11-19 15:18:50 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 定义
欧拉回路：图G中经过每一条一次边并且仅一次的回路称作欧拉回路。
欧拉路径：图G中经过每一条边一次并且仅一次的路径叫做欧拉路径。
欧拉图：存在欧拉回路的图叫欧拉图
半欧拉图：存在欧拉路径但不存在欧拉回路的图叫半欧拉图。
# 判断
定理1：**无向图** G为欧拉图，当且仅当G为连通图且所有定点的度数为偶数
推论1(小学奥数)：无向图G为欧拉图，当且仅当有2个顶点的度数为奇数，其他所有均为偶数时。
定理2：**有向图** G为欧拉图，当且仅当G的基图**联通**，且所有顶点的**入度等于出度**。(基图：忽略有向图所有边的方向，得到的无向图成为该有向图的基图)。
推论二：有向图为半欧拉图，当且仅当G的基图联通，并且存在顶点u的入度比出度大1，v入度比出度小1，其他所有点入度等于出度。
性质一：当C是图中一个简单回路，此回路删去，留下的图的各极大联通子图都存在一条欧拉回路。（显然，用点将各联通子图连接，才能形成欧拉回路。）
性质二：当C1,C2是两个简单回路，无边相交，仅有一点公共，可以将其合并成另一个简单回路。
# 操作步骤
1.在图G中找到一个回路C；
2。将图G 中属于回路C的边删除
3.在残留图的各极大连同子图中分别寻找欧拉回路
4.将各极大连同子图的欧拉回路合并到C中，得到图G的欧拉回路；
其实没有说的那么玄乎，其实就是从一个点u出发，遍历到达的每个点，然后把到达的每个点v的路径删掉，然后继续搜索(魔改版tarjan？)最后把u->v的边加入栈S。At last，依次取出栈s中的各元素，得到原图G的欧拉回路。复杂度$O(|E|)$
# 一些小技巧
1.你可以把每一条边遍历以后，在钱向星里面把head[x]改成edges[i].next以达到删边的效果。
2.代码里还有把循环里面的int i改成int &i的小优化，但是注意这样以后在循环中使用的时候要复制一下，因为你push_stack的时候传入的是引用，在stack里面可能会对i进行操作，导致值改变，然后就出锅了。
# 例题
[uoj117](http://uoj.ac/problem/117)
代码：
```cpp

//
// Created by dhy on 18-11-24.
//
# pragma GCC optimize("Ofast")
# include <stack>
# include <cstdio>
# include <set>
using namespace std;
const int MAXN = (int)1e5+10;
const int MAXM = (int)2e5+10;
struct edge{
    int t,w,next;
}edges[MAXM<<1];
int head[MAXN];
int top = 0;
int type;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
stack<int> stk;
bool vis[MAXN<<1];
void dfs(int u){//undirected graph
    for(int &j = head[u];j;j = edges[j].next){
        int i = j;
        if(!vis[(i+1)>>1]){
            vis[(i+1)>>1] = true;
            dfs(edges[i].t);
            stk.push((i&1)?((i+1)>>1):-((i+1)>>1));
        }
    }
}
void dfs2(int u){//directed graph
    for(int &i = head[u];i;i = edges[i].next){
        int j = i;
        if(!vis[j]){
            vis[j] = true;
            dfs2(edges[j].t);
            stk.push(j);
        }
    }

}
int in[MAXN],out[MAXN];
int main(void){
    int n,m;
    type = read();
    n = read(),m = read();
    int u;
    int f,t,w;
    for(int i = 1;i<=m;i++){
        f = read(),t = read();
        u = f;
        add(f,t,1);
        out[f]++;
        in[t]++;
        if(type==1)add(t,f,1);
    }
    if(type==1){//对于无向图
        for(int i = 1;i<=n;i++){
            if(!(in[i]+out[i]&1)==0){//无向图度之和为偶数
                printf("NO");
                return 0;
            }
        }
        dfs(u);
        if(stk.size()!=m){//找到的答案小于边数，说明图根本不连通
            printf("NO");
            return 0;
        }
        printf("YES\n");
        while(!stk.empty()){
            printf("%d ",stk.top());
            stk.pop();
        }
    }else{//对于无向图
        for(int i = 1;i<=n;i++){
            if(in[i]!=out[i]){//入度等于出度
                printf("NO");
                return 0;
            }
        }
        dfs2(u);
        if(stk.size()!=m){
            printf("NO");
            return 0;
        }
        printf("YES\n");
        while(!stk.empty()){
            printf("%d ",stk.top());
            stk.pop();
        }
    }

    return 0;
}
```