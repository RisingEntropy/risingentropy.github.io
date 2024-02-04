---
title: SCOI2016萌萌哒
date: 2019-05-03 15:40:13 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
一个长度为n的大数，用S1S2S3...Sn表示，其中Si表示数的第i位,S1是数的最高位，告诉你一些限制条件，每个条件表示为四个数，l1，r1，l2，r2，即两个长度相同的区间，表示子串Sl1Sl1+1Sl1+2...Sr1与Sl2Sl2+1Sl2+2...Sr2完全相同。
比如n=6时，某限制条件l1=1，r1=3，l2=4，r2=6，那么123123，351351均满足条件，但是12012，131141不满足条件，前者数的长度不为6，后者第二位与第五位不同。问满足以上所有条件的数有多少个。
#  输入
第一行两个数n和m，分别表示大数的长度，以及限制条件的个数。接下来m行，对于第i行,有4个数li1，ri1，li2，ri2，分别表示该限制条件对应的两个区间。1<=n<=10^5，1<=m<=10^5，1<=li1,ri1,li2,ri2<=n；并且保证ri1-li1=ri2-li2。
#  输出
一个数，表示满足所有条件且长度为n的大数的个数，答案可能很大，因此输出答案模10^9+7的结果即可
#  样例输入
```
4 2
1 2 3 4
3 3 3 3
```
#  样例输出
```
90
```
# 解答
神仙题！反正我是想不到。首先需要想到的是，两段区间要完全一样，那么其实它们就是一个区间。可以使用并查集维护两端区间，处于同一个集合内的元素要相同，只需要最后统计独立的集合有多少个就行了。但是考虑到另一个问题：如果没两个区间之间每个点都要连边，那么，总复杂度是$O(mn)$的。肯定不行啊。于是可以使用类似于懒标记的方法。把每个区间先连为一个集合，等所有的区间都连完了，再来下推。然后为了方便下推，我们把每个区间类似于ST表地预处理，这样就方便处理了。
代码(带注释)：
```cpp
/*
* Created by BeyondStars on 2019 05 03
*/
# include <iostream>
# include <algorithm>
using namespace std;
const int MAXN = (int)1e5+10;
const long long mod = (long long)1e9+7;
int f[MAXN][18];
int cnt,id[MAXN*18];
int fa[MAXN*18];
int find(int x){return x==fa[x]?x:fa[x]=find(fa[x]);}
void unionn(int x,int y){int f1 = find(x),f2 = find(y);if(f1>f2)swap(f1,f2);fa[f2] = f1;}
bool judge(int x,int y){return find(x)==find(y);}
int n,m;
int main(){
    cin>>n>>m;
    for(int i = 1;i<=n;i++){
        for(int j = 0;j<=17;j++){
            f[i][j] = ++cnt;id[cnt] = i;fa[cnt] = cnt;//预处理st表
            //把每个点为起点，一定长度的区间看为一个新的点，并查集就维护这个点
        }
    }
    int l1,r1,l2,r2;
    for(int i = 1;i<=m;i++){
        cin>>l1>>r1>>l2>>r2;
        for(int j = 17;j>=0;j--){
            if (l1+(1<<j)-1<=r1) {
                unionn(f[l1][j],f[l2][j]);//2个区间互相并查集维护
                l1+=(1<<j);l2+=(1<<j);
            }
        }
    }
    for(int j = 17;j>=1;j--){
        for(int i = 1;i+(1<<j)-1<=n;i++){
            int faq = find(f[i][j]),sta = id[faq];//点i所在的段和那一段的起点(并查集中的父亲维护)
            unionn(f[sta][j-1],f[i][j-1]);//把他pushdown下去
            unionn(f[sta+(1<<j-1)][j-1],f[i+(1<<j-1)][j-1]);//后一段pushdown下去
        }
    }
    long long ans = 9;
    for(int i = 2;i<=n;i++)if(fa[f[i][0]]==f[i][0])ans = ans*10ll%mod;//统计答案
    cout<<ans;
    return 0;
}
```
