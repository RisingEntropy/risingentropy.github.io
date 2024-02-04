---
title: unknown title
date: 2019-10-03 16:23:27 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 测试
#  T1
求由 1 到 n 一共 n 个数字组成的所有排列中，逆序对个数为 k 的有多少个
# 解答
动态规划：
dp[i][j]表示长度为i，逆序对个数为j的方案数，那么有如下转移：
$dp[i][j] = dp[i-1][j]+\sum dp[i-1][k](1\le k<i)$
然后对于后面那一坨，做一个前缀和优化。但是要注意一点，就是j的范围，因为我们在枚举的时候，逆序对的上界是一个$min(\frac{i*(i-1)}{2},k)$，但是当逆序对的上界较小的时候，在维护逆序对的时候更新不到后面去，导致后面转移的时候前缀和为0，所以干脆上界就直接设为k好了。
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 2010;
const int mod = 10000;
int dp[MAXN][MAXN];
int sum[MAXN][MAXN];
void file(){
	freopen("permut.in","r",stdin);
	freopen("permut.out","w",stdout);
}
int main(){
//	file();
	int T;scanf("%d",&T);
	while(T--){
		memset(sum,0,sizeof(sum));
		memset(dp,0,sizeof(dp));
		int n,k;scanf("%d%d",&n,&k);
		dp[1][0]=1;for(int i=0;i<=k;i++)sum[1][i]=1;
		for(int i = 2;i<=n;i++){
			dp[i][0] = 1;sum[i][0] = 1;
			for(int j = 1;j<=k;j++){
				dp[i][j] = sum[i-1][j];
				if(j-i>=0)dp[i][j] = (dp[i][j]-sum[i-1][j-i]+mod)%mod;//对于j<i的情况，前缀和不需要减
				sum[i][j] = (sum[i][j-1]+dp[i][j])%mod;
			}
		}
		printf("%d\n",dp[n][k]);
	}
	return 0;
}
```
# T2
一个长度为 n 的序列，对于每个位置 i 的数 ai 都有一个优美值，其定义是：找到序列中最 长的一段 [l, r]，满足 l ≤ i ≤ r，且 [l, r] 中位数为 ai（我们比较序列中两个位置的数的大小时， 以数值为第一关键字，下标为第二关键字比较。这样的话 [l, r] 的长度只有可能是奇数），r - l+ 1 就是 i 的优美值。
接下来有 Q 个询问，每个询问 [l, r] 表示查询区间 [l, r] 内优美值的最大值。
# 解答
这是一个做法很巧妙的题。枚举每一个数，然后分别从左往右和从右往左扫描，然后如果遇到大于它的数，就S++，否则就S--，然后这样子对于每一个位置都可以得到一个S，把它作为每个点的权值，然后对于这个权值可以得到一个长度。左右都做一便，然后再枚举每一个权值，如果存在左边是x，右边也存在-x，那么就尝试更新这个点的答案。重点想一下这个权值的作用，其实就是第K大的意思
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN  = 2010;
int L[MAXN*2],R[MAXN*2],a[MAXN],v[MAXN];
int n;
void init(){
	int cnt = 0;
	for(int i = 1;i<=n;i++){
		cnt = 0;
		memset(L,255,sizeof(L));memset(R,255,sizeof(R)); 
		L[n] = R[n] = 0; 
		for(int j = i-1;j>=1;j--){
			if(a[j]>a[i])cnt++;
			else cnt--;
			L[n+cnt] = i-j;
		}
		cnt = 0;
		for(int j = i+1;j<=n;j++){
			if(a[j]>=a[i])cnt++;
			else cnt--;
			R[n+cnt] = j-i;
		}
		for(int j = 1-i;j<=i-1;j++){
			if(L[n+j]>=0&&R[n-j]>=0){
				v[i] = max(v[i],L[n+j]+1+R[n-j]);
			}
		}
	}
} 
struct node{int mx;}tree[MAXN<<2];
void pushup(int k){tree[k].mx = max(tree[k<<1].mx,tree[k<<1|1].mx);}
void build(int k,int l,int r){
	if(l==r){
		tree[k].mx = v[l];return;
	}	
	int mid = l+r>>1;
	build(k<<1,l,mid);build(k<<1|1,mid+1,r);
	pushup(k);
}
int query(int k,int l,int r,int x,int y){
	if(l>=x&&r<=y)return tree[k].mx;
	int mid = l+r>>1,ret = 0;
	if(x<=mid)ret = query(k<<1,l,mid,x,y);
	if(y>mid)ret = max(ret,query(k<<1|1,mid+1,r,x,y));
	return ret;
}
int main(){
	scanf("%d",&n);
	for(int i = 1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	init();build(1,1,n);
	int q;scanf("%d",&q);
	while(q--){
		int l,r;
		scanf("%d %d",&l,&r);
		printf("%d\n",query(1,1,n,l,r));
	}
	return 0;
}
```
# T3
一开始你有一个空集，集合可以出现重复元素，然后有 Q 个操作
add s
在集合中加入数字 s。
del s
在集合中删除数字 s。保证 s 存在
cnt s
查询满足 a&s = a 条件的 a 的个数
# 解答
设dp[S1][S2]表示高8位为S1，低8位为S2的数有多少个，就是拆位的思想。
维护f[pre][suf],表示满足k1&pre=k1中suf=k2的个数，加入a时更新满足条件的区间，查询s时，先找到s的前缀pre1,由以上性质可得a[pre1]中所有a 的前半段都满足,这时只需在此区间中循环查找suf满足的个数即可。
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 1000;
int dp[MAXN][MAXN];
char c[MAXN];
int main(){
	int q,v;scanf("%d",&q);
	while(q--){
		scanf("%s",c);
		if(c[0]=='a'){
			scanf("%d",&v);
			int hi = v>>8,lo = v&255,cmp = 255^lo;
			dp[hi][lo]+=1;
			for(int y = cmp;y!=0;y = (y-1)&cmp){
				dp[hi][y|lo]+=1;
			}	
		}else if(c[0]=='c'){
			scanf("%d",&v);
			int ans = 0;
			int hi = v>>8,lo = v&255,cmp = 255^lo;
			ans = dp[0][lo];
			for(int y = hi;y!=0;y = (y-1)&hi){
				ans+=dp[y][lo];
			}
			printf("%d\n",ans);
		}else{
			scanf("%d",&v);
			int hi = v>>8,lo = v&255,cmp = 255^lo;
			dp[hi][lo]-=1;
			for(int y = cmp;y!=0;y = (y-1)&cmp){
				dp[hi][y|lo]-=1;
			}	
		}
	}
	return 0;
}
```
其实暴力也能艹过去