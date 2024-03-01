---
title: luogu P2252 取石子游戏
date: 2018-10-30 20:32:57 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
有两堆石子，数量任意，可以不同。游戏开始由两个人轮流取石子。游戏规定，每次有两种不同的取法，一是可以在任意的一堆中取走任意多的石子；二是可以在两堆中同时取走相同数量的石子。最后把石子全部取完者为胜者。现在给出初始的两堆石子的数目，你先取，假设双方都采取最好的策略，问最后你是胜者还是败者。

# 输入输出格式
#  输入格式：
输入共一行。
第一行共两个数a, b，表示石子的初始情况。
#  输出格式：
输出共一行。
第一行为一个数字1、0或-1，如果最后你是胜利者则为1；若失败则为0；若结果无法确定则为-1。
# 输入输出样例
#  输入样例# 1： 
```
8 4
```
#  输出样例# 1： 
```
1
```
# 解答
其实这道题不要想多了去用SG函数。因为我目前对SG函数还不是特别了解。就是去看看几个经典的博弈论模型就行。这道题是一个典型的威佐夫博弈。
一下是介绍：
>有两堆各若干的物品，两人轮流从其中一堆取至少一件物品，至多不限，或从两堆中同时取相同件物品，规定最后取完者胜利。
直接说结论了，若两堆物品的初始值为（x，y），且x`<`y，则另z=y-x；
记w=（int）[（（sqrt（5）+1）/2）*z ]；
若w=x，则先手必败，否则先手必胜。

AC代码:
```cpp
# include <iostream>
using namespace std;
int main(void){
    int n,m;
    cin>>n>>m;
    if(n<m){n=n^m;m=m^n;n=n^m;}
    if(int((n-m)*1.618)==m)cout<<0;else cout<<1;
    return 0;
}
```