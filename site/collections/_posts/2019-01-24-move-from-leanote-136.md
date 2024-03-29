---
title: bzoj 4521 Cqoi2016手机号码
date: 2019-01-24 16:31:07 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Description
人们选择手机号码时都希望号码好记、吉利。比如号码中含有几位相邻的相同数字、不含谐音不
吉利的数字等。手机运营商在发行新号码时也会考虑这些因素，从号段中选取含有某些特征的号
码单独出售。为了便于前期规划，运营商希望开发一个工具来自动统计号段中满足特征的号码数
量。
工具需要检测的号码特征有两个：号码中要出现至少3个相邻的相同数字，号码中不能同
时出现8和4。号码必须同时包含两个特征才满足条件。满足条件的号码例如：13000988721、
23333333333、14444101000。而不满足条件的号码例如：1015400080、10010012022。
手机号码一定是11位数，前不含前导的0。工具接收两个数L和R，自动统计出[L,R]区间
内所有满足条件的号码数量。L和R也是11位的手机号码。
#  Input
输入文件内容只有一行，为空格分隔的2个正整数L,R。
10^10 < =  L < =  R < 10^11
#  Output
输出文件内容只有一行，为1个整数，表示满足条件的手机号数量。

#  Sample Input
```
12121284000 12121285550
```
#  Sample Output
```
5
```
样例解释

满足条件的号码： 12121285000、 12121285111、 12121285222、 12121285333、 12121285550
# 解答
数位DP是最套路的DP。暴力设计状态：$dp[i][j][k][l][m][n]$表示第$i$位，上一位为$j$，连续几个数的长度为$k$，$m$和$n$分别表示是否出现过4和8.好了开始DP就好了。
代码如下
```cpp
# include<cstdio>
# include<cstring>
# include <iostream>
using namespace std;
long long F[12][10][4][2][2];
int num[15];
long long dfs(int len,int nm,int st,bool limit,bool has4,bool has8){
    if(len==0) {
         return st>=3;
    }
    if(!limit&&F[len][nm][st][has4][has8]!=-1)return F[len][nm][st][has4][has8];
    int mx = limit?num[len]:9;long long ans = 0;
    for(int i = 0;i<=mx;i++){
        if(len==11&&i==0)continue;
        if((has4&&i==8)||(has8&&i==4))continue;
        int continous = 1;
        if(st==3)continous = 3;else
        if(i==nm)continous = st+1;
        ans += dfs(len-1,i,continous,limit&&i==mx,has4||i==4,has8||i==8);
    }
    if(!limit)F[len][nm][st][has4][has8] = ans;
    return ans;

}
long long work(long long n){
    int len = 0;
    while(n)num[++len] = n%10,n/=10;
    return dfs(len,10,0,true,false,false);
}
int main(){
    memset(F,-1,sizeof(F));
    long long a,b;
    cin>>a>>b;
    if(a<=10000000000)cout<<work(b);else
    cout<<work(b)-work(a-1);
    return 0;
}
```