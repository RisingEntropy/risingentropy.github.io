---
title: SP2885 to reivew
date: 2018-09-16 15:14:57 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include<bits/stdc++.h>     //万能头文件
# define INF 0x3f3f3f3f
using namespace std;        //养成好习惯
typedef vector<int> vec;
map <string,vec> f;
vec e[100005];
char word[1005];
int n,Length[100005];
double dis[100005];
bool vis[100005];
string pre[100005];
bool dfs(int u,double k)
{
    vis[u] = true;
    for(vector <int> ::iterator it = e[u].begin();it != e[u].end();it++)
    {
        int v = *it;
        if(Length[v]*1.0 - k + dis[u] > dis[v])
        {
            dis[v] = Length[v]*1.0 - k + dis[u];
            if(vis[v] || dfs(v,k)) return true; 
        }
    }
    vis[u] = false;
    return false;
}
bool jud(double k)
{
    for(int i = 1;i <= n;i++) dis[i] = 0;
    memset(vis,0,sizeof(vis));
    for(int i = 1;i <= n;i++)
     if(dfs(i,k)) return true;
    return false;
}
int main()
{
    while(scanf("%d",&n) && n)   //while语句和输入
    {
        f.clear();
        for(int i = 1;i <= n;i++) e[i].clear();
        for(int i = 1;i <= n;i++)
        {
            scanf("%s",word);   //输入
            Length[i] = strlen(word);
            if(Length[i] < 2) continue;
            char Temp[3];
            for(int j = 0;j < 2;j++) Temp[j] = word[j];
            Temp[2] = '\0';
            pre[i] = Temp;
            for(int j = 0;j < 2;j++) Temp[j] = word[Length[i]-2+j];
            Temp[2] = '\0';
            string temp = Temp;
            f[temp].push_back(i);
        }
        for(int i = 1;i <= n;i++)    //for循环
        {
            if(Length[i] < 2) continue;    //如果Length[i]小于2，则继续
            if(f.count(pre[i]))
             for(vector<int> :: iterator step = f[pre[i]].begin();step != f[pre[i]].end();step++) e[*step].push_back(i);
        }
        double s = 0,t = 1000;    //double定义s,t
        while(t - s > 0.0001)
        {
            double mid = (s+t)/2.0;
            if(jud(mid)) s = mid;
            else t = mid;
        }
        if(s < 0.99999) printf("No solution.\n");   //输出
        else printf("%.2lf\n",s);   //输出
    }
}
```