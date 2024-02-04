---
title: 斯特林数学习
date: 2019-08-20 18:58:45 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 两类斯特林数
#  第一类斯特林数
意义：$\begin{bmatrix}n\\m\end{bmatrix}$表示$n$元素分成$m$个环的方案数
$\begin{bmatrix}n\\m \end{bmatrix} = \begin{bmatrix}n-1\\m-1\end{bmatrix}+(n-1) * \begin{bmatrix} n-1\\m \end{bmatrix}$
理解：考虑从$n−1$个元素推过来，如果两个空环肯定是不符合的空一个环则单独成环，如果$n−1$的时候就没有空环就任意放在一个元素前
性质$$n! = \sum\limits_{i = 0}^{n}\begin{bmatrix}n\\i\end{bmatrix}$$
#  第二类斯特林数
$\begin{Bmatrix} n\\m\end{Bmatrix}$表示$n$个有区别的小球丢进$m$个无区别的盒子的方案数。
计算：
$$\begin{Bmatrix}n\\m\end{Bmatrix}=\begin{Bmatrix}n-1\\m-1\end{Bmatrix}+m*\begin{Bmatrix}n-1\\m\end{Bmatrix}$$
性质
$m^n=\sum\limits_{i=0}^{m}\begin{Bmatrix}n\\i\end{Bmatrix}*i!*C(m,i)$
反正我觉得联赛也考不到这玩意，既然L喊看一下就了解一下吧。