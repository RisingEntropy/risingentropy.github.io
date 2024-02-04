---
title: 停课复习
date: 2019-09-28 10:07:38 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 三分
[SCOI 传送带](http://192.168.110.251/problempage.php?contest_id=1130&prob=2)
三分模板题
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <cmath>
using namespace std;
const double eps = 1e-9;
double ax,ay,bx,by,cx,cy,dx,dy;
double p,q,r;
double S(double x) {
	return x*x;
}
inline double getdis(double x1,double y1,double x2,double y2) {
	double dis1 = sqrt(S(x1-ax)+S(y1-ay));
	double dis2 = sqrt(S(x1-x2)+S(y1-y2));
	double dis3 = sqrt(S(x2-dx)+S(y2-dy));
	return dis1/p+dis2/r+dis3/q;
}
double work(double x,double y) {
	double lx = cx,rx = dx;
	double ly = cy,ry = dy;
	while(fabs(rx-lx)>eps||fabs(ry-ly)>eps) {
		double nx1 = lx+(rx-lx)/3.0,ny1 = ly+(ry-ly)/3.0;
		double nx2 = lx+2.0*(rx-lx)/3.0,ny2 = ly+2.0*(ry-ly)/3.0;
		double dis1 = getdis(x,y,nx1,ny1),dis2 = getdis(x,y,nx2,ny2);
		if(dis1>dis2)lx = nx1,ly = ny1;
		else rx = nx2,ry = ny2;
	}
	return getdis(x,y,lx,ly);
}
int main() {
	cin>>ax>>ay>>bx>>by;
	cin>>cx>>cy>>dx>>dy;
	cin>>p>>q>>r;
	double lx = ax,ly = ay;
	double rx = bx,ry = by;
	while(fabs(rx-lx)>eps||fabs(ry-ly)>eps) {
		double nx1 = lx+(rx-lx)/3.0,ny1 = ly+(ry-ly)/3.0;
		double nx2 = lx+2.0*(rx-lx)/3.0,ny2 = ly+2.0*(ry-ly)/3.0;
		double dis1 = work(nx1,ny1),dis2 = work(nx2,ny2);
		if(dis1>dis2)lx = nx1,ly = ny1;
		else rx = nx2,ry = ny2;
	}
	printf("%.2lf",work(lx,ly));
	return 0;
}
```
# DAG上概率期望
woj2287
XXX发现他生活的村有很多值钱的石头。XXX 所在的村有 N 堆石头，第 i 堆的价值为 Vi。另有 M 条单向道路连接这些石头堆，满足从任意一堆石头出发沿着这些道路不会回到 起点。XXX 打算来一次捡石头之旅。由于他没有地图，他无法知道应该怎么走。因此他 只能采取这样的策略：每次从当前所在石头堆等概率随机选择一条可走的道路，走过去。 XXX 到达一堆石头后就会立刻把它们捡进自己的包里面。初始时，XXX 将等概率随机 空降到一个石头堆。现在，xxx向请你帮他算出他期望能得到多少价值的石头。

千万注意，不可以建立反图计算，因为反图中计算的出度是原来的入度，这样概率就错了，Orzzzzzzzz
代码：
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
# include <queue>
using namespace std;
const int MAXN = (int)1e5+10;
struct edge{int t,next;}edges[MAXN<<1];
int head[MAXN],top;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
double dp[MAXN],v[MAXN];
int n,m;
int in[MAXN],sze[MAXN];
queue<int> q;
void topo(){
	for(int i = 1;i<=n;i++)if(!in[i])q.push(i);
	while(!q.empty()){
		int top = q.front();q.pop();
		if(sze[top])dp[top]/=double(sze[top]);
		dp[top]+=v[top];
		for(int i = head[top];i;i = edges[i].next){
			int t = edges[i].t;
			sze[t]++;dp[t]+=dp[top];
			if(!--in[t])q.push(t);
		}
	}
} 
int main(){
	scanf("%d %d",&n,&m);
	int f,t;
	for(int i = 1;i<=n;i++)scanf("%lf",&v[i]);
	for(int i = 1;i<=m;i++){
		scanf("%d %d",&f,&t);
		add(t,f);in[f]++;
	}
	
	topo();
	double res = 0.0;
	for(int i = 1;i<=n;i++)res+=dp[i];
	printf("%.2lf",res/double(n));
	return 0;
}
```
# 简单的概率期望
woj4159
没想到这道题卡死我的是套路。。。。看到那个数据范围就知道要预处理然后$O(1)$回答。。。预处理的时候前缀和优化一下就行了Orz还有就是逆元要递推
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = (int)1e7+10;
const long long mod = 998244353;
int dp[MAXN];
int inv[MAXN];
int main(){
	long long sum = 0;
	inv[1] = inv[0] = 1;
	for(int i = 2;i<=(int)1e7;i++)inv[i] = (mod-mod/i)*inv[mod%i]%mod;
	for(int i = 2;i<=(int)1e7;i++){
		dp[i] = (sum*inv[i-1])%mod;
		dp[i] = (1ll*dp[i]+1ll*i*inv[i-1])%mod;
		sum = (sum+1ll*dp[i])%mod;
	} 
 	int T;
	scanf("%d",&T);
	while(T--){
		long long x,q;
		scanf("%d %d",&x,&q);
		printf("%lld\n",dp[q-x+1]);
	}
	return 0;
}
```
# 大模拟
NOIP2015斗地主，遇到大模拟不要害怕，写就行了，代码也就百把行，主要心态要稳。
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
# 区间DP
[glod在奔跑中吃草](http://192.168.110.251/problempage.php?problem_id=2082)
区间DP+记忆化搜索，dp[l][r][0/1]表示已经吃完区间$[l,r]$之后，当前在左边/右边，给全局造成的变质期的和最小。
那么显然有如下转移方程式：
$$dp[l][r][0] = min(dp[l-1][r][0]+dis[l,l-1]*(n-(r-l+1)),dp[l][r+1][0]+dis[r,r+1]*(n-(r-l+1)))$$
代码：
```cpp
# include <iostream>
# include <algorithm>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 1010;
const int INF = 1e9;
int dp[MAXN][MAXN][2];
int pos[MAXN];
int n;
int dfs(int l,int r,int d){
	if(l==1&&r==n)return 0;
	if(dp[l][r][d]!=-1)return dp[l][r][d];
	int ret = INF;
	int p;
	if(d==0)p = l;else p = r;
	if(l!=1){
		ret = min(ret,dfs(l-1,r,0)+(pos[p]-pos[l-1])*(n-1-(r-l)));
	}
	if(r!=n){
		ret = min(ret,dfs(l,r+1,1)+(pos[r+1]-pos[p])*(n-1-(r-l)));
	}
	return dp[l][r][d] = ret;
}
int main(){
	int L;scanf("%d %d",&n,&L);
	for(int i = 1;i<=n;i++)scanf("%d",&pos[i]);
	pos[++n] = L;sort(pos+1,pos+1+n);
	int p;
	for(int i = 1;i<=n;i++)if(pos[i]==L){p = i;break;}
	memset(dp,-1,sizeof(dp));
	printf("%d",dfs(p,p,0));
	return 0;
}
```
# trie
[SCOI背单词](http://192.168.110.251/problempage.php?problem_id=1459)
还是不错的一道题，就是题面太垃圾了，根本不可读。
对于如下三种操作：

 1. s的后缀在s后面加入，代价：n*n
 2. s的后缀在s前面加入，且序号为y
 3. s没有后缀，代价为x
 
对于1、操作，肯定把它的后缀在它之前加入最优。对于4，把它连向0后缀即可。
后缀不好处理，就转换成前缀处理就好了。trie上终止节点向父亲连边。然后从小的子树开始赋点的编号。答案就是$\sum id[x]-id[fa[x]]$
代码：
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
# include <vector>
# include <algorithm>
using namespace std;
const int MAXN = 510010;
const int Segma = 27;
int tree[MAXN][Segma],cnt,val[MAXN],root;
inline int id(char c){return c-'a';}
vector<int> G[510010];
void add(int f,int t){
	G[f].push_back(t);
}
void insert(char *s){
	int len = strlen(s);
	int curr = root;
	for(int i = 0;i<len;i++){
		int idx = id(s[i]);
		if(!tree[curr][idx])tree[curr][idx] = ++cnt;
		curr = tree[curr][idx];
	}
	val[curr] = 1;
}
void dfs(int x,int fa){
	if(val[x])add(fa,x);
	for(int i = 0;i<Segma;i++){
		if(tree[x][i])dfs(tree[x][i],val[x]?x:fa);
	}
}
int sze[MAXN],dfn[MAXN],dfn_cnt = -1;
long long ans;
void dfs2(int x){
	sze[x] = 1;
	for(int i = 0;i<G[x].size();i++){
		int t = G[x][i];
		dfs2(t);
		sze[x]+=sze[t];
	}
}
bool cmp(int x,int y){
	return sze[x]<sze[y];
}
void dfs3(int x,int faId){
	dfn[x] = ++dfn_cnt;
	ans+=1ll*(dfn[x]-faId);
	sort(G[x].begin(),G[x].end(),cmp);
	for(int i = 0;i<G[x].size();i++){
		int t = G[x][i];
		dfs3(t,dfn[x]);
	}
}
char ss[MAXN];
signed main(){
	int n;scanf("%d",&n);
	for(int i = 1;i<=n;i++){
		scanf("%s",ss);reverse(ss,ss+strlen(ss));
		insert(ss);
	}
	dfs(root,0);dfs2(0);dfs3(0,0);
	printf("%d\n",ans);
	return 0;
}
```
# 曼哈顿距离 分治
[bomb](http://192.168.110.251/problempage.php?problem_id=3618# )
对于最大值，我们发现所谓的马哈顿距离的最大，就是一个最大的可以框住三个点的矩形，它可以如下方式产生：
 1.一个点确定了一个xy，另外两个点确定了x和y
 2.一个点确定了一个xy，另外一个点也确定了一个xy，第三个点没什么卵用，但是必须存在。
那么最大值一定是在一下几个点里面产生的:
Xmax+Ymax,-Xmin+Ymax,-Xmin-Ymin,Xmax-Ymin,Xmin,Xmax,Ymin,Ymax .
其实就是吧曼哈顿距离展开来维护，线段树的做法也是同理。
代码中：
```cpp
ansmax = max(ansmax,addmax-xmin-ymin);//三个点确定
ansmax = max(ansmax,xmax+ymax-addmin);//三个点确定
ansmax = max(ansmax,submax-xmin+ymax);//x-y-x'+y'
ansmax = max(ansmax,xmax-ymin-submin);//同上
```
就是做的这件事情。(想出来的人好聪明Orz)
然后对于最小值，参考平面最近点对的做法，直接分治就行，当区间内点数少于15的时候直接跑暴力，然后后面的做法差不多，注意后面有个细节。
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <algorithm>
using namespace std;
const int MAXN = 100010;
struct p{int x,y;bool operator<(const p &p2){return x==p2.x?y<p2.y:x<p2.x;}}ps[MAXN];
p tmp[MAXN];
int ansmin = 0x3f3f3f3f;
int getdis(p *pps,int i,int j,int k){
	return abs(pps[i].x-pps[j].x)+abs(pps[i].x-pps[k].x)+abs(pps[j].x-pps[k].x)+\
	abs(pps[i].y-pps[j].y)+abs(pps[i].y-pps[k].y)+abs(pps[j].y-pps[k].y);
}
int getdis(p &p1,p &p2){return abs(p1.x-p2.x);}
bool cmp(p &p1,p &p2){return p1.y==p2.y?p1.x<p2.x:p1.y<p2.y;}
void solve(int l,int r){
	if(r-l<=15){
		for(int i = l;i<=r;i++)
			for(int j = i+1;j<=r;j++)
				for(int k = j+1;k<=r;k++){
					ansmin = min(ansmin,getdis(ps,i,j,k));
				}
		return;
	}
	int mid = l+r>>1,cnt = 0;solve(l,mid);solve(mid+1,r);
	for(int i = l;i<mid;i++)if(getdis(ps[i],ps[mid])<ansmin)tmp[++cnt] = ps[i];
	for(int i = mid;i<=r;i++)if(getdis(ps[i],ps[mid])<ansmin)tmp[++cnt] = ps[i];
	int rl = 1;
	sort(tmp+1,tmp+cnt+1,cmp);//注意这里要排序
	for(int i = 3;i<=cnt;i++){
		while(abs(tmp[i].y-tmp[rl].y)>=ansmin)rl++;//及时排除不和法的情况
		for(int j = rl;j<=i-1;j++){
			for(int k = j+1;k<=i-1;k++){
				ansmin = min(ansmin,getdis(tmp,i,j,k));
			}
		}
	}
}
int main(){
	int n;scanf("%d",&n);
	int addmin,submin,ansmax,xmin,xmax,ymax,addmax,submax,ymin;
	addmin = submin = ansmin = xmin = ymin = 1<<30;
	addmax = submax = ansmax = xmax = ymax = -1<<30;
	int x,y;
	for(int i = 1;i<=n;i++){
		scanf("%d %d",&x,&y);
		ps[i].x = x,ps[i].y = y;
		addmin = min(addmin,x+y);addmax = max(addmax,x+y);
		submin = min(submin,x-y);submax = max(submax,x-y);
		xmax = max(xmax,x);ymax = max(ymax,y);
		xmin = min(xmin,x);ymin = min(ymin,y);
	}
	ansmax = max(ansmax,addmax-xmin-ymin);ansmax = max(ansmax,xmax+ymax-addmin);
	ansmax = max(ansmax,submax-xmin+ymax);ansmax = max(ansmax,xmax-ymin-submin);
	sort(ps+1,ps+1+n);solve(1,n);
	printf("%d\n%d",ansmax*2,ansmin);
	return 0;
}
```