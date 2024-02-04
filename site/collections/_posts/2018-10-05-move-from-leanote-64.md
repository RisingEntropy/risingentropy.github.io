---
title: 数学板子
date: 2018-10-05 14:16:39 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 线性筛质数
```cpp
int v[MAXN];//每个数的最小质因子
int prime[MAXN];
int cnt;
void get_list(){
    for(int i=2;i<=maxn;i++){
        if(!not_prime[i]){
            primes[++cnt] = i;
        }
        for(int j = 1;i<=cnt&&i*prime[j]<MAX;j++){
            not_prime[i*prime[j]] = true;
            if(i%primes[j]==0){//即比一个合数大的质数和该合数的乘积可用一个更大的合数和比其小的质数相乘得到
                break;
            }
        }
    }
}
```
# 质因数分解
```cpp
int factors[log2N];
int pows[log2N];
void divide(int x){
    int cnt = 0;
    for(int i = 2;i*i<=x;i++){
        if(x%1==0){
            factor[++cnt] = i;
            pows[cnt]=0;
            while(x%i==0){
                x/=i;
                pows[cnt]++;//去除所有的i
            }
        }
    }
    if(x>1){//若此时x已经被分解来只剩一个质数了
        factor[++cnt]=x;
        pows[cnt]=1;
    }
    for(int i = 1;i<=cnt;i++){
        cout<<prime[i]<<'^'<<pows[i]<<endl;//分解完了，输出就行
    }
}
```
# 1-N每个数的正约数集合--倍数法
复杂度O($Nlog_2N$)
```cpp
vector<int> factor[N];
for(int i = 1;i<=n;i++)
    for(int j = 1;j<=n/i;j++)
        facotr[i*j].push_back(i);
```
# 求GCD
```cpp
int gcd(int a,int b){
    int temp = b;
    while(b!=0){
        temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}
```
# 拓展欧几里得算法(很重要)
```cpp
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
```
# 矩阵快速幂
```cpp
# include<iostream>
# include<string.h>
using namespace std;
long long e[105][105];
long long m[105][105];
long long temp[105][105];
int n;
const int mod = (int)1e9+7;
void mul(long long a[105][105],long long b[105][105]){
	memset(temp,0,sizeof(temp));
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=n;j++){
			for(int k = 1;k<=n;k++){
				temp[i][j] += (a[i][k]*b[k][j])%mod;
				temp[i][j]%=mod;
			}
		}
	}	
	for(int i = 1;i<=n;i++)
		for(int j = 1;j<=n;j++)
			a[i][j] = temp[i][j];
}
int main(void){
	ios::sync_with_stdio(false);
	long long k;
	cin>>n>>k;
	for(int i = 1;i<=n;i++)
		for(int j = 1;j<=n;j++){
			cin>>m[i][j];
			e[i][i] = 1;
		}
		
	while(k){
		if(k&1){
			mul(e,m);
		}
		mul(m,m);
		k>>=1;
	}
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=n;j++)
			cout<<e[i][j]<<' ';
	cout<<endl;	
	}
	return 0;
}
```
# 阶乘逆元
```cpp
void pre()  
{  
    fac[0] = 1;  
    for(int i = 1; i <= MAX; i++)  
        fac[i] = (fac[i - 1] * i) % MOD; //处理f[n]的逆元 
    inv_fac[MAX] = qpow(fac[MAX], MOD - 2);  
    for(int i = MAX - 1; i >= 0; i--)  
        inv_fac[i] = (inv_fac[i + 1] * (i + 1)) % MOD;   
} 
--------------------- 
作者：超超越 
来源：CSDN 
原文：https://blog.csdn.net/kiwi_berrys/article/details/54834977 
版权声明：本文为博主原创文章，转载请附上博文链接！
```