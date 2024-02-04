---
title: Poj2505
date: 2018-10-31 15:26:20 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
Description

Stan and Ollie play the game of multiplication by multiplying an integer p by one of the numbers 2 to 9. Stan always starts with p = 1, does his multiplication, then Ollie multiplies the number, then Stan and so on. Before a game starts, they draw an integer 1 < n < 4294967295 and the winner is who first reaches p >= n.
Input
Each line of input contains one integer number n.
Output
For each line of input output one line either 
Stan wins. 
or 
Ollie wins. 
assuming that both of them play perfectly.
Sample Input
162
17
34012226
Sample Output
Stan wins.
Ollie wins.
Stan wins.
# 翻译
就是给你一个数，然后从1开始乘，乘数是2-9，两个人轮流乘，先得到大于等于n得数的人胜
# 解答
先分析问题：
如果n在2-9之间，那么肯定是先手胜。是n局面。那么可以由p和n的转化，可以发现当n在9-18范围内，肯定是p的局面。这样一个**循环节** (我的感性理解)就为18。那么，我们就看看n有多少个这样的循环节，去除这些循环节以后，剩下的数是多少。如果剩下的数小于等于9，那么先手胜，否则，后手胜。
于是我们可以写下以下代码:
```cpp
# include <cstdio>
# include <iostream>
# include <cstring>
using namespace std;
int main(){
    long long n;
    while(scanf("%lld",&n)!=EOF) {
        while(n>18)n/=18;
        if (n <= 9)cout << "Stan wins."<<endl; else cout << "Ollie wins."<<endl;
    }
    return 0;
}
```
但是不用说，这样的代码是WA掉的，为什么呢？题目中有一句话**winner is who first reaches p >= n.** 也就是说，得到的数可以大于等于n。就说明除到最后可能出现向9.5个这样的循环节，那么因为整形是向下取整，肯定会WA掉，所以要把n的类型改成double即可AC。
AC代码:
```cpp
# include <cstdio>
# include <iostream>
# include <cstring>
using namespace std;
int main(){
    double n;
    while(scanf("%lf",&n)!=EOF) {
        while(n>18)n/=18;
        if (n <= 9)cout << "Stan wins."<<endl; else cout << "Ollie wins."<<endl;
    }
    return 0;
}
```
