---
title: 最小生成树板子
date: 2018-09-15 21:52:41 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# Prime luoguP3366
```cpp
//
// Created by dhy on 18-9-15.
//
# include <queue>
# include <iostream>
using namespace std;
struct edge{
    int t,w,next;
    bool operator<(const edge &e2)const{
        return w>e2.w;
    }
}edges[10000000];
int head[10000000];
int top = 0;
bool vis[10000000];
void add(int f,int t,int w){
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;

}
inline void push_edge(priority_queue<edge> &q,int u){
    for(int i = head[u];i!=0;i = edges[i].next){
        q.push(edges[i]);
    }
}
int prime(int n){
    priority_queue<edge> q;
    vis[1] = true;
    push_edge(q,1);
    int ans = 0;
    for(int i = 1;i<n;){
        if(q.empty()){
            return -233;
        }
        edge e = q.top();
        q.pop();
        while(vis[e.t]){
            e = q.top();
            q.pop();
        }
        ans+=e.w;
        vis[e.t] = true;
        push_edge(q,e.t);
        i++;
    }
    return ans;
}
int main(void){
    ios::sync_with_stdio(false);
    int n,e;
    cin>>n>>e;
    int f,t,w;
    for(int i = 1;i<=e;i++){
        cin>>f>>t>>w;
        add(f,t,w);
        add(t,f,w);
    }
    int ans = prime(n);
    if(ans==-233)cout<<"orz"<<endl;
    else cout<<ans<<endl;
    return 0;
}
```
# kruskal
```cpp
//
// Created by dhy on 18-9-15.
//
# include <queue>
# include <iostream>
# include <algorithm>
using namespace std;
struct edge{
    int f,t,w;
}edges[10000000];
bool cmp(const edge& e1,const edge &e2){return e1.w<e2.w;}

int father[10000000];
int find(int x){
    if(father[x]!=x){
        father[x] = find(father[x]);
    }
    return father[x];
}
void uni(int x,int y){
    father[find(y)] = find(x);
}
inline bool judge(int x,int y){
    return find(x)==find(y);
}
int top = 0;
int kruskal(int n,int e){
    sort(edges+1,edges+top+1,cmp);
    int cnt = 0;
    int ans = 0;
    for(int i = 1;i<=e;i++){
        int x = edges[i].f;
        int y = edges[i].t;
        if(!judge(x,y)){
            cnt++;
            uni(x,y);
            ans+=edges[i].w;
        }
        if(cnt==n-1)return ans;
    }
    if(cnt!=n-1)return -233;
}
int main(void){
    ios::sync_with_stdio(false);
    int n,e;
    cin>>n>>e;
    int f,t,w;
    for(int i = 1;i<=n;i++)father[i] = i;

    for(int i = 1;i<=e;i++){
        cin>>f>>t>>w;
        edges[++top].f = f;
        edges[top].t = t;
        edges[top].w = w;
    }
    int ans = kruskal(n,e);
    if(ans==-233)cout<<"orz"<<endl;
    else cout<<ans<<endl;
    return 0;
}
```
