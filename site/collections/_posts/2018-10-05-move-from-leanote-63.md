---
title: tarjan双连通分量
date: 2018-10-05 10:29:07 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

点:
```cpp
//tarjan find cut point
edge stack[10000];
int dfn[10000];
int low[10000];
int stop;
int dfn_cnt;
int bcc_num[1000];//哪个点属于哪个双连通分量 
int bcc_cnt;//有多少个双连通分量
vector<int> bcc[10000];//每个双连通分量有哪些点 
bool iscut[1000];
int root;
void tarjan(int x,int fa){
    low[x] = dfn[x] = ++dfn_cnt;
    int child = 0;
    for(int i = head[x];i!=0;i = edges[i].next){
        int v = edges[i].t;
        if(!dfn[i]){//下一个点没有被访问过; 
            stack[++stop] = edges[i];
            tarjan(edges[i].t,x);
            child++;
            low[x] = min(low[x],low[edges[i].t]);
            if(low[v]>dfn[x]){
                iscut[x] = true;
                ++bcc_cnt;
                bcc[bcc_cnt].clear();
                while(true){
                    edge e = stack[stop--];
                    if(bcc_num[e.f]!=bcc_cnt){
                        bcc[bcc_cnt].push_back(e.f);
                        bcc_no[e.f] = bcc_cnt;
                    }
                    if(bcc_num[e.t]!=bcc_cnt){//取出这些边与其相邻的点，组成一个双连通分量 
                        bcc[bcc_cnt].push_back(e.t);
                        bcc_no[e.t] = bcc_cnt;
                    }
                    if(e.f == x&&e.t = v){
                        break;//直到取出边(u,v) 
                    }
                }
            }
        }else{
            if(dfn[x]>dfn[v]&&v!=fa){
                stack[++top] = edges[i];
                low[x] = min(low[x],dfn[edges[i].t]) ;
            }
        }
    }
    if(fa<=&&child==1){
        iscut[x] = false; 
    }
}
void findbcc(int n){
    //初始化一些东西，如果全局变量的话不需要
    for(int i = 1;i<=n;i++){
        if(!dfn[i]){
            tarjan(i,-1);//-1应该是一个虚拟根节点 
        }
    } 
}
```
边：
```cpp
//tarjan find cut point
edge stack[10000];
int dfn[10000];
int low[10000];
int stop;
int dfn_cnt;
int bcc_num[1000];//哪个点属于哪个双连通分量 
int bcc_cnt;//有多少个双连通分量
vector<int> bcc[10000];//每个双连通分量有哪些点 
bool isbridge[1000];
int root;
void tarjan(int x,int fa){
    low[x] = dfn[x] = ++dfn_cnt;
    for(int i = head[x];i!=0;i = edges[i].next){
        int v = edges[i].t;
        if(!dfn[i]){//下一个点没有被访问过; 
            tarjan(edges[i].t,x);
            low[x] = min(low[x],low[edges[i].t]);
            if(low[v]>dfn[x]){
                isbridgs[i] = isbridge[i^1] = true;
            }
        }else{
            if(dfn[x]>dfn[v]&&v!=fa){
                stack[++top] = edges[i];
                low[x] = min(low[x],dfn[edges[i].t]) ;
            }
        }
    }
}
void dfs(int index){
    dfn[index] = true;
    bcc_num[index] = bcc_cnt;
    for(int i = head[index];i!=0;i = edges[i].next){
        int v = edges[i].t;
        if(isbridge[i])continue;
        if(!dfn[v]){
            dfs(v);
        }
    }
}
void find_ebcc(int n){
    //做一些初始化，把数组初始化了 
    for(int i = 1;i<=n;i++){
        if(!dfn[n]){
            tarjan(i,-1);
        }
    }
    memset(dfn,0,sizeof(dfn));
    for(int i = 1;i<=n;i++){
        if(!dfn[i]){
            bcc_cnt++;
            dfs(i);
        }
    } 
}
```