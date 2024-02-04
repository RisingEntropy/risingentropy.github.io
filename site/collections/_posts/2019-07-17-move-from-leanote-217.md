---
title: 【线段树+合并位】
date: 2019-07-17 11:32:07 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
构造一个长度为n的非负整数序列x，满足m个条件，第i个条件为x[li]|x[li+1]|…|x[ri]=pi。
#  输入
第一行两个整数n,m。接下来m行每行三个整数li,ri,pi。
#  输出
如果存在这样的序列x，第一行输出Yes，第二行输出n个不超过2^30-1的非负整数表示x[1]~x[n]，否则输出一行No。
#  样例输入 
````
2 1
1 2 1
```
#  样例输出
```
Yes
1 1
```
提示
对于30%的数据，n,m<=1000。
对于另外30%的数据，pi<=1。
对于100%的数据，n,m<=100000，1<=li<=ri<=n，0<=pi<2^30。
标签
洛谷2017八连测R2
# 解答
首先按照套路，可以想到建立31颗线段树，但是这样子带个31的大常数，复杂度直逼$O(nlog^2n)$但似乎测评机跑得快，可以切。但是想到31颗线段树的做法之后，可以考虑如何优化。我们发现每一位之间是独立的，也就是说，我们可以把一颗线段树合并起来，并且借用位之间的联系，方便各种区间查询和修改。
然后我们发现要是对区间内某些数的每一位进行修改，就只需要或上p就行了，那么接下来我们考虑如何进行标记合并，我们发现如果遇上一下情况
$$\ \ \ \ 1010111$$
$$|\ \ \ \ 1010101$$
$$------------------$$
这样的标记怎么办呢？虽然它们是矛盾的，但是我们暂时不管矛盾的地方，要想把这两个p的信息全部传递下来，也就是所有的0都要传递下来，我们必须使用与运算，这样就可以把信息全部传递下来了。最后由于在传递信息的时候没有考虑是否矛盾的情况，所以我们需要$O(nlogn)$地判断一次是否矛盾。总复杂度$O(NlogN)$
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 123333;
int n,m;
struct node{int v,tag;}tree[MAXN<<2];
void pushup(int k){tree[k].v = tree[k<<1].v|tree[k<<1|1].v;}
void work(int k,int v){tree[k].v&=v;}
void pushdown(int k){work(k<<1,tree[k].v);work(k<<1|1,tree[k].v);}
void build(int k,int l,int r){
	if(l==r){tree[k].v = (1<<30)-1;return;}
	int mid = l+r>>1;
	build(k<<1,l,mid);build(k<<1|1,mid+1,r);
	pushup(k);
}
void modify(int k,int l,int r,int x,int y,int v){
	if(l>=x&&r<=y){tree[k].v&=v;return;}
	pushdown(k);
	int mid = l+r>>1;
	if(x<=mid)modify(k<<1,l,mid,x,y,v);
	if(y>mid)modify(k<<1|1,mid+1,r,x,y,v);
	pushup(k);
}
int query(int k,int l,int r,int x,int y){
	if(l>=x&&r<=y)return tree[k].v;
	int mid = l+r>>1;
	int res = 0;
	pushdown(k);
	if(x<=mid)res=query(k<<1,l,mid,x,y);
	if(y>mid)res|=query(k<<1|1,mid+1,r,x,y);
	return res;
}
int li[MAXN],ri[MAXN],qi[MAXN];
int res[MAXN];
int main(){
	int n,m;cin>>n>>m;
	build(1,1,n);
	for(int i = 1;i<=m;i++){
		cin>>li[i]>>ri[i]>>qi[i];
		modify(1,1,n,li[i],ri[i],qi[i]);
	}
	bool flag = true;
	for(int i = 1;i<=m;i++){
		int tmp = query(1,1,n,li[i],ri[i]);
		if(tmp!=qi[i]){
			flag = false;break;
		}
	}
	if(flag==false){
		cout<<"No";return 0;
	}
	cout<<"Yes"<<endl;
	for(int i = 1;i<=n;i++)cout<<query(1,1,n,i,i)<<' ';
	return 0;
}
```