---
title: "Book Reading: Mathematics Methods for Physics, Chapter II"
date: 2024-02-05 15:28:35 +0800
image: 'https://cdn.risingentropy.top/images/posts/20240107172456.png'
tags: [book-reading, math]
description: Chapter 2
---
# 第二章 傅里叶级数

## 傅里叶系数

首先，我们需要知道$sin$和$cos$的正交性，即：

$$
\int_0^{2\pi}1\cdot\cos nx\mathrm{d}x=0,\quad\int_0^{2\pi}1\cdot\sin nx\mathrm{d}x=0\\

\int_0^{2\pi}\cos mx\cdot\cos nx\mathrm{d}x=0,\quad\int_0^{2\pi}\sin mx\cdot\sin nx\mathrm{d}x=0\\

\int_0^{2\pi}\cos mx\cdot\sin nx\mathrm{d}x=0
$$

这个正交性在后面非常重要。

一个以$2\pi$为周期的函数的傅里叶展开可以写成：

$$
f(x)=a_0+\sum_{n=1}^\infty\left(a_n\cos nx+b_n\sin nx\right).
$$

关键的问题在于其系数的计算，对于$a_0$我们直接开始积分：

$$
\begin{aligned}
\int_{0}^{2\pi}f(x)\mathrm{d}x& =\int_{0}^{2\pi}\left[a_{0}+\sum_{n=1}^{\infty}\left(a_{n}\cos nx+b_{n}\sin nx\right)\right]\mathrm{d}x  \\
&=2\pi a_{0}+\sum_{n=1}^{\infty}a_{n}\underbrace{\int_{0}^{2\pi}\cos nx\mathrm{d}x}_{=0}+\sum_{n=1}^{\infty}b_{n}\underbrace{\int_{0}^{2\pi}\sin nx\mathrm{d}x}_{=0} \\
&=2\pi a_{0}
\end{aligned}
$$

于是乎，$a_0=\frac{1}{2\pi}\int_0^{2\pi}f(x)\mathrm{d}x$。对于后面的系数$a_n,b_n$，直接乘上一个$sinnx,cosnx$，由于不同角速度的项积了分后为零，就只剩下了相同角速度的项。书上的例子是：

$$
\begin{aligned}
\int_{0}^{2\pi}f(x)\cos mx\mathrm{d}x=& \int_{0}^{2\pi}\cos mx\left[a_{0}+\sum_{n=1}^{\infty}\left(a_{n}\cos nx+b_{n}\sin nx\right)\right]\mathrm{d}x  \\
&=a_{0}\underbrace{\int_{0}^{2\pi}\cos mx\mathrm{d}x}_{=0}+\sum_{n=1}^{\infty}b_{n}\underbrace{\int_{0}^{2\pi}\cos mx\sin nx\mathrm{d}x}_{=0} \\
&+\sum_{n=1}^{\infty}a_{n}\int_{0}^{2\pi}\mathrm{cos}mx\cos nx\mathrm{d}x \\
&\left.=\sum_{n=1}^{\infty}a_{n}\left\{\begin{array}{ll}{\pi}&{(m=n)}\\{0}&{(m\neq n)}\\\end{array}\right.\right. \\
&=\pi\sum_{n=1}^{\infty}a_{n}\delta_{mn}
\end{aligned}
$$

其中$\delta_{mn}$就是当$m=n$时为1,其他时候为0。拓展到周期为$L$的函数上面（满足狄利克雷条件），系数的公式就是：

$$
\begin{gathered}
a_{0}={\frac{1}{2L}}\int_{-L}^{L}f(t)\mathrm{d}t \\
a_{n} =\frac{1}{L}\int_{-L}^{L}f(t)\cos\frac{n\pi}{L}t\mathrm{d}t \\
\boldsymbol{b}_{n} =\frac{1}{L}\int_{-L}^{L}f(t)\sin\frac{n\pi}{L}t\mathrm{d}t 
\end{gathered}
$$

### 半幅傅里叶系数

就是说一个定义域为$(0,L)$的函数，也可以进行傅里叶展开，有两种形式：余弦形式和正弦形式。说白了就是把函数看成偶函数/奇函数，然后进行傅里叶展开。公式如下：

$$
\phi(x)=\sum_{n=1}^{\infty}C_{n}\sin\frac{n\pi x}{L}\\

C_{n}=\frac{2}{L}\int_{0}^{L}\phi(x)\sin\frac{n\pi x}{L}\mathrm{d}x\quad(n=1,2,3,\cdots)\\


\phi(x)=D_{0}+\sum_{n=1}^{\infty}D_{n}\cos\frac{n\pi x}{L}\\

D_{0}=\frac{1}{L}\int_{0}^{L}\phi(x)\mathrm{d}x\\
D_{n}=\frac{2}{L}\int_{0}^{L}\phi(x)\cos\frac{n\pi x}{L}\mathrm{d}x\quad(n=1,2,3,\cdots)
$$

## 傅里叶积分

对于非周期信号也可以进行傅里叶展开。首先，它需要满足绝对可积条件，即：

$$
\int_{-\infty}^{\infty}|f(x)|\mathrm{d}x<\infty 
$$

有了绝对可积条件后，傅里叶级数里面$a_0$项就可以写为：

$$
a_{0}=\frac{1}{2L}\int_{-L}^{L}f(t)\mathrm{d}t\xrightarrow{L\rightarrow\infty}0
$$

然后，令$\omega_n=\frac{n\pi}{L}$，则有：

$$
\Delta\omega=\omega_{n}-\omega_{n-1}=\frac{\pi}{L}
$$

然后就可以把求和写成积分：

$$
\sum_{n=1}^{\infty}\cdots\Delta\omega\xrightarrow{L\to\infty}\int_{0}^{\infty}\cdots d\omega 
$$

把傅里叶级数改写成积分形式：

$$
\begin{aligned}
\sum_{n=1}^{\infty}a_{n}\cos{\frac{n\pi}{L}}x& =\sum_{n=1}^{\infty}\frac{1}{L}\left[\int_{-L}^{L}f(t)\cos\frac{n\pi}{L}t\mathrm{d}t\right]\cos\frac{n\pi}{L}x  \\
&=\sum_{n=1}^{\infty}\frac{\Delta\omega}{\pi}\left[\int_{-L}^{L}f(t)\cos\omega_{n}t\mathrm{d}t\right]\cos\omega_{n}x\\
&\xrightarrow{L\to\infty}\int_{0}^{\infty}d\omega\left[\frac{1}{\pi}\int_{-\infty}^{\infty}f(t)\cos\omega t\mathrm{d}t\right]\cos\omega x
\end{aligned}
$$

总之，非周期函数的傅里叶积分可以写成如下形式：

$$
f(x)=\int_{0}^{\infty}[A(\omega)\cos\omega x+B(\omega)\sin\omega x]\mathrm{d}\omega 
$$

其中：

$$
\begin{aligned}A(\omega)&=\frac{1}{\pi}\int_{-\infty}^\infty f(t)\cos\omega t\mathrm{d}t\\B(\omega)&=\frac{1}{\pi}\int_{-\infty}^\infty f(t)\sin\omega t\mathrm{d}t\end{aligned}
$$
