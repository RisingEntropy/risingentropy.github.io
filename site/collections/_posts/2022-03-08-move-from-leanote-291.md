---
title: 一点小想法
date: 2022-03-08 20:00:31 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 想法
对于人眼来说，看东西颜色是非常重要的。天空中飘着红色带点黄色的东西，只需要瞟一眼，就可以知道那是国旗。而计算机处理图像是按照（R,G,B）分立成3个通道的方式处理的，也就是说，计算机没有把颜色作为一个整体处理，把三个通道割裂开了（SEnet也只是简单加权）。那能否让计算机向人眼一样，把颜色信息利用起来呢？

# 思考
计算机中，任何一个都可以写成(R,G,B)的形式，换种方式：$Color = x_1*R+x_2*G+x_3*B$，也就是说，任意一种颜色都是(R,G,B)的线性表出，(R,G,B)是颜色空间的一组基。但是由线性代数知识可知，同一个空间的基不止一个，为什么非要用(R,G,B)表示呢？我能不能选取三个我喜欢的颜色$(C_1,C_2,C_3)$来表示呢？(保证$C_1,C_2,C_3$在(R,G,B)表示下的矩阵可逆)用线性代数知识，可以有一下公式:
$$\begin{bmatrix}C_1\\ C_2\\C_3\end{bmatrix}=\begin{bmatrix}x_1,y_1,z_1\\x_2,y_2,z_2\\x_3,y_3,z_3\end{bmatrix}\begin{bmatrix}R\\G\\B\end{bmatrix}$$
由坐标变换:
$$
\begin{bmatrix}R\\G\\B\end{bmatrix}=\begin{bmatrix}x_1,y_1,z_1\\x_2,y_2,z_2\\x_3,y_3,z_3\end{bmatrix}^{-1}\begin{bmatrix}C_1\\ C_2\\C_3\end{bmatrix}
$$
那么任何一个(R,G,B)表示下的颜色，用$(C_1,C_2,C_3)$表示，可以表示为:
$$\begin{bmatrix}r\ g\ b\end{bmatrix}\begin{bmatrix}R\\G\\B\end{bmatrix}=\begin{bmatrix}r\ g\ b\end{bmatrix}\begin{bmatrix}x_1,y_1,z_1\\x_2,y_2,z_2\\x_3,y_3,z_3\end{bmatrix}^{-1}\begin{bmatrix}C_1\\ C_2\\C_3\end{bmatrix}
$$
，此时，我们就得到了这个颜色在新的颜色系统$(C_1,C_2,C_3)$下的坐标。只要我们$(C_1,C_2,C_3)$选择合理，显然有一个结论
>一个颜色C与$C_i(i = 1,2,3)$越接近，那么它在这个基底上的系数就越大

如此，我们就可以通过在这个“变换过的通道”上面的分量值，判断两个颜色是否相近。这样我们就可以非常优秀地通过物体的颜色特征来找到这个物体。**更有用的一个猜想是：因为$C_i $其实是RGB的一个组合，我们这样相当于把RGB三个通道统一起来看了，这和SEnet的权重有一点相似，但是又不完全一样，因为SEnet是把三个通道简单加权，而这里不是简单加权，是根据我需要的物体的色彩特征，考虑颜色特征，而非通道特征**
# 实验
我做了一个小实验，把一个草原的照片中的草提取出来：
原图：![title](https://cdn.risingentropy.top/images/posts/22749fdab644142b47ea19f.png)

把三个颜色(自选的三个，包括深绿色)作为新的基底后，提取在“深绿色通道的图像”

![title](https://cdn.risingentropy.top/images/posts/22749fdab644142b47ea19f.png)

----------

可以发现，这个想法很好的把草的特征提取出来了，并且和其他物体区分开了
# 代码：
```python
from PIL import Image
import numpy as np
# 自己任意选取的三个颜色
base_color1 = (55, 93, 10)  #  深绿色
base_color2 = (16, 181, 245)  #  蓝色
base_color3 = (155, 171, 39)  #  浅绿色
#  已验证构成的矩阵可逆
ori_mat = np.array([list(base_color1), list(base_color2), list(base_color3)])# 将三个颜色的RGB值组成矩阵
inv_mat = np.linalg.inv(ori_mat)# 求逆


def pixelTranform(pix):# 将每个像素的RGB值转化为新的颜色通道下的值
    rgb_mat = np.zeros((1, 3))
    rgb_mat[0][0] = pix[0]
    rgb_mat[0][1] = pix[1]
    rgb_mat[0][2] = pix[2]
    res = np.matmul(rgb_mat, inv_mat)
    return res[0][0], res[0][1], res[0][2]


img = Image.open("test.jpg")
resImg = Image.new("RGB", (img.width, img.height))
resarray = np.zeros((img.width, img.height, 3))
meanGreen = 0# 为了凸显草地，会将整个图的深绿色分量减去一个深绿色分量的平均值
for i in range(0, img.width):
    for j in range(0, img.height):
        res_pix = pixelTranform(img.getpixel((i, j)))
        resarray[i][j][0] = res_pix[0]
        resarray[i][j][1] = res_pix[1]
        resarray[i][j][2] = res_pix[2]
        meanGreen = meanGreen + res_pix[0]

meanGreen = meanGreen / (1.0 * img.width * img.height)

for i in range(0,img.width):
    for j in range(0,img.height):
        resarray[i][j][0] = max(resarray[i][j][0]-meanGreen,0)# 新的颜色基底下，减去平均值后，不保证值是正的，所以要处理一下，这里相当于Relu

resarray = (resarray - np.min(resarray)) / (np.max(resarray) - np.min(resarray))# 归一化

resarray = resarray * 255# 映射回255

resarray = resarray.astype(int)
# 储存图像
for i in range(0, img.width):
    for j in range(0, img.height):
        resImg.putpixel((i, j), (resarray[i][j][0], 0, 0))

resImg.save("result.jpg")# 为了方便，直接保存RGB图，然后后面用matlab只读取R通道，得到深绿色的灰度图

```

# 更进一步的思考
一开始的颜色目前我是人工手动选取的，那是否可以作为参数让机器学习到最优参数呢？因为很多东西其实是有颜色特征的（虽然猫有黑色和白色，但是亚洲人的皮肤都是黄皮肤，所以是有应用场景的）。再进一步，能不能让机器不再学习RGB通道图像，而是学习出来的的通道的图像呢？这样会不会有更好的效果以及更低的复杂度。例如上图，**这么处理后，其实草地的颜色特征已经非常明确了，而这么处理后，图形特征不会丢失。至少不会比就在RGB图上学习差**。

