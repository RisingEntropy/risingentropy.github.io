---
title: "Book Reading: Mathematics Methods for Physics, Chapter I"
date: 2024-01-05 15:28:35 +0800
image: 'https://cdn.risingentropy.top/images/posts/20240107172456.png'
tags: [book-reading, math]
description: Chapter 1
---
# 读前感
电子科大信通学院的数学相关课程属实垃圾，一坨答辩。几把电工数学四节课讲完复变？你要不要看看你在讲什么？系统建模与仿真？光给我讲状态矩阵怎么算，又不讲怎么用，怎么算网上一堆我要你教？信通早晚要完蛋，傻逼学院。自学罢！先读顾樵老师的数学物理方法。

# 第一章 基础知识

## 1.1 常微分方程模型与求解
这个部分讲了几个例题，程度由浅入深。

### 例一
这是一个马尔萨斯人口模型，简单的线性微分方程求解。方程如下：
$$
\frac{du}{dt}=\alpha u
$$
简单，没啥好说的。

### 例二
例一的进阶，将线性的的方程改成了非线性。看点是套公式。方程如下：
$$
\frac{du}{dt}=\alpha u - \beta u^2
$$
把方程改写，$du$和$dt$分开到等号两边，得到
$$
\frac{M\mathrm{d}u}{u(u-M)}=-\alpha \mathrm{d}t
$$
然后两边积分，注意两边积分式子的含义要相同，得到：
$$
M\int_{N}^{u(\boldsymbol{t})}\frac{\mathrm{d}u}{u(u-M)}=-\alpha\int_{0}^{t}\mathrm{d}t
$$
考虑积分表里面的公式：
$$
\int\frac{\mathrm{d}u}{(u+a)(u+b)}=\frac1{b-a}\ln\frac{a+u}{b+u}\quad(a\neq b)
$$
就可以得到结果了。

<font color=Red>在求解的时候需要注意一下，用积分表的式子会出现这样的结果$ln \frac{N}{-M+N}$，这样$ln$里面就有负数了，我们不用管他，直接把两个$ln$相减的式子画成除号，分子分母的负数就都没了。</font>

### 例三

一个LC振荡电路的例子。看点是初始条件的设置。得到简单的微分方程：
$$
\frac{\mathrm{d}^2Q}{\mathrm{d}t^2}+\frac{Q}{LC}=0
$$
这样的形式的方程通解是：
$$
Q(t)=A\cos\frac{t}{\sqrt{L\overline{C}}}+B\sin\frac{t}{\sqrt{L\overline{C}}}
$$
设置边界条件$Q(0)=C,Q'(0)=0$，直接解出$A,B$就行。

### 例四
是一个单摆问题，看点是线性化，以及解的形式。小球重力，切向分量受力为$F=mgsin\theta$。切向速度为$v=l\frac{\mathrm{d}\theta}{\mathrm{d}t}$,然后各种简单的联立，得到该问题的微分方程：
$$
\frac{\mathrm{d}^2\theta}{\mathrm{d}^2t}+\frac{g}{l}\sin\theta=0
$$
这个是非线性的，如果摆动角度小，则有$\theta\approx sin\theta$，换成线性的，发现和前面的问题有类似的形式$\frac{\mathrm{d}^{2}y}{\mathrm{d}^{2}x}+k^{2}y=0$。然后解就行了。

这种方程的通解是： $y(x)=A\cos kx+B\sin kx$。可以写成<font color=Red>驻波形式：</font>$y(x)=E\sin{(kx+\delta)}\text{或}y(x)=E\cos{(kx+\delta)}$，以及<font color=Red>行波形式：</font>$y(x)=C\exp(\mathrm{i}kx)+D\exp{(-\mathrm{i}kx)}$

选取哪种形式就看哪个形式的系数0更多。
### 例五
R-G传输线，看点是方程的形式。写出这样的简单震动的方程：
$$
\frac{\mathrm{d}^{2}y}{\mathrm{d}^{2}x}-k^{2}y=0
$$
利用：
$$
\cosh x=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2},\quad\sinh x=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}
$$
把解写成这样的形式：
$$
y(x)=A\cosh kx+B\sinh kx
$$
选取原则也是尽量让系数尽可能多的为0

### 例六
非常有意思的一个例子，看点：选取方程稳态解、代换解耦。这里我不太能明白为什么能代换，对于一些微元的代换我是非常害怕的，不知道什么时候就出问题了。好像微积分课也没细讲。本题的方程：
$$
\begin{aligned}\frac{\mathrm{d}x}{\mathrm{d}t}&=k_1x-\mu xy\\\frac{\mathrm{d}y}{\mathrm{d}t}&=\nu xy-k_2y\end{aligned}
$$
找稳态点，满足：
$$
\left.\frac{\mathrm{d}x}{\mathrm{d}t}\right|_{x=x_0,y=y_0}=0,\quad\left.\frac{\mathrm{d}y}{\mathrm{d}t}\right|_{x=x_0,y=y_0}=0
$$
在这一点满足：
$$
\begin{aligned}x_\mathrm{o}&=\frac{k_2}\nu\\y_\mathrm{o}&=\frac{k_1}\mu\end{aligned}
$$
于是乎解的形状就变成了：
$$
\begin{array}{c}x=x_\mathrm{o}+\xi\\y=y_\mathrm{o}+\eta\end{array}
$$
带入本题方程：
$$
\begin{aligned}\frac{\mathrm{d}\xi}{\mathrm{d}t}&=k_1\xi-\mu x_0\eta-\mu y_0\xi-\mu\xi\eta\\\frac{\mathrm{d}\eta}{\mathrm{d}t}&=\nu x_0\eta+\nu y_0\xi-k_2\eta+\nu\xi\eta\end{aligned}
$$
忽略掉$\xi\eta$这种二阶无穷小，然后带入$x_0,y_0$，得到：
$$
\begin{aligned}\frac{\mathrm{d}\xi}{\mathrm{d}t}&=-k_2\frac{\mu}{\nu}\eta\\\frac{\mathrm{d}\eta}{\mathrm{d}t}&=k_1\frac{\nu}{\mu}\xi\end{aligned}
$$
两边求下导，带一下，得到解耦式子：
$$
\begin{aligned}&\frac{\mathrm{d}^2\xi}{\mathrm{d}t^2}+k_1k_2\xi=0\\&\frac{\mathrm{d}^2\eta}{\mathrm{d}t^2}+k_1k_2\eta=0\end{aligned}
$$
熟悉的感觉，直接开始解，解得：
$$
x=\frac{k_2}{\nu}+E_1\sin\left(\sqrt{k_1k_2}t+\delta_1\right)\\
\\
y=\frac{k_{1}}{\mu}+E_{2}\sin\left(\sqrt{k_{1}k_{2}}t+\delta_{2}\right)
$$

## 1.2 矢量微分算子和拉普拉斯算子
### 1.2.1矢量微分算子
老熟人：
$$
\nabla=\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}
$$

标量函数$u$的梯度:
$$
\nabla u=\frac{\partial u}{\partial x}i+\frac{\partial u}{\partial y}j+\frac{\partial u}{\partial z}k
$$

矢量函数${E}$的散度：
$$
\nabla\cdot\boldsymbol{E}=\left(\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}\right)\cdot(E_x\boldsymbol{i}+E_y\boldsymbol{j}+E_z\boldsymbol{k})=\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}
$$

矢量函数$E$的旋度：
$$
\left.\nabla\times E=\left|\begin{array}{ccc}i&j&k\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\E_x&E_y&E_z\end{array}\right.\right|=\left|\begin{array}{cc}\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\E_y&E_z\end{array}\right|i-\left|\begin{array}{ccc}\frac{\partial}{\partial x}&\frac{\partial}{\partial z}\\E_x&E_z\end{array}\right|j+\left|\begin{array}{ccc}\frac{\partial}{\partial x}&\frac{\partial}{\partial y}\\E_x&E_y\end{array}\right|k\\
=\left(\frac{\partial E_x}{\partial y}-\frac{\partial E_y}{\partial z}\right)\boldsymbol{i}+\left(\frac{\partial E_x}{\partial z}-\frac{\partial E_x}{\partial x}\right)\boldsymbol{j}+\left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right)\boldsymbol{k}
$$

拉普拉斯算子：
$$
\nabla^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}
$$
拉普拉斯算子作用于标量函数$u$得到：
$$
\nabla^{2}u\equiv\nabla\cdot(\nabla u)=\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}}
$$
作用于矢量函数$E$得到：
$$
\nabla^{2}\boldsymbol{E}=(\nabla^{2}E_{x})\boldsymbol{i}+(\nabla^{2}E_{y})\boldsymbol{j}+(\nabla^{2}E_{z})\boldsymbol{k}
$$
然后就是一堆等式，注意，这些等式要求$u$和$E$有二阶连续偏导数：
$$
\begin{aligned}
&(1)\nabla(u+v)=\nabla u+\nabla v;  \\
&(2)\nabla\cdot(\boldsymbol{E}+\boldsymbol{F})=\nabla\cdot\boldsymbol{E}+\nabla\cdot\boldsymbol{F};  \\
&(3)\nabla\times(\boldsymbol{E}+\boldsymbol{F})=\nabla\times\boldsymbol{E}+\nabla\times\boldsymbol{F};  \\
&(4) \nabla\cdot(u\boldsymbol{E})=(\nabla u)\cdot\boldsymbol{E}+u(\nabla\cdot\boldsymbol{E});  \\
&(5)\nabla\times(u\boldsymbol{E})=(\nabla u)\times\boldsymbol{E}+u(\nabla\times\boldsymbol{E}); \\
&(6)\nabla\cdot(\boldsymbol{E}\times\boldsymbol{F})=\boldsymbol{F}\cdot(\nabla\times\boldsymbol{E})-\boldsymbol{E}\cdot(\nabla\times\boldsymbol{F});\\&(7)\nabla\times(\boldsymbol{E}\times\boldsymbol{F})=(\boldsymbol{F}\cdot\nabla)\boldsymbol{E}-\boldsymbol{F}(\nabla\cdot\boldsymbol{E})-(\boldsymbol{E}\cdot\nabla)\boldsymbol{F}+\boldsymbol{E}(\nabla\cdot\boldsymbol{F});\\&(8)\nabla(\boldsymbol{E}\cdot\boldsymbol{F})=(\boldsymbol{F}\cdot\nabla)\boldsymbol{E}+(\boldsymbol{E}\cdot\nabla)\boldsymbol{F}+\boldsymbol{F}\times(\nabla\times\boldsymbol{E})+\boldsymbol{E}\times(\nabla\times\boldsymbol{F});\\
&(9)\nabla \times(\nabla u)=0\\
&(10)\nabla \cdot(\nabla \times E) = 0\\
&(11)\nabla \times(\nabla \times E) = \nabla (\nabla \cdot E)-\nabla ^2E
\end{aligned}
$$
### 1.2.2 拉普拉斯算子
有若干相关的方程：

拉普拉斯方程：$\nabla^2u=0$

亥姆霍兹方程：$\nabla^2u+k^2u=0$

波动方程：$\frac{\partial^2u}{\partial t^2}=a^2\nabla^2u$

热传导方程：$\frac{\partial u}{\partial t}=a^2\nabla^2u$

薛定谔方程：$\mathrm{i}\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\nabla^2\psi+V(r)\psi$
#### 极坐标系中的拉普拉斯算子
$$
\nabla^2u=\frac{\partial^2u}{\partial r^2}+\frac1r\frac{\partial u}{\partial r}+\frac1{r^2}\frac{\partial^2u}{\partial\theta^2}
$$
#### 球坐标拉普拉斯算子
$$
\nabla^2u=\frac1{r^2}\frac\partial{\partial r}\left(r^2\frac{\partial u}{\partial r}\right)+\frac1{r^2\sin\theta}\frac\partial{\partial\theta}\left(\sin\theta\frac{\partial u}{\partial\theta}\right)+\frac1{r^2\sin^2\theta}\frac{\partial^2u}{\partial\phi^2}
$$