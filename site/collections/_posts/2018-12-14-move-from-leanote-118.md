---
title: POJ 2411Mondriaan's Dream
date: 2018-12-14 19:26:38 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Squares and rectangles fascinated the famous Dutch painter Piet Mondriaan. One night, after producing the drawings in his 'toilet series' (where he had to use his toilet paper to draw on, for all of his paper was filled with squares and rectangles), he dreamt of filling a large rectangle with small rectangles of width 2 and height 1 in varying ways.

![图片标题](https://cdn.risingentropy.top/images/posts/c1393ceab6441051a006bbf.png)
Expert as he was in this material, he saw at a glance that he'll need a computer to calculate the number of ways to fill the large rectangle whose dimensions were integer values, as well. Help him, so that his dream won't turn into a nightmare!

Input Specification

The input file contains several test cases. Each test case is made up of two integer numbers: the height h and the width w of the large rectangle. Input is terminated by h=w=0. Otherwise, 1<=h,w<=11.

Output Specification

For each test case, output the number of different ways the given rectangle can be filled with small rectangles of size 2 times 1. Assume the given large rectangle is oriented, i.e. count symmetrical tilings multiple times.
![图片标题](https://cdn.risingentropy.top/images/posts/c1393ceab6441051a006bbf.png)
Sample Input
```
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
```
Sample Output
```
1
0
1
2
3
5
144
51205
```
# 解答
其实是一道状压dp的裸题！
我们以当前扩展到了第$i$行作为状态，然后用1表示`竖着的矩形的上面的一个`0表示其他情况
![图片标题](https://cdn.risingentropy.top/images/posts/c1393ceab6441051a006bbf.png)
那么怎么转移呢？
设$F[i,j]$为第$i$行为$j$状态的时候的分割总数。j是用十进制记录的$M$位的二进制数。
第$i-1$行的形态$k$能够转移到$j$时，当且仅当：

 1. $j$和$k$的`按位与`运算的结果为$0$。这保证了每个数字$1$的下方必须是$0$，代表补全竖着的$1\times 2$的长方形
 2. $j$和$k$执行按位或运算的结果的二进制表示中，每一段连续的$0$都必须有偶数个
这些0代表若干个横着的$1\times 2$长方形，奇数个$0$无法分割成这种形态
我们需要预处理出$[0,2^M-1]$内所有满足“每一段连续的$0$都必须有偶数个”的整数，记录在集合S中
方程：$$F[i,j] = \sum_{j\&k=0并且j|k\in S}F[i-1,k]$$
然后dp的初始值：F[0,0] = 1,其余为0
目标：F[N,0]
复杂度$O(2^M2^MN) = O(4^MN)$
**注意，打出来的数非常大，需要用long long**
code:
```cpp
# include <cstdio>
# include <iostream>
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
int F[12][1<<11];
bool canGo[1<<11];
int main(){
	int n,m;
	while(cin>>n>>m&&n){
		for(int i = 0;i<1<<m;i++){
			bool cnt = 0,has_odd = 0;
			for(int j = 0;j<m;j++){
				if(i>>j&1)has_odd|=cnt,cnt = 0;
				else cnt^=1;
			}
			canGo[i] = has_odd|cnt?0:1;
		}
		F[0][0] = 1;
		for(int i = 1;i<=n;i++){
			for(int j = 0;j<1<<m;j++){//遍历每个状态
				F[i][j] = 0;
				for(int k = 0;k<1<<m;k++){//便利可以转移的状态 
					if((j&k)==0&&canGo[j|k])F[i][j]+=F[i-1][k];
				} 
			}
		}
		cout<<F[n][0]<<endl;
	}
	return 0;
}
```