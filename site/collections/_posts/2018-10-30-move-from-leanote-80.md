---
title: luogu P1247 取火柴游戏
date: 2018-10-30 16:14:49 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
输入k及k个整数n1，n2，…，nk，表示有k堆火柴棒，第i堆火柴棒的根数为ni；接着便是你和计算机取火柴棒的对弈游戏。取的规则如下：每次可以从一堆中取走若干根火柴，也可以一堆全部取走，但不允许跨堆取，也不允许不取。
谁取走最后一根火柴为胜利者。
例如：k＝2，n1＝n2＝2，A代表你，P代表计算机，若决定A先取：
A：(2,2)→(1,2) {从一堆中取一根}
P：(1,2)→(1,1) {从另一堆中取一根}
A：(1,1)→(1,0)
P：(1,0)→ (0,0) {P胜利}
如果决定A后取：
P：(2,2)→(2,0)
A：(2,0)→ 0,0) {A胜利}
又如k＝3，n1=1，n2＝2，n3＝3，A决定后取：
P：(1,2,3)→(0,2,3)
A：(0,2,3)→(0,2,2)
A已将游戏归结为(2,2)的情况，不管P如何取A都必胜。
编一个程序，在给出初始状态之后，判断是先取必胜还是先取必败，如果是先取必胜，请输出第一次该如何取。如果是先取必败，则输出“lose”。
# 输入输出格式
#  输入格式：
第一行，一个正整数k
第二行，k个整数n1，n2，…，nk
# 输出格式:
如果是先取必胜，请在第一行输出两个整数a，b，表示第一次**从第b堆取出a个** 。第二行为第一次取火柴后的状态。如果有多种答案，则输出`<`b，a`>`字典序最小的答案(即b最小的前提下a最小)。
如果是先取必败，则输出“lose”。

# 输入输出样例
#  输入样例# 1：
```
3
3 6 9
```
#  输出样例# 1： 
```
4 3
3 6 5
```
#  输入样例# 2： 
```
4
15 22 19 10
```
#  输出样例# 2： 
```
lose
```
# 解答
这道题其实比较考验对异或和的理解。对于异或和与是否存在先手胜的策略问题参加[我的博客](http://denghaoyu.leanote.com/post/%E5%8D%9A%E5%BC%88%E8%AE%BA)
但是这道题比较磨人，要输出方案。其实只要理解到异或和就行。
根据某个定理，设X为$a_1\ xor a_2\ ...\ xor a_n$的异或和，如果X不等于0，那么不仅存在先手胜的策略，而且存在$a_i\ xor\ X = 0$，那么我们就拿一些石子，拿完以后使所有石子异或和为0，也就是说，后手局的时候，永远不存在可以胜的策略。对于这个$a_i$是多少呢？由于要使字典序最小，那么我们从头开始找，看看$a_i\ xor\ X$是否小于$a_i$因为是取石子游戏，不能不取，所以有如上结论。
还有一个疑惑点：为什么当X = 0时，任意$a_i\ xor\ X=0$。证明如下
$$X = a_1\ xor\ a_2\ xor\ ...\ xor\ a_n$$
由[异或的运算性质](https://baike.baidu.com/item/%E5%BC%82%E6%88%96)（异或的结合律）可得：
$$a_1\ xor\ a_2\ xor...xor\ (a_i\ xor\ X)\ xor ...xor\ a_n = 0$$
$$Q.E.D$$

AC代码：
```cpp
# include <cstdio>
# include <cstring>
using namespace std;
long long read(){
    long long x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
    while(c>='0'&&c<='9'){x = x*10+c-'0';c = getchar();}
    return x*f;
}
long long a[500010];
int main(void){
    long long k = 0;
    k = read();
    long long X = 0;
    long long temp;
    for(int i = 1;i<=k;i++){
        temp = read();
        a[i] = temp;
        X^=temp;
    }
    if(!X){
        printf("lose");
    }else{
        for(int i = 1;i<=k;i++){
            if((a[i]^X)<a[i]&&((a[i]^X)^X)==0){
                printf("%lld %d\n",a[i]-(a[i]^X),i);
                a[i] = a[i]^X;
                break;
            }
        }
        for(int i = 1;i<=k;i++)printf("%lld ",a[i]);
    }
    return 0;
}
```
