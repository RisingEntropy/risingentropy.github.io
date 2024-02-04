---
title: luogu P1290
date: 2018-10-30 15:21:22 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
欧几里德的两个后代Stan和Ollie正在玩一种数字游戏，这个游戏是他们的祖先欧几里德发明的。给定两个正整数M和N，**从Stan开始**，从其中较大的一个数，减去较小的数的正整数倍，当然，得到的数不能小于0。然后是Ollie，对刚才得到的数，和M，N中较小的那个数，再进行同样的操作……直到一个人得到了0，他就取得了胜利。下面是他们用(25，7)两个数游戏的过程：
Start：25 7
Stan：11 7
Ollie：4 7
Stan：4 3
Ollie：1 3
Stan：1 0
Stan赢得了游戏的胜利。
现在，假设他们完美地操作，谁会取得胜利呢？
# 输入输出格式
#  输入格式：
第一行为测试数据的组数C。下面有C行，每行为一组数据，包含两个正整数M, N。（M, N不超过长整型。）
#  输出格式：
对每组输入数据输出一行，如果Stan胜利，则输出“Stan wins”；否则输出“Ollie wins”
# 输入输出样例
#  输入样例# 1： 
```
2
25 7
24 15
```
#  输出样例# 1： 
```
Stan wins
Ollie wins
```
# 解答
一下均假设SG(n,m)函数中n>m
这道题可以爆搜，但是因为我在学博弈论，看了题解，所以用博弈论来做
对于SG(n,m)当中，如果m==0的话，说明对于此局面先手必负。因为上一个人经过计算已经得到0了。所以SG(n,0) = 0;
那么我们现在来计算SG函数，由$$SG(n,m) = mex(\{SG(n,n-m),SG(n,n-2m),SG(n,n-3m)....SG(n\%m,n)\})$$
其中，最后一个SG(n%m,n)是交换过，因为保证n\>m 
对于SG(n,n-2m)有：
$$SG(n,n-2m)=mex(\{SG(n,n-3m),SG(n,n-4m),SG(n,n-5m)...SG(m,n\%m)\})$$
由此推下去，可以发现SG(n,n-km)的值只与SG(m,n%m)相关。
那么如果SG(m,n%m)==0 即是当前局面是p(先手必负)，那么对于SG(n,m-kn)都是1，2,3,4，即n(先手必胜)局面。 
如果SG(m,n%m)==1,即n(先手必胜)局面，设k为n/m(整除),那么SG(n,n-(k-1)*m)==mex{SG(n%m,m)} == 0，对于其他的SG函数，均为2,3,4,5...即n(先手必胜)局面。
特别判断一下如果n/m==1,那么此状态的SG函数就等于!SG(n,n%m)(如果这里理解不了，可以看一下p和n的互相转化)。否则，SG函数就等于1;
所以写一个类似于gcd的函数就出来了。
```cpp
# include <cstdio>
# include <cstring>
using namespace std;
long long read(){
	long long x = 0,f = 1;
	static char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = x*10+c-'0';c = getchar();}
	return x*f;
}
bool SG(long long n,long long m){
	if(m==0)return false;
	if(n/m == 1)return !(m,n%m);
	else{return true;}
}
inline long long max(long long a,long long b){return a>b?a:b;}
inline long long min(long long a,long long b){return a<b?a:b;}
int main(void){
	long long c = read();
	long long n,m;
	while(c--){
		n = read();
		m = read();
		if(SG(max(m,n),min(n,m))){
			printf("Stan wins\n");
		}else{
			printf("Ollie wins\n");
		}
	}
	return 0;
}
```