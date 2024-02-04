# 题面
# Description

在一年前赢得了小镇的最佳草坪比赛后，FJ变得很懒，再也没有修剪过草坪。现在，
新一轮的最佳草坪比赛又开始了，FJ希望能够再次夺冠。

然而，FJ的草坪非常脏乱，因此，FJ只能够让他的奶牛来完成这项工作。FJ有N
(1 <= N <= 100,000)只排成一排的奶牛，编号为1...N。每只奶牛的效率是不同的，
奶牛i的效率为E_i(0 <= E_i <= 1,000,000,000)。

靠近的奶牛们很熟悉，因此，如果FJ安排超过K只连续的奶牛，那么，这些奶牛就会罢工
去开派对:)。因此，现在FJ需要你的帮助，计算FJ可以得到的最大效率，并且该方案中
没有连续的超过K只奶牛。

#Input

* 第一行：空格隔开的两个整数N和K

* 第二到N+1行：第i+1行有一个整数E_i


#Output

* 第一行：一个值，表示FJ可以得到的最大的效率值。
Sample Input
```
5 2
1
2
3
4
5
```

输入解释：
```
FJ有5只奶牛，他们的效率为1，2，3，4，5。他们希望选取效率总和最大的奶牛，但是
他不能选取超过2只连续的奶牛
```
Sample Output
```
12
```

FJ可以选择出了第三只以外的其他奶牛，总的效率为1+2+4+5=12。


#解答
其实就是单调队列优化的dp。首先，我们先设计一个最朴素的方程，之后再来优化。不难~~难死我了~~ 设计出如下方程
$$F[i] = \underset{i-K \leq j\leq i}{max}(F[i],F[j-1]+sum[i]-sum[j])$$

`F[i]`的含义是前$i$头奶牛中，选一些奶牛获得的最大效率。然后因为一段连续的奶牛不能超过$K$，所以要枚举一下断点$j$，这个$j$号奶牛不选。于是乎就可以推出如下方程。我们发现i可以看做是常量，那么就可以使用单调队列优化，优化后的方程式如下
$$F[i] = \underset{i-K \leq j\leq i}{max}(F[i],F[j-1]-sum[j])+sum[i]$$
那么，我们就维护一个**$j$单调递增，$F[j-1]-sum[j]$也单调递增的单调队列**，为什么可以这样呢？因为我们发现对于$k_1$和$k_2$有$i-K\leq k_1<k_2<i$如果有$F[k_1-1]-sum[k_1]<F[k_2]-sum[k_2]$那么，就意味着$k_2$永远不会成为最优解，也就是说$k_2$将永远不会成为决策的一部分，那么我们还考虑它干嘛？直接删掉不管了。这就是单调队列优化dp的精髓。通俗一点，就是如果k1比k2小，并且它代表的值还比k2小，也就是说它的生存能力小于k2，就可删掉。~~当一个选手比你小，还比你强，你就永远打不过他了~~
然后看了题解开心的像个智商250的智障~~NOIP2018我250分~~一样的我开始写起了代码。
```cpp
//
// Created by dhy on 18-12-31.
//
#include <iostream>
#include <deque>
using namespace std;
long long F[100010];
long long s[100010];
long long d[100010];
int main(){
    int N,K;
    cin>>N>>K;
    for(int i = 1;i<=N;i++){cin>>s[i];s[i]+=s[i-1];}
    deque<int> q;
    for(int i = 1;i<=N;i++){
        d[i] = F[i-1]-s[i];
        while(!q.empty()&&d[q.back()]<=d[i])q.pop_back();
        q.push_back(i);
        while(!q.empty()&&q.front()<i-K)q.pop_front();
        F[i] = d[q.front()]+s[i];
    }
    cout<<F[N]+1;
    return 0;
}
```
然后挂了9个点，冥思苦想不得其因。然后看了题解，我也没搞懂l = 0 r = 1的含义。然后瞎向单调队里里面加了两个元素0和1，洛谷数据过了，但是bzoj数据却过不了。然后又一次陷入沉思，突然，我想起了四个字：**初始状态**。对呀！我的单调队列没有维护初始状态。对于$i<k$我们直接$F[i] = sum[i]$，然后维护一下单调队列就完事了呀！于是乎花了5小时终于A了这道题。
```cpp
//
// Created by dhy on 18-12-31.
//
#include <iostream>
#include <deque>
using namespace std;
long long F[100010];
long long s[100010];
long long work(int j){return F[j-1]-s[j];}
int main(){
    long long N,K;
    cin>>N>>K;
    for(int i = 1;i<=N;i++){cin>>s[i];s[i]+=s[i-1];}
    deque<int> q;
    for(int i = 1;i<=K;i++){
        F[i] = s[i];
        while(!q.empty()&&work(q.back())<=work(i))q.pop_back();
        q.push_back(i);
    }
    for(int i = K+1;i<=N;i++){
        while(!q.empty()&&q.front()<i-K)q.pop_front();
        while(!q.empty()&&work(q.back())<=work(i))q.pop_back();
        q.push_back(i);
        F[i] = work(q.front())+s[i];
    }
    cout<<F[N];
    return 0;
}
```
好了，到这里，我又积累了一点关于dp的坑了。~~元旦作业呀，做不完了~~
推销一下我的博客[dhy的博客](denghaoyu.leanote.com)