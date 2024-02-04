---
title: 【NOIP专题】NOIP2015
date: 2019-09-29 11:08:41 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# T1
[神奇的幻方](https://www.luogu.org/problem/P2615)
水题，模拟就行。但是初赛可能会考幻方补全程序.
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
using namespace std;
const int MAXN = 40*40;
int row[MAXN],col[MAXN];
int res[40][40];
int n;
int main(){
	scanf("%d",&n);
	res[1][(n+1)/2] = 1;
	row[1] = 1;col[1] = (n+1)/2;
	for(int i = 2;i<=n*n;i++){
		if(row[i-1]==1&&col[i-1]!=n){
		//若 (K-1) 在第一行但不在最后一列，则将 K 填在最后一行， (K-1) 所在列的右一列
			row[i] = n,col[i] = col[i-1]+1;
			res[row[i]][col[i]] = i;
		}else if(col[i-1]==n&&row[i-1]!=1){
			//若（K-1)在最后一列但不在第一行，则将K填在第一列，（K-1)所在行的上一行；
			col[i] = 1;row[i] = row[i-1]-1;
			res[row[i]][col[i]] = i;
		}else if(row[i-1]==1&&col[i-1]==n){
			//若（K-1)在第一行最后一列，则将K填在（K-1)的正下方；
			row[i] = row[i-1]+1;col[i] = col[i-1];
			res[row[i]][col[i]] = i;
		}else{
			if(res[row[i-1]-1][col[i-1]+1]==0){
				row[i] = row[i-1]-1;col[i] = col[i-1]+1;
				res[row[i]][col[i]] = i;
			}else{
				row[i] = row[i-1]+1;col[i] = col[i-1];
				res[row[i]][col[i]] = i;
			}
		}
	}
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=n;j++){
			printf("%d ",res[i][j]);
		}
		puts("");
	}
	return 0;
}
```
# T2
[信息传递](https://www.luogu.org/problem/P2661)
就是求最小环
```cpp
# include<cstdio>
# include<cstring>
# include<algorithm>
# define N 200005
# define M 200005
# define inf (1ll<<31ll)-1
using namespace std;
int t,cnt,sum,top,ans=inf;
int low[N],dfn[N],sta[N];
int first[N],v[M],next[M];
bool insta[N];
void add(int x,int y)
{
	t++;
	next[t]=first[x];
	first[x]=t;
	v[t]=y;
}
void Tarjan(int x)
{
	int i,k;
	cnt++;
	low[x]=cnt;
	dfn[x]=cnt;
	top++;
	sta[top]=x;
	insta[x]=true;
	k=first[x];
	for(i=first[x];i;i=next[i])
	{
		k=v[i];
		if(!dfn[k])
		{
			Tarjan(k);
			low[x]=min(low[x],low[k]);
		}
		else if(insta[k])
		  low[x]=min(low[x],dfn[k]);
	}
	if(low[x]==dfn[x])
	{
		int sum=0;
		do
		{
			sum++;
			i=sta[top--];
			insta[i]=false;
		}
		while(i!=x);
		if(sum!=1)
		  ans=min(ans,sum);
	}
}
int main()
{
	int n,i,x;
	scanf("%d",&n);
	for(i=1;i<=n;++i)
	{
		scanf("%d",&x);
		add(i,x);
	}
	for(i=1;i<=n;++i)
	  if(!dfn[i])
	    Tarjan(i);
	printf("%d",ans);
	return 0;
}
```
# T3
[斗地主](https://www.luogu.org/problem/P2668)
模拟题，策略就是先找顺子，再找带的，最后出单牌。反正这题是因为数据水，这种策略其实是错误的。
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 16;
int card[MAXN];
void add(int v){
	if(v>=3&&v<=10)card[v-2]++;
	if(v==1)card[12]++;
	if(v==11)card[9]++;
	if(v==12)card[10]++;
	if(v==13)card[11]++;
	if(v==0)card[14]++;
	if(v==2)card[13]++;
}
int ans;
void dfs(int x){
	if(x>=ans)return;
	int k = 0;
	for(int i = 1;i<=12;i++){//顺子
		if(!card[i])k = 0;
		else{
			k++;
			if(k>=5){
				for(int j = i;j>=i-k+1;j--)card[j]--;
				dfs(x+1);
				for(int j = i;j>=i-k+1;j--)card[j]++;
			}
		}
	}
	k = 0;
	for(int i = 1;i<=12;i++){//双顺子 
		if(card[i]<=1)k = 0;
		else{
			k++;
			if(k>=3){
				for(int j = i;j>=i-k+1;j--)card[j]-=2;
				dfs(x+1);
				for(int j = i;j>=i-k+1;j--)card[j]+=2;
				}
		}
	}
	k = 0;
	for(int i = 1;i<=12;i++){//三顺子 
		if(card[i]<=2)k = 0;
		else{
			k++;
			if(k>=2){
				for(int j = i;j>=i-k+1;j--)card[j]-=3;
				dfs(x+1);
				for(int j = i;j>=i-k+1;j--)card[j]+=3;
				k = 0;
			}
		}
	}
	for(int i = 1;i<=13;i++){
		if(card[i]==3){
			card[i]-=3;
			for(int j = 1;j<=14;j++){//三带一 
				if(card[j]&&j!=i){
					card[j]--;
					dfs(x+1);
					card[j]++;
				}
			}
			for(int j = 1;j<=13;j++){//三代一对 
				if(card[j]>=2&&i!=j){
					card[j]-=2;
					dfs(x+1);
					card[j]+=2;
				}
			}
			card[i]+=3;
		}else if(card[i]==4){
			card[i]-=3;
			for(int j = 1;j<=14;j++){//三带一 
				if(card[j]&&j!=i){
					card[j]--;
					dfs(x+1);
					card[j]++;
				}
			}
			for(int j = 1;j<=13;j++){//三代一对 
				if(card[j]>=2&&i!=j){
					card[j]-=2;
					dfs(x+1);
					card[j]+=2;
				}
			}
			card[i]+=3;
			card[i]-=4;
			for(int j = 1;j<=14;j++){//四带一 
				if(card[j]>0&&j!=i){
					for(int k = 1;k<=14;k++){
						if(j==k&&j==14&&card[14]==2){//四带大小王 
							card[14]-=2;
							dfs(x+1);
							card[14]+=2;
						}else if(j!=k&&i!=k&&card[k]>0){
							card[j]--;card[k]--;
							dfs(x+1);
							card[j]++;card[k]++;
						}
					}
				}
			}
			for(int j = 1;j<=13;j++){
				if(j!=i&&card[j]>=2)
				for(int k = 1;k<=13;k++){
					if(j!=k&&i!=k&&card[k]>=2){
						card[j]-=2;card[k]-=2;
						dfs(x+1);
						card[j]+=2;card[k]+=2;
					}
				}
			} 
			card[i]+=4;
		}
	} 
	for(int i = 1;i<=14;i++)if(card[i])x++;
	ans = min(ans,x);
}

int main(){
	int T,n;
	scanf("%d %d",&T,&n);
	while(T--){
		memset(card,0,sizeof(card)); 
		int x,y;
		ans = n;
		for(int i = 1;i<=n;i++){
			scanf("%d %d",&x,&y);
			add(x);
		}
		dfs(0);
		printf("%d\n",ans);
	}
	return 0;
}
```
# T4
[跳石头](https://www.luogu.org/problem/P2678)
二分板子题
```cpp
# include<cstdio> 
int read(){
	int flag = 1,n = 0;
	char ch;
	ch = getchar();
	while(ch>'9'||ch<'0'){
		if(ch=='-')flag = -1;
		ch = getchar();
	}
	while(ch>='0'&&ch<='9'){
		n*=10;
		n+=ch-'0';
		ch = getchar();
	}
	return n*flag;
}

int L,M,N;
int stones[50010];
bool check(int l){
	int tot = 0;
	int last = 0;
	for(int i = 1;i<=N;i++){
		if(stones[i]-last<l){
			tot++;
		}else{
			last = stones[i];
		}
		if(tot>M)return false;
	}
	if(L-last<l)tot++;
	return tot<=M;
}
int main(void){
	L = read();N = read();M = read();
	for(int i = 1;i<=N;i++){
		stones[i] = read();
	}
	int l = 0;int r = L;
	while(l<r){
		int mid = (l+r+1)>>1;
		if(check(mid)){
			l = mid;
		}else{
			r = mid-1;
		}
	}
	printf("%d",l);
	return 0;
}
```
# T5
[子串](https://www.luogu.org/problem/P2679)
显然是个DP。dp[i][j][k][0/1]表示A匹配i位B匹配j位分成k段，第i位选不选。
则有如下转移
若A[i]=B[j]
$dp[i][j][k][0] = dp[i-1][j][k][0]+dp[i-1][j][k][1]$
$dp[i][j][k][1] = dp[i-1][j-1][k-1][0]+dp[i-1][j-1][k-1][1]+dp[i-1][j-1][k][1]$
否则
$dp[i][j][k][0] = dp[i-1][j][k][0]+dp[i-1][j][k][1]$
$dp[i][j][k][1] = 0$
代码:
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 1010;
const int MAXM = 210;
const int mod = 1000000007;
int dp[2][MAXM][MAXM][2];
char A[MAXN],B[MAXN];
int n,m,kk;
void write(int x){
	if(x>9)write(x/10);
	putchar(x%10+'0');
}

int main(){
	scanf("%d%d%d",&n,&m,&kk);
	scanf("%s %s",A+1,B+1);
	dp[1][0][0][0] = dp[0][0][0][0] = 1;
	for(register int i = 1;i<=n;i++){
		for(register int j = 1;j<=m;j++){
			for(register int k = 1;k<=kk;k++){
				if(A[i]==B[j]){
					dp[i&1][j][k][0] = (dp[(i-1)&1][j][k][0]+dp[(i-1)&1][j][k][1])%mod;
					dp[i&1][j][k][1] = (dp[(i-1)&1][j-1][k][1]+(dp[(i-1)&1][j-1][k-1][1]+dp[(i-1)&1][j-1][k-1][0])%mod)%mod;
				}else{
					dp[i&1][j][k][0] = (dp[(i-1)&1][j][k][0]+dp[(i-1)&1][j][k][1])%mod;
					dp[i&1][j][k][1] = 0;
				}
			}
		}
	}
	write((dp[n&1][m][kk][0]+dp[n&1][m][kk][1])%mod);
	return 0;
} 
```
# T6
[运输计划](https://www.luogu.org/problem/P2680)
可以一眼看出是个二分答案。然后统计出长度大于mid的路径的条数。考虑如何统计一条边被多少条路径经过，考虑树上差分。sum[x]++,sum[y]++,sum[lca]-=2；即可从底到顶统计出来。然后找到一条长度大于mid的，被超过num条路径经过的边即可。
代码：
```cpp
# include<cstdio>
# include<cstring>
# define M 300001
# include<algorithm>
using namespace std;
struct nn{
    int to,next,val;
};
nn ed[M<<1];
struct nnn {
    int a,b,ans,dist;
};
nnn lca[M];
int head[M],tot,b[M];
int n,m,ans,l,r;
int f[M][31],dep[M],dis[M],sum[M];
inline int read() {
    int x=0;char c=getchar();
    while(c>'9'||c<'0') c=getchar();
    while(c>='0'&&c<='9') x=10*x+c-48,c=getchar();
    return x;
}
inline void add(int x,int y,int z) {
    ed[++tot].to=y;
    ed[tot].val=z;
    ed[tot].next=head[x];
    head[x]=tot;
}
inline void dfs(int x,int from,int de,int l) {
    dep[x]=de;
    dis[x]=l;
    f[x][0]=from;
    for(int i=head[x];i;i=ed[i].next) {
        int v=ed[i].to;
        if(v!=from) {
            b[v]=i;
            dfs(v,x,de+1,l+ed[i].val);
        }
    }
}
inline int LCA(int a,int b) {
    if(dep[a]<dep[b]) swap(a,b);
    int t=dep[a]-dep[b];
    for(int i=0;i<=30;i++)
      if((1<<i)&t) a=f[a][i];
    if(a==b) return a;
    for(int i=30;i>=0;i--) 
      if(f[a][i]!=f[b][i])
        a=f[a][i],b=f[b][i];
    return f[a][0];
}
inline void updata(int now,int from) {
    for(int i=head[now];i;i=ed[i].next) {
        int v=ed[i].to;
        if(v!=from) {
            updata(v,now);
            sum[now]+=sum[v];
        }
    }
}
inline bool check(int x) {
    int cnt=0,dec=0;
    memset(sum,0,sizeof(sum));
    for(int i=1;i<=m;i++)
      if(lca[i].dist>x) {
        cnt++;
        sum[lca[i].a]++;
        sum[lca[i].b]++;
        sum[lca[i].ans]-=2;
        dec=max(dec,lca[i].dist-x);
      }
    updata(1,1);
    for(int i=1;i<=n;i++) if(sum[i]==cnt&&ed[b[i]].val>=dec) return true;
    return false;
}
int main() {
    n=read();m=read();
    for(int i=1;i<n;i++) {
        int x,y,z;
        x=read();y=read();z=read();
        add(x,y,z);add(y,x,z);
    }

    dfs(1,1,0,0);
    for(int j=1;j<=30;j++)
      for(int i=1;i<=n;i++)
        f[i][j]=f[f[i][j-1]][j-1];
    for(int i=1;i<=m;i++) {
        lca[i].a=read();
        lca[i].b=read();
        lca[i].ans=LCA(lca[i].a,lca[i].b);
        lca[i].dist=dis[lca[i].a]+dis[lca[i].b]-(dis[lca[i].ans]<<1);
        r=max(r,lca[i].dist);
    }
    r++;
    while(l<r) {
        int mid=(l+r)>>1;
        if(check(mid)) ans=r=mid;
        else l=mid+1;
    }
    printf("%d\n",ans);
    return 0;
}
```