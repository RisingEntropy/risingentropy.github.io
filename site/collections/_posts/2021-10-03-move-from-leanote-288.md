---
title: 矩阵与变换研讨
date: 2021-10-03 23:31:35 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---




#   报告中涉及的一些概念和约定

1. 图像的基本几何变换：在本文中指“平移变换”，“旋转变换”，“缩放变换”，“镜像变换”。图像的几何变换可以改变图像的空间位置关系，但是不改变图像的色彩特征。



2. 模型矩阵：对于一个矩阵乘法表示的变换 $\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}a_{1,1},a_{1,2},a_{1,3}\\a_{2,1},a_{2,2},a_{2,3}\\a_{3,1},a_{3,2},a_{3,3}\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}$本报告中将$\begin{bmatrix}a_{1,1},a_{1,2},a_{1,3}\\a_{2,1},a_{2,2},a_{2,3}\\a_{3,1},a_{3,2},a_{3,3}\end{bmatrix}$称为模型矩阵,在代码中用`mat_moudle` 表示





3. 坐标矩阵： 上述概念中$\begin{bmatrix}x\\y\\1\end{bmatrix}$被称为坐标矩阵
4. 代码中涉及的图像表示方法：图像由一个个像素构成，每个像素的颜色由RGBA四个参数描述，分别表示 红 绿 蓝3元色的分量及$\alpha$通道(表示透明度)
5. 矩阵元的行列编号从`0`开始
6. 时间复杂度：描述算法运行时间随着数据规模增大而增大情况的函数用$\Theta$记号表示，通常忽略常数，如：$\Theta(5*n)=\Theta(n)$
#   概况
本文意在探讨矩阵乘法在图像变换处理中的运用，以加深对线性代数的理解水平和运用能力，同时粗略了解计算机图像处理。本文会探讨使用矩阵进行图像变换的必要性及优势。示例程序采用C++语言基于Qt框架编写。
#  对像素处理
代码中，使用`Pixel`表示单个像素，其包括原始`x,y`坐标(coordinate_mat坐标矩阵储存)，变换过后的`x',y'`(res坐标矩阵储存)坐标和像素的RGBA值，然后`Pixel`中存在一个`transfer`函数，其接受一个矩阵作为参数，该矩阵即为模型矩阵，通过该矩阵对该像素的坐标进行变换。
绘制图像的方式为逐个像素绘制，这导致了程序卡顿。绘制具体细节不在本文讨论范围内。可参考附带的程序源码。
不做任何变换的图像效果如下：

![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#  矩阵变换
#   平移变换
平移变换就是变换前后像素的水平及垂直坐标发生了变化。以矩阵的形式表示平移前后的像素关系是为：
$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}1\ \ 0 \ \ \ \Delta x \\0\ \ \  1\ \  \Delta y\\0\ \ \ \  0\ \ \   1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}x+\Delta x\\y+\Delta y\\1\end{bmatrix}$

效果如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#   镜像变换
镜像变换分为水平镜像和垂直镜像。水平镜像是以$y$轴为对称轴；垂直镜像是以$x$轴为对称轴。
水平镜像变换公式如下：
$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}-1\ \ 0 \ \ \ \omega \\0\ \ \  1\ \  0\\0\ \ \ \  0\ \ \   1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}-x+\omega\\y\\1\end{bmatrix}$其中$\omega$的意义是图像对称过后其进行平移一段距离，防止其坐标超出显示区域。
效果如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
垂直镜像变换公式:
$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}1\ \ 0 \ \ \ 0\\0\ \  -1\ \  h\\0\ \ \ \  0\ \ \   1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}x\\-y+h\\1\end{bmatrix}$其中$h$的意义是图像对称过后其进行平移一段距离，防止其坐标超出显示区域。
效果如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#   旋转变换
旋转变换是指图像绕某一点以逆时针或者顺时针旋转一定的角度，长按逆时针方向旋转。为了得到旋转后的新坐标，要经过三个步骤：
>1.坐标原点平移到图像中心处
2.针对新的远点做旋转变换
3.将坐标原点移动回左上角处

变换矩阵可以表示为：
$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}cos\theta\ \ -sin\theta \ \ \ 0\\sin\theta\ \ \ \ \  cos\theta\ \ \ 0\\0\ \ \ \  \ \ \ \  0\ \ \ \ \ \  \   1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}xcos\theta-ysin\theta\\xsin\theta+ycos\theta\\1\end{bmatrix}$

为了简单起见，在事件过程中，我并没有按照3个步骤，而是现将图像平移一段距离，保证旋转过后任然在显示区域内，然后再进行旋转。具体方式是：用一个平移矩阵左乘旋转矩阵作为模型矩阵，然后再进行变换。即：
```cpp
mat_moudle = mat_translate*mat_rotate;
```
效果如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#   缩放变换
图像的缩放指的是通过删掉或者增加像素来改变图像的尺寸。当图像缩小时，图像会变得更清晰；当图像放大时，图像质量会有所下降，因此需要插值。插值算法不在本文讨论范围内，故本文不对变换过后的图像做插值处理。
缩放变换矩阵为：
$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}\alpha\ \ 0 \ \ \ 0\\0\ \   \beta\ \ \ 0\\0\ \ \    0\ \   1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}\alpha x\\\beta y\\1\end{bmatrix}$
当$\alpha=\beta$时，表示等比缩放，$\alpha，\beta>1$时表示放大，反之表示缩小。需要特别注意的是，放大会产生空白像素，若不做插值处理，图像质量会受到极大影响。
效果如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#   使用矩阵的意义与优势
在做此次研讨以前，我一直有个疑惑：为什么非要用矩阵，上述变换得到的坐标矩阵我不需要矩阵运算也能得到，也可以得到相同的效果。但是不妨思考一个问题：对一张图像先平移，后旋转，再放大，最后镜像对称处理，我们需要做多少次运算？如果不使用矩阵，仅仅平凡处理，上一次变换的结果作为下一次变换的输入，4次变换需要对这个图像的每个像素做4次计算，即$4*width*height$次运算(即k次变换的时间复杂度为$\Theta(k*m*n)$)，且过程极其容易出错，代码冗繁。若使用矩阵，我们可以把变换过程和结果分离。先对变换过程处理，处理完了最后体现到变换结果上去，实现极为简单，只需要矩阵乘法即可。如上述4次变换，4次矩阵相乘计算次数为$4*3*3*3=108$,则总计算次数为$108+width*height$(即k次变换的时间复杂度为$\Theta(k+m*n)$)，计算次数大大减少，且变换过程越复杂，计算次数减少越明显。如示例程序中的左右镜像放大，左右镜像平移和平移放大操作，其代码实现仅仅是几个矩阵相乘即可完成，极其简单且灵活。

从另一角度思考，观察我们的模型矩阵$\begin{bmatrix}1\ \ 0 \ \ \ \omega \\0\ \ \  1\ \  0\\0\ \ \ \  0\ \ \   1\end{bmatrix}$（以水平变换为例）为什么是一个`3`阶矩阵？考虑变换的方程
$\left \{ 
\begin{array}{c}
x'=ax+by+c\\y'=cx+dy+e
\end{array}
\right. $
意味着$x'$需要3个元素`[a,b,c]`才能确定(y同理)，通过3阶矩阵刚好可以建立$x,y,C$之间的关系，且不依赖于前面变换的结果。而不使用矩阵的话，每一次维护$x'(y')$都需要依赖于前一次的计算结果，耦合度大大增加。更为巧妙的是，由于矩阵具有结合律，使得矩阵运算可以并行计算(可以理解为拆成几个部分多台计算机同时计算)，对于大量的变换可以通过并行计算技术节约大量时间，而不适用矩阵直接“硬维护”，使得每一次变换结果都依赖于上一次，根本不可能并行计算。

从行列式的角度考虑，通过分块矩阵计算，不难发现模型矩阵的行列式恒为`1`也就是说可以方便得求出其逆,且其逆即为其伴随矩阵，而如果“硬维护”，求逆将会非常困难。
#   补充：矩阵的控制点变换
图像的控制点变换是指根据输入和输出的图像的控制点的位置信息，将图像进行变换。利用控制点变换可以进行图像的变形处理，以达到某种特殊效果。通俗地讲，就是根据变换前后3个对应的点的坐标关系，解出整个变换矩阵。（如下是克拉默法则解法）
以三角形区域变换为例：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
坐标变换矩阵如下：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
求解参数：
![title](https://cdn.risingentropy.top/images/posts/15a6ca5ab644142b41cb4b4.png)
#   参考资料

数字图像处理原理与实现方法(全红艳 曹桂涛) 机械工业出版社 2014年1月第1版第1次印刷

Qt5 reference:[https://doc.qt.io/qt-5/reference-overview.html](https://doc.qt.io/qt-5/reference-overview.html)

代码及文档：[https://github.com/RisingEntropy/LinearAlgebraDiscussion](https://github.com/RisingEntropy/LinearAlgebraDiscussion)