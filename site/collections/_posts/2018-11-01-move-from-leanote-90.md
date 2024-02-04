---
title: luogu P2320 [HNOI2006]鬼谷子的钱袋
date: 2018-11-01 15:42:10 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题目描述
鬼谷子非常聪明，正因为这样，他非常繁忙，经常有各诸侯车的特派员前来向他咨询时政。
有一天，他在咸阳游历的时候，朋友告诉他在咸阳最大的拍卖行（聚宝商行）将要举行一场拍卖会，其中有一件宝物引起了他极大的兴趣，那就是无字天书。
但是，他的行程安排得很满，他已经买好了去邯郸的长途马车票，不巧的是出发时间是在拍卖会快要结束的时候。于是，他决定事先做好准备，将自己的金币数好并用一个个的小钱袋装好，以便在他现有金币的支付能力下，任何数目的金币他都能用这些封闭好的小钱的组合来付账。
鬼谷子也是一个非常节俭的人，他想方设法使自己在满足上述要求的前提下，所用的钱袋数最少，并且不有两个钱袋装有相同的大于1的金币数。假设他有m个金币，你能猜到他会用多少个钱袋，并且每个钱袋装多少个金币吗？
# 输入输出格式
#  输入格式：
包含一个整数，表示鬼谷子现有的总的金币数目m。其中，1≤m ≤1000000000。
#  输出格式：
两行，第一行一个整数h，表示所用钱袋个数
第二行表示每个钱袋所装的金币个数，由小到大输出，空格隔开
# 输入输出样例
#  输入样例# 1： 
```
3
```
#  输出样例# 1： 
```
2
1 2
```
# 解答
这道题是个骗分的好题！你想想，要把它拆了，加起来和还正好等于它本身，并且还可以构成它自己，首先我~~一下子~~就想到了二进制拆分，然后直接上lowbit运算，直接把这个数拆了，那么就有了如下代码:
```cpp
# include <stdlib.h>
# include <cstdio>//打表程序
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
int ans[64];
int cnt;
int main(void){
    int n = read();
    while(n>0){
    	ans[++cnt] = n&-n;
    	n-=n&-n;
    }
    printf("%d\n",cnt);
    for(int i = 1;i<=cnt;i++){
    	printf("%d ",ans[i]);
    }
    return 0;
}
```
但是这样是WA掉的，因为原因很简单，如果是5，那么这样算出来的是1,4,但实际上答案是1,2,2。但是由于这道题数据相当水，可以过80分！那么正解是什么呢？我们如果想到二进制拆分了，那么离正解也不远了。首先，n/2肯定是要在里面的不然怎么凑？那么我们就把问题转化到了n/2，对于n/2也一样，因为我们已经把问题转化到了一个一样的子问题。那么我们就可以写下如下代码：
```cpp
# pragma GCC optimize("Ofast")
# include <fstream>
# include <stdlib.h>
# include <algorithm>
# include <cstdio>//打表程序
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
int ans[100];
int cnt = 0;
int main(void){
    int n = read();
    while(n>0){
        ans[++cnt] = (n+1)/2;
        n/=2;
    }
    printf("%d\n",cnt);
    for(int i = cnt;i>=1;i--){
        printf("%d ",ans[i]);
    }
    return 0;
}
```