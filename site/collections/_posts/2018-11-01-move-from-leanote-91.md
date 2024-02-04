---
title: luogu P3396 哈希冲突
date: 2018-11-01 10:33:13 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
题目背景
此题约为NOIP提高组Day2T2难度。
# 题目描述
众所周知，模数的hash会产生冲突。例如，如果模的数p=7，那么4和11便冲突了。
B君对hash冲突很感兴趣。他会给出一个正整数序列value[]。
自然，B君会把这些数据存进hash池。第value[k]会被存进(k%p)这个池。这样就能造成很多冲突。
B君会给定许多个p和x，询问在模p时，x这个池内数的总和。
另外，B君会随时更改value[k]。每次更改立即生效。
保证1`<`=p`<`n1`<`=p`<`n.
# 输入输出格式
# 输入格式：
第一行，两个正整数n,m，其中n代表序列长度，m代表B君的操作次数。
第一行，n个正整数，代表初始序列。
接下来m行，首先是一个字符cmd，然后是两个整数x,y。
若cmd='A'，则询问在模x时，y池内数的总和。
若cmd='C'，则将value[x]修改为y。
# 输出格式：
对于每个询问输出一个正整数，进行回答。
# 输入输出样例
#  输入样例# 1： 
```
10 5
1 2 3 4 5 6 7 8 9 10
A 2 1
C 1 20
A 3 1
C 5 1
A 5 0
```
#  输出样例# 1： 
```
25
41
11
```
# 说明
#  样例解释
A 2 1的答案是1+3+5+7+9=25.
A 3 1的答案是20+4+7+10=41.
A 5 0的答案是1+10=11.数据规模
对于10%的数据，有n<=1000,m<=1000.
对于60%的数据，有n<=100000.m<=100000.
对于100%的数据，有n<=150000,m<=150000.
保证所有数据合法，且1<=value[i]<=1000.
# 解答
其实这道题数据比较水~~暴力模拟91分~~。暴力对抗随机数据好像比较强。暴力代码：
```cpp
// luogu-judger-enable-o2
# pragma GCC optimize("Ofast")
# include <cstdio>
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
const int MAXN =  150000;
int a[MAXN];
long long F[400][400];
int main(void){
    int n,m;
    n = read(),m = read();
    for(int i = 1;i<=n;i++){
        a[i] = read();
    }
    char c;
    int x,y;
    int ans = 0;
    char s[3];
    while(m--){
        scanf("%s",s);
        if(s[0]=='A'){
            x = read(),y = read();
            ans = 0;
            for(int i = y;i<=n;i+=x){
                ans+=a[i];
            }
            printf("%d\n",ans);
        }else{
            x = read();
            y = read();
            a[x] = y;
        }
    }
    return 0;
}
```
但是我们还是来想正解吧。正解是分块~~优雅的暴力~~ 它非常的骚。分块有如下特点
>就是对于一定数据范围内(一般取$\sqrt n$)，我们把它打表打出来，然后$O(1)$查询。又或者直接把一组数据分成$\sqrt n (+1)$块，每块$\lfloor \sqrt(n)\rfloor$个数据，然后直接乱搞.-----沃·镃基硕·德

我们把n分成两部分：小于$\sqrt(n)$的一部分，其余的一部分。然后对于小于根号n的部分。为什么呢？如果我们预处理全部的部分，那么查询复杂度是$O(n^2)$的。如果我们预处理出F[i][j]表示%i意义下，结果为j的值得和是多少，这样预处理复杂度也是$O(n^2)$的，虽然这样查询是$O(1)$。**对于这种查询和预处理/修改复杂度差别比较大的或者差不多但是都不够理想的(例如树状数组维护单点或者区间修改的前缀和)，我们通常用分块来做~~乱搞~~** 
于是乎对于这道题，我们预处理$\sqrt n$的部分，其余的直接暴力(暴力：你是不是看不起我???)至于修改，我们要把预处理的数组和原数组都同时修改了，修改代码如下
```cpp
x = read();
y = read();
for(int i = 1;i*i<=n;i++){
    F[i][x%i]+=y-a[x];
}
a[x] = y;
```
注意，在读入'A'和'C'的时候，**不可以getchar()** 因为这样会把换行符和回车读进来，要读入成一个字符串！
AC代码:
```cpp
// luogu-judger-enable-o2
# pragma GCC optimize("Ofast")
# include <cstdio>
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
const int MAXN =  150000;
int a[MAXN];
long long F[400][400];
int main(void){
    int n,m;
    n = read(),m = read();
    for(int i = 1;i<=n;i++){
        a[i] = read();
        for(int j = 1;j*j<=n;j++){
            F[j][i%j] += a[i];
        }
    }
    char s[3];
    int x,y;
    while(m--){
        scanf("%s",s);
        if(s[0]=='A'){
            x = read(),y = read();
            if(x*x<=n){
                printf("%d\n",F[x][y]);
            }else{
                int ans = 0;
                for(int i = y;i<=n;i+=x){
                    ans += a[i];
                }
                printf("%d\n",ans);
            }
        }else{
            x = read();
            y = read();
            for(int i = 1;i*i<=n;i++){
                F[i][x%i]+=y-a[x];
            }
            a[x] = y;
        }
    }
    return 0;
}
```