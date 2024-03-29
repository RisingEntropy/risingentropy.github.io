---
title: luogu P2197
date: 2018-10-30 10:37:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
甲，乙两个人玩Nim取石子游戏。
nim游戏的规则是这样的：地上有n堆石子（每堆石子数量小于10000），每人每次可从任意一堆石子里取出任意多枚石子扔掉，可以取完，不能不取。每次只能从一堆里取。最后没石子可取的人就输了。假如甲是先手，且告诉你这n堆石子的数量，他想知道是否存在先手必胜的策略。
# 输入输出格式
#  输入格式：
第一行一个整数T<=10,表示有T组数据
接下来每两行是一组数据，第一行一个整数n，表示有n堆石子，n<=10000;
第二行有n个数，表示每一堆石子的数量
#  输出格式：
共T行，如果对于这组数据存在先手必胜策略则输出"Yes",否则输出"No"，不包含引号，每个单词一行。
# 样例
输入样例# 1： 
```
2
2
1 1
2
1 0
```
输出样例# 1： 
```
No
Yes
```
# 解答
最基本的Nim博弈论游戏，其实就是判断所有石子数的异或和是否为0.如果为0则不存在先手必胜的策略，否则，存在先手必胜的策略。
证明：
设$k = A_1\ xor A_2\ xor A_3...\ xor A_n$
我们看最后一个情况，如果k=0，那么当前情况是p(先手必负)，那么它一定是由n(先手必胜)转移过来。
对于任意一个局面，$k = x \neq 0$，设x的二进制表示下最高位1在第j位。那么至少存在一堆石子$A_i$,它的第j位是1.那么$A_i\ xor x< A_i$，我们就从$A_i$堆中取走若干石子，使其变为$A_i
\ xor x$就得到了一个各堆石子数异或起来等于0的局面。
对于任意一个局面，如果$k=0$，那么无论如何取石子，得到的局面下各堆石子异或起来都不等于0.可用反证法证明，假设$A_i$被取成了$A'_i$,并且$A_1\ xor A_2\ xor\ A_3..xor A_i' ...xor A_n=0$。由异或运算的消去律得到$A_i'=A_i$与之前不能不取石子的规则矛盾。
用数学归纳法可知，k=0时，为必胜局面，一定存在一种让对手"各堆石子异或起来等于 0"的局面。
AC代码：
```cpp
# include <cstdio>
int read(){
	int x = 0,f = 1;
	static char c = getchar();
	while(c<'0'||c>'9')c = getchar();
	while(c>='0'&&c<='9')x = x*10+c-'0',c = getchar();
	return x*f;
}
int main(void){
	int T;
	T = read();
	int ans = 0;
	int a,l;
	while(T--){
		l = read();
		ans = 0;
		while(l--){
			a = read();
			ans^=a;
		}
		if(ans!=0){
			printf("Yes\n");
		}else{
			printf("No\n");
		}
	}
}

```