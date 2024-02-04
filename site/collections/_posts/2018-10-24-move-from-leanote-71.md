---
title:   Codeforces Round # 503 (by SIS, Div. 2) C Elections
date: 2018-10-24 08:40:31 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Berland地区的腐败现象非常常见。

马上有一场选举，你事先知道了选民和政党的数量，分别为  $n$  和  $m$  ，对于每一位选民，你知道他将要选举哪一个政党，不过，每一位选民都会在接受一定数额的金钱之后改变他的主意。如果你给第  $i$  位选民  $c_i$  数额的比特币，他就会选举任何你希望他选举的政党。

你的目的是让Berland的联合党赢得这场选举，联合党必须拥有比其它政党都多的选票，在此基础之上，你希望花费的比特币尽可能少。

输入格式

第一行包含两个整数  $n$  和  $m$ .

接下来  $n$  行每一行两个整数——  $p_i$  和  $c_i$  ，这一位选民将会选举政党的编号，和使他改变主意的最少比特币数额。

特别地，联合党的编号是1.

输出格式

一个整数，使联合党赢得选举所需花费的最少比特币数额。

# 输入输出样例
```
输入样例# 1： 
1 2
1 100
输出样例# 1： 
0
输入样例# 2： 
5 5
2 100
3 200
4 300
5 400
5 900
输出样例# 2： 
500
输入样例# 3： 
5 5
2 100
3 200
4 300
5 800
5 900
输出样例# 3： 
600
```
# 解答
其实这个题很明显是个贪心的题~~动态规划我不会~~。但是这个题的贪心非常有意思，体现了**正难则反**的思想。一开始，我的贪心策略是用一个堆存所有的党派，每个党派里面又用堆来存支持者，然后从支持者人数多的党派里面选取价格最小的来行贿。很明显，这样的贪心策略是不正确的！那么什么是正确的贪心策略呢？首先我们可以发现如果从投票者作为出发点，来进行贪心，这样似乎很有难度。那么我们考虑从答案出发，枚举最后的答案。假设目前枚举的答案是A，除了1号党派以外，其他所有党派的支持人数都应该**严格小于**1号党派。也就是说，我们必须把其它所有支持人数大于A的党派里面价格最小的几个行贿了。如果最后1号党派的支持人数仍然没有达到A,那么我们就应该从小到大，把可以行贿(可以行贿的意思是之前没有行贿过)的人全部行贿了，直到最后支持者人数为A。我们只需要从1...n/2来枚举每个答案就行了。
但是要注意一个个坑：
1.如果只有1号党派，那么最后应该判断一下cost是否被更改过，如果没有，应该输出0.
以下是AC代码：
```cpp
# include <iostream>
# include <algorithm>
# include <cstdio>
# include <queue>
# include <vector>
# include <cstring>
using namespace std;
typedef pair<int,int> voter;//第一个表示价格，第二个表示id
vector<voter> parties[3010];
int used[3010];
voter voters[3010];
inline long long min(long long a,long long b){return a>b?b:a;}
int main(void){
    ios::sync_with_stdio(false);
    int n,m;
    cin>>n>>m;
    int pi,ci;
    for(int i = 1;i<=n;i++){
        cin>>pi>>ci;
        parties[pi].push_back(make_pair(ci,i));
        voters[i] = make_pair(ci,i);
    }
    sort(voters+1,voters+n+1);
    for(int i = 1;i<=m;i++){
        sort(parties[i].begin(),parties[i].end());
    }
    long long cost = 0x7fffffffffff;
    for(int supporter = parties[1].size();supporter<=n+1>>1;supporter++){//枚举每一个最后的支持者
        long long current_cost = 0;
        int current_supporter = parties[1].size();
        memset(used,false,sizeof(used));
        for(int i = 0;i<parties[1].size();i++){
            used[parties[1][i].second] = true;
        }
        for(int i = 2;i<=m;i++){
            if(parties[i].size()>=supporter){
                for(int k = 0;k<parties[i].size();k++){//把多出的部分的人必须行贿
                    current_cost+=parties[i][k].first;
                    used[parties[i][k].second] = true;
                    current_supporter++;
                    if(parties[i].size()-k-1<supporter){
                        break;
                    }
                }
            }
        }
        if(current_supporter<=supporter){//就是说把多出来的人全部行贿以后，还是不够，那么就要从小到大来行贿了
            for(int i = 1;i<=n&&current_supporter<supporter;i++){
                if(!used[voters[i].second]){//从小到大排序，把对应编号的voter标记为使用过
					current_supporter++;
                    current_cost+=voters[i].first;
                    used[voters[i].second] = true;
                }
            }
        }
        cost = min(cost,current_cost);
    }
    cout<<(cost==0x7fffffffffff?0:cost);
    return 0;
}
```
