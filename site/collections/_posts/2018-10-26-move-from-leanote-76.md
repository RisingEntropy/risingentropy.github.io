---
title: CF1036B
date: 2018-10-26 08:32:23 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# Diagonal Walking v.2

[原题目](http://codeforces.com/contest/1036/problem/B)
在一个笛卡尔平面上(就是平面直角坐标系), 从点(0, 0)开始出发, 每一步可以向周围的八个点走. 例如, 从(0, 0), 可以走到的点是:
(1, 0);
(1, 1);
(0, 1);
(-1, 1);
(-1, 0);
(-1, -1);
(0, -1);
(1, -1).
如果一步从点(x1, y1)走到(x2, y2), 且x1 != x2 && y1 != y2, 则称这一步为diagonal move(斜步).
现在有 q 个询问, 第 i 个询问的目标是走正好 ki 步到达点(ni, mi). 在所有可能的移动中希望能走斜步最多的一种. 你的目标是找到最多的“斜步”数量, 或者是发现无法用刚好 ki 步从(0, 0)走到(ni, mi).
记住可以访问任意一个点任意次数.
输入:
第一行有一个整数 q (1 <= q <= 1e4), 表示询问个数.
接下来 q 行, 在这 q 行中的第 i 行有三个整数 ni, mi, ki (1 <= ni, mi, ki <= 1e18), 分别表示目标坐标的 x 轴, y 轴和要求的步数.
输出:
q 个整数, 如果第 i 个询问无解, 则输出 -1 , 否则就输出最大的“斜步”步数.
#  样例1
#  输入
```
3
2 2 3
4 3 7
10 1 9
```
#  输出
```
1
6
-1
```
# 解答
其实这个策略好像比较难想，可能是因为我太笨了吧。策略是走到m,n中较小的那个数所在的那一行或列。然后判断剩下的步数与当前点到m目标点的距离(水平距离或者竖直距离)是不是偶数，如果是的话，那么接下来的所有步数都可以斜着走。如果**剩余步数**是奇数的话，应该在原点的时候就水平与竖直都走一步。这样就可以使剩余步数是偶数了，然后把(1,1)当做原点来计算就行了。如果剩余距离是奇数，那么就应该在原点的时候就水平**或**竖直走一次。至于这个的正确性，其实可以自己画个图简单看一下，有一定的贪心的思想在里面，就是尽量走斜步。同时还有一个很重要的思想：转化为子问题的思想。
代码:
```cpp
# include <iostream>
using namespace std;
inline unsigned long long max(unsigned long long a,unsigned long long b){return a>b?a:b;}
inline unsigned long long min(unsigned long long a,unsigned long long b){return a<b?a:b;}
int main() {
    int q;
    unsigned long long n,m,k;
    cin>>q;
    while(q--){
        cin>>n>>m>>k;
        if(max(m,n)>k){cout<<-1<<endl;continue;}
        unsigned long long ans = 0;
        if((max(m,n)-min(m,n)&1)==0&&(k-min(m,n))&1==1){//如果到达min(m,n)所在的行或列以后，到目标点的距离是个奇数，说明在一开始的时候就要向(1,1)移动
            n-=1;
            m-=1;
            k-=2;
        }
        ans = min(m,n);//移动到min(m,n)
        k -= min(m,n);//剩余步数
        unsigned long long  dis = max(m,n)-min(m,n);//看看距离
        if(dis&1){//如果距离是个奇数,那么应该一开始就向左或者右移动一下,然后斜着走
            k--;
            ans+=k;
        }else{//如果距离是个偶数，剩下的直接全部斜着走
            ans+=k;
        }
        cout<<ans<<endl;
    }
    return 0;
}
```

