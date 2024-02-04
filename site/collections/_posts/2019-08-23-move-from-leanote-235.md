---
title: 中国剩余定理(CRT)
date: 2019-08-23 13:22:02 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 中国剩余定理
#  内容：
设$m_1,m_2.m_3,m4$是一组两两互质的数，设$m = \prod\limits_{i=1}^nm_i,M_i = m/m_i,t_i$是线性同余方程$M_it_i\equiv1(mod\  m_i)$的一个解，那么对于任意的$n$个整数$a_i,a_2...a_n$，方程组
$$\begin{Bmatrix}x\equiv a_i(mod\ m_i)\\x\equiv a_2(mod\  m_2)\\.\\.\\x\equiv a_n(mod\ m_n)
\end{Bmatrix}$$
有整数解：为$x=\sum\limits_{i=1}^{n}a_iM_it_i$
# 证明
因为$M_i$是除了$m_i$以外所有模数的倍数，所以$\forall k\neq i,a_iM_it_i\equiv 0(mod\ m_k)$。又因为$a_iM_it_i\equiv a_i(mod m_i)$所以CRT成立。
$$Q.E.D.$$
其实我觉得还是挺显然的。
# 应用
[P1495 曹冲养猪](https://www.luogu.org/problem/P1495)
观察题目不难列出如下柿子:
$$\begin{Bmatrix}x\equiv b_1(mod\ a_1)\\x\equiv b_2(mod\ a_2)\\...\\x\equiv b_n(mod\ a_n)\end{Bmatrix}$$
然后根据中国剩余定理，处理处$M_i$和$t_i$，由于要最小，我们直接对$M$进行取模就好了。注意一点的是$M$的值可能很大，有题目可得为$1000^{10}$所以需要使用`long long`
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 1010;
long long a[MAXN],b[MAXN],M[MAXN],t[MAXN];
int exgcd(long long a,long long b,long long &x,long long &y){
	if(b==0){
		x = 1,y = 0;return a;
	}else{
		exgcd(b,a%b,x,y);
		int t = x;x = y;y = t-(a/b)*y;
	}
}
int main(){
	int n;cin>>n;
	for(int i = 1;i<=n;i++){
		cin>>a[i]>>b[i];
	}
	long long MM = 1;
	for(int i = 1;i<=n;i++)MM*=a[i];
	long long x,y;
	for(int i = 1;i<=n;i++){
		M[i] = MM/a[i];
		exgcd(M[i],a[i],x,y);
		t[i] = (x%a[i]+a[i])%a[i];
	}
	x = 0;
	for(int i = 1;i<=n;i++)x = (x+((b[i]*M[i]*t[i])%MM+MM)%MM)%MM;
	cout<<x;
	return 0;
}
```
poj3900 拓展欧几里得解同余方程组
由于这道题不保证互质，所以CRT就不能用了。需要使用拓展欧几里得算法。拓展欧几里得定理的主要思想就是合并方程组。
拓展欧几里得算法的原理如下：
要合并$$x\equiv r_1(mod\ a_1)\\x\equiv r_2(mod\ a_2)$$
可以化为如下形式：
$$x=k_1a_1+r_1 \\ x=k_2a_2+r_2$$
由于求得的$x$是同一个值，所以可以有
$$k_1a_1+r_1=k_2a_2+r_2$$
$$-> k_1a_1-k_2a_2=r_2-r_1$$
于是通过拓展欧几里得算法解出$k_1$可以得到如下柿子
$$x_1=k_1a_1+r_1\\ x_2 = k_2a_2+r_2$$此时求出来的$x$是两个方程的共同的解。那么显然有结论$$x_1\equiv x (mod\ lcm(a1,a2))$$
证明可以看这个wcr神仙的博客[数学杂记](https://blog.csdn.net/g21wcr/article/details/102467429)
进一步化简
$$x\equiv x_1(mod\ a_1a_2/gcd(a_1,a_2))$$
然后合并完成以后，其实最后的方程的形式就是$$x\equiv x'(mod\ gcd(a_1,a_2,a_3.....)$$，由于后面是gcd，所以就不用解方程了，$x'$就是答案。
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# define clear(x) memset(x,0,sizeof(x))
using namespace std;
const int MAXN = (int)1e5+10;
long long M[MAXN],t[MAXN],m[MAXN],a[MAXN];
long long exgcd(long long a,long long b,long long &x,long long &y) {
	if(b==0) {
		x = 1,y = 0;
		return a;
	} else {
		long long d = exgcd(b,a%b,x,y);
		long long t = x;
		x = y;
		y = t - (a/b)*y;
		return d;
	}
}
long long gcd(long long a,long long b){return b==0?a:gcd(b,a%b);}
int main() {
	int n;
	while(scanf("%d",&n)!=EOF) {
		long long a1,b1,a2,b2,x,y,d;
		cin>>a1>>b1;
		bool flag = true;
		for(int i = 1;i<n;i++){
			cin>>a2>>b2;
			long long d = exgcd(a1,a2,x,y);
			if((b2-b1)%d)flag = false;
			else{
				x*=(b2-b1)/d;
				long long n1 = a2/d;
				x = (x%n1+n1)%n1;
				b1 = x*a1+b1;
				a1 = a1*a2/d;
			}
		}
		if(flag)cout<<b1<<endl;
		else cout<<-1<<endl;
	}
	return 0;
}
```
生理周期poj1006
可以说是中国剩余定理的板子题，建议不要打数组，把几个值全部变量定义来，这样可以加深对CRT的理解~~方便卡常~~。
代码:
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 10;
const int P = 23;
const int E = 28;
const int I = 33;
const int M = P*E*I;
int gcd(int a,int b,int &x,int &y){
	if(b==0){
		x = 1,y = 0;return a;
	}else{
		gcd(b,a%b,x,y);
		int t = x;x = y;y = t - (a/b)*x;
	}
}
int main(){
	int p,e,i,d;
	int cases = 0;
	while(scanf("%d%d%d%d",&p,&e,&i,&d)!=EOF){
		if(p==-1&&e==-1&&i==-1&&d==-1)break;
		int x,y,t,ans = 0;
		{//P
			gcd(M/P,P,x,y);
			t = x;
			ans+= M/P*p*t;
			ans = (ans%M+M)%M;
		}
		{//E
			gcd(M/E,E,x,y);
			t = x;
			ans+=M/E*e*t;
			ans = (ans%M+M)%M;
		}
		{//I
			gcd(M/I,I,x,y);
			t = x;
			ans += M/I*i*t;
			ans = (ans%M+M)%M;
		}
		if(ans<=d)ans+=M;
		printf("Case %d: the next triple peak occurs in %d days.\n",++cases,ans-d);
	}
	return 0;
}
```
