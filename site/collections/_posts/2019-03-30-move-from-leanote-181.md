---
title: 20190330考试
date: 2019-03-30 16:19:41 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# T1重置序reset
一个芯片可以有N种不同的状态，不妨设为0到N-1。其中，0状态是准备状态。当芯片出现错误时，可能会处于任意状态。因此需要一个重置序列来将它变成准备状态。你的任务就是寻找这个重置序列。
当芯片处于状态i时接收了命令j，它会立刻转变成状态d[i,j]。对于任意初始状态，你找到的重置序列都应最终将它变成准备状态。在此基础上，你找到的重置序列应该最短。
#  输入
第一行两个整数$n,m（2<=n<=8，1<=m<=16）$，表示状态数和命令数。
接下来n行每行m个整数，表示状态i在接收到命令j时会变成状态d[i,j]。注意，状态和命令都是从0开始编号的。其中，0是唯一一个准备状态。保证$0<=d[i,j]<n$。
#  输出
输出一个序列表示最短操作序列。用16进制数来表示操作$(0-9,a-f)$。数码之间、行尾都不应有多余字符。如果有多组解，输出字典序最小的一组。如果无解，输出-1。
样例输入
```
3 4
2 1 1 2
1 0 0 0
0 0 0 1
```
样例输出
```
101
```
提示
【样例说明】
三种状态都会通过这个序列最终变成状态0：
0->1->1->0
1->0->2->0
2->0->2->0
算是状态压缩dp吧。。。观察发现n的范围非常小，我们用一个整数作为状态，状态里面每个位表示芯片状态是否存在。然后就考虑转移，我们枚举转移，又由于字典序最小，直接bfs就好了。初始状态为$(1<<n)-1$目标状态$1$，因为只剩一个0状态了，也就是0位上为1。
代码：
```cpp
# include <iostream>
# include <cstdio>
# include <queue>
# include <vector>
using namespace std;
const int N = 10,S = 1<<16;
int q[S],op[S],fa[S],G[N][N*2],front,tail,f[S];
int n,m;
void print(int x){
	if(op[x]==-1)return;
	print(fa[x]);
	printf("%x",op[x]);
}
int bfs(int s){
	f[s] = 1;
	front = tail = 1;
	op[tail] = -1;fa[tail] = 0;
	q[tail++] = s;
	while(tail!=front){
		int t = q[front];
		if(t==1)return front;
		for(int i = 0;i<m;i++){
			int x = 0;
			for(int j = 0;j<n;j++){
				if(t&(1<<j))x|=1<<G[j][i];
			}
			if(x&&!f[x]){
				f[x] = 1;
				q[tail] = x;
				fa[tail] = front;
				op[tail] = i;
				tail++;
			}
		}
		front++;
	}
	return 0;
}
int main(){
	cin>>n>>m;
	for(int i = 0;i<n;i++)
		for(int j = 0;j<m;j++)
			cin>>G[i][j];
	int ans = bfs((1<<n)-1);
	if(ans)print(ans);else cout<<-1<<endl;
	return 0;
}
```

# T2
你的防线成功升级，从原来的一根线变成了一棵树。这棵树有 N 个炮台，炮台与炮台之间 有 N-1 条隧道。你要选择一些炮台安装哨戒炮。在第 i 个炮台上安装哨戒炮得到的防御力为 vi。上次说过，哨戒炮离得太近会产生神奇的效果。具体来说，对于炮台 i，如果它安装了 哨戒炮且和 k 个哨戒炮用隧道直接相连，那么其防御力会变化 k*di。其中 di 为炮台 i 的抗 干扰属性值。如果为正，干扰对其有正的作用；为负，干扰对其有负的作用；为 0，则完全 不受干扰。
你的整套防线的防御力为所有哨戒炮的防御力之和。求防线的最大防御力
#  输入
第一行一个整数 N，表示炮台数量。
第二行 N 个整数表示 vi。
第三行 N 个整数表示 di。
接下来 N-1 行每行两个整数描述一条隧道。
#  输出
输出一行一个整数表示答案
样例输入
```
2
1 1
0 0
1 2
```
样例输出
```
2
```
提示
对于 20%的数据，$N <= 20$。
对于 40%的数据，$N <= 100$。
对于 70%的数据，$N <= 5000$。
对于 100%的数据，$N <= 100000$
最水的一道题，树形dp，但是注意long long ，不开long Long 只有10分，见祖宗
```cpp
# include <cstdio>
const int MAXN = 100010;
struct edge{int t,next;}edges[MAXN<<2];
int head[MAXN],top;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
long long max(long long a,long long b){return a>b?a:b;}
long long dp[MAXN][2];
long long v[MAXN],d[MAXN];
void dfs(int x,int fa){
	dp[x][1] = v[x];dp[x][0] = 0;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		if(t==fa)continue;
		dfs(t,x);
		dp[x][1] += max(dp[t][0],d[t]+d[x]+dp[t][1]);
		dp[x][0] += max(dp[t][0],dp[t][1]);
	}
}
int main(){
	int n;scanf("%d",&n);
	for(int i = 1;i<=n;i++)scanf("%lld",&v[i]);
	for(int i = 1;i<=n;i++)scanf("%lld",&d[i]);
	int f,t;
	for(int i = 1;i<n;i++){
		scanf("%d %d",&f,&t);
		add(f,t);add(t,f);
	}
	dfs(1,0);
	printf("%lld",max(dp[1][1],dp[1][0]));
	return 0;
}
```
# T3里程表
Farmer John's cows are on a road trip! The odometer on their car displays an integer mileage value, starting at X (100 <= X <= 10^18) miles at the beginning of their trip and ending at Y (X <= Y <= 10^18) miles at the end of their trip. Whenever the odometer displays an 'interesting' number (including at the start and end of the trip) the cows will moo. A number is 'interesting' if when you look at all its digits except for leading zeros, at least half of these should be the same. For example, the numbers 3223 and 110 are interesting, while the numbers 97791 and 123 are not.
Help FJ count how many times the cows will moo during the trip.
农民约翰的牛正开始一个美妙的旅程。牛车的里程表上显示一个整数表示里程，旅程开始时里程数为$X(100 <= X <= 10^18)$，结束时里程数为$Y(X <= Y <= 10^18)$。每当里程表显示一个有趣的数时（包括起点和终点数），牛们会发出愉快的叫声。
对于一个里程数的每一位，如果有至少一半的数字时相同的，则这个里程数一个有趣的数。例如：3223和110是有趣的数，而$97791$ 和 $123$则不是。
请计算，整个旅程中，牛们会发出多少吃愉快的叫声。
输入
Line 1: The first line will contain two integers, X and Y, separated by a space.
输出
Line 1: A single integer containing how many times the cows will moo during the trip.
样例输入
```
110 133
```
样例输出
```
14
```
提示
The trip starts with the odometer at 110 and ends at 133.
The cows moo when the odometer reads 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 131, and 133.
标签
USACO2014 US Open, Silver
数位dp，第一次计算出1-9每个数字出现次数超过一半的数的个数，再求出2个数各占一半的数的个数，然后一减就好了。
代码：
```cpp
# include <iostream>
# include <cstring>
using namespace std;
long long dp[20][20][20][20];
long long dp2[20][20][20][20];
int nm[20];
long long dfs1(int pos,int num,int cnt,int len,bool lead,bool limit){
	if(pos==0){return cnt*2>=len;}
	if(!lead&&!limit&&dp[pos][num][cnt][len]!=-1)return dp[pos][num][cnt][len];
	long long ans = 0;int mx = limit?nm[pos]:9;
	for(int i = 0;i<=mx;i++){
		ans+=dfs1(pos-1,num,cnt+(i==num&&(!lead||i!=0)),len-(lead&&i==0),i==0&&lead,limit&&i==mx);
	}
	if(!lead&&!limit)dp[pos][num][cnt][len] = ans;
	return ans;
}
long long dfs2(int pos,int num1,int num2,int cnt1,int cnt2,int len,int lead,int limit){
	if(pos==0)return cnt1*2==len&&cnt1==cnt2;
	if(!lead&&!limit&&dp2[pos][cnt1][cnt2][len]!=-1)return dp2[pos][cnt1][cnt2][len];
	long long ans = 0;int mx = limit?nm[pos]:9;
	if(lead)ans+=dfs2(pos-1,num1,num2,cnt1,cnt2,len-1,true,false);
	if(num1<=mx&&(num1!=0||!lead))ans+=dfs2(pos-1,num1,num2,cnt1+1,cnt2,len,false,limit&&num1==mx);
	if(num2<=mx&&(num2!=0||!lead))ans+=dfs2(pos-1,num1,num2,cnt1,cnt2+1,len,false,limit&&num2==mx);
	if(!lead&&!limit)dp2[pos][cnt1][cnt2][len] = ans;
	return ans;
}
long long work(long long x){
	long long ans = 0;
	int len = 0;
	while(x){
		nm[++len] = x%10;x/=10;
	}
	for(int i = 0;i<=9;i++)ans+=dfs1(len,i,0,len,true,true);
	for(int i = 0;i<=9;i++)
		for(int j = i+1;j<=9;j++)
			memset(dp2,-1,sizeof(dp2)),ans-=dfs2(len,i,j,0,0,len,true,true);
	return ans;
}
int main(){
	long long l,r;
	memset(dp,-1,sizeof(dp));
	memset(dp2,-1,sizeof(dp2));
	cin>>l>>r;
	cout<<work(r)-work(l-1);
	return 0;
}
```