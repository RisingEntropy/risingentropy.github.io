---
title: 【倍增 哈希】01串
date: 2019-10-11 21:17:18 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
某日，小 Q 得到了一种新的生成 01 串的代码

给定一个整数 Z< M，执行 n 次下列语句会得到一个 01 串
```
z=[(a*z+c)/k]%m;
if (z< m/2) return 0;
else return 1;
```
现在小 Q 已经得到了某串 01 串，小 Q 想知道有多少个可能的不同的最初的 Z 可以生成这个 01 串。

输入
第一行五个整数 a, c, k, m, n。

第二行 n 个连续的 01 数字描述 01 串。

输出
一行一个整数表示答案

样例输入
```
3 6 2 9 2
10
```
样例输出
```
4
```
提示
对于 30%的数据，1<=n,m<=10^3
对于 60%的数据，1<=n<=10^3
对于 100%的数据，1<=n<=10^5，1<=m<=10^6，0<=a,c<=m，1<=k<=m
# 解答
~~没想到吧？是个倍增~~哈希+倍增用nxt[i][j]表示$i$号数走$2^j$步以后到达的数，然后用hash[i][j]表示数i走$2^j$步以后的哈希值，然后直接比较就好了。代码也还是比较好写，但是注意上述状态的定义，i是从0开始的。
代码：
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = (int)1e5+10;
const int MAXM = (int)1e6+10;
const unsigned int base = 17;
inline char nc(){
	static char buf[100000],*p1 = buf,*p2 = buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
template<typename T>
inline void read(T &x){
	x = 0;
	char c = nc();
	while(c<'0'||c>'9'){c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
}
inline int getdigit(){
	char c = nc();
	while(!isdigit(c))c = nc();
	return c^48;
}
long long  a,c,k,m,n;
unsigned int hash[MAXM][20];
unsigned int pw[MAXM];
int nxt[MAXM][20];
char str[MAXM];
unsigned int calc(int z){return((a*z+c)/k)%m;}
unsigned int Calc(int k){
	unsigned int ret = 0;
	for(int i = 19;i>=0;i--){
		if(n&(1<<i)){
			ret = ret*pw[i]+hash[k][i];
			k = nxt[k][i];
		}
	}
	return ret;
}
unsigned int target;
int main(){
	read(a),read(c),read(k),read(m),read(n);
	for(int i = 1;i<=n;i++)target = (target*base+getdigit());
	pw[0] = base;
	for(int i = 1;i<=20;i++)pw[i] = pw[i-1]*pw[i-1];
	for(int i = 0;i<m;i++){
		nxt[i][0] = calc(i);
		hash[i][0] = (nxt[i][0]>=m/2);
	}
	for(int i = 1;i<=19;i++){
		for(int j = 0;j<m;j++){
			nxt[j][i] = nxt[nxt[j][i-1]][i-1];
			hash[j][i] = hash[j][i-1]*pw[i-1]+hash[nxt[j][i-1]][i-1];
		}
	}
	int ans = 0;
	for(int i = 0;i<m;i++){
		if(Calc(i)==target)ans++;
	}
	cout<<ans;
	return 0;
}
```
然后考试的时候我瞎几把写了一个记忆化搜索，居然有60分，并且还跑得比std快，就是空间不太够。
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <map>
using namespace std;
const int MAXN = (int)1e6+10;
inline char nc(){
	static char buf[100000],*p1 = buf,*p2 = buf;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
template<typename T>
inline void read(T &x){
	x = 0;T f = 1;
	char c = nc();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = nc();}
	while(c>='0'&&c<='9'){x = x*10+(c^48);c = nc();}
	x*=f;
}
inline char gc(){
	char c = nc();
	while(c==10||c==' '||c=='\r')c = nc();
	return c;
}
struct edge{int t,next;}edges[MAXN<<1];
int head[MAXN],top;
void add(int f,int t){
	edges[++top].next = head[f];
	edges[top].t = t;
	head[f] = top;
}
int a,c,k,m,n;
int z;
inline int work(){
	z=((a*z+c)/k)%m;
	if (z<m/2)return 0;
	else return 1;
}
char str[MAXN];
void file(){
	freopen("zero.in","r",stdin);
	freopen("zero.out","w",stdout);
}
inline void bf(){
	register int res = 0;
	for(register int i = 0;i<m;i++){
		z = i;
		bool flag = true;
		for(register int j = 1;j<=n;j++){
			if(work()!=str[j]-'0'){
				flag = false;break;
			}
		}
		if(flag)res++;
	}
	printf("%d",res);
}
map<int,int> dp[MAXN];
bool dfs(int x,int dep){
	if(dp[x][dep]==1)return true;
	if(dp[x][dep]==2)return false;
	if(dep==n+1){
		dp[x][dep] = 1;return true;
	}
	bool flag = false;
	for(int i = head[x];i;i = edges[i].next){
		int t = edges[i].t;
		int nxt = t<(m/2)?0:1;
		if(dep==n||str[dep+1]==nxt+'0'){
			if(dfs(t,dep+1)==1)flag = true;
			if(flag){
				dp[x][dep] = 1;return true;
			}
		}
	}
	dp[x][dep] = 2;return false;
}
inline void correct(){
	for(int z = 0;z<m;z++){
		add(z,((a*z+c)/k)%m);
	}
	int cnt = 0;
	for(int i = 0;i<m;i++)if(dfs(i,0))cnt++;
	printf("%d\n",cnt);
}
int main(){
    int size=300<<20;
    __asm__ ("movq %0,%%rsp\n"::"r"((char*)malloc(size)+size));//提交用这个 
	read(a),read(c),read(k),read(m),read(n);
	for(register int i = 1;i<=n;i++)str[i] = gc();
	correct();
    exit(0);//必须用exit 
}

```