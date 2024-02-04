---
title:  P3369 【模板】普通平衡树(乱搞法)
date: 2018-12-21 23:15:54 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
您需要写一种数据结构（可参考题目标题），来维护一些数，其中需要提供以下操作：

插入$x$数
删除$x$数(若有多个相同的数，因只删除一个)
查询$x$数的排名(排名定义为比当前数小的数的个数$+1$。若有多个相同的数，因输出最小的排名)
查询排名为$x$的数
求$x$的前驱(前驱定义为小于$x$，且最大的数)
求$x$的后继(后继定义为大于$x$，且最小的数)
输入输出格式
输入格式：
第一行为$n$，表示操作的个数,下面$n$行每行有两个数$opt$和$x$，optopt表示操作的序号( $1 \leq opt \leq 6 $ )

输出格式：
对于操作$3,4,5,6$每行输出一个数，表示对应答案

输入输出样例
输入样例# 1： 
```
10
1 106465
4 1
1 317721
1 460929
1 644985
1 84185
1 89851
6 81968
1 492737
5 493598
```
输出样例# 1： 
```
106465
84185
492737
```
# 解答
相信各种平衡树大佬们都会写的溜地不得了了，我来一种暴力吊打表算的办法吧!
这是我在一个晚自习肝完作业后想到的。我们先考虑另一个问题，如果这里的$x$的范围不是$[-10^7,10^7]$而是$[1,100]$，那么还会有必要写平衡树吗？答案是否定的，我们可以直接用一个数组来存$x$出现的次数(记为cnt[x])。操作流程如下

 1. 对于1操作，直接cnt[x]++
 2. 对于2操作，如果cnt[x]>0则cnt[x]--否则不管
 3. 对于3操作，直接暴力计算$\sum_{i = 1}^{x-1}cnt[i]$最后加上1即可
 4. 对于4操作，直接从cnt[1]开始累加，如果加到pos这个位置以后，累计和大于x，直接返回pos
 5. 对于5操作，从x-1开始向1开始暴力跑，找到的第一个cnt[x]不为0的位置，就是答案
 6. 对于6操作，同5一样，只不过是从x+1开始跑到100

对于$[1,100]$的x可以这么做，那能不能在$[-10^7,10^7]$上也这么跑暴力呢？显然，是可以的，我们把数据离散化一下，离散化的步骤如下
  >把所有询问全部离线(就算这道题强制在线也不管，因为这样的离线根本不影响)，然后把操作数从大到小排序，从大到小为每个数赋予一个离散化以后的值i(i从1开始递增)，之后，全部使用离散化以后的i代替操作数来操作。注意一下，对于4操作，其实离散化是没有用的，为了实现简便，我们就照样这么做，但是在计算的时候，就按照原来的值来做就好了
  
  这样就离散化好了，然后再按操作顺序排个序，然后从头开始愉快地回答询问。我们用nums[i]表示离散化之后的数i对应的离散化之前的数是多少。
  然后对于询问1，我们只需要cnt[i]++;就好了
  对于询问2，如果cnt[i]>0我们就cnt[i]--;好了
  对于询问3，4,5，做法和上面所说的一样，直接上暴力
  以下是部分代码
操作1
```cpp
void insert(int val){
    int id = val;
    cnt[id]++;
}
```
操作2
```cpp
  void del(int val){
    int id = val;
    if(cnt[id]>0)cnt[id]--;
}
```
操作3
```cpp
int getRank(int val){
    int Id = val;
    int ans = 0;
    for(int i = 0;i<Id;i++)ans+=cnt[i];//直接从1开始往后怼
    return ans+1;
}
```
操作4
```cpp
int getVal(int rank){
    int ans = cnt[1];
    int pos = 1;
    while(ans<rank)//从头开始往后怼
        ans+=cnt[++pos];
    return nums[pos];
}
```
操作5
```cpp
int getPre(int val){
    int Id = val-1;
    while(Id>=1)if(cnt[Id]>0)return nums[Id];else Id--;//上面以及提到过的暴力跑法
    return 444;
}
```
操作6
```cpp
int getBack(int val){
    int Id = val+1;
    while(Id<=id)if(cnt[Id]>0)return nums[Id];else Id++;
    return 444;
}

```
**注意了**，这个做法会TLE掉好几个点，需要吸氧才能过去。但是`NOIplus`不能开O2怎么办呢？其实我也想到了解决办法，就是使用树状数组来维护cnt数组，然后使用线段树来查找前缀和为x的点，但是因为我比较懒，所以没有去实现，读者可以自己试一下，这样就把$O(n)$的查询前驱后继改成了$O(logN)$。
总体代码如下
```cpp
# include <algorithm>
# include <cstring>
# include <cstdio>
using namespace std;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}
const int MAXN = 1000010;
int nums[MAXN],id;
struct op{
    int opt,val,time,id;
    bool operator<(const op &op2)const {return val<op2.val;}
}ops[MAXN];
bool cmp(const op &op1,const op &op2){
    return op1.time<op2.time;
}
int cnt[MAXN];
int n;
void insert(int val){
    int id = val;
    cnt[id]++;
}
void del(int val){
    int id = val;
    if(cnt[id]>0)cnt[id]--;
}
int getRank(int val){
    int Id = val;
    int ans = 0;
    for(int i = 0;i<Id;i++)ans+=cnt[i];
    return ans+1;
}
int getVal(int rank){
    int ans = cnt[1];
    int pos = 1;
    while(ans<rank)
        ans+=cnt[++pos];
    return nums[pos];
}
int getPre(int val){
    int Id = val-1;
    while(Id>=1)if(cnt[Id]>0)return nums[Id];else Id--;
    return 2333;
}
int getBack(int val){
    int Id = val+1;
    while(Id<=id)if(cnt[Id]>0)return nums[Id];else Id++;
    return 23333;
}

int main(void){
    n = read();
    for(int i = 1;i<=n;i++)ops[i].opt = read(),ops[i].val = read(),ops[i].time = i;
    sort(ops+1,ops+n+1);
    ops[0].val = 0x7f7f7f7f;//这里是为了方便后面离散化赋新值
    id = 0;
    for(int i = 1;i<=n;i++){
        if(ops[i].val==ops[i-1].val)ops[i].id = ops[i-1].id;
        else nums[++id] = ops[i].val,ops[i].id = id;
    }
    int cnt = 0;
    sort(ops+1,ops+1+n,cmp);
    for(int i = 1;i<=n;i++){
        if(ops[i].opt==1){insert(ops[i].id);continue;}
        else if(ops[i].opt == 2){del(ops[i].id);continue;}
        else if(ops[i].opt == 3){printf("%d\n",getRank(ops[i].id));continue;}
        else if(ops[i].opt == 4){printf("%d\n",getVal(ops[i].val));continue;}
        else if(ops[i].opt == 5){printf("%d\n",getPre(ops[i].id));continue;}
        else printf("%d\n",getBack(ops[i].id));
    }
    return 0;
}
```