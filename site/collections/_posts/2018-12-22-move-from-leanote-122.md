---
title: poj1821
date: 2018-12-22 23:13:23 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面

A team of k (1 <= K <= 100) workers should paint a fence which contains N (1 <= N <= 16 000) planks numbered from 1 to N from left to right. Each worker i (1 <= i <= K) should sit in front of the plank Si and he may paint only a compact interval (this means that the planks from the interval should be consecutive). This interval should contain the Si plank. Also a worker should not paint more than Li planks and for each painted plank he should receive Pi $ (1 <= Pi <= 10 000). A plank should be painted by no more than one worker. All the numbers Si should be distinct. 

Being the team's leader you want to determine for each worker the interval that he should paint, knowing that the total income should be maximal. The total income represents the sum of the workers personal income. 

Write a program that determines the total maximal income obtained by the K workers. 
#  Input

The input contains: 
Input 

N K 
L1 P1 S1 
L2 P2 S2 
... 
LK PK SK 

#  Semnification 

N -the number of the planks; K ? the number of the workers 
Li -the maximal number of planks that can be painted by worker i 
Pi -the sum received by worker i for a painted plank 
Si -the plank in front of which sits the worker i 
#  Output

The output contains a single integer, the total maximal income.
#  Sample Input
```
8 4
3 2 2
3 2 3
3 3 5
1 1 7 
```
#  Sample Output
```
17
```
#  Hint

Explanation of the sample: 

the worker 1 paints the interval [1, 2]; 

the worker 2 paints the interval [3, 4]; 

the worker 3 paints the interval [5, 7]; 

the worker 4 does not paint any plank 
Source

# 解答
首先设计状态，我们用$F[i,j]$表示前$i$个工人粉刷前j个木板的最大收益，那么如何转移呢？

 1. 第$i$个工匠可以什么也不刷，此时$F[i][j]=F[i-1,j]$
 2. 第$j$块木板可以空着不刷，此时$F[i][j] = F[i][j-1]$
 3. 第$i$个工匠粉刷第$K+1$到第$j$块木板。由题意，该工匠粉刷总数不能超过$Li$，且必须粉刷$Si$，所以需要满足：$k+1\leq S_i\leq Li$并且$j-k\leq Li$于是乎就有$$F[i,j] = \underset{j-Li\leq k\leq Si-1}{max}{F[i-1,k]+Pi*(j-k)}其中j\geq Si$$


如何优化呢？不难发现如下规律

 1. P_i *j除定值$i$外，只有状态变量$j$
 2. F[i-1,k]-p_i*k除$i$以外，只有决策变量$k$

那么状态转移方程可以转移为$$F[i,j] = \underset{j-Li\leq k\leq Si-1}{max}{F[i-1,k]-Pi*k}+Pi*j其中j\geq Si$$
然后就可以用上单调队列优化的dp了。
我们发现对于$k_1$和$k_2$如果k1比k2更靠后，那么随着j的增长，k2会比k1更先被淘汰，并且，如果k1和k2满足$$F[i-1,k1]-pi*k1\geq F[i-1,k2]-pi*k2$$那么就意味着，k2永远不会成为最优解，那么直接排除候选集合。综上，我们只需要维护一个决策点k单调递增，数值$F[i-1,k]-Pi*k$单调递减的队列。只有这个队列中的决策才有可能在某一时刻成为最优决策。这个队列满足以下条件：

 1. 当j变大时，检查队头元素，把小于$j-Li$的决策出队
 2. 查询最优解时，队头就是所求
 3. 有一个新的决策要加入集合时，在队尾检查$F[i-1,k]-Pi*k$的单调性，把无用决策从队尾直接出队，最后把新决策加入队尾。
 
那么对于这道题，从内层循环开始时(j=Si)，建立一个空的单调队列，把$[max(S_i-L_i,0),S_i-1]$中的决策依次加入候选集合，对于每个$j=Si~N$,先在队头检查决策合法性，然后取队头为最优决策进行状态转移。每个决策入队出队依次，转移复杂度$O(1)$总体复杂度$O(MN)$
代码：
```cpp
//
// Created by dhy on 18-12-22.
//
# include <cstring>
# include <iostream>
# include <deque>
# include <algorithm>
using namespace std;
struct worker{int si,li,pi;}workers[110];
bool operator<(const worker &w1,const worker &w2){return w1.si<w2.si;}
int F[110][16010];
int cal(int i,int k){//前面提到过的小优化，方便计算
    return F[i-1][k]-workers[i].pi*k;
}
int n,m;
int main() {
    cin>>n>>m;
    for(int i = 1;i<=m;i++)cin>>workers[i].li>>workers[i].pi>>workers[i].si;
    sort(workers+1,workers+m+1);//按Si从大到小排序，这样就可以愉快地按线性dp的方式来啦
    for(int i = 1;i<=m;i++){
        deque<int> q;//这里我采用双端队列，方便维护这个单调队列
        for(int k = max(0,workers[i].si-workers[i].li);k <= workers[i].si-1;k++){
            //int k = max(0,workers[i].si-workers[i].li)是为了强制包含si，然后枚举从si
之前的哪个木板开始刷(题目说了是连续的)
            //k <= workers[i].si-1是为了防止把si这一块刷2次
            while(!q.empty()&&cal(i,q.back())<=cal(i,k))q.pop_back();//排除队列里面根本不可能出现在决策的集合
            q.push_back(k);//把当且决策加入集合
        }
        for(int j = 1;j<=n;j++){//开始枚举每一块木板
            F[i][j] = max(F[i-1][j],F[i][j-1]);//不粉刷时的转移
            if(j>=workers[i].si){//粉刷k+1~j块木板的转移
                while(!q.empty()&&q.front()<j-workers[i].li)q.pop_front();//排除不合法的决策
                if(!q.empty())F[i][j] = max(F[i][j],cal(i,q.front())+workers[i].pi*j);//队列飞控时，取队头进行状态转移
            }
        }
    }
    cout<<F[m][n]<<endl;
    return 0;
}
```