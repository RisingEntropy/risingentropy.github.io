---
title: unknown title
date: 2018-11-06 14:34:18 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
#  题目描述
有q次操作，每次操作是以下两种：
1、 加入一个数到集合中
2、 查询，查询当前数字与集合中的数字的最大异或值，最大and值，最大or值
#  输入
第一行1个正整数Q表示操作次数
接下来Q行，每行2个数字，第一个数字是操作序号OP（1,2），第二个数字是X表示操作的数字
#  输出
输出查询次数行，每行3个整数，空格隔开，分别表示最大异或值，最大and值，最大or值
#  样例输入
【输入样例1】
```
5
1 2
1 3
2 4
1 5
2 7
```
【输出样例1】
```
7 0 7
5 5 7
```
【样例解释1】
询问4时，已插入2、3，最大异或值为4^3=7，最大and值为4&3或4&2=0，最大or值为4|3=7
询问7时，已插入2、3、5，最大异或值为7^2=5，最大and值为7&5=5，最大or值为7|2=7|3=7|5=7
【输入样例2】
```
10
1 194570
1 202332
1 802413
2 234800
1 1011194
2 1021030
2 715144
2 720841
1 7684
2 85165
```
【输出样例2】
```
1026909 201744 1032061
879724 984162 1048062
655316 682376 1043962
649621 683464 1048571
926039 85160 1011199
```
提示
对于%10的数据1<=Q<=5000
对于另%10的数据保证 X<1024
对于另%40的数据保证1<=Q<=100000
对于所有数据保证1<=Q<=1000000,1<=X<=2^20 保证第一个操作为1操作。
# 解答
·一道01trie的题。对于异或，就是构建一颗trie，然后从高位开始贪心，往1贪。关于构建trie，主要对trie代码实现是否足够熟悉。
·对于与
由于与的运算特点，两个都是1的情况才都是1。我们使用bit[x][i]表示x的第i位是多少。那么对于一个bit[x][i]=1, 我们应该选取的那个数的第i位也最好是1,如果有1，那么我们当然就选咯！
·对于或
只要有1个1，结果就是1。如果当前的数的i位是1的话，那么就不需要从集合中找一个第i位为1的数了。如果为0的话，就需要从集合中找到第i位是1的数。
至于以上怎么实现呢？一个一个爆搜？？？$tan\ 90$我们可以通过某些标记，给他构造出来！采用dfs的思想，我们把已知的一个数的每一位变成0或者1，这样可以得到它的"子集"这个子集需要子集理解一下。然后判断集合中是否有需要的数，就只需要看看这个“子集”就可以了，最终会把它给构造出来！
AC代码
```cpp
# include <cstdio>
# include <cstring>
# include <cmath>
# include <algorithm>
# include <set>
# include <queue>
# include <iostream>
# include <stack>
# pragma GCC optimize("Ofast")
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const int MAXN = (1<<21)+5;
int trie[MAXN][2];
bool sub[MAXN];
int ptr;
int mark(int x){//其实就是把一个数的每一位，算出“子集”
    sub[x] = true;
    for(int i = 19;i>=0;i--)
        if((x>>i&1)&&(!sub[x^(1<<i)]))
            mark(x^(1<<i));
}
void insert(int x){
    int p = 0,k;//trie插入操作
    for(int i = 19;~i;i--){
        k = x>>i&1?1:0;
        if(!trie[p][k])
            trie[p][k] = ++ptr;
        p = trie[p][k];
    }
}
int queryXor(int x){
    int ans =0,k,p = 0;
    for(int i = 19;~i;i--){//trie查询操作
        k = (x>>i&1?0:1);//注意这里0和1是反的，原因参见异或的运算规律
        if(trie[p][k]){
            p = trie[p][k];
            if(k)ans|=1<<i;
        }else{
            p = trie[p][k^1];
            if(k^1)ans|=1<<i;
        }
    }
    return ans;
}
int queryAnd(int x){//查询与
    int ans = 0;
     for(int i = 19;~i;i--)
         if((x>>i&1)&&sub[ans|1<<i])//如果这一位是1，并且集合中存在一个这一位也是1的数
             ans|=1<<i;
    return ans;
}
int queryOr(int x){//查询或
    int ans = 0;
    for(int i = 19;~i;i--)
        if(!(x&(1<<i))&&sub[ans|1<<i])//如果这一位不为1，就看看集合中存不存在这一位为1的数
            ans|=1<<i;
    return ans;
}
int main(){
    int Q;
    Q = read();
    int x,y;
    while(Q--){
        x = read(),y = read();
        if(x==1){
            insert(y);
            mark(y);
        }else{//注意要查询的是集合中的符合条件的数，所以要算一下再输出
            printf("%d %d %d\n",queryXor(y)^y,queryAnd(y)&y,queryOr(y)|y);
        }
    }
    return 0;
}
```