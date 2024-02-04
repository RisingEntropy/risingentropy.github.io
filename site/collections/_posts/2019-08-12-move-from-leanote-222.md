---
title: 【线段树】luoguP3960
date: 2019-08-12 22:50:46 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
`Sylvia` 是一个热爱学习的女孩子。

前段时间， `Sylvia` 参加了学校的军训。众所周知，军训的时候需要站方阵。 `Sylvia` 所在的方阵中有$n × m$名学生，方阵的行数为 $n$，列数为 $m$。

为了便于管理，教官在训练开始时，按照从前到后，从左到右的顺序给方阵中 的学生从$ 1 $到$ n × m $编上了号码（参见后面的样例）。即：初始时，第 $i $行第$ j $列 的学生的编号是$(i − 1) × m + j$。

然而在练习方阵的时候，经常会有学生因为各种各样的事情需要离队。在一天 中，一共发生了 $q$ 件这样的离队事件。每一次离队事件可以用数对$(x , y) (1≤x≤n, 1≤y≤m)$描述， 表示第 x 行第 y 列的学生离队。

在有学生离队后，队伍中出现了一个空位。为了队伍的整齐，教官会依次下达 这样的两条指令：

向左看齐。这时第一列保持不动，所有学生向左填补空缺。不难发现在这条 指令之后，空位在第 $x$ 行第 $m$ 列。

向前看齐。这时第一行保持不动，所有学生向前填补空缺。不难发现在这条 指令之后，空位在第$ n $行第 $m$ 列。

教官规定不能有两个或更多学生同时离队。即在前一个离队的学生归队之后， 下一个学生才能离队。因此在每一个离队的学生要归队时，队伍中有且仅有第 $n $行 第$ m$ 列一个空位，这时这个学生会自然地填补到这个位置。

因为站方阵真的很无聊，所以 $Sylvia$ 想要计算每一次离队事件中，离队的同学 的编号是多少。

注意：每一个同学的编号不会随着离队事件的发生而改变，在发生离队事件后 方阵中同学的编号可能是乱序的。

输入
输入共 $q+1$ 行。
第$ 1$ 行包含 3 个用空格分隔的正整数 $n, m, q$，表示方阵大小是$ n $行 $m$ 列，一共发生了 $q$ 次事件。
接下来 $q$ 行按照事件发生顺序描述了 $q$ 件事件。每一行是两个整数 $x, y$， 用一个空 格分隔， 表示这个离队事件中离队的学生当时排在第 $x$ 行第$ y $列
输出
按照事件输入的顺序，每一个事件输出一行一个整数，表示这个离队事件中离队学 生的编号。
样例输入
```
2 2 3
1 1
2 2
1 2
```
样例输出
```
1
1
4
```
# 解答
很不错额一道线段树的好题，前两天才学了线段树分治以及动态开点的线段树，刚好来写一下这道题。听大佬们说可以`splay`水过，但是我太弱了，太久没有写`spay`这种一写一下午的东西了。我们建立$n+1$个线段树，分别维护$n$行及最后一列。每次操作就从相应的一行中找到第y个数，如果第y个数的下标大雨了了n，说明已经出去了超过那么多人了，只有从那个节点所代表的的vector里面找出$pos-m$个数，对于最后一列，同样使用一个vector维护，查询的时候如果线段树里面的人数已经少于要查询的人数了，就从vector里面取那么多个人粗来就好啦。
代码
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <vector>
using namespace std;
const int MAXN = (int)3e5+10;
int tree[MAXN*20][2],sum[MAXN*20],cnt,root[MAXN];
int pos;
int n,m,q,mx;
vector<long long> v[MAXN*20];
int query(int k,int l,int r,int w){
	if(l==r){return l;}
	int mid = l+r>>1;int tmp = mid-l+1-sum[tree[k][0]];
	if(tmp>=w)return query(tree[k][0],l,mid,w);
	else return query(tree[k][1],mid+1,r,w-tmp);
}
void modify(int &k,int l,int r,int pos){
	if(!k)k = ++cnt;
	sum[k]++;
	if(l==r)return;
	int mid = l+r>>1;
	if(pos<=mid)modify(tree[k][0],l,mid,pos);
	else modify(tree[k][1],mid+1,r,pos);
}
long long work1(int x,long long y){
	pos = query(root[n+1],1,mx,x);
	modify(root[n+1],1,mx,pos);
	long long ans = pos<=n?(long long)pos*m:v[n+1][pos-1-n];
	v[n+1].push_back(y?y:ans);
	return ans;
}
long long work2(int x,int y){
	pos = query(root[x],1,mx,y);
	modify(root[x],1,mx,pos);
	long long ans = pos<m?(long long)(x-1)*m+pos:v[x][pos-m];
	v[x].push_back(	work1(x,ans));
	return ans;
}
int main(){
	scanf("%d%d%d",&n,&m,&q);
	mx = max(m,n)+q;
	int x,y;
	while(q--){
		scanf("%d%d",&x,&y);
		if(y==m)printf("%lld\n",work1(x,0));
		else printf("%lld\n",work2(x,y));
	}
	return 0;
}
```