---
title: 【冷门知识点】支配树
date: 2019-05-31 20:53:29 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 支配树
在一个有向图中，有一个起点R，对于任意点W，对于R->W的任意路径都经过点P，则称P为W的支配点。设idom[i]表示距离i最近的支配点。在原图基础上，idom[i]向i连边构成一颗新树，称为支配树
#  支配树的性质
1.支配树是以R为根的一棵树
2.对于任意点i，到根r路径上经过的点集{xi}是原图上r->i的必经点
3.对于任意的i，它是子树中每个点的必经点
#  求得
#  半必经点
在dfs搜索树中，对于一个节点Y，存在某个点X能够通过一系列点pi（不包含X和Y）到达点Y且∀i dfn[i]>dfn[Y]，我们就称X是Y的半必经点，记做semi[Y]=X
通俗理解：semi[x]就是x在dfs树中所有祖先中z，能不经过 z​ 和 x​ 之间的树上的点而到达 x​ 的点中深度最小的。
#  半必经点性质

 1. semi[x]一定是x的祖先
 2. semi[x]一定是确定的
 3. 半必经点不一定是必经点
 4. semi[x]深度不小于idom[x]，即idom[x]在semi[x]祖先链上

~~证明的话，咕咕了~~
#  半必经点的作用
保留dfs树的树边，连接semi[i]->i构建新图。不改变原图支配关系，且构成一个dag图。
#  计算
对于点x，有边(y,x)
• 若dfn[y]$<$dfn[x](树边或前向边） 且dfn[y]$<$dfn[semi[x]] ,semi[x]=y
• 根据定义显然
• 若dfn[y]>dfn[x]（后向边或横叉边），找到y的一个祖先semi值最小
的z且dfn[z]>dfn[x]，用semi[z]更新semi[x]
#  计算idom
#  性质

 1. idom[x]的深度不大于semi[x]
 2. 设点集P是semi[x]（不包含）到x路径上的点，t是P中semi最小的点(1、若semi[t]=semi[x],则idom[x]=semi[x]2、若semi[t]!=semi[x],则idom[x]=idom[t])

#  算法

 1. 按dfs序搜索原图得到dfn，从dfn大到小考虑节点
 2. 利用带权并查集维护每个点到祖先链上semi值最小值
 3. 设当前计算semi[x],对于（y,x）若dfn[y]>dfn[x],则直接根据 更新（y的semi已经计算完）若dfn[y]$<$dfn[x]，则semi[y]没有更新，y是并查集独立点， 同样更新
 4. 用x=semi[y]->y更新y的idom，直接查询y祖先链上最小值
 5. 最后将semi[x]!=idom[x]的节点idom按dfn从小到大刷新一次

#  代码实现
wdnmd 并查集打错了，跳了一晚上
HDU4694
```cpp
//
// Created by dhy on 19-6-7.
//
# include <iostream>
# include <vector>
# include <cstring>
using namespace std;
const int MAXN = 1e5+10;
struct graph{
    vector<int> G[MAXN];
    void add(int f,int t){
        G[f].push_back(t);
    }
    void clear(){
        for(int i = 1;i<MAXN;i++)G[i].clear();
    }
}G,rG,sG,tree;
int dfn[MAXN],id[MAXN],fa[MAXN],semi[MAXN],idom[MAXN];
int dfn_cnt;
int belong[MAXN],val[MAXN];
int n,m;
int ans[MAXN];
void reset(){
    memset(ans,0, sizeof(ans));
    memset(dfn,0, sizeof(dfn));
    memset(fa,0, sizeof(fa));
    memset(semi,0, sizeof(semi));
    memset(idom,0, sizeof(idom));
    memset(belong,0, sizeof(belong));
    memset(val,0, sizeof(val));
    memset(id,0, sizeof(id));
    dfn_cnt = 0;
    G.clear(),rG.clear(),sG.clear(),tree.clear();
}

void getdfn(int x,int f){
    dfn[x] = ++dfn_cnt;id[dfn_cnt] = x;
    fa[x] = f;
    for(int i = 0;i<G.G[x].size();i++){
        int t = G.G[x][i];
        if(dfn[t])continue;
        getdfn(t,x);
    }
}
int find(int x){
    if(belong[x]==x)return x;
    int fx = find(belong[x]);
    if(dfn[semi[val[belong[x]]]]<dfn[semi[val[x]]])val[x] = val[belong[x]];//wdnmd就是这里
    belong[x] =fx;return fx;
}
void tarjan(){
    for(int j = dfn_cnt;j>1;j--){
        int x = id[j];
        for(int i = 0;i<rG.G[x].size();i++){//尝试更新semi
            int t = rG.G[x][i];
            if(!dfn[t])continue;
            find(t);
            if(dfn[semi[val[t]]]<dfn[semi[x]])
                semi[x] = semi[val[t]];
        }
        sG.add(semi[x],x);//建图
        belong[x] = fa[x];
        int now = fa[x];
        for(int i = 0;i<sG.G[now].size();i++){//图上使用更新fa[x]为semi的点，更新为新找到的那个点
            int t = sG.G[now][i];
            find(t);
            if(semi[val[t]]==now)idom[t] = now;如果semi[x]=semit[t]，说明idom[x]=semi[x]
            //此时semi=now
            else idom[t] = val[t];否则就是idom[x]=idom[t]，实现的时候写成idom[t]=t，后面在处理
        }
    }
    for(int i = 2;i<=dfn_cnt;i++){
        int t = id[i];
        if(idom[t]!=semi[t])idom[t] = idom[idom[t]];//处理
        tree.add(idom[t],t);
    }
}
void getans(int x,int sum){
    ans[x] = x+sum;
    for(int i = 0;i<tree.G[x].size();i++){
        int t = tree.G[x][i];
        getans(t,x+sum);
    }
}
int main(){
    while(scanf("%d%d",&n,&m)!=EOF){
        reset();int f,t;
        for(int i = 1;i<=m;i++){
            scanf("%d%d",&f,&t);
            G.add(f,t);rG.add(t,f);
        }
        for(int i = 1;i<=n;i++)belong[i] =semi[i] =val[i] = i;
        getdfn(n,0);
        tarjan();
        getans(n,0);
        for(int i = 1;i<n;i++)printf("%d ",ans[i]);
        printf("%d",ans[n]);puts("");

    }
    return 0;
}
```
 
