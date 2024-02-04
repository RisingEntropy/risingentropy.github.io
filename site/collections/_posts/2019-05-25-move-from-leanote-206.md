---
title: 4556woj整除
date: 2019-05-25 15:33:32 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
麦克雷有一个 1→n 的排列，他想知道对于一些区间，有多少对区间内的数（x，y），满足x能被y整除。
输入
第一行包含 2 个正整数 n，m。表示有 n个数，m 个询问。
接下来一行包含n 个正整数，表示麦克雷有的数列。
接下来 m 行每行包含 2 个正整数l，r。表示询问区间[l,r]。
输出
共m 行，每行一个整数，表示满足条件的对数。
样例输入
```
10 9
1 2 3 4 5 6 7 8 9 10
1 10
2 9
3 8
4 7
5 6
2 2
9 10
5 10
4 10
```
样例输出
```
27
14
8
4
2
1
2
7
9
```
提示
30%: 1≤n,m≤100
100%: 1≤n,m≤2∗105,1≤pi≤n
# 解答
难题。我们考虑把所有询问离线，然后以`r`排序，递增，这样来方便回答。然后记`last[i]`为第i个数所有在前面的`因数或者倍数`所在的坐标。然后开始回答每个询问，对于`r端点`为`r`的询问，我们先把它前面所有因数或者倍数统计(用树状数组维护前缀和，修改的时候起始修改点为last[i][j]即前面的i或者j个因数or倍数，因为这样从哪里开始，数对的个数就多了一个)。然后在根据l统计答案。具体就是当前总的数对的个数-从1到l的数对的个数。至于为什么可以这样呢？解释如下：
我们发现这满足区间减法，即[l,r]的答案等于[1,r]-[1,l-1]再减去两个数分别在[1,l-1]和[l,r]的数对的个数，它们的共同点就是数对中的一个数的左边始终在[1,l-1]所以直接区间减掉就好了。这题有点难。~~我智商不够~~
```cpp
# include <iostream>
# include <cstdio>
# include <vector>
using namespace std;
const int MAXN = (int)2e5+10;
struct query{
	int l,r,id;
};
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}
vector<int> last[MAXN];
int sum[MAXN];
int a[MAXN],p[MAXN];
int n,m;
inline int lowbit(int x){return x&-x;}
inline void modify(int x){while(x<=n){sum[x]++;x+=lowbit(x);}}
inline int ask(int x){int ret = 0;while(x>0){ret+=sum[x];x-=lowbit(x);}return ret;}
int ans[MAXN];
vector<query> qs[MAXN];
int main(){
	n = read(),m = read();
	for(int i = 1;i<=n;i++){
		a[i] = read();p[a[i]] = i;
	}
	for(int i = 1;i<=n;i++){
		for(int j = i;j<=n;j+=i){
			if(p[j]<p[i]){//把一个数前面的因数或者倍数标记出来
				last[p[i]].push_back(p[j]);
			}else last[p[j]].push_back(p[i]);
		}
	}
	int l,r;
	for(int i = 1;i<=m;i++){
		l = read(),r = read();qs[r].push_back(query{l,r,i});//离线所有询问
	}
	int cnt = 0;
	for(int i = 1;i<=n;i++){
		for(int j = 0;j<last[i].size();j++){
			cnt++;modify(last[i][j]);//统计[1,r]内所有的数对，从数对的另一个数开始整体加1
		}
		for(int j = 0;j<qs[i].size();j++){
			ans[qs[i][j].id] = cnt-ask(qs[i][j].l-1);//前面说过，直接减掉就好了，这样就包括了左端点在[1,l-1]右端点在[l,r]的情况
		}
	}
	for(int i = 1;i<=m;i++)printf("%d\n",ans[i]);
}
```