---
title: 【NOIP专题】NOIP2018
date: 2019-09-15 09:06:10 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# NOIP2018
评价：这年的NOIP感觉质量很屑，完全是在乱搞，听说Day2T2是因为漏题的原因直接换成了清华校内集训的T1。~~分明就是我太菜了~~
# T1
[题面](https://www.luogu.org/problem/P1969)
#  解答
水题，做个差分，把正的加起来就行了。
```cpp
//
// Created by dhy on 18-11-10.
//
# include <cstdio>
# include <cstdlib>
const int MAXN = 100010;
int read(){
    int x = 0,f = 1;
    char c = getchar();
    while(c>'9'||c<'0'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar();}
    return x*f;
}
int a[MAXN];
int d[MAXN];
int main(){
    int n = read();
    for(int i = 1;i<=n;i++){
        a[i] = read();
        d[i] = a[i]-a[i-1];
    }
    int ans = 0;
    for(int i = 1;i<=n;i++){
        if(d[i]>0)ans+=d[i];
    }
    printf("%d\n",ans);
    return 0;
}
```
# T2
[题面](https://www.luogu.org/problem/P5020)
#  解答
背包，排个序，然后尝试用小的更新大的。
代码：
```cpp
//
// Created by dhy on 18-11-10.
# include <cstdio>
# include <algorithm>
# include <cstring>
# include <cstdlib>
using namespace std;
int read(){
    int x = 0,f = 1;
    char c = getchar();
    while(c>'9'||c<'0'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar();}
    return x*f;
}
const int MAXVAL = 25010;
int a[MAXVAL];
bool f[MAXVAL];
int main(){
    int T = read();
    while(T--){
    	memset(f,false,sizeof(f));
        int n = read();
        int ans = n;
        for(int i = 1;i<=n;i++){
            a[i] = read();
        }
        sort(a+1,a+1+n);
        f[0] = true;
        for(int i = 1;i<=n;i++){
        	if(f[a[i]]){
        		ans--;
        		continue;
			}
			for(int j = a[i];j<=a[n];j++)f[j] = f[j]|f[j-a[i]];
		}
        printf("%d\n",ans);
    }
    return 0;
}
```
# T3
[题面](https://www.luogu.org/problem/P5021)
#  解答
首先不难看出是个二分加树上的一个操作。考虑如何判断解是否可行。记$f[i]$表示节点$i$的子树中，满足条件的路径有多少种，$g[i]$表示节点$i$的子树中，最长的一条链的长度，然后对于每个节点，直接合并子树中的$f$然后把$g$全部丢到`multiset`里面，每次取最小的，再找一个刚好可以拼凑成$mid$的值拼凑，更新$f$
代码：
```cpp
// luogu-judger-enable-o2
# include <iostream>
# include <cstring>
# include <cstdio>
# include <set>
# include <algorithm>
# define clean(x) memset(x,0,sizeof(x))
using namespace std;
const int MAXN = 101000;
struct edge{int t,w,next;}edges[MAXN<<1];
int head[MAXN],top;
void add(int f,int t,int w){
	edges[++top].next = head[f];
	edges[top].t = t;
	edges[top].w = w;
	head[f] = top;
}
int f[MAXN],g[MAXN];
multiset<int> st[MAXN];
int n,m;
void dfs(int x,int fa,int mid){
	st[x].clear();f[x] = 0,g[x] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa)continue;
		dfs(t,x,mid);
		g[x]+=g[t];
		int v = f[t]+edges[i].w;
		if(v>=mid)g[x]++;
		else st[x].insert(v);
	}
	while(!st[x].empty()){
		if(st[x].size()==1){
			f[x] = max(f[x],*st[x].begin());
			break;
		}else{
			multiset<int>::iterator it;
			it = st[x].lower_bound(mid-*st[x].begin());
			if(it==st[x].begin()&&st[x].count(*it)==1)it++;
			if(it==st[x].end()){
				f[x] = max(f[x],*st[x].begin());
				st[x].erase(st[x].find(*st[x].begin()));
			}else{
				g[x]++;
				st[x].erase(st[x].find(*it));
				st[x].erase(st[x].find(*st[x].begin()));
			}
		}
	}
}
bool check(int mid){
	dfs(1,1,mid);
	return g[1]>=m;
}
int main(){
	scanf("%d%d",&n,&m);
	int f,t,w;
	int sum = 0;
	for(int i = 1;i<n;i++){
		scanf("%d%d%d",&f,&t,&w);
		add(f,t,w);add(t,f,w);
		sum+=w;
	}
	int l = 0,r = sum;
	while(l<r){
		int mid = l+r+1>>1;
		if(check(mid))l = mid;
		else r = mid-1;
	}
	printf("%d\n",l);
	return 0;
}
```
# T4
[题面](https://www.luogu.org/problem/P5022)
#  解答
暴力枚举断一条边，然后贪心做就好了
代码：
```cpp
// luogu-judger-enable-o2
# include <iostream>
# include <vector>
# include <cstring>
# include <algorithm>

using namespace std;
vector<int> G[5010];
int vis[5010];
namespace tree{
    vector<int> ans;
    void dfs(int x){
        vis[x] = true;
        ans.push_back(x);
        for(int i = 0;i<G[x].size();i++){
            if(!vis[G[x][i]])dfs(G[x][i]);
        }
    }
    void main(){
        dfs(1);
        for(int i = 0;i<ans.size();i++)cout<<ans[i]<<' ';
    }
}
int n,m;
int edge[5010][2];
namespace ringBasedTree{
    vector<int> ans,temp;
    int del_f,del_t;
    bool chect(int u,int v){
        if((u==del_f&&v==del_t)||(u==del_t&&v==del_f)){
            return false;
        }
        return true;
    }
    void dfs(int x){
        vis[x] = true;
        temp.push_back(x);
        for(int i = 0;i<G[x].size();i++){
            if(chect(x,G[x][i])&&!vis[G[x][i]]){
                dfs(G[x][i]);
            }
        }
    }
    void main(){
        for(int i = 1;i<=n;i++)ans.push_back(9999);
        for(int i = 1;i<=m;i++){
                memset(vis,false, sizeof(vis));
                del_f = edge[i][0],del_t = edge[i][1];
                temp.clear();
                dfs(1);
                if(temp<ans&&temp.size()==n)ans = temp;
        }
        for(int i = 0;i<ans.size();i++)cout<<ans[i]<<' ';
    }
}
int main(void){
    cin>>n>>m;
    int x,y;
    for(int i = 1;i<=m;i++){
        cin>>x>>y;
        edge[i][0] = x;
        edge[i][1] = y;
        G[x].push_back(y),G[y].push_back(x);
    }
    for(int i = 1;i<=n;i++)sort(G[i].begin(),G[i].end());
    if(m==n-1){
        tree::main();
    }else{
        ringBasedTree::main();
    }
    return 0;
}
```
# T5
[题面](https://www.luogu.org/problem/P5023)
我不会，据说可以dfs套dfs找规律得50分
# T6
[题面](https://www.luogu.org/problem/P5024)
我不会，DDP板子题