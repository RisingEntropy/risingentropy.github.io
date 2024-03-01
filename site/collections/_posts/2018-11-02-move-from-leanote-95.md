---
title: luoguP1352没有上司的舞会
date: 2018-11-02 20:04:20 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
某大学有N个职员，编号为1~N。他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树，父结点就是子结点的直接上司。现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数Ri，但是呢，如果某个职员的上司来参加舞会了，那么这个职员就无论如何也不肯来参加舞会了。所以，请你编程计算，邀请哪些职员可以使快乐指数最大，求最大的快乐指数。
# 输入输出格式
输入格式：
第一行一个整数N。(1<=N<=6000)
接下来N行，第i+1行表示i号职员的快乐指数Ri。(-128<=Ri<=127)
接下来N-1行，每行输入一对整数L,K。表示K是L的直接上司。
最后一行输入0 0
# 输出格式：
输出最大的快乐指数。

# 输入输出样例
#  输入样例# 1： 
```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
0 0
```
#  输出样例# 1： 
```
5
```
# 解答
这题怎么大家都用dp来做啊。看到这道题，首先看到：如果上司去了，那么职员就不去了。嗯？这不是[阳光封锁大学](https://www.luogu.org/problemnew/show/P1330)么？二分图匹配？？不会！怎么办？染色啊！如下图(我们用黑色表示要去，白色表示不去)

