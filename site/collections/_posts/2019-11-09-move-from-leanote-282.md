---
title: NOIP2011 观光公交  LOJ加强版 心得
date: 2019-11-09 21:46:05 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

> $O(nlog(n))$的做法真是清奇无比，~~目前已花8h+的时间。。。~~ 9h成功AC
主要是写心得，所以放在归纳总结里

# 题面
风景迷人的小城 $Y$ 市，拥有 $n$  个美丽的景点。由于慕名而来的游客越来越多，$Y$ 市特意安排了一辆观光公交车，为游客提供更便捷的交通服务。观光公交车在第$0$ 分钟出现在 $1$ 号景点，随后依次前往 $ 2、3 、4 ……n $号景点。从第 $i$ 号景点开到第 $i+1$ 号景点需要 $D_i$ 分钟。任意时刻，公交车只能往前开，或在景点处等待。

设共有 $m$ 个游客，每位游客需要乘车$1$ 次从一个景点到达另一个景点，第 $i$ 位游客在 $T_i$ 分钟来到景点 $A_i$ ，希望乘车前往景点 $B_i$ （$A_i<B_i$）。为了使所有乘客都能顺利到达目的地，公交车在每站都必须等待需要从该景点出发的所有乘客都上车后才能出发开往下一景点。

假设乘客上下车不需要时间。

一个乘客的旅行时间，等于他到达目的地的时刻减去他来到出发地的时刻。因为只有一辆观光车，有时候还要停下来等其他乘客，乘客们纷纷抱怨旅行时间太长了。于是聪明的司机ZZ给公交车安装了 $k$ 个氮气加速器，每使用一个加速器，可以使其中一个 $D_i$ 减 $1$ 。对于同一个 $D_i$ 可以重复使用加速器，但是必须保证使用后 $D_i$ 大于等于 $0$ 。

那么ZZ该如何安排使用加速器，才能使所有乘客的旅行时间总和最小？

<font color ="red">对于 $100\%$ 的数据，$n，m\le 10^5，k\le5\times10^6，D_i\le1000。$ </font>

-----------------
# 开题
拿到题后有一个“显而易见”的贪心：一条道路不能加速次数过多而导致车等人，所以加速有一个范围，同时每次加速选择一条人数最多的路（我知道这个东西错的很凶）
所以线段树区间修改，区间查询最大值，同时把过短的边赋为$- \infty$
复杂度$O(klog(n))$。~~美滋滋~~
然后我就挂了
#  错因一：
**不考虑一条边会对后面连续的一些边产生影响**
也就是说区间查询最大值不是最优的决策了
也就是说我要开始推公式了

分析后可得

$$ans=\sum_{i=2}^nTim_i*cnt_i-\sum T_i$$

这个式子很重要也很有用！
其中$Tim_i$表示公交车到达第$i$号景点的时间，$cnt_i$表示在$i$景点下车的人数

显然的，如果我们设$Begin_i$为从$i$号景点发车的时间，那么有

$$Tim_i=Begin_{i-1}+D_{i-1}$$

所以分析一波$Begin$的式子
首先我们设$i$号景点最晚到的旅客的时间为$Maxn_i$
$$Begin_i=max\left(Maxn_i,Begin_{i-1}+D_{i-1} \right)$$
发现这是一个递推式，尝试把它拆开

$$
Begin_i=max\left(Maxn_i,max(Maxn_{i-1}+D_{i-1},Begin_{i-2}+D_{i-2}+D_{i-1})\right)
$$

像这样一直拆下去，就得到了这样一个奇妙的式子
$$
Begin_i=max\left(Maxn_i,\underset{1\le j<i}{max}\begin{Bmatrix}Maxn_j+D_{j\to i}\end{Bmatrix}\right)
$$
把$D_{j\to i}$拆成前缀和形式$pre_i-pre_j$,再稍稍变一下形，就有：

$$
Begin_i=max\left(Maxn_i,\underset{1\le j<i}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}+pre_i\right)\\
=max\left(Maxn_i-pre_i,\underset{1\le j<i}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}\right)+pre_i
$$

合并后完成变形：
$$
Begin_i=\underset{1\le j\le i}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}+pre_i
$$
这时再回过头来看答案，可以推一波
$$
\sum_{i=2}^nTim_i*cnt_i-\sum T_i\\
=\sum_{i=2}^n(Begin_{i-1}+D_{i-1})*cnt_i-\sum T_i\\
=\sum_{i=2}^n\left(\underset{1\le j\le i-1}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}+pre_{i-1}+D_{i-1}\right)*cnt_i-\sum T_i
$$
$pre_{i-1}+D_{i-1}$就是$pre_i$，那么我们就维护一下${max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}$就好了，线段树解决

至此脑子烧糊，想不出怎么贪心了
于是去瞟了网上唯一一份题解，豁然开朗

设$S_i$表示景点$i$公交到达时间和游客最晚时间之差，显然如果$S_i>0$就有提速的余地
于是推一波这个东西

$$
S_i=Tim_i-Maxn_i\\
=Begin_{i-1}+D_{i-1}-Maxn_i\\
=\underset{1\le j\le i-1}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}+pre_{i-1}+D_{i-1}-Maxn_i\\
=\underset{1\le j\le i-1}{max}\begin{Bmatrix}Maxn_j-pre_j\end{Bmatrix}-(Maxn_i-pre_i)
$$

通俗点讲，如果$i$号点前面有比它小的点，那么那个点可以对$i$号点产生影响
那么现在就很清楚了：一个点能影响后面连续一段比它小的点，一个点是否优秀取决于它区间内除它以外的点的$cnt$总和（因为减小$1$的权值就减小了$\sum\limits_{i=l+1}^rcnt_i$的答案）
所以把所有区间丢进堆里，权值为$\sum cnt$

现在考虑修改答案（我要吐了md）
如果我们修改$D_i$，它会让它后面所有的$pre$减小，也就是在线段树上的区间加操作，同时在$k>0$不断加速的过程中，总会有一个点与左端点一样大，那么就分割区间，由于最多操作$2n$个区间，总复杂度$O(nlog(n))$。~~美滋滋~~
然后我又挂了
#  错因二：
**没有考虑$D_i$减成负数的情况**
此时$D_i=0$，区间变成$l+1\to r$
艹
完成以上工作LOJ 60分（黑线）
#  错因三：
**没有考虑$cnt_{r+1}$对区间l~r的贡献**
用人话就是：如果公交可能提前到站，仍会产生贡献，因为会有人在这一站下车，所以说区间最小长度为1

可是怎么还是60分？

#  错因四：
**处理$D_i\to 0$的过程有锅**
不知道读者发现没有
因为是让区间左端点最大，而上面的过程显然没有保证。
不慌，分析一下$S_i$的式子，可以知道需要存一个旧区间的“左端点”值，与当前左端点值取$max$（相当于旧左端点仍然管辖，只是不能直接减小$D_i$了）

还是60分，心态有点小崩

#  错因五
mmp wtcl
不能直接存旧左端点值，因为可能这个值会被修改
所以我们存旧左端点的位置，取$max$时查询一下就好了
至此收获$\color{green}{Accepted}$
附上最终代码
```
# include<bits/stdc++.h>
using namespace std;
inline char nc(){
	static char buf[100000],*p1=buf,*p2=buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
//# define nc getchar
inline int read(){
	int x=0,f=1;
	char ch=nc();
	for(;!isdigit(ch);ch=nc())if(ch=='-')f=-1;
	while(isdigit(ch)){x=(x<<1)+(x<<3)+(ch^48);ch=nc();}
	return x*f;
}
typedef long long ll;
const int N=1e5+3;
struct tree{
	int l,r;
	long long maxn,maxpos,lazy;
	inline tree friend operator +(tree l,tree r){
		tree ret={0,0,0,0,0};ret.l=l.l;ret.r=r.r;
		if(l.maxn>=r.maxn)ret.maxpos=l.maxpos;
		else ret.maxpos=r.maxpos;
		ret.maxn=max(l.maxn,r.maxn);return ret;
	}
}t[N<<2];
int cnt[N],maxn[N],sum[N],pre[N],d[N];
//# define lim(i) (maxn[i+1]-maxn[i])
struct tour{
	int tim,l,r;
}p[N*10];
inline bool cmp(tour a,tour b){
	if(a.l==b.l)return a.tim<b.tim;
	return a.l<b.l;
}
int n,m,k;ll T;
# define lc (p<<1)
# define rc ((p<<1)|1)
inline void pushup(int p){
	if(t[lc].maxn>=t[rc].maxn)t[p].maxpos=t[lc].maxpos;
	else t[p].maxpos=t[rc].maxpos;
	t[p].maxn=max(t[lc].maxn,t[rc].maxn);
}
inline void pushnow(int p,int w){
	t[p].maxn+=w;t[p].lazy+=w;
}
inline void pushdown(int p){
	if(t[p].lazy!=0){
		pushnow(lc,t[p].lazy);pushnow(rc,t[p].lazy);t[p].lazy=0;
	}
}
void build(int p,int l,int r){
	t[p].l=l;t[p].r=r;t[p].lazy=0;
	if(l==r){t[p].maxn=maxn[l]-pre[l],t[p].maxpos=l;return;}
	int mid=(l+r)>>1;
	build(lc,l,mid);build(rc,mid+1,r);
	pushup(p);
}
void lmy(int p,int pl,int pr,int w){
	int l=t[p].l,r=t[p].r;
	if(pl<=l&&r<=pr){pushnow(p,w);return;}
	int mid=(l+r)>>1;pushdown(p);
	if(pl<=mid)lmy(lc,pl,pr,w);
	if(pr>mid)lmy(rc,pl,pr,w);
	pushup(p);
}
tree glf(int p,int pl,int pr){
	int l=t[p].l,r=t[p].r;
	if(pl<=l&&r<=pr){return t[p];}
	pushdown(p);int mid=(l+r)>>1;
	if(pl<=mid&&pr>mid)return glf(lc,pl,pr)+glf(rc,pl,pr);
	else if(pl<=mid)return glf(lc,pl,pr);
	else return glf(rc,pl,pr);
}
struct segment{
	int l,r;ll sum, vis;
	segment(int _l=0,int _r=0,ll _sum=0,ll _vis=0):l(_l),r(_r),sum(_sum),vis(_vis){}
	const bool operator <(const segment &b)const{
		return sum<b.sum;
	}
};
priority_queue<segment>q;

int main(){
	n=read();m=read();k=read();
	for(int i=1;i<n;i++)d[i]=read(),pre[i+1]=pre[i]+d[i];
	for(int i=1;i<=m;i++){
		p[i].tim=read();p[i].l=read();p[i].r=read();T+=p[i].tim;
		maxn[p[i].l]=max(maxn[p[i].l],p[i].tim);cnt[p[i].r]++;
	}
	build(1,1,n);
	for(int i=1;i<=n+1;i++)sum[i]=sum[i-1]+cnt[i];
	for(int i=2,last=1,lastval=maxn[1]-pre[1];i<=n;i++){
		if(maxn[i]-pre[i]>=lastval)q.push(segment(last,i-1,sum[i]-sum[last],last)),last=i,lastval=maxn[i]-pre[i];
		if(i==n&&last!=n)q.push(segment(last,i,sum[i]-sum[last],last));
	}
	while(k&&!q.empty()){
		segment now=q.top();q.pop();
		if(now.l==now.r){
			if(k<=d[now.l])lmy(1,now.l+1,n,k),d[now.l]-=k,k=0;
			else k-=d[now.l],lmy(1,now.l+1,n,d[now.l]),d[now.l]=0;
			continue;
		}
		int x=glf(1,now.l+1,now.r).maxn,lmaxn=max(glf(1,now.l,now.l).maxn,glf(1,now.vis,now.vis).maxn);
		if(k<=min(d[now.l],lmaxn-x)){lmy(1,now.l+1,n,k);d[now.l]-=k;k=0;}
		else{
			if(lmaxn-x>=d[now.l]){
				lmy(1,now.l+1,n,d[now.l]);k-=d[now.l];d[now.l]=0;
				if(now.l+1>now.r)continue;
				if(now.l+1<=now.r)q.push(segment(now.l+1,now.r,sum[now.r+1]-sum[now.l+1],now.vis));
			}else{
				lmy(1,now.l+1,n,lmaxn-x);k-=lmaxn-x;d[now.l]-=lmaxn-x;
				if(now.l+1>now.r)continue;
				int pos=0;
				pos=glf(1,now.l+1,now.r).maxpos;
				if(now.l<=pos-1)q.push(segment(now.l,pos-1,sum[pos]-sum[now.l],now.vis));
				if(pos<=now.r)q.push(segment(pos,now.r,sum[now.r+1]-sum[pos],pos));
			}
			
		}
	}
	for(int i=1;i<n;i++)pre[i+1]=pre[i]+d[i];
	ll ans=-T;
	for(int i=2;i<=n;i++)ans+=cnt[i]*(glf(1,1,i-1).maxn+pre[i]);
	printf("%lld",ans);
	return 0;
}
```


$\color{orange}{FIN}$


