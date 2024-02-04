---
title: CSP-S 注意事项
date: 2019-09-28 14:06:06 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

- [] 不要用size做变量名
- [] 头文件,比如`cstdio`
- [] 老版本编译器在结构体内定义比较大小运算符重载记得后面加`const`
- [] m和n变量名不要反
- [] 保证暴力不要挂
- [] 卡常暴力超级读优不要写挂
- [] 要开long long 的题一定检查好哪些地方会有影响，千万不要一些地方开的是longlong另一些地方开的是int!!估计好数据范围