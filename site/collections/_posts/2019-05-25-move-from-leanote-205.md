---
title: 20190525考试
date: 2019-05-25 15:12:27 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 考试
不干啦，爆零啦！
# T1选数问题
在麦克雷的面前有N 个数，以及一个 R∗C 的矩阵。现在他的任务是从N 个数中取出R∗C 个，并填入这个矩阵中。矩阵每一行的法值为本行最大值与最小值的差，而整个矩阵的法值为每一行的法值的最大值。现在，麦克雷想知道矩阵的最小法值是多少。
输入
输入共两行。
第一行是三个整数：n，r，c。
第二行是n个整数 Pi。
输出
输出一个整数，即满足条件的最小的法值。
样例输入
```
7 2 3
170 205 225 190 260 225 160
```
样例输出
```
30
```
提示
30%:1≤n,r,c≤100
50%: 1≤n,r,c≤1000
100%:1≤r,c≤104,r∗c≤n≤5∗105,0`<`pi≤109)
# 解答
一眼题，裸裸的二分啊！！！居然把判断解写炸了。我为什么要用`upper_bound`来找合适的列的位置，在判断是否合法？直接位置+n是否合法就行了啊？最后$100->20$
```cpp
# include <iostream>
# include <algorithm>
# include <cstdio>
using namespace std;
const int MAXN = (int)5e5+10;
int a[MAXN];
int n,r,c;
bool check(int x){
	int ans = 0,i = 1;
	while(i<=n-c+1){
		int j = i+c-1;
		if(a[j]-a[i]<=x)ans++,i = j+1;
		else i++;
	}
	return ans>=r;
}
int main(){
	scanf("%d%d%d",&n,&r,&c);
	for(int i = 1;i<=n;i++)scanf("%d",&a[i]);
	sort(a+1,a+n+1);
	int l = 0,r = (int)1e9+10;
	while(l<r){
		int mid = l+r>>1;
		if(check(mid))r = mid;
		else l = mid+1;
	}
	cout<<l;
	return 0;
}
```
# T2矩阵
在麦克雷的面前出现了一个有n∗m 个格子的矩阵，每个格子用“.”或“# ”表示，“.”表示这个格子可以放东西，“# ”则表示这个格子不能放东西。现在他拿着一条 1∗2 大小的木棒，好奇的他想知道对于一些子矩阵，有多少种放木棒的方案。

输入
第一行包含 2 个正整数 n，m。

接下来 n 行每行包含 m个字符“.”或“# ”。

第 n+1 行包含 1 个正整数 q，表示询问次数。

接下来 q 行每行包含 4 个正整数 r1，c1，r2，c2，分别表示询问的子矩阵的左上格子和右下格子的位置

输出
输出共 q行，每行包含 1 个整数，表示该询问的方案数。

样例输入
```
5 8
....# ..# 
.# ......
#  .# ....
#  ..# .#  
........ 
4
1 1 2 3
4 1 4 1
1 2 4 5
2 5 5 8
```
样例输出
```
4
0
10
15
```
![图片标题](https://cdn.risingentropy.top/images/posts/ce8ec35ab64417774002219.png)
# 解答
裸的二维前缀和+小小的容斥得分：$100ptr$
```cpp
# include <iostream>
# include <cstdio>
using namespace std;
int dp[510][510];
char tp[510][510];
int map[510][510];
int n,m;
inline int work(int l1,int r1,int l2,int r2){
	l1--,r1--;
	int ret = dp[l2][r2]-dp[l1][r2]-dp[l2][r1]+dp[l1][r1];
	for(int i = l1+1;i<=l2;i++){ 
		int x = r1;
		if(map[i][x]==1&&map[i][x+1]==1)ret--;
	}
	for(int i = r1+1;i<=r2;i++){
		int x = l1;
		if(map[x][i]==1&&map[x+1][i]==1)ret--;
	}
	return ret;
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i = 1;i<=n;i++)scanf("%s,",tp[i]+1);
	for(int i =1;i<=n;i++){
		for(int j = 1;j<=m;j++){
			map[i][j] = (tp[i][j]=='.'?1:-1);//1可放 -1不可放 
		}
	}
	int t1,t2,t3;
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=m;j++){
			if(i==1){
				if(j<=1)continue;
				if(map[i][j]==1&&map[i][j-1]==1)dp[i][j] = dp[i][j-1]+1;
				else dp[i][j] = dp[i][j-1];
			}else if(j==1){
				if(i<=1)continue;
				if(map[i][j]==1&&map[i-1][j]==1)dp[i][j] = dp[i-1][j]+1;
				else dp[i][j] = dp[i-1][j];
			}else{
				dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1];
				if(map[i][j-1]==1&&map[i][j]==1)dp[i][j]+=1;
				t1 = dp[i][j];
				if(map[i-1][j]==1&&map[i][j]==1)dp[i][j]+=1;
				t1 = dp[i][j];
			}
		}
	}
	int q;scanf("%d",&q);
	int l1,r1,l2,r2;
	while(q--){
		scanf("%d%d%d%d",&l1,&r1,&l2,&r2);
		printf("%d\n",work(l1,r1,l2,r2));
	}
	return 0;
}
```
# T3整除
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
# 总结
细节上出了很多锅，至于T3那个是智商问题，博主也没有办法