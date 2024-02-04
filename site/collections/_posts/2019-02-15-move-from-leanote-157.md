---
title: CF1114E
date: 2019-02-15 13:48:01 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
[Codeforces 1114E Arithmetic Progression](https://codeforces.com/contest/1114/problem/E)
题目大意：给你一个打乱了顺序的**等差数列**，你有60次询问，每次可以询问每个位置的数是多少，或者可以询问有没有严格大于x的数。然后请你求出这个序列的最小值和公差。
# 解答
我对不起lyt老师，教了我等差数列，我还是不会。这道题，二分最大值+随机。先二分查找出最大的数，大约用去30次机会，在随机获取30个数，求个gcd，就可以求出公差了。这样错误的概率为$ 1.86185·10^{-9}.$(数据来源：官方题解)。毕竟这是我做的第一道交互题，不知道咋调试。太弱了。注意一下，rand函数要自己写一个，毕竟std里面的范围比较小，如果出题人比较毒瘤，把数据全部丢到那个范围以外，卡死我。
rand函数如下：
```
inline int rnd(){    //自己的rand
    static int seed=19260817;//光速逃
    return seed=(((seed*666666ll+20050818)%998244353)^1000000754)%10902060817;
}
```

```cpp
# include <cstdio>
# include <algorithm>
# include <stdio.h>
# include <vector>
# include <iostream>
using namespace std;
const int MAXN = 100010;
using namespace std;
int asks = 0;
int getBigger(int x){
    cout<<"> "<<x<<endl;
    cout.flush();
    int s;cin>>s;
    return s;
}
int getVal(int pos){
    cout<<"? "<<pos<<endl;
    cout.flush();
    int s;cin>>s;
    return s;
}
inline int rnd(){    //自己的rand
    static int seed=19260817;
    return seed=(((seed*666666ll+20050818)%998244353)^1000000754)%10902060817;
}
int a[70];
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int main(){
    int n;
    cin>>n;
    cout.flush();
    int ans ;
    int l = 0,r = (int)1e9+1;
    while(l<=r){
        int mid = l+r>>1;
        asks++;
        if(getBigger(mid))l = mid+1;
        else r = mid-1,ans = mid;
    }
    int maxx = ans;
    int d = 0;
    for(int i = 1;i<=59-asks;i++)a[i] = getVal(rnd()%n+1);
    for(int i = 1;i<=59-asks;i++){
        for(int j = i+1;j<59-asks;j++)d = gcd(d,abs(a[i]-a[j]));
    }
    cout<<"! "<<maxx-d*(n-1)<<' '<<d;
    return 0;
}
```