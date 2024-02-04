---
title: luogu P2158 [SDOI2008]仪仗队
date: 2018-10-30 08:21:09 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
作为体育委员，C君负责这次运动会仪仗队的训练。仪仗队是由学生组成的N * N的方阵，为了保证队伍在行进中整齐划一，C君会跟在仪仗队的左后方，根据其视线所及的学生人数来判断队伍是否整齐(如下图)。 
![](https://cdn.risingentropy.top/images/posts/bd7a8b4ab644138b80012bb.png)
现在，C君希望你告诉他队伍整齐时能看到的学生人数。
#  输入输出格式
#  输入格式：
共一个数N

#  输出格式：
共一个数，即C君应看到的学生人数。
# 输入输出样例
#  输入样例1:
```
4
```
#  输出样例1:
```
9
```
# 解答
分析一下这道题，我们发现当点$(x,y)$中，gcd(x,y)=1的时候，这个点才可以被看见(原因的话，从斜率的角度来看)。那么对于每一个y，我们只需要求出$\varphi(y)$就可以了。那么答案就是：
$$3+2\times \sum_{i=2}^{N}\varphi(i)$$
这里面的3是左下角那三个点可以被看见，特判一下。乘以2是因为这个图形有对称性。

那么利用Eratosthenes筛法(就是最~~脑残~~简单的素数筛法)，直接在$O(N\ logN)$的复杂度内求出2~N中的每个数的欧拉函数。(其实这样做的道理就是当a`<`b且a、b互质的时候，a与b的倍数也互质，再结合欧拉函数的求法可以直接这样求出很多数的欧拉函数)代码如下
```cpp
 for(int i = 2;i<=n;i++){
        if(phi[i]==i){
            for(int j = i;j<=n;j+=i){
                phi[j] = phi[j]/i*(i-1);
            }
        }
    }
```
然后统计答案就行，注意，统计答案的时候y应该从2到N-1。因为(1,1)(1,0)(0,1)这三个点已经被统计，而当$y=N$的时候，就已经是对角线了，所以不计入答案。
AC代码：
```cpp
# include <iostream>
using namespace std;
int phi[40100];
int main(void){
    int n;cin>>n;
    int ans = 0;
    if(n==1){cout<<0;return 0;}
    for(int i = 2;i<=n;i++)phi[i] = i;
    for(int i = 2;i<=n;i++)
        if(phi[i]==i)
            for(int j = i;j<=n;j+=i)
                phi[j] = phi[j]/i*(i-1);
    for(int i = 2;i<n;i++)ans += phi[i];
    cout<<ans*2+3;
    return 0;
}![图片标题](https://cdn.risingentropy.top/images/posts/bd7a8b4ab644138b80012bb.png)
```