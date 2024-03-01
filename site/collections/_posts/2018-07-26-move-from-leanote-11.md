---
title: 拓补排序与关键路径
date: 2018-07-26 19:23:45 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# AOV网络
1.定义：在现代化管理中，人们常用有向图来描述和分析一项工程的计划和实施过程，一个工程常被分为多个小的子工程，这些子工程被称为活动（Activity)，在有向图中若以顶点表示活动，有向边表示活动之间的先后关系，这样的图简称为AOV网
说白了AOV就是一个有向无环图(DAG)

# 2.拓补排序算法
AOV网中，把所有活动排成一个序列，使得每个活动的前去活动都排在该活动之前，这个过程称为拓补排序，所得到的活动序列叫拓补序列。
**一个AOV网的拓补序列不唯一，但是所有活动的前驱活动必须在此之前**
对于每一个点
算法思想：
1选择一个入度为0的顶点并输出；
2然后从AOV网中删除此顶点，及以此顶点为起点的所有关联边//尤其是以此为起点的边
3重复以上两步，直到不存在入度为0的顶点为止；
4若输出的顶点数小于AOV的顶点数，则输出有回路信息，否则输出顶点序列就是一种拓补序列
5从第四步可以看出拓补排序可以用来判断一个有向图是否有环，只有有向无环图才存在拓补序列。于是就满足了无后效性，上dp
·如果在有环的图上拓扑排序
·环上的点以及环指向的点不会被访问到
·
算法实现
```cpp
    1数据结构：indgree[i],顶点i的入度
                stack栈
    2初始化top=0栈顶指针置零
    3将初始状态所有入度为0的顶点压栈
    4I = 0计数器
    while(栈非空){
        1 顶点出栈，输出v；i++;
        for(v的每一个后继顶点u)
        1 indgree[u]--;
        2if indgree[u] = 0顶点入栈(好像bfs啊啊啊啊)
    }
    然后算法结束了
```

# 关键路径
1.定义:在现代化管理中，人们常用有向图来描述和分析一项工程的计划和实施过程，一个工程常被分为多个小的子工程，这些子工程被称为活动（Activity)，在带权有向图中若以顶点表示事件，有向边表示活动，边上的权值表示该活动持续的时间，这样的图简称为AOE网。——————百毒百科
源点：整个工程的开始
汇点：整个工程的结束，只有入边，没有出边。其余事件编号为2-(n-1)
关键路径就是从源点到汇点具有最大路径的长度

