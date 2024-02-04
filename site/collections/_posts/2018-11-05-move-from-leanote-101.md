---
title: luoguP2709 小B的询问
date: 2018-11-05 15:36:48 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
小B有一个序列，包含N个1~K之间的整数。他一共有M个询问，每个询问给定一个区间[L..R]，求Sigma(c(i)^2)的值,其中i的值从1到K，其中c(i)表示数字i在[L..R]中的重复次数。小B请你帮助他回答询问。

# 输入输出格式
#  输入格式：
第一行，三个整数N、M、K。

第二行，N个整数，表示小B的序列。

接下来的M行，每行两个整数L、R。

# 输出格式：
M行，每行一个整数，其中第i行的整数表示第i个询问的答案。

# 输入输出样例
#  输入样例# 1： 
```
6 4 3
1 3 2 1 1 3
1 4
2 6
3 5
5 6
```
#  输出样例# 1： 
```
6
9
5
2
```
说明
对于全部的数据，1<=N、M、K<=50000
# 解答
一道莫队算法裸题。对于莫队算法，就是将每个查询离线排序，至于这个排序方法，通常是把它分成$\sqrt n$块，然后在同一块内的的查询按照**右端点**排序(或者按照奇偶排序，暂时用不到，联赛后再来解释)，最后暴力求出第一个查询，然后拓展后面的查询；
注意在移动的时候的l++和++l，不要搞反了。
代码：
```cpp
# include <cstdio>
# include <cstring>
# include <cmath>
# include <algorithm>
using namespace std;
int read(){
	int x = 0,f = 1;
	static char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = (x<<1)+(x<<3)+c-'0';c = getchar();}
	return x*f;
}
const int MAXN = 50010;
int a[MAXN];
int C[MAXN];
int sum;
inline void add(int x){
	sum-=C[a[x]]*C[a[x]];C[a[x]]+=1;sum+=C[a[x]]*C[a[x]];
}
inline void del(int x){
	sum-=C[a[x]]*C[a[x]];C[a[x]]-=1;sum+=C[a[x]]*C[a[x]];
}
struct query{
	int l,r,id,block;
	bool operator<(const query &q1)const{
		return block<q1.block||(block==q1.block&&r<q1.r);
	}
}q[50010];
int ans[50010];
int len;
int main(){
	int n,m;
	n = read(),m = read(), read();
	for(int i = 1;i<=n;i++)a[i]=read();
	len = sqrt(n);
	for(int i = 1;i<=m;i++){
		q[i].l= read();q[i].r = read();
		q[i].block = q[i].l/len+1;
		q[i].id = i;
	}
	sort(q+1,q+m+1);
	int l = q[1].l;
	int r = q[1].l-1;
	for(int i = 1;i<=m;i++){
		while(l<q[i].l)del(l++);
		while(r>q[i].r)del(r--);
		while(l>q[i].l)add(--l);
		while(r<q[i].r)add(++r);
		ans[q[i].id] = sum;
	}
	for(int i = 1;i<=m;i++){
		printf("%d\n",ans[i]);
	}
	return 0;
}
```