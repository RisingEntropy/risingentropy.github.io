---
title: FFT&NTT
date: 2019-08-30 20:42:06 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# FFT
学习了FFT ~~法法塔~~ 感受到了人和人之间是有不少差距的Orz。
首先要介绍一个单位根，说的玄妙，其实就把它看做一个角度好了，然后在坐标系里面以自己角的大小为步长，进行旋转，然后它会回到自己就完了。如果我口胡太严重了，就去看这篇[博客](https://www.luogu.org/blog/command-block/fft-xue-xi-bi-ji)好了，写的很好，但是我感觉它代码有问题。
首先介绍一下单位根($\omega_n^1$)的一些性质：
$\omega_n^k = (\omega_n^1)^k$
$\omega_{2n}^{2k} = \omega_n^k$
$\omega_n^0 = 1$
$\omega_n^k*\omega_n^j = \omega_n^{j+k}$
然后就差不多使用如下性质。然后再说FFT。FFT是用来求卷积的，所谓的卷积就是由两个函数生成第三个函数的运算。即$h(x) = \int\limits_{-\infty}^{\infty}f(i)*g(x-i)$，然后这玩意和傅里叶变化有很大关系，可以简化计算。注意由于计算机只能处理非连续的数据，所以需要把上面的积分符号换成$\sum$。FFT的过程如下
$F(x) = a_0+a_0x^1+...+a_nx^n$
然后按照奇偶项拆开
$F(x) = (a_0+a_2x^2...)+x*(a_1x^1+...)$
化为,然后发现这玩意可以分治
$F(x) = FL(x^2)+x*FR(x^2)$
把x代为单位根：
$$
F(x) = FL(x^2)+x*FR(x^2)\\
F(w_n^k) = FL((w_{n}^k)^2)+w_n^kFR((w_{n}^k)^2)\\
F(w_n^k) = FL(w_{n/2}^k)+w_n^kFR(w_{n/2}^k)\\
solve:w_n^0...w_n^{n/2-1}\\
to: w_n^{n/2-1}...w_n^{n-1}\\
$$
假设$k<n/2$,由于：
$$
w_n^k = w_n^{k\%n}
$$
所以可以做如下转化
$$
F(w_n^{k+n/2}) = FL((w_n^{k+n/2})^2)+w_n^{k+n/2}FR((w_n^{k+n/2})^2)\\
bacause\\
(w_n^k)^j = w_n^{kj}\\
therefore\\
=FL(w_n^{2k+n})+w_n^{k+n/2}FR(w_n^{2k+n})\\
w_n^k = w_n^{k\%n}\\
= FL(w_n^{2k})+w_n^{k+n/2}FR(w_n^{2k})\\
w_{2n}^{2k} = w_n^k\\
= FL(w_{n/2}^k)+w_n^{k+n/2}FR(w_{n/2}^k)\\
w_n^{k+n/2} = -w_n^{k}\\
therefore \\
FL(w_{n/2}^k)-w_n^{k}FR(w_{n/2}^k)
$$
然后计算就行了。最后有一个玄学蝴蝶优化，大概就是不写递归的感觉，因为分治就像一个线段树，于是我把每个区间单独取出来处理一下，就免了递归，方便卡常
板子代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <cmath>
using namespace std;
const int MAXN = (int)4e6+10;
const double PI = acos(-1);
struct complex{
	double x,y;
	complex(double a = 0.0,double b = 0.0):x(a),y(b){}
	complex operator+(complex b){return complex(x+b.x,y+b.y);}
	complex operator-(complex b){return complex(x-b.x,y-b.y);}
	complex operator*(complex b){return complex(x*b.x-y*b.y,x*b.y+y*b.x);}
}f[MAXN],g[MAXN];
int n,m,len;
int R[MAXN],lg;
void init(){for(int i = 0;i<len;i++)R[i] = (R[i>>1]>>1)|((i&1)<<(lg-1));}
void DFT(complex *f,int op){
	for(int i = 0;i<len;i++)if(i<R[i])swap(f[i],f[R[i]]);
	for(int j = 1;j<len;j<<=1){
		complex base = complex(cos(PI/j),op*sin(PI/j));
		for(int k = 0;k<len;k+=(j<<1)){
			complex t(1,0);
			for(int l = 0;l<j;l++,t = t*base){
				complex nx = f[k+l],ny = f[j+k+l]*t;
				f[k+l] = nx+ny;
				f[k+j+l] = nx-ny;
			}
		}
	}
}


int main(){
	scanf("%d%d",&n,&m);
	for(int i = 0;i<=n;i++)scanf("%lf",&f[i].x);
	for(int i = 0;i<=m;i++)scanf("%lf",&g[i].x);
	m+=n;lg = 0;
	for(n = 1;n<=m;n<<=1)lg++;
	len = n;init();
	DFT(f,1);DFT(g,1);
	for(int i = 0;i<=n;i++)f[i] = f[i]*g[i];
	DFT(f,-1);
	for(int i = 0;i<=m;i++)printf("%d ",(int)(fabs(f[i].x)/n+0.5));
	return 0;
}
```
# NTT
上面的做法因为要使用三角函数和复数，复数又要用到double，卡精度卡的厉害。于是考虑能不能优化。现引出原根的概念：
设$p = r*2^k+1$k足够大，设原根为$g$,则$g^{0~n-1}$为互不相同的整数。然后定义剩余系下的原根$\omega_n^1 = g^{(p-1)/n}$可以证明它是一个整数，且$g^{0~n-1}$为互不相同的整数。
然后这个原根拥有和FFT的复数一样的性质。用就行了。但是要注意一点，不同的模数对应不同的原根，如998244353对应的原根是3，3在模998244353意义下的的逆元是332748118。原根的求法如下：
原根的判定：如果$g^k\equiv 1(mod p)$中k的最小解为(mod-1)，则g是一个原根。
求法就是枚举1-100(因为大部分原根都小于100)，然后判断就行了。判断的过程就是枚举(mod-1)的因数，如果它满足上述条件，说明这个数不是模mod意义下的原根。
然后代码里面有一些细节，比如FFT里面的
```cpp
complex base = comple(cos(PI/j),op*(PI/j))
```
来实现DFT和IDFT的过程，但是使用NTT就更简单了，直接计算原根的k次方或者原根的逆元的k次方来实现。具体代码就是：
```cpp
long long base = fp(op==1?g:revg,mod-1/(j*2));
```
至于为什么j要乘以2，我也没搞清楚，这两天状态太差了。
代码实现如下：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <cmath>
using namespace std;
const long long mod = 998244353;
const int MAXN = 4e6+10;
const long long G = 3;
int n,m,R[MAXN];
long long f[MAXN],g[MAXN],invG = 332748118;
inline int read() { 
    char c = getchar(); int x = 0, f = 1;
    while(c < '0' || c > '9') {if(c == '-') f = -1; c = getchar();}
    while(c >= '0' && c <= '9') x = x * 10 + c - '0', c = getchar();
    return x * f;
}
long long fp(long long b,long long p = mod-2){
	long long ans = 1;
	while(p){
		if(p&1)ans = ans*b%mod;
		b = b*b%mod;
		p>>=1;
	}
	return ans;
}
int len,lg;
void init(){
	for(int i = 0;i<len;i++)R[i] = (R[i>>1]>>1)|((i&1)<<(lg-1));
}
void NTT(long long *f,int op){
	for(int i = 0;i<len;i++)if(i<R[i])swap(f[i],f[R[i]]);
	for(int j = 1;j<len;j<<=1){
		long long base = fp(op==1?G:invG,(mod-1)/(j<<1));
		for(int k = 0;k<len;k+=(j<<1)){
			long long t = 1;
			for(int l = 0;l<j;l++,t = (t*base)%mod){
				int nx = f[k+l],ny = f[j+k+l]*t%mod;
				f[k+l] = (nx+ny)%mod;
				f[j+k+l] = (nx-ny+mod)%mod;
			}
		}
	}
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i = 0;i<=n;i++)f[i] = read();
	for(int i = 0;i<=m;i++)g[i] = read();
	m+=n;
	for(len = 1;len<=m;len<<=1)lg++;init();
	NTT(f,1);NTT(g,1);
	for(int i = 0;i<len;i++)f[i] = f[i]*g[i]%mod;
	NTT(f,-1);
	long long rev = fp(len,mod-2);
	for(int i = 0;i<=m;i++)printf("%lld ",(f[i]*rev%mod+mod)%mod);
	return 0;
}
```