---
title: luoguP1516
date: 2018-10-08 15:22:33 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题目描述
两只青蛙在网上相识了，它们聊得很开心，于是觉得很有必要见一面。它们很高兴地发现它们住在同一条纬度线上，于是它们约定各自朝西跳，直到碰面为止。可是它们出发之前忘记了一件很重要的事情，既没有问清楚对方的特征，也没有约定见面的具体位置。不过青蛙们都是很乐观的，它们觉得只要一直朝着某个方向跳下去，总能碰到对方的。但是除非这两只青蛙在同一时间跳到同一点上，不然是永远都不可能碰面的。为了帮助这两只乐观的青蛙，你被要求写一个程序来判断这两只青蛙是否能够碰面，会在什么时候碰面。

我们把这两只青蛙分别叫做青蛙A和青蛙B，并且规定纬度线上东经0度处为原点，由东往西为正方向，单位长度1米，这样我们就得到了一条首尾相接的数轴。设青蛙A的出发点坐标是x，青蛙B的出发点坐标是y。青蛙A一次能跳m米，青蛙B一次能跳n米，两只青蛙跳一次所花费的时间相同。纬度线总长L米。现在要你求出它们跳了几次以后才会碰面。

# 输入输出格式
#  输入格式：
输入只包括一行5个整数x，y，m，n，L

其中$0<x≠y < =2000000000，0 < m、n < =2000000000，0 < L < =2100000000$。

#  输出格式：
输出碰面所需要的天数，如果永远不可能碰面则输出一行"Impossible"。

#  输入输出样例
输入
```
1 2 3 4 5
```
输出:
```
4
```
# 题解
其实是一道拓展欧几里得算法的裸题主要是通过推导公式：
由题：
$$X+am\equiv Y+an(mod L)$$
即a天后跳到了同一位置
然后变个型
$$X+am - (Y+an)=kL$$
再变一下
$X-Y+a(m-n)=kL$
$$a(m-n)-kL=Y-X$$
提个负号出来
$$a(n-m)+kL = X-Y$$
于是乎成了不定方程，那么只需要求解一个特解，然后找最小解就行
又因 为$$X_k = X_{min}+\frac{L}{gcd(n-m,L)}$$
那么$$k_{mid} = X_k mod \frac{L}{gcd(n-m,L)}---(1)$$
然后又因为我们的方程是建立在(gcd(n-m,L))上的，而不是建立在n-m上的，所以需要乘一个$\frac{n-m}{gcd(n-m,L)}$//注意，这一步是建立在(1)之上的，所以要先乘再模;
代码：
```cpp
# include<iostream>
using namespace std;
long long x0,y0;
long long d;
void extend_gcd(long long a,long long b){
	if(b==0){
		x0 = 1;
		y0 = 0;
		d = a;
	}else{
		extend_gcd(b,a%b);
		long long t = x0;
		x0 = y0;
		y0 = t-(a/b)*y0;
	}
}
int main(void){
	ios::sync_with_stdio(false);
	long long x,y,m,n,L;
	cin>>x>>y>>m>>n>>L;
	if(n<m){
		swap(m,n);
		swap(x,y);
	}
	extend_gcd(n-m,L);
	long long mod = L/d;
	if((x-y)%d!=0){//注意提到的一个定理ax+by=c 当且仅当gcd(a,b)|c时，有整数解
		cout<<"Impossible";
	}else{
		cout<<(x0*(x-y)/d%mod+(L/d))%mod<<endl;//取在X-Y下的最小解
	}
}
```
>参考：写的超级好的题解：[_pks 'w的题解](https://pks-loving.blog.luogu.org/solution-p1516)