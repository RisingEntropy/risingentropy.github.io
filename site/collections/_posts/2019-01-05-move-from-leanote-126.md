---
title: P3957 跳房子
date: 2019-01-05 23:12:47 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
跳房子，也叫跳飞机，是一种世界性的儿童游戏，也是中国民间传统的体育游戏之一。 跳房子的游戏规则如下：

在地面上确定一个起点，然后在起点右侧画 $n$ 个格子，这些格子都在同一条直线上。每 个格子内有一个数字（整数），表示到达这个格子能得到的分数。玩家第一次从起点开始向 右跳， 跳到起点右侧的一个格子内。第二次再从当前位置继续向右跳，依此类推。规则规定： 玩家每次都必须跳到当前位置右侧的一个格子内。玩家可以在任意时刻结束游戏，获得的分 数为曾经到达过的格子中的数字之和。

现在小 R 研发了一款弹跳机器人来参加这个游戏。但是这个机器人有一个非常严重的 缺陷，它每次向右弹跳的距离只能为固定的 $d$。小 R 希望改进他的机器人，如果他花 $g$ 个金 币改进他的机器人，那么他的机器人灵活性就能增加 $g$， 但是需要注意的是，每次弹跳的距 离至少为 $1$。 具体而言， 当$g < d$时， 他的机器人每次可以选择向右弹跳的距离为 $d-g, d-g+1, d-g+2， …， d+g-2， d+g-1， d+g$； 否则（当$g ≥ d$时），他的机器人每次可以选择向右弹跳的 距离为 $1， 2， 3， …， d+g-2， d+g-1， d+g$.

现在小 R 希望获得至少 $k$ 分，请问他至少要花多少金币来改造他的机器人
# 输入格式
第一行三个正整数 $n， d， k$， 分别表示格子的数目， 改进前机器人弹跳的固定距离， 以 及希望至少获得的分数。 相邻两个数之间用一个空格隔开。

接下来 $n$ 行，每行两个正整数$xi, si$，分别表示起点到第$i$个格子的距离以及第$i$个格子的 分数。 两个数之间用一个空格隔开。 保证$xi$按递增顺序输入。
# 输出格式
共一行，一个整数，表示至少要花多少金币来改造他的机器人。若无论如何他都无法获 得至少 $k$ 分，输出$-1$。
# 输入输出样例
#  输入样例# 1： 
```
7 4 10
2 6
5 -3
10 3
11 -3
13 1
17 6
20 2
```
输出样例# 1： 
```
2
```
输入样例# 2： 
```
7 4 20
2 6
5 -3
10 3
11 -3
13 1
17 6
20 2
```
输出样例# 2： 
```
-1
```
# 解释
【输入输出样例 1 说明】

花费 2 个金币改进后， 小 R 的机器人依次选择的向右弹跳的距离分别为 2， 3， 5， 3， 4， 3， 先后到达的位置分别为 2， 5， 10， 13， 17， 20， 对应 1, 2, 3, 5, 6, 7 这 6 个格子。这些格 子中的数字之和 15 即为小 R 获得的分数。

【输入输出样例 1 说明】

花费 2 个金币改进后， 小 R 的机器人依次选择的向右弹跳的距离分别为 2， 3， 5， 3， 4， 3， 先后到达的位置分别为 2， 5， 10， 13， 17， 20， 对应 1, 2, 3, 5, 6, 7 这 6 个格子。这些格 子中的数字之和 15 即为小 R 获得的分数。

本题共 10 组测试数据，每组数据 10 分。对于全部的数据满足1 ≤ n ≤ 500000, 1 ≤ d ≤ 2000, 1 ≤ xi,k ≤ 109, |si| < 105。

对于第 1， 2 组测试数据， n ≤ 10；

对于第 3， 4， 5 组测试数据， n ≤ 500

对于第 6， 7， 8 组测试数据， d = 1
# 解答
二分+dp
首先考虑如何dp
其实状态转移方程比较好想吧，就是向前面找，找到可以接上然后如果得分比较高就更新解。如下
$$F[i] = \underset{k(x[k]+max_step>=x[i])\leq j<i}{a} (F[i],F[j]+a[i])$$
max_step其实就是二分出的答案g+d的距离
我们还需要预处理一个min_step,值是d-g,还需要特判一下它是否小于0，如小于0，改为1(为什么呢？读题就知道了，最小跳一步)。然后看到这个方程，日常单调队列，维护j上升，F[j]也上升的序列，然后如果存在F[j]>k，那么这样是可行的，直接return true;
**注意，跑长度的时候，要跑xi编号，而不是直接跑距离，这样会爆掉**
代码：
```cpp
//
// Created by dhy on 19-1-5.
//
# include <iostream>
# include <deque>
# include <cstring>
using namespace std;
const int MAXN = 500010;
int x[MAXN];
int s[MAXN];
int n,d,k;
long long dp[MAXN];
bool work(int g){
    int maxx = d+g;
    int minn = d-g<=0?1:d-g;//最小距离不能为负的，就是最小往前跳的位置比如
    //d = 999, g = 10，就是说只有距离大于999-10=989的点才能转移过来
    //又比如d = 10 g = 20， 那么从1的距离就可以跳过来,就是跳的最小距离是1，不能为负的
    deque<int> q;
    memset(dp,0x8c, sizeof(dp));//赋值为很小的值
    int cur = 0;
    dp[0] = 0;//初始化状态
    for(int i = 1;i<=n;i++){
        for(;cur<i&&x[cur]+minn<=x[i];cur++){//预处理出j<i并且能够通过最小跳跃距离跳到i
            if(q.empty())q.push_back(cur);
            else {
                if(dp[cur] == dp[MAXN-5])continue;
                while (!q.empty()&&dp[q.back()]<=dp[cur])q.pop_back();
                q.push_back(cur);
            }
        }
        while (!q.empty()&&x[q.front()]+maxx<x[i])q.pop_front();//排除队头不合法的解
        if(!q.empty())dp[i] = dp[q.front()]+s[i];//转移
        else dp[i] = dp[MAXN-6];//如果不能转移，那么这个点就到不了，防止影响，改为很小的值(其实不改也可以，因为dp数组早就以及设为-INF了)
        if(dp[i]>=k)return true;
    }
    return false;
}
int main(){
    cin>>n>>d>>k;
    for(int i = 1;i<=n;i++){
        cin>>x[i]>>s[i];
    }
    int l = 0,r = x[n];
    while(l<r){//快乐的二分
        int mid = l+r>>1;
        if(work(mid))r = mid;
        else l = mid+1;
    }
    cout<<l;
    return 0;
};
//NOIP2019 RP++
```