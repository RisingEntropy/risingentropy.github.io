---
title: LCA
date: 2018-08-11 09:26:41 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 树上倍增
见模板
# 欧拉遍历序
欧拉序是dfs序的一种，就是在dfs的时候的顺序，计算可以如下
>法1、在每个结点进和出都加进序列。 
    >>1、求某个点到根节点的额权值和。方法是：需要在进的点处做加法，出的点处做减法，查询某点就只需要查询对应的前缀即可。 
*2、求某个子树的权值和。方法是：需要在进的点处做加法，求某个点最后一次出现的位置的前缀和减去第一次出现的位置的前一个位置的前缀和即可。

>法2、只要到达每一个结点就把他加进序列。



# 树的重心
概念：**树的重心也叫树的质心。找到一个点,其所有的子树中最大的子树节点数最少,那么这个点就是这棵树的重心,删去重心后，生成的多棵树尽可能平衡。**
