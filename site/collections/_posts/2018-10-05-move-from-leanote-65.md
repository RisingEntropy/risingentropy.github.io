---
title: 约数
date: 2018-10-05 16:18:35 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 整除
b|a表示b整除a(a%b=0)
性质
1.a|b且b|c 则$\forall$x,y有a|xb+yc
2.若a|b且b|c,那么a|c
3.设m$\neq$0,则a|b，当且仅当ma|mb
4.若a|b且b|a则a=$\pm$b
# 约数
根据算数基本定理，若N可以被唯一分为N=$p_1^{c_1}P_2^{c_2}...P_m^{c_m}$且pi是质数满足p1`<`p2`<`p3...`<`pm,则N的正约数集合可以写作{$p_1^{c_1},P_2^{c_2},...P_m^{c_m}$}
那么，正N的约数为
$(C_1+1)\times(C_2+1)\times...(C_m+1)=\prod_{i=1}^{m}(C_i+1)$
所有正约数的和为
$(1+p_1+p_{1}^{2}+...+p_{1}^{c_i})\times....\times(1+p_{m}+p_{m}^2+...p_{m}^{c_m})=\prod_{i=1}^{m}(\sum_{j=0}^{c_i}(p_i)^j)$
求他的正约数集合--板子里有
# 倍数法的推论
1-N每个数的约数个数的总和大约为NlogN(不超过？)
# 最大公因数与最小公倍数
gcd(m,n)最大公约数
lcm(m,n)最小公倍数
#  一些性质
1.a|b,b|m 那么lcm(a,b)|m
2.d|a,d|b,则d|gcd(a,b)
3.lcm(am,bm)=m*lcm(a,b)
**4.a*b=gcd(a,b)*lcm(a,b)**
#  gcd求法
1.唯一分解定理，没前途
2.欧几里得算法
$$gcd(a,b)=gcd(b,a \% b)$$
3.二进制算法
若a=b则gcd(a,b) = a;
若 a，b均为偶数 gcd(a,b) = 2gcd(a/2,b/2)
若a为偶，b为奇 gcd(a,b) = gcd(a/2,b);
若ab均为奇，gcd(a,b) = gcd(a-b,b)//更相减损术
#  lcm求法
根据a*b=gcd(a,b)*lcm(a,b)
# 同余问题
几个定理
1.$a\equiv b$当且仅当m|(a-b)
2.$a\equiv b (mod m)$当且仅当存在整数k，使得a=b+km;
**费马小定理：若p是质数，对于任意整数$a$有$a^p=a(mod p)$**
**欧拉定理：若正整数a,n互质，则$a^{\varphi(n)}\equiv1(mod\ n)$,其中$\varphi $为欧拉函数。欧拉函数是小于或等于n的正整数中与n互质的数的数目（φ(1)=1）**
欧拉定理推论：
若a，n互质，那么对于任意正整数b有，$a^b\equiv a^{b\ mod \varphi(n)}(mod\ n)$
# 同余的性质：
其实和等式的性质一样，**除了除法这条**
若a ≡ b(mod n),c ≡ d(mod n),则
(1）a + c ≡ b + d(mod n)
(2) ac ≡ bd(mod n)
(3) ka ≡ kb(mod n),k为任意整数
(4) a^m ≡ b^m(mod n)，m为正整数
# 拓展欧几里得算法
定理1.若a,b均不为0，则存在整数x,y 使得ax+by=gcd(a,b)
证明：
　设 ax1+by1=gcd(a,b);
　bx2+(a % b)y2=gcd(b,a % b);
　根据朴素的欧几里德原理有 gcd(a,b)=gcd(b,a % b);
　则:ax1+by1=bx2+(a % b)y2;
　即:ax1+by1=bx2+(a-(a/b)*b)y2=ay2+bx2-(a/b)*by2;
　根据恒等定理得：x1=y2; y1=x2-(a/b)*y2;
在找到ax+by=gcd(a, b)的一组解x0,y0后，应该是得到ax+by=c的一组解x1 = x0*(c/gcd(a,b)),y1 = y0*(c/gcd(a,b))，
~~OI中的结论，只需要关注其正确性，不需要关注证明.-----沃兹基硕德~~
作用：求不定方程详见证明。其实就是归纳法的思想。一本通P396
代码实现
```cpp
void ex_gcd(int a,int b,int &mod,int &x,int &y){
    int t;
    if(b==0){
        mod = a;
        x = 1;
        y = 0
    }else{
        ex_gcd(b,a%b,mod,x,y);
        t = x;
        x = y;
        y = t-(a/b)*y;//这里很重要
    }
}
```
3.最后要注意的一点，扩展欧几里得算法算出的x1可能为负数，这显然是不成立的。又因为
x=x1+b*t;
y=y1-a*t;
所以x1的值可以写成(x%m+m)%m。这样的话负数也转成了正数，就可以输出答案啦！
# 一个非常重要的定理
<font color="red">对于不定方程，ax+by=c当且仅当gcd(a,b)|c时，方程有解</font>
#  拓展欧几里得算法的作用
1.求出一个不定方程的特解$x_0$和$y_0$然后$x_0 y_0$同时乘上$c/d$就得到了 就得到了方程的一组特解(c\d)x0,(c\d)y0;
实际上，方程$ax+by=c$的通解可以表示为x=$\frac{c}{d}x_0 +k\frac{b}{d}  \ \ \ y=\frac{c}{d}y_0-k\frac{a}{d}(k\in Z)$
求最小解：
见下面
习题：青蛙的约会
# 线性同余方程
定义1:给定整数a,b,m，求一个整数x满足$a\times b \equiv b(mod\ m)$，因为未知数的次数为1，所以我们称之为一次同余方程，也称线性同余方程。

$a*x\equiv b(mod\ m)$ 等价于a*x-b是m的倍数，不妨设为-y倍。于是乎方程就可以被改写成a*x+m*y = b。然后只需要接不定方程a*x+m*y = b。
#  一个定理
a,b,m是整数，且m>0 ,gcd(a,m) = d，如果d|b,则方程恰好有d个模m不同余的姐，否则，方程无解。
方程的解：
假设方程$x_0$为$ax\equiv b (mod  m)$的任意一个解，则该方程对模m恰好有d个不同的解，分别为xi = x0+i*(m/d)(0<=i<=d-1)
(大于0)最小解：
就是如果求出 ax+by=c 的一组特解，那 a(x-bt)+b(y+at)=c 肯定成立。
然后调整.其实也可以不断调整x，直到x小于0，那么上一个x就是最小解
那么可以写成（假设x，y为找到的一组特解）：
```cpp
    (x/d%(b/d)+b/d)%(b/d);//其实是为了防止x小于0
```
# 乘法逆元
[参考](https://www.luogu.org/blog/zjp-shadow/cheng-fa-ni-yuan)
定义：$若a*x\equiv 1 (mod \ b)$且a与b互质，那么我们就能定义: x为a的逆元，记为$a^{-1}$(mod\ p)
 ，所以我们也可以称x为a的倒数，它有一个特殊的小性质：$b\times b^{-1} \equiv 1(mod\ p)$
# 计算逆元
#  1.拓展欧几里得算法解不定方程
 解方程ax + by = 1;
 code:
```cpp
# include<iostream>
using namespace std;
int x,y;
void ex_gcd(int a,int b){
	if(b==0){
		x = a;
		y = 0;
	}else{
		ex_gcd(b,a%b);
		int temp = x;
		x = y;
		y = temp - (a/b)*y;
	}
}
int main(void){
	int a,b;
	cin>>a>>b;
	ex_gcd(a,b);
	x = (x%b+b)%b;
	cout<<x;
}
```
# 费马小定理求逆元
#  费马小定理
$若p为素数，a为正整数，且a、p互质。 则有a^{p-1} \equiv 1 (\bmod {p})$
那么
$a*x\equiv 1 (mod\ p)$
则
$a*x\equiv a^{p-1}(mod\ p)$
那么
$x\equiv a^{p-2}(mod\ p)$
然后只需要求出$a^{p-2}\ mod\  p$的值就行了,求逆元其实就是pow(x,mod-2)注意此时mod必须为质数
code:
```cpp
ll fpm(ll x, ll power, ll mod) {
    x %= mod;
    ll ans = 1;
    while (power) {
        if (power & 1) ans = (ans * x) % mod;
        x = (x * x) % mod;
        power >>= 1;
    }
    return ans;
}
```
# 线性递推逆元
背板！！！背板！！！背板！！！；
```cpp
inv[1] = 1;
inv[i] = (p-p/i)*inv[p%i]%p;
```
# 矩阵快速幂
一些概念与定义：
矩阵就是一个数字阵列
1.方阵：行数和列数相等的矩阵如
$$\begin{bmatrix} 1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}$$
单位矩阵：主对角线上的元素都是1，其余元素全为0的n阶矩阵被称为n阶单位矩阵，记为In或En，通常用I或E表示。
# 矩阵运算
加减：把两个矩阵对应位置上的数相加减
乘法
2个要素：
1.A的列数和B的行数必须相等
2.如果A是一个n*r的矩阵，B是一个r*m的矩阵；那么A*B=C 的 
**其实$C_{i,j}$就等于A的i行的元素与B的第j列的元素的乘积的和**
用公式描述就是
设Ａ是n*m的矩阵，Ｂ是m*p的矩阵，那么C=A*B就是n*p的矩阵
$$C_{i,j}=\sum_{k=1}^m\ A_{i,j}*B_{j,k}$$
# 方阵乘幂
求方阵A的n次方，$A^n$
# 矩阵乘法应用
#  矩阵快速幂
用于递推的！东西有点多，我不想打markdown，参考一本通提高版P416
代码：见板子
# 欧拉函数
1~N中与N互质的数的个数被称为欧拉函数，记为$\varphi(N)$。
又因为算数基本定理，所以:
$$\varphi(N)=N*\frac{p_1-1}{p_1}*\frac{p_2-1}{p_2}*\frac{p_3-1}{p_3}...*\frac{p_m-1}{p_m}=N*\prod_{质数p|N}(1-\frac{1}{p})$$
其实就是在分解质因数的时候就可以计算了
板子：
```cpp
int phi(int N){
	int ans = N;
	for(int i = 1;i<=sqrt(N);i++){
		if(!N%i){
			ans=ans/i*(i-1);
			while(N%i==0)N/=i;
		}
	}
	if(N>1)ans=ans/N*(N-1);
	return ans;
}
```