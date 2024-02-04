---
title: P2890 [USACO07OPEN]便宜的回文Cheapest Palindrome
date: 2019-02-14 22:25:02 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
追踪每头奶牛的去向是一件棘手的任务，为此农夫约翰安装了一套自动系统。他在每头牛身上安装了一个电子身份标签，奶牛通过扫描器的时候，系统可以读取奶牛的身份信息。目前，每个身份都是由一个字符串组成的，长度为M (1 ≤ M ≤ 2000)，所有的字符都取自N个、小写字母。奶牛们都是顽皮的动物，有时它们会在通过扫描器的时候倒着走，这样一个原来身份为abcb 的奶牛就可能有两个不同的身份了（abcb 和 bcba），而如果身份是 abcba 的话就不会有这个问题了。、约翰想改变奶牛们的身份，使他们不管怎么走读起来都一样。比如说，abcb可以在最后加个 a，变成回文 abcba；也可以在前面加上 bcb，变成回文 bcbabcb；或者去除字母 a，保留的 bcb 也是一条回文。总之，约翰可以在任意位置删除或插入一些字符使原字符串变成回文。不巧的是，身份标签每增加或删除一个字母都要付出相应的费用（0 ≤ 费用代价 ≤ 10000）。给定一头奶牛的身份标签和增加或删除相关字母的费用，找出把原来字符串变成回文字符串的最小费用。注意空字符串也是回文。
#  输入
第一行：两个用空格分开的整数：N和M。
第二行：一个长度恰好为M的字符串，代表初始的身份标签。
第三行到第N + 2行：每行为一个用空格分开的三元组：其中包括一个字符和两个整数，分别
表示增加或删除这个字符的费用。
#  输出
只有一个整数，表示改造这个身份标签的最小费用。
#  样例输入
```
3 4
abcb
a 1000 1100
b 350 700
c 200 800
```
#  样例输出
```
900
```
# 解答
d。。。。dp。用dp[i][j]表示把区间[i,j]全部转化成回文的所需最小价格。但是怎么转移？我们~别人~~想，如果[i+1,j]都被还原成了回文，现在要拓展到[i,j]只需要在末尾加一个或者把这个s[i]删掉就可以了，对于[i,j-1]也是一样，比一下那个小，就选哪个。
代码：
```cpp
//
// Created by dhy on 19-2-14.
//
# include <cstring>
# include <iostream>
using namespace std;
const int MAXN = 2005;
int s[MAXN];int dp[MAXN][MAXN];
int del[MAXN],add[MAXN];
int main(){
    char c;
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
    int n,m;
    cin>>n>>m;
    for(int i = 1;i<=m;i++){
        cin>>c;
        s[i] = c-'a';
    }
    int d,a;
    for(int i = 1;i<=n;i++){
        cin>>c;cin>>a>>d;
        del[c-'a'] = d;
        add[c-'a'] = a;
    }
    for(int l = 2;l<=m;l++){
        for(int i = 1;i+l-1<=m;i++){
            int j = i+l-1;
            if(s[i]==s[j])dp[i][j] = dp[i+1][j-1];
            else{
                dp[i][j] = min(dp[i+1][j]+min(add[s[i]],del[s[i]]),dp[i][j-1]+min(add[s[j]],del[s[j]]));
            }
        }
    }
    cout<<dp[1][m];
    return 0;
}

```