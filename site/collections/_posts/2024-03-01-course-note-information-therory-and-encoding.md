---
title: "Course Note: Information Theory"

date: 2024-03-01 15:28:35 +0800

image: 'https://cdn.risingentropy.top/images/posts/20240301174111.png'

tags: [course-note, information-theory]

description: Course note for information theory
---
# Textbook: Elements of Information

## Chapter 2

### 熵

离散随机变量$X$的熵被定义为：

$$
H(X)=-\sum p(x)\log p(x)
$$

同时，他也是随机变量$\frac{1}{p(X)}$的期望值，即：$H(X)=E\log \frac{1}{p(X)}$。熵满足如下性质：

$$
1. H(X)\geq 0\\
2. H_b(X)=(\log_ba)H_a(X)
$$

熵有许多意义，其中一种意义是：描述一个随机信号的最短序列的期望长度。

### 联合熵

一对离散随机变量$(X,Y)$的联合熵$H(X,Y)$被定义为：

$$
H(X,Y)=-\sum\limits_{x\in \mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(x,y),
$$

他也可以被写为$p(X,Y)$的期望。


### 条件熵

条件熵被定义为：

$$
\begin{aligned}
H(Y|X)&=\sum\limits_{x\in\mathcal{X}}p(x)H(Y|X=x)\\
&=-\sum\limits_{x\in\mathcal{X}}p(x)\sum\limits_{y\in\mathcal{Y}}p(y|x)\log p(y|x)\\
&=-\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(y|x)\\
&=-E\log p(Y|X)
\end{aligned}
$$

其实也是条件概率的对数的期望


### 链式法则
