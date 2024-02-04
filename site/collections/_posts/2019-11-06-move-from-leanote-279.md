---
title: 赛前补坑
date: 2019-11-06 15:26:11 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 懵逼乌斯反演相关证明
已知$F(n)=\sum_{d|n}f(d)$其中$F$和$f$是积性函数
莫比乌斯反演定理：
$f(n) = \sum_{d|n}\mu(d)F(\lfloor\frac{n}{d}\rfloor)$
利用狄利克雷卷积
$$
F = I\times f\\F\times \mu=I\times f\times\mu\\F\times\mu=f\times(I\times \mu)\\F\times\mu=f\times\epsilon\\F\times\mu=f
$$
综上$f(n)=\sum_{d|n}\mu(d)\times F(\frac{n}{d})$更普遍的，得到$f(n)=\sum_{d|n}\mu(d)\times F(\lfloor\frac{n}{d}\rfloor)$