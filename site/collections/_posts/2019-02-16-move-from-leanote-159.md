---
title: woj2443 L的鞋子
date: 2019-02-16 11:26:46 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
L是壕，他非常喜欢鞋子，他专门在他的别墅中修建了一个鞋柜，鞋柜是呈线性的，为了好找鞋子，他把他的鞋子分成了c种。虽然L没有小学毕业，但是对数字非常偏爱，他很忌讳奇数，因为他觉得不吉利（壕都是这样的）。他想知道对于一个区间[l,r]中，有多少种鞋子恰好出现正偶数次。
#  输入
第一行3个整数，n,c,m
第二行n个数，每个数Ai在[1,c]，表示第i双鞋子的样式
接下来m行，每行2个整数l,r，表示询问[l,r]的答案
#  输出
m行，回答答案
样例输入
```
5 5 3
1 1 2 2 3
1 5
3 4
2 3
```
样例输出
```
2
1
0
```
提示
共有10组测试数据
1-4组n,m=500，2000，5000，10000，c=1000
5-7组n,m=20000，30000，40000，c=10000
8-10组n,m=50000，80000，100000，c=100000
数据保证随机生成
# 解答
莫队裸题。注意一下区间左右移动。
```cpp
# include <cstdio>
# include <algorithm>
# include <stdio.h>
# include <vector>
# include <iostream>
using namespace std;
const int MAXM = 100010;
const int MAXN = 100010;
int block_len;
struct Q{int l,r,id;bool operator<(const Q&q1){int x = (l-1)/block_len+1;int y = (q1.l-1)/block_len+1;return x==y?r<q1.r:x<y;}}querys[MAXM];
int top;
int a[MAXN],cnt[MAXN],ans;
int anss[MAXM];
void add(int pos){
    cnt[a[pos]]++;
    if(cnt[a[pos]]%2==0)ans++;
    else if(cnt[a[pos]]%2==1&&cnt[a[pos]]!=1)ans--;
}
void del(int pos){
    cnt[a[pos]]--;
    if(cnt[a[pos]]%2==0&&cnt[a[pos]]!=0)ans++;
    else if(cnt[a[pos]]%2==1)ans--;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int n,c,m;cin>>n>>c>>m;
    int l = 0,r = 0;
    for(int i = 1;i<=n;i++){
        cin>>c;a[i] = c;
    }
    block_len = sqrt(n);
    for(int i = 1;i<=m;i++){
        cin>>l>>r;
        querys[++top].l = l,querys[top].r = r,querys[top].id = i;
    }
    sort(querys+1,querys+1+top);
    l = 1,r = 1;cnt[a[1]]++;
    for(int i = 1;i<=m;i++){
        while(l>querys[i].l)add(--l);
        while(r<querys[i].r)add(++r);
        while(l<querys[i].l)del(l++);
        while(r>querys[i].r)del(r--);
        anss[querys[i].id] = ans;
    }
    for(int i = 1;i<=m;i++)cout<<anss[i]<<endl;
    return 0;
}
```