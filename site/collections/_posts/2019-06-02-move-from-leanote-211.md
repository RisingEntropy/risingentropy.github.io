---
title: 【最小树形图】bzoj 4349 最小树形图
date: 2019-06-02 19:10:48 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
小C现在正要攻打科学馆腹地------计算机第三机房。而信息组的同学们已经建好了一座座堡垒，准备迎战。小C作为一种高度智慧的可怕生物，早已对同学们的信息了如指掌。
攻打每一个人的堡垒需要一个代价，而且必须攻打若干次才能把镇守之人灭得灰飞烟灭。
当小C在绞尽脑汁想攻打方案时，突然从XXX的堡垒中滚出来一个纸条：一个惊人的秘密被小C发现了：原来各个堡垒之间会相互提供援助，但是当一个堡垒被攻打时，他对所援助的堡垒的援助就会停止，因为他自己已经自身难保了。也就是说，小C只要攻打某个堡垒一次之后，某些堡垒就只需要花更小的代价攻击了。
现在，要你求消灭全机房要用掉代价最小多少。
#  Input
第一行一个数N，(N`<`=50),表示机房修建的堡垒数。
接下来N行，每行两个数，第一个实数Ai表示攻打i号堡垒需要的代价Ai(0`<`Ai`<=`1000)。第二个数Bi(0`<`Bi`<`100)表示i号堡垒需要被攻打Bi次。
接下来一个数k，表示总共有k组依赖关系。
接下来k行每行三个数x，y，z(x,y,为整数，z为实数)，表示攻打过一次x号堡垒之后，攻打y号堡垒就只要花z的代价，保证z比y原来的代价小。
不需要攻打的城堡不允许攻打。
#  Output
一行，一个实数表示消灭全机房要用的最小代价，保留两位小数。
#  Sample Input
```
3 										
10．00  1
1.80  1 
2.50	 2
2
1  3  2.00
3  2  1.50
```
Sample Output
```
15.50
```
# 解答
最小树形图板题~~题目名称暴露了一切~~。出题人牛逼
建立一个虚点，连向所有点，然后跑出每个点都打一次的最小代价。然后再来以每次都是最小代价的打法，对每个点再打$times[i]-1$次。代码如下
```cpp
//
// Created by dhy on 19-6-2.
//

# include <iostream>
# include <cstdio>
# include <cstring>
# include <iomanip>
using namespace std;
# define LL long long
const int MAXN = 60;
const int MAXM = 3000;
struct edge{int f,t;double w;}edges[MAXM];
int id[MAXN],vis[MAXN],fa[MAXN];double dis[MAXN];
bool mark[MAXN];
double cost[MAXN];
int times[MAXN];
int top;
void add(int f,int t,double w){
    edges[++top].f = f;
    edges[top].t = t;
    edges[top].w = w;
}
const double INF = 1e19;
double zhuliu(int root,int n,int m){
    double res = 0;
    while(true) {
        for(int i = 0;i<=n;i++)mark[i] = false,dis[i] = INF;
        for(int i = 1;i<=m;i++){
            int f = edges[i].f,t = edges[i].t;
            if(f!=t&&edges[i].w<dis[t]){
                dis[t] = edges[i].w;
                fa[t] = f;
            }
        }
        for(int i = 0;i<=n;i++){
            if(dis[i]==INF&&i!=root)mark[i] = true;
        }
        int cnt = 0;
        memset(vis,-1,sizeof(vis));
        memset(id,-1, sizeof(id));
        dis[root] = 0;
        for(int i = 0;i<=n;i++){
            if(mark[i])continue;
            int t = i;
            res+=dis[t];
            while(id[t]==-1&&t!=root&&vis[t]!=i){
                vis[t] = i;
                t = fa[t];//it will come back to itself
            }
            if(id[t]==-1&&t!=root){
                for(int u = fa[t];u!=t;u = fa[u]){//mark the ring
                    id[u] = cnt;
                }
                id[t] = cnt++;
            }
        }
        if(cnt==0)return res;
        for(int i = 0;i<=n;i++)if(id[i]==-1)id[i]=++cnt;
        for(int i = 1;i<=m;i++){
            int f = edges[i].f,t = edges[i].t;
            edges[i].f = id[f];edges[i].t = id[t];
            if(id[f]!=id[t])edges[i].w-=dis[t];
        }
        n = cnt;root = id[root];
    }
}
int main(){
    int n;cin>>n;
    for(int i = 1;i<=n;i++){
        cin>>cost[i]>>times[i];
        if(times[i]!=0){
            add(0,i,cost[i]);
        }else{
            mark[i] = true;
        }
    }
    double res = 0;
    int k;cin>>k;
    int f,t;double w;
    for(int i = 1;i<=k;i++){
        cin>>f>>t>>w;
        if(t==0)continue;
        if(mark[t]||mark[f])continue;
        add(f,t,w);
        cost[t] = min(cost[t],w);
    }
    for(int i = 1;i<=n;i++)if(!mark[i])res+=(times[i]-1)*cost[i];
    res += zhuliu(0,n,top);
    cout.setf(ios::fixed);
    cout<<setprecision(2)<<res;
    return 0;
}
```