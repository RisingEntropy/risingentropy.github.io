---
title: 【点分治】woj 2336 Boatherds
date: 2019-05-18 17:03:18 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
描述
求一颗树上距离为K的点对是否存在

输入
n,m

接下来n-1条边a,b,c描述a到b有一条长度为c的路径

接下来m行每行询问一个K

输出
对于每个K每行输出一个答案，存在输出“AYE”,否则输出”NAY”(不包含引号)

样例输入
```
12 3
1 2 16
1 3 17
3 4 19
4 5 8
5 6 7
1 7 19
1 8 2
7 9 18
5 10 0
7 11 11
5 12 7
16
13
29
```
样例输出
```
AYE
NAY
AYE
```
提示
数据范围 对于30%的数据n<=100 对于60%的数据n<=1000,m<=50
对于100%的数据n<=10000,m<=100,c<=1000,K<=10000000

# 解答
点分治~~淀粉质~~的模板题题，只需要把子树里面的所有路径全部搜出来，然后枚举每个询问，看看是否可以凑出来就行了。~~我的代码不知道怎么回事，始终锅了，用的别人的代码~~
```cpp
# include<iostream>
# include<vector>
# include<algorithm>
# include<queue>
# include<cstring>
# include<cstdio>
using namespace std;

int read()
{
    int f=1,x=0;
    char ss=getchar();
    while(ss<'0'||ss>'9'){if(ss=='-')f=-1;ss=getchar();}
    while(ss>='0'&&ss<='9'){x=x*10+ss-'0';ss=getchar();}
    return f*x;
}

const int inf=10000000;
const int maxn=100010;
int n,m;
struct node{int v,dis,nxt;}E[maxn<<1];
int tot,head[maxn];
int maxp[maxn],size[maxn],dis[maxn],rem[maxn];
int vis[maxn],test[inf],judge[inf],q[maxn];
int query[1010];
int sum,rt;
int ans;

void add(int u,int v,int dis)
{
    E[++tot].nxt=head[u];
    E[tot].v=v;
    E[tot].dis=dis;
    head[u]=tot;
}

void getrt(int u,int pa)
{
    size[u]=1; maxp[u]=0;
    for(int i=head[u];i;i=E[i].nxt) 
    {
        int v=E[i].v;
        if(v==pa||vis[v]) continue;
        getrt(v,u);
        size[u]+=size[v];
        maxp[u]=max(maxp[u],size[v]);
    }
    maxp[u]=max(maxp[u],sum-size[u]);
    if(maxp[u]<maxp[rt]) rt=u;
}

void getdis(int u,int fa)
{
    rem[++rem[0]]=dis[u];
    for(int i=head[u];i;i=E[i].nxt)
    {
        int v=E[i].v;
        if(v==fa||vis[v])continue;
        dis[v]=dis[u]+E[i].dis;
        getdis(v,u);
    }
}

void calc(int u)
{
    int p=0;
    for(int i=head[u];i;i=E[i].nxt)
    {
        int v=E[i].v;
        if(vis[v])continue;
        rem[0]=0; dis[v]=E[i].dis;
        getdis(v,u);//处理u的每个子树的dis

        for(int j=rem[0];j;--j)//遍历当前子树的dis
        for(int k=1;k<=m;++k)//遍历每个询问
        if(query[k]>=rem[j])
        test[k]|=judge[query[k]-rem[j]];
        //如果query[k]-rem[j]d的路径存在就标记第k个询问

        for(int j=rem[0];j;--j)//保存出现过的dis于judge
        q[++p]=rem[j],judge[rem[j]]=1;
    }
    for(int i=1;i<=p;++i)//处理完这个子树就清空judge
    judge[q[i]]=0;//特别注意一定不要用memset，会T

}

void solve(int u)
{   
    //judge[i]表示到根距离为i的路径是否存在
    vis[u]=judge[0]=1; calc(u);//处理以u为根的子树
    for(int i=head[u];i;i=E[i].nxt)//对每个子树进行分治
    {
        int v=E[i].v;
        if(vis[v])continue;
        sum=size[v]; maxp[rt=0]=inf;
        getrt(v,0); solve(rt);//在子树中找重心并递归处理
    }
}

int main()
{
    n=read();m=read();
    for(int i=1;i<n;++i)
    {
        int u=read(),v=read(),dis=read();
        add(u,v,dis);add(v,u,dis);
    }
    for(int i=1;i<=m;++i)
    query[i]=read();//先记录每个询问以离线处理

    maxp[rt]=sum=n;//第一次先找整棵树的重心
    getrt(1,0); 
    solve(rt);//对树进行点分治

    for(int i=1;i<=m;++i)
    {
        if(test[i]) printf("AYE\n");
        else printf("NAY\n");
    }
    return 0;
}
```
我的代码
```cpp
# include <iostream>
# include <set>
# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <bitset>
using namespace std;
const int MAXN = (int)3e4+10;
struct edge{
    int t,w,next;
}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
int size[MAXN],root,mi,n,k;
int son[MAXN];
int sum;
bool vis[MAXN];
int dis[MAXN],cnt,num_dis[10000010];
int query[1100],res[1100],m;
void getroot(int x,int fa){
	size[x] = 1;son[x] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa||vis[t])continue;
		getroot(t,x);
		size[x]+=size[t];son[x] = max(son[x],size[t]);
	}
	son[x] = max(son[x],sum-size[x]);
	if(son[x]<son[root])root = x;
}
int cal(int x,int fa,int ds){
	dis[++cnt] = ds;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa||vis[t])continue;
		cal(t,x,ds+edges[i].w);
	}
}
int que[MAXN];
void dfs(int x){
	que[0] = 0;
	vis[x] = true;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].next;cnt = 0;
		if(vis[t])continue;
		cal(t,t,edges[i].w);
		for(int j = 1;j<=m;j++){
			for(int k = 1;k<=cnt;k++){
				if(query[j]>=dis[k])res[j]|=num_dis[query[j]-dis[k]];
			}
		}
		for(int j = 1;j<=cnt;j++){
			que[++que[0]] = dis[j];num_dis[dis[j]] = 1;
		}
	}
	for(int i = 1;i<=que[0];i++)num_dis[que[i]] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(vis[t])continue;
		sum = size[t];root = 0;getroot(t,0);
		dfs(root);
	}
}
int main(){
	cin>>n>>m;
	int f,t,w;
	for(int i = 1;i<n;i++){
		cin>>f>>t>>w;
		add(f,t,w);add(t,f,w);
	}
	for(int i = 1;i<=m;i++)cin>>query[i];
	sum = n;root = 0;son[0] = n;
	getroot(1,0);
	dfs(root);
	for(int i = 1;i<=m;i++)cout<<(res[i]!=0?"AYE":"NAY")<<endl;;
	return 0;
}
```