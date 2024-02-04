---
title: 点、边双联通分量
date: 2019-05-02 21:36:42 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 点、边双联通分量
小知识点，记一下
# 点双联通分量
性质

 1. 任意两点间至少存在两条点不重复的路径等价于图中删去任意一个点都不会改变图的连通性，即BCC中无割点
 2. **若BCC间有公共点，则公共点为原图的割点**
 3. 无向连通图中割点一定属于至少两个BCC，非割点只属于一个BCC
 
做法
 在Tarjan过程中维护一个栈，每次Tarjan到一个结点就将该结点入栈，回溯时若目标结点low值不小于当前结点dfn值就出栈直到目标结点（目标结点也出栈），将出栈结点和当前结点存入BCC

代码：
```cpp
# include<cstdio>
# include<cctype>
# include<vector>
using namespace std;
struct edge
{
    int to,pre;
}edges[1000001];
int head[1000001],dfn[1000001],dfs_clock,tot;
int num;//BCC数量 
int stack[1000001],top;//栈 
vector<int>bcc[1000001];
int tarjan(int u,int fa)
{
    int lowu=dfn[u]=++dfs_clock;
    for(int i=head[u];i;i=edges[i].pre)
        if(!dfn[edges[i].to])
        {
            stack[++top]=edges[i].to;//搜索到的点入栈 
            int lowv=tarjan(edges[i].to,u);
            lowu=min(lowu,lowv);
            if(lowv>=dfn[u])//是割点或根 
            {
                num++;
                while(stack[top]!=edges[i].to)//将点出栈直到目标点 
                    bcc[num].push_back(stack[top--]);
                bcc[num].push_back(stack[top--]);//目标点出栈 
                bcc[num].push_back(u);//不要忘了将当前点存入bcc 
            }
        }
        else if(edges[i].to!=fa)
            lowu=min(lowu,dfn[edges[i].to]);
    return lowu;
}
void add(int x,int y)//邻接表存边 
{
    edges[++tot].to=y;
    edges[tot].pre=head[x];
    head[x]=tot;
}
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        add(x,y),add(y,x);
    }
    for(int i=1;i<=n;i++)//遍历n个点tarjan 
        if(!dfn[i])
        {
            stack[top=1]=i;
            tarjan(i,i);
        }
    for(int i=1;i<=num;i++)
    {
        printf("BCC# %d: ",i);
        for(int j=0;j<bcc[i].size();j++)
            printf("%d ",bcc[i][j]);
        printf("\n");
    }
    return 0;
}

双连通分量
```
# 边双连通分量
对于一个连通图，如果任意两点至少存在两条“边不重复”的路径，则说图是点双连通的，边双连通的极大子图称为边双连通分量。
边双联通分量的计算方法比较简单
首先，对于边双联通分量里的点我们是不用考虑的。
因此我们先用tarjan把边双联通分量缩出来
这样的话必定会形成一棵树
接下来考虑贪心，对于任意三个不在同一边双联通分量里且入度唯一的点
我们在他们中间连一条边，这样一定是最优的
因此我们只需要统计入度为1的点就行了
最后的答案为(ans+1)/2