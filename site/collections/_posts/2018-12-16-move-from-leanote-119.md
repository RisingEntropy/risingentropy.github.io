---
title: Educational Codeforces Round 56(Div.2)C  Mishka and the Last Exam
date: 2018-12-16 09:35:51 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
[神奇的传送门](http://codeforces.com/contest/1093/problem/C)
题目翻译如下：
给你一个长度为$\frac{n}{2} n$是偶数的序列$b_1,b_2,b_3...b_\frac{n}{2}$，构造一个非严格单调增的序列$a_1,a_2,a_3....a_n$使得$b_i = a_i + a_{n-i+1}$成立

# 解答
其实不难发现，$a[\frac{n}{2}] = \lfloor b[n]/2\rfloor \ \ \ \ a[\frac{n}{2}+1] = \lceil b[n]/2 \rceil$
然后把这两个构造出来以后，就可以从倒数第二个开始构造了。构造的方法如下

 1. 令$j = n-i+1$,即$j$就是$b[i]$在$a$数组中的后面一半的那一部分
 2. 先令$a[j] = a[j-1]$看看前面的$a[i]$是否满足$a[i]\leq a[i+1]$如果满足，那么直接填进去。如果不满足，那么就令$a[i] = a[i+1]$然后$a[j]$的值就很明显了，肯定是$b[i] - a[i]$啦  

综上，整个数组就构造完了。然后输出就好咯！
代码:
```cpp
//
// Created by dhy on 18-12-15.
//
# include <iostream>
# include <cstring>
# include <string>
using namespace std;
const int MAXN = (int)2e6+10;
long long a[MAXN];
long long ans[MAXN];
int main(){
    int n;
    cin>>n;
    int mid = n/2;
    for(int i = 1;i<=n>>1;i++)cin>>a[i];
    ans[mid] = a[mid]>>1;
    ans[mid+1] = a[mid]-ans[mid];
    for(int i = mid-1,j=mid+2;i>=1&&j<=n;i--,j++){
        ans[j] = ans[j-1];
        long long diff = a[i]-ans[j];
        if(diff>ans[i+1])ans[i] = ans[i+1],ans[j] = a[i]-ans[i];
        else ans[i] = diff;
    }
    for(int i = 1;i<=n;i++)cout<<ans[i]<<' ';
    return 0;
}
```
注意一下`ans`数组不要开小了，我一开始不知道哪根筋不对了，把`ans`开成了$MAXN/2$然后肯定是WA了呀，于是乎就在`test 12`WA 了两次。

第一次做出CF的C题，好开心啊！