---
title: 数学2
date: 2018-10-19 20:06:49 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 圆排列
从n个不同元素中不重复地取出m（1≤m≤n）个元素在一个圆周上，叫做这n个不同元素的圆排列。如果一个m-圆排列旋转可以得到另一个m-圆排列，则认为这两个圆排列相同。
# 不相异元素排列
如果在n个元素中，有m种不同的元素，每种元素有ai个，满足$\sum_i a_i=n$
n个元素的全排列有n!种，再除去每一种元素的重复情况。因此答案为：$$\frac{n!}{n_1!\times n_2!\times ...\times n_m!}$$(n1,n2为每种元素个种数)
>eg:把3个相同的黄球，2个相同的蓝球，4个相同的白球摆成一排，问有多少种不同排列
# 可重复组合
从n个元素里面取出m个元素，允许元素重复，则组合数记为$C_{n+m-1}^m$
# 二项式定理
$(ax+by)^n = \sum^{n}_{k=0}C^k_na^{n-k}x^{n-k}b^ky^{k}$
# 组合数计算
$$C_n^m=\frac{n!}{m!(m-n)!}$$
下面递推式亦可
$$C（n,m）=C(n-1,m-1)+C(n-1,m)$$
# Lucas定理
若p是**质数**，则对于任意整数$1\leq m\leq n$,有：
$$C_n^m\equiv C_{n\ mod\ p}^{m\ mod\ p}\times C_{n/p}^{m/p}(mod\ p)$$
也就是把n和m表示成p进制数，对p进制下的每一位分别计算组合数，最后乘起来~~不懂，大雾~~
# 卡特兰数
~~就是给定n个0和n个1，它们按照某种顺序排成长度为2n的序列，满足任意前缀中0的个数都不少于1的个数的序列的数量~~
$$Cat_n=\frac{C^n_{2n}}{n+1}$$
#  计算
1.上面的公式
2.满足的递推式
令h(1)＝1，catalan数满足递归式：
h(n)= h(1)*h(n-1) + h(2)*h(n-2) + ... + h(n-1)h(1) (其中n>=2)
该递推关系的解为：h(n)=c(2n-2,n-1)/n (n=1,2,3,...)
#  应用
1.n个左括号和n个右括号组成的合法括号序列的数量为Cat。
2.1,2...n经过一个栈，形成的合法出栈序列的数量为Cat。
3.n个节点构成的不同二叉树的数量为Cat
4.在平面直角坐标系上每一步只能向上或者向右走，从(0,0)走到(n,n)并且除两个端点以外不接触直线y=x的路线数量为2$2Cat_{n-1}$
