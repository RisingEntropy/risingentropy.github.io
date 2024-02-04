---
title: 椭圆
date: 2019-08-29 13:34:18 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 定义
平面上到两点$F_1,F_2$距离之和为定长的点的轨迹。$F_1,F_2$被称为焦点。**定长大于两点距离**
eg：
![title](https://cdn.risingentropy.top/images/posts/d676568ab644124a3002081.png)
由题，$|PM| = r+1,{PN} = 3-r$所以
    $$|PM|+|PN| = 4>|MN|$$
    所以是个椭圆
# 标准方程
$$\frac{x^2}{a^2}+\frac{y^2}{b^2} = 1$$
并且还有一个非常nice的结论
若两焦点均落在x轴上，设两焦点距离为$2c$，定长为$2a$，则存在$a^2-c^2=b^2$
![title](https://cdn.risingentropy.top/images/posts/d676568ab644124a3002081.png)
# 参数关系
$\frac{x^2}{a^2}+\frac{y^2}{b^2} = 1$两焦点始终落在x轴上，且在长轴上。
1.焦距：2c是两焦点之间的距离，c是半焦距！！！不要写错了
设长轴两端点为AB,短轴两端点为CD。则
$|AB| = 2a,|CD| = 2b$
半长轴长：a,半短轴长b。有结论就是$a^2-c^2=b^2$
当然存在的前提就是a>b，否则就变成了焦点在y轴上的椭圆。
eg：![title](https://cdn.risingentropy.top/images/posts/d676568ab644124a3002081.png)
焦点在y轴上的椭圆的标准方程是$\frac{y^2}{a^2}+\frac{x^2}{b^2} = 1  c^2 = a^2+b^2$