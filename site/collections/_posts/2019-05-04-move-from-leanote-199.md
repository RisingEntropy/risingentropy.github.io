---
title: 【线段树(trie树)】woj2645 hyc的xor/mex
date: 2019-05-04 13:43:05 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
NOIP2017就要来了，备战太累，不如做做hyc的新题？

找回自信吧！

一句话题意：n个数，m个操作

操作具体来讲分两步

1.读入x，把n个数全部xor上x

2.询问当前n个数的mex

意味着每次操作后你都需要输出一次

(注意：是mex,即集合内未出现过的最小非负整数

举2个例子 mex(4,33,0,1,1,5)=2 mex(1,2,3)=0)

输入
第一行两个整数n，m 意义同题面(1 ≤ n, m ≤ 3 * 10^5)

第二行 n个数 ai (0 ≤ ai ≤ 3 * 10^5)

接下来 m 行

每行一个整数 x

表示将所有数xor上x (0 ≤ x ≤ 3 * 10^5).

输出
一共m行

每行表示当前n个数的xor

样例输入
```
5 4
0 1 5 6 7
1
1
4
5
```
样例输出
```
2
2
0
2
```
提示
30%数据n,m<=1000

100%数据同“输入”

标签
mogician原创
# 解答
比较难的一道题。首先我们建立一颗1e6的权值线段树，标记一下哪些地方有数。也就是说走到一个地方，如果那个地方cnt不为1，那就存在这个数。然后把这棵线段树看做一颗trie。
>树我一开始没搞懂为什么可以看出trie树，其实是可以的，因为我们看到我们线段树的写法中：`lc = k<<1` `rc = k<<1|1`这不就是trie树里面的走0还是走1吗？

在走的时候，如果当前位被异或上了1，那么就往反方向走。为什么呢？因为异或`1`以后，就相当于是trie树上左右儿子交换了一下(LCT里面的区间交换)，本来要走左边的，现在成了走右边。还要注意一点，就是如果该走的这个区间被压满了，只能被迫走另外的方向，答案加上($1<<depth$)。
代码
```cpp
# include <iostream>
# include<cstring>
# include<cstdio>
using namespace std;
inline int read(){
    int ans=0;
    char ch=getchar();
    while(!isdigit(ch))ch=getchar();
    while(isdigit(ch))ans=(ans<<3)+(ans<<1)+(ch^48),ch=getchar();
    return ans;
}
const int INF = (1<<19)-1;
const int MAXN = (int)3e5+10;
struct node{int l,r,cnt;}tree[MAXN*4];
int s[20];
void pushup(int k){tree[k].cnt = tree[k<<1].cnt+tree[k<<1|1].cnt;}
void build(int k,int l,int r){
    tree[k].l = l;tree[k].r = r;
    if(l==r){
        tree[k].cnt = 0;
        return;
    }
    int mid = l+r>>1;
    build(k<<1,l,mid);build(k<<1|1,mid+1,r);
}
void update(int k,int x){
    if(tree[k].l==tree[k].r){tree[k].cnt = 1;return;}
    int mid = tree[k].l+tree[k].r>>1;
    if(x<=mid)update(k<<1,x);
    else update(k<<1|1,x);
    pushup(k);
}
int query(int k,int depth){
    if(tree[k].l==tree[k].r){return 0;}
    int tmp = k<<1|s[depth];
    if(tree[tmp].cnt==tree[tmp].r-tree[tmp].l+1)return query(tmp^1,depth-1)+(1<<depth);
    return query(tmp,depth-1);
}
int n,m,t;
int main(){
    n = read(),m = read();
    build(1,0,INF);
    while(n--){
        t = read();update(1,t);
    }
    while(m--){
        t = read();
        for(int i = 1;i<=19;i++){
            if(t&(1<<i))s[i]^=1;
        }
        printf("%d\n",query(1,18));
    }
}
```