---
title: 哈希表
date: 2018-09-07 20:14:53 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 哈希表
其实就是把很多数对一个大质数取模，然后把模数相等的放到一个链表里面，最后查询就行了。有点像~~非常像~~前向星存图
# 构造
1.除余法
选一个适当的数b，然后用其对b取模的数作为哈希值，即H(x) = x mod b,如果b的约数越多，冲突概率就越大。
2.乘积取整
我们用key乘一个(0,1)之间的实数A(最好无理数，$\frac{ \sqrt5 -1}{2}$是个很好的数)得到一个(0,key)之间的实数，取小数部分，乘以哈希表的大小M再向下取整，即可得到key在哈希表中的位置。函数表达式如下
$$H(key)=\{M(key*A mod 1)\}$$
3.基数转换法
我们吧key看作是另一种k进制的数，然后把它转化为十进制然后再用除余法对它取模，基数和模数互质(其实就是类似于字符串哈希)，最后放进哈希表


