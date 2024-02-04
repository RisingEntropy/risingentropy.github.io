---
title: 【概率期望 [LightOJ 1265] Island of Survival
date: 2019-08-26 20:22:06 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
大概就是说有t只老虎，d只鹿，和你，有如下关系

 1. 老虎遇上鹿，鹿死
 2. 老虎遇上你，你死
 3. 你遇上鹿，鹿死不死无所谓
 4. 老虎遇上老虎，都死
 
只有老虎和鹿都死完的时候你才叫做生存，求你生存的概率
# 解答
其实有好几种做法，考虑DP的话可能不得行，因为清空数组的时候耗费的时间太多了，所以只能考虑结论题。
我们发现鹿的存在并不影响概率，所以只需要考虑老虎就行了。如果老虎有奇数条，那么概率就是0，如果有偶数条，记为2n条，可以有如下公式计算：$$P = \frac{2n\choose 2}{2n+1\choose 2}+\frac{2n-2\choose 2}{2n-2+1\choose 2}...\frac{2\choose 2}{2\choose 3}$$
然后这个式子它等于一个$$\frac{2n*(2n-1)}{(2n+1)*(2n)}*\frac{(2n-2)*(2n-3)}{(2n-1)(2n-2)}...\frac{2*1}{3*2}$$
然后约分以后它等于$$P = \frac{1}{2n+1}$$
所以$O(1)$的直接算就好了。
代码：
```cp
# include <iostream>
# include <cstring>
# include <cstdio>
# define clear(x) memset(x,0,sizeof(x))
using namespace std;
const int MAXN = 1010;
double dp[MAXN][MAXN];
void dfs(int t,int d){
    if(t>=2){
        dp[t-2][d]+=dp[t][d]*t/(t+d+1)*(t-1)/(t+d);
        dfs(t-2,d);
    }
    if(d){
        dp[t][d-1]+=dp[t][d]*2*t/(t+d+1)*d/(t+d);
        dfs(t,d-1);
    }
}
int main(){
    int T;scanf("%d",&T);
    int cases = 0;
    while (T--){
        int t,d;scanf("%d%d",&t,&d);
        // clear(dp);
        // dp[t][d] = 1;
        // dfs(t,d);
        // double ans = 0.0;
        // for(int i = 0;i<=d;i++)ans+=dp[0][i];
        // printf("Case %d: %.6lf\n",++cases,ans);//鬼知道为什么会TLE艹
        double ans = 0.0;
        if(t&1)printf("Case %d: %.6lf\n",++cases,0.0);
        else ans = 1.0/(t+1.0),printf("Case %d: %.6lf\n",++cases,ans);
    }
    return 0;
}
```