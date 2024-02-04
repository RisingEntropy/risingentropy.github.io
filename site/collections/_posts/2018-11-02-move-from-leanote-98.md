---
title: 树的重心，中心，最长路径
date: 2018-11-02 10:42:45 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 树的重心
>树的重心也叫树的质心。找到一个点,其所有的子树中最大的子树节点数最少,那么这个点就是这棵树的重心,删去重心后，生成的多棵树尽可能平衡。 --百度
求取：
从一个没有求取过的点开始，求它的各子树的节点数，记为cnt,那么就看cnt和n-cnt-1哪个大就行。
代码（抄的）:

```cpp
# include <iostream>
# include <string.h>
# include <stdio.h>
 
using namespace std;
const int N = 20005;
const int INF = 1<<30;
 
int head[N];
int son[N];
bool vis[N];
int cnt,n;
int ans,size;
 
struct Edge
{
    int to;
    int next;
};
 
Edge edge[2*N];
 
void Init()
{
    cnt = 0;
    size = INF;
    memset(vis,0,sizeof(vis));
    memset(head,-1,sizeof(head));
}
 
void add(int u,int v)
{
    edge[cnt].to = v;
    edge[cnt].next = head[u];
    head[u] = cnt++;
}
 
void dfs(int cur)
{
    vis[cur] = 1;
    son[cur] = 0;
    int tmp = 0;
    for(int i=head[cur];~i;i=edge[i].next)
    {
        int u = edge[i].to;
        if(!vis[u])
        {
            dfs(u);
            son[cur] += son[u] + 1;
            tmp = max(tmp,son[u] + 1);
        }
    }
    tmp = max(tmp,n-son[cur]-1);
    if(tmp < size || tmp == size && cur < ans)
    {
        ans = cur;
        size = tmp;
    }
}

--------------------- 
作者：acdreamers 
来源：CSDN 
原文：https://blog.csdn.net/acdreamers/article/details/16905653 
版权声明：本文为博主原创文章，转载请附上博文链接！
```

# 树的最长路径
从任意一个点出发，找到离这个点最远的点$p_1$然后从$p_1$出发，找到距$p_1$最远的点$p_2$，那么$p_1\ p_2$所构成的路径就是最短路径
代码(懒得写，抄的):
```cpp
# include<queue>  
# include<vector>  
# include<cstdio>  
# include<cstring> 
# include<iostream>  
# include<algorithm>   
using namespace std;    
struct Node  
{  
	int to,cap;  
};  
const int N=100010;
vector<Node> v[N];  
int vis[N],dis[N],ans;  
 
int bfs(int x)  
{  
    memset(dis,0,sizeof(dis));  
    memset(vis,0,sizeof(vis));  
    queue<int> q;  
    q.push(x);  
    vis[x]=1;  
    int point=0;  
    while(!q.empty())  
    {  
        int f=q.front();  
        q.pop();  
        if(dis[f]>ans)  
        {  
            ans=dis[f];  
            point=f;  
        }  
        for(int i=0;i<v[f].size();i++)  
        {  
            Node temp=v[f][i];  
            if(vis[temp.to]==0)  
            {  
                vis[temp.to]=1;  
                dis[temp.to]=dis[f]+temp.cap;  
                q.push(temp.to);  
            }  
        }  
    }  
    return point;  
}  
 
int main()  
{  
    int n;
    while(~scanf("%d",&n))  
    {  
        for(int i=1;i<=n-1;i++)  
        {  
            int x,y;    
            scanf("%d %d",&x,&y);  
            v[x].push_back((Node){y,1});  
            v[y].push_back((Node){x,1});  
        }  
        ans=0;  
        int point=bfs(1);  
        ans=0;  
        bfs(point);  
        printf("%d\n",ans);  
        for(int i=1;i<=n;i++) v[i].clear();  
    }  
}  

```
# 树的中心
首先第一个dfs求出所有每个节点i在其子树中的正向最大距离和正向次大距离和d[i][0]和d[i][1]（如果i节点在子树中最大距离经过了2号儿子，那么次大距离就是不经过2号儿子的最大距离）。并且还要标记c[i]=j表示节点i在其子树中的最大距离经过了节点j（即j是i的一个儿子）。 
由上步我们获得了正向最大距离，正向次大距离和最大距离的儿子节点标记。画图可以知道我们建立的这棵树，i节点的最远距离只有两种选择：i节点所在子树的最大距离，或者i节点连接它的父节点所能到达的最大距离。（即前者往下走，后者先往上走之后很可能也往下走） 
所以我们只要求出反向最大距离d[i][2]（即i节点往它的父节点走所能到达的最大距离）就可以知道i节点在整个树中能走的最大距离了。 
d[i][2]求法：i节点往它的父节j点走，如果它的父节点的正向最大距离不经过i的话，那么d[i][2]要不就是它父节点的反向最大距离+W[i][j]要不就是它父节点的正向最大距离+ W[i][j]. 
如果它的父节点的正向最大距离经过i的话，那么d[i][2]要不就是它父节点的反向最大距离+W[i][j]要不就是它父节点的正向次大距离+ W[i][j]. 
上面就是dfs2要求的值。最终f[i]=max（d[i][0]，d[i][2]）


其余的见一本通P304
但是要记住以下几点：
以d1[i]表示以i为根的子树中，i到叶子节点的距离最大值；
d2[i]表示以i为根的子树中，i到叶子结点的距离次大值；
分别用c1[i]和c2[i]表示d1[i]d2[i]是从哪个子树更新来的。
u[i]表示除了以i为根的子树中的叶节点外，其他叶子结点到i的最大值。
然后计算d1,d2。设j是i的子节点那么：
1.若d1[j]+dis[i][j]>d1[i] 那么d2[i] = d1[i],d1[i] = d1[j]+dis[i][j]
2.否则d1[j]+dis[i][j]>d2[i]那么d2[i] = d1[j]+dis[i][j]
(2)
设p[i] = x;//i的父节点为x
若$c1[x]\neq i$即d1[x]不从i更新而来，那么u[i]=max{d1[x],u[x]}+dis[x][i]
若c1[x]=i，即d1[x]从i更新而来的，那么u[i]=max{d2[x],u[x]}+dis[x][i];
(3)
在n个节点里面找最大值
t[i] = max{u[i],d1[i]}
ans = min{t[i]}
代码：
```cpp
# include<bits/stdc++.h>
# define N 10005
using namespace std;
int tot,head[N],vet[N<<1],Next[N<<1],val[N<<1];
void add(int x,int y ,int z){
    tot++;
    vet[tot]=y;
    val[tot]=z;
    Next[tot]=head[x]; 
    head[x]=tot;
}//边表
int d[N][3];
int c[N];
int dfs1(int u,int fa){
    if(d[u][0]>=0)return d[u][0];
    d[u][0]=d[u][1]=d[u][2]=c[u]=0; 
    for(int i=head[u];i;i=Next[i]){
        int v=vet[i];
        if(v==fa)continue;
        if(d[u][0]<dfs1(v,u)+val[i]){
            c[u]=v;
            d[u][1]=max(d[u][1],d[u][0]);
            d[u][0]=dfs1(v,u)+val[i];
        }
        else if(d[u][1]<dfs1(v,u)+val[i]) 
            d[u][1]=max(d[u][1],dfs1(v,u)+val[i]);
    }
    return d[u][0];
}//计算正向最大和正向次大
void dfs2(int u,int fa){
    for(int i=head[u];i;i=Next[i]){
        int v=vet[i];
        if(v==fa)continue;
        if(v==c[u])d[v][2]=max(d[u][2],d[u][1])+val[i];
        else d[v][2]=max(d[u][2],d[u][0])+val[i];
        dfs2(v,u);
    }
}//计算反向最大
int main(){
    int n;
    while(~scanf("%d",&n)){
        tot=0;
        memset(d,-1,sizeof(d));
        memset(head,-1,sizeof(head));
        memset(c,-1,sizeof(c));
        for(int i=2;i<=n;i++){
            int v,w;
            scanf("%d%d",&v,&w);
            add(i,v,w);
            add(v,i,w);
        }//读入构图
        dfs1(1,-1);
        dfs2(1,-1);
        for(int i=1;i<=n;i++)
            printf("%d\n",max(d[i][0],d[i][2]));
    }
    return 0;
}
--------------------- 
作者：罪_蒟蒻PDD 
来源：CSDN 
原文：https://blog.csdn.net/qq_36316033/article/details/81026602 
版权声明：本文为博主原创文章，转载请附上博文链接！
```
一语道破：
2.    树的中心

概念：树的直径的中点。

求法：有多种，如DP，广搜，深搜等。

简单的方法是，先求树的直径，再找到直径中点即可。