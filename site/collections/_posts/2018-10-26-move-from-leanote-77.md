---
title: OKR-A Horrible Poem 题解 luogu3538
date: 2018-10-26 11:21:02 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
题目描述
Bytie boy has to learn a fragment of a certain poem by heart. The poem, following the best lines of modern art, is a long string consisting of lowercase English alphabet letters only. Obviously, it sounds horrible, but that is the least of Bytie's worries.
First and foremost, he completely forgot which fragment is he supposed to learn. And they all look quite difficult to memorize...
There is hope, however: some parts of the poem exhibit certain regularity. In particular, every now and then a fragment, say , is but a multiple repetition of another fragment, say  (in other words, , i.e., , where  is an integer). In such case we say that  is a full period of  (in particular, every string is its own full period).
If a given fragment has a short full period, Bytie's task will be easy. The question remains... which fragment was that?
Make a gift for Bytie - write a program that will read the whole poem as well as a list of fragments that Bytie suspects might be the one he is supposed to memorize, and for each of them determines its shortest full period.
给出一个由小写英文字母组成的字符串S，再给出q个询问，要求回答S某个子串的最短循环节。
如果字符串B是字符串A的循环节，那么A可以由B重复若干次得到。
# 输入输出格式
#  输入格式：
In the first line of the standard input there is a single integer  ().
In the second line there is a string of length  consisting of lowercase English alphabet letters-the poem.
We number the positions of its successive characters from 1 to .
The next line holds a single integer  () denoting the number of fragments.
Then the following  lines give queries, one per line.
Each query is a pair of integers  and  (), separated by a single space, such that the answer to the query should be the length of the shortest full period of the poem's fragment that begins at position  and ends at position .
In tests worth in total 42% of the points  holds in addition.
In some of those, worth 30% of points in total,  holds as well.
#  输出格式：
Your program should print  lines on the standard output.
The -th of these lines should hold a single integer - the answer to the -th query.
# 输入输出样例
#  输入样例# 1： 
```
8
aaabcabc
3
1 3
3 8
4 8
```
#  输出样例# 1：
```
1
3
5
```
# 解答
其实解决这道题的工具是哈希，但是精髓是线性筛素数。没错，这道题带有浓郁的数学味道。首先我们要明白一下几个东西(题解里告诉我的)
>1.如果$s$是$[l,r]$的循环节，那么$len_{[l,r]}$一定是$s$长度的倍数
2.如果$s$是$[l,r]$的循环节，那么[l,r-s]=[l+s,r]，正确性其实可以自己想一想，不难。
3.如果要使s的长度最小，我们可以枚举$len_{[l,r]}$的因数，从小到大枚举。
4.如果$s$是一个循环节，那么$ks k\in Z^*$也是一个循环节(前提是长度要小于区间长度)

那么怎么获得$len_{[l,r]}$的因数呢？这是一个问题，能想到这里，这道题就可以A了。首先，我们可以直接枚举，但是这样的复杂度是$O(\sqrt{n})$的，介于这道题死不要脸卡常(必须写快读，否则卡不过)，所以$O(\sqrt(n)$的复杂度过不了。那么我们看看算数基本定理，发现我们可以通过把长度拆分成若干质因数，然后通过不同质因数的组合，得到大小不同的质因数。
那么第一步，就是写出一个线筛：
```cpp
void prime(){
    for(int i = 2;i<=MAXN;i++){
        if(!not_prime[i]){
            prime_table[++prime_cnt] = i;
            min_prime_factor[i] = i;
        }
        for(int j = 1;j<=prime_cnt&&i*prime_table[j]<=MAXN;j++){
            not_prime[i*prime_table[j]] = true;
            min_prime_factor[i*prime_table[j]] = prime_table[j];
            if(!(i%prime_table[j]))break;
        }
    }
}
```
这里面我们用min_prime_factor[i]来表示i的最小质因数是多少，然后通过i/min_prime_factor[i]就可以表示另一个因数(可能是个合数)，然后又对另一个因数拆分，就可以得到i从大到小的不同因数啦(代码里面有说吗后面的一个储存i的质因数的数组factor为什么是递增的(不一定严格递增，但是不影响))。
接下来就是第二步啦！
第二步也很简单，就是判断$len_{[i,j]}$的每一个因数的长度是否可以构成一个循环节，如果可以，就把它分解了看看它的因数是不是可以，因为如果k是一个循环节，那么2k,3k也一定可以构成循环节。
一下就是我写的烂的不得了的代码咯，略略略！
```cpp

# include <cstring>
# include <cstdio>
using namespace std;
const int MAXN = 500010;
char str[MAXN];
int n;
unsigned long long Hash[MAXN];
const int base = 13131;
unsigned long long poww[MAXN];
int mod = 1e9+7;
int prime_table[MAXN];
bool not_prime[MAXN];
int min_prime_factor[MAXN];//min_prime_factor[i]表示i的最小质因子是多少
int factor[MAXN];
int factor_cnt;
int prime_cnt;
int read(){
    int x = 0,f = 1;
    static char c;
    c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c= getchar();}
    while(c>='0'&&c<='9')x = x*10+c-'0',c = getchar();
    return x*f;
}
void prime(){
    for(int i = 2;i<=MAXN;i++){
        if(!not_prime[i]){
            prime_table[++prime_cnt] = i;
            min_prime_factor[i] = i;
        }
        for(int j = 1;j<=prime_cnt&&i*prime_table[j]<=MAXN;j++){
            not_prime[i*prime_table[j]] = true;
            min_prime_factor[i*prime_table[j]] = prime_table[j];
            if(!(i%prime_table[j]))break;
        }
    }
}
void calPow(){
    poww[0] = 1;
    for(int i = 1;i<=n;i++){
        poww[i] = poww[i-1]*base;
    }
}
void cal_hash(){
    for(int i = 1;i<=n;i++){
        Hash[i] = Hash[i-1]*base+str[i]-'a'+1;
    }
}
unsigned long long getHash(int l,int r){//返回以s开始，包括s的，长度为n的区间的哈希
    return Hash[r]-Hash[l-1]*poww[r-l+1];
}
bool judge(int l,int r,int len){
    return getHash(l,r-len)==getHash(l+len,r);
}
int main() {
    n = read();
    scanf("%s",str+1);
    prime();
    calPow();
    cal_hash();
    int q;
    q = read();
    int l,r;
    while(q--){
        l = read();
        r = read();
        int len = r-l+1;
        if(judge(l,r,1)){
            printf("%d\n",1);
        }else{
            factor_cnt = 0;
            while(len!=1){
                factor[++factor_cnt] = min_prime_factor[len];
                len = len / min_prime_factor[len];//可以保证factor里面因数是递减的，原因应该可以想明白
                //因为min_prime_factor[i]储存的是i的最小质因数，不断这样计算下去，facotr里面的数会越来越小。
            }
            len = r-l+1;
            for(int i = 1;i<=factor_cnt;i++){
                if(judge(l,r,len/factor[i])){
                    len /= factor[i];
                }
            }
            printf("%d\n",len);
        }
    }
    return 0;
}
```