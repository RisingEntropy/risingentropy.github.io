---
title: 弱♂子hxy的模拟后总结
date: 2019-10-24 16:17:55 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 10-22
$pts:170$
劳资……~~T2$N$打成$n$就被高一学弟们爆踩了~~
#  T1 $100\ pts$

我猜只有我这样的垃圾才用了三分吧……
明显是个下凸包，所以答案一定在0点上，那么就把零点从小到大sort，答案就是
$$min(-prea_i*x-preb_i+sufa_{i+1}*x+sufb_i)$$
#  T2 $50\ pts$
无语（最大数据全过了
#  T3 $20\ pts$
看T3 ~~正解打了~~就xjb打了个暴力，没有打70pts欧拉回路（主要我也打不来
正解一如既往地毒瘤，涉及边的合并，就那样吧，以后再说

# 10-23 practice（滑稽
#  T1 神仙模拟 $pts\ 57$
读入挂了，没有处理root，完了
#  T2 妙哉 $pts\ 20$
原来绝对值符号可以这么拆：
$$x_1-x_2<=|x_1-x_2|>=x_2-x_1$$
所以对于每个元素的5个数都有这个结论，所以$O(2^5)$枚举一下这五个数的情况，统一赋正负，答案一定出现在某一情况的某两个元素中。由式子知，维护赋值后最大值和最小值
#  T3 $pts\ 20$
~~算错复杂度了~~
直接$O(n^2)$压缩矩阵元素，单调栈求出每个元素左、右边第一个比它小的位置，完了
#  T4 $pts\ 0$
其实就是练我们瞎搞的能力
爆搜可以套**状压**剪枝，也可以根据**性质**直接判断，分类讨论k1k2枚举答案……但是我一个都没想到

纵观以上两次考试，究其原因是~~我太菜了~~没有努力的去找各类性质，没有对问题细心的去进行剖析，而这类努力往往是能收到较好回报的（但仍改变不了T2炸了50分的事实）

# 10-24 
#  被吊打了
#  T1 
水的一批，考场上还想多了，感兴趣的可以看看我yy出的题……

#  T2 $pts\ 50$
败在没有去推*任何的结论* 和重构我的状态定义……都是因为懒
对着我的状态定义死磕了2h没有任何回报
结论：最多需要二层括号使得一层括号内的贡献极大化（我还真不一定能想出来
#  T3 $pts\ 20$
暴力都打挂了……为什么我要开T2
其实专攻T2T3一道题是可行的（而且当时根据我的状况应该攻T3）
结论：最优路线一定可以只在矩形上拐弯，且不走回头路
（其实都挺傻逼的）所以只用算出纵向的代价，且只保留每个矩形靠左的那条边
用set模拟下整个过程，维护在y轴上以前端点的坐标和答案，求出每条线段每个端点的答案，并且可以证明，一个端点的最优解一定是y轴坐标大于或小于它的第一个点
删掉每条线段y坐标内的点，一共$2n$个点，总共$O(nlog(n))$

**总结**：在考场上要选择好策略，例如dp方程重构确实很难，所以要选择适合自己的题、推尽量多的结论，不要在一道题上吊死

# 10-26
~~md考的什么jb玩意~~
#  T1 $pts\ 100$
~~打表可以做。~~
正解是有这么个式子：
$$x_i^2=\frac14[(x_{i-1}+1)^2+(x_{i-1}-1)^2]+\frac12x_{i-1}^2$$
也就是
$$x_i^2=x_{i-1}^2+\frac12$$
y轴上同理（lzg我对不起你）

#  T2 $30\ pts$
**树上信息维护好题**
当时拿到这题：~~“哇sb树上差分”~~
冷静读题后光速打脸
本题毒瘤之处在于B,C两树互有限制，so直接差分只是全代码的$1\over2$
放出两种最终实现：

- [] 树状数组+差分标记

> 在C边能造成贡献的地方打上插入和删除标记，计算时仅考虑边的子树内的标记，因此要在最后$dfs$时将进入节点和离开节点时的计算结果相减
计算时在C树上找到此B树边所对应的两个端点，询问路径上有哪些边被插入了，$dfs$序实现
前者实现了B对C的限制，后者实现了C对B的限制

- [] 线段树合并（未实现）

> 把差分标记打入线段树里（线段树端点对应C树中的剖分），从B树底部向上做。在每个节点合并线段树并加入&删除标记，在C树上路径查询被标记的边
#  不想理T3

# 10-29
~~㕛被吊打了~~
#  T1 $pts\ 60$
按理说是送的……但不知为何我想了个拿不到分的鬼畜方法
既然式子长这样：$ax+by=c$
那么$\Delta x=\frac bd$时$\Delta y=-\frac ad$
所以若我们让$b>a$，那么~~显然~~答案就变成求$x$的最小正整数解或最大负整数解

#  T2 $pts\ 10$
没有把dp方程写下来……因此自认为写了个正确的dp

 - 难点一：叒考了的$strictly\ weak\ ordering$
 我们需要把一定有先后顺序的两元素交换，因为相互冲突的不造成贡献、不影响结果，相互没有限制的……相互都能造成贡献，从而满足了“能够造成贡献的都排在前面”
 - 难点二：被坑了的$dp$方程（此时仅考虑i放的情况）
 $$\begin{cases}dp_{i,j}=dp_{i-1,j}+w\ \ (a_i<j<=b_i)\\
dp_{i,a_i}=max \left( dp_{i,j} \right) +w\ \ \left(j<=min(a_i,b_i)\right)\end{cases}$$

#  T3 ~~隐藏的sb题~~ $pts\ 15$
but我考场上没想出来……
多源最短路能求出每个普通点最近的特殊点的距离，并且可以证明，枚举每一条边时更新两端的点能更新出正确的答案

> **冷静！**考试的时候切忌浮躁
尤其是最近几次考试，浏览题解后其实都没有一头雾水，也就是可做的
求其原因是急于求成和畏难心理，导致了考场上没有高效的思考出问题

# 10-30 
刺激
#  T1 $pts\ 100$
二维偏序问题。
#  T2 $pts\ 40-40$
2D/1D dp问题，用到了四边形不等式的知识……
#  T3 $pts\ 0$
分治高斯消元~~是个什么东西~~

-----
# NOV.

$1,2$号刺激的一批
# 11-1
#  T1 $pts~100$
GCD模板题，记得开long long
#  T2 $pts~70$
哈希大法好

> 正解：对于每个询问区间长度在母串上滑动一个窗口，用桶来记录两个串是否相似（桶忽略元素种类），同时维护一个$diff/same$值，$O(n)$回答每个询问

#  T3 $pts~40$
做法挺多的，考场上想出了正解但是因为前面浪费的时间有点多没有打完，值得反思

 1. 区间修改，单点查值（我）：从小到大统计每个点对其他点的贡献
 2. 单调修改，区间查值：从小到大统计其他点对当前点的贡献（相当于做法一的逆作法，但要好实现的多）
 3. 拆位（待填坑）

# 11-2
#  T1 $pts~65$
一道算法简单的题，但是卡常，不能用map，需要用哈希表……求逆元用exgcd……

#  T2 $pts~70$
真·假算法
如果从大到小排序，能方便地知道方案的合法性，所做出的决策没有**后效性**，从小到大排序就不行
*dp永远都不能有后效性* ~~ddp管我P事~~

#  T3 $pts~16$
cout<<0有16分……这告诉了我们什么……
正解是一个略恶心的计数类dp（恶心在为了避免重复考虑而枚举编号最小的那个子树，虽说这方法也很经典）

> 在3.5h内做三题本来就对我们的时间分配是一个挑战，在很多时候不要花过多时间重复检查，实在不放心对拍即可
发现对于一些问题，用逆向思维或颠倒（操作）顺序、正难则反等技巧会有奇效（1号T3、2号T2）

# 11-5
#  T1 $pts~100$
想清楚模拟和贪心的策略就OK
#  T2 $pts~5$
~~正解写挂~~
对于最小生成树小于$X$的情况，直接求出满足要求的边数$cnt_1$和大于要求的边数$cnt_2$，$(2^{cnt_1}-1)*2^{cnt_2}*2$搞一下即可
对于等于$X$的情况，求出所有能组成最小生成树的边$cnt1$，答案$(2^{cnt_1}-2)*2^{n-cnt_1}$
（减2是因为整棵树不能颜色相同，不乘2是因为ta枚举了所有的情况）
#   T3 $pts~0$
因为**暴力过于不优秀** TLE丢了20分，主要是因为没有充分利用数据的特性（比如可以int存方案，sort比大小）
以后千万不能再犯

正解是重链剖分dfs树倍增，emmm

# 11-6
~~mdzzT~~
#  T1 $pts~0$
又是个不优秀的暴力，不过也不能怪我。就当~~复习下莫反~~思维游♂戏
$$
求\sum_{i=1}^n\sum_{j=1}^m{gcd(i,j)\choose B} \\\\
变形为\sum_{k=1}^{up}{k\choose B}\sum_{i=1}^n\sum_{j=1}^m[gcd(i,j)=k]\\
分块：\sum_{k=1}^{up}{k\choose B}\sum_{i=1}^{ \lfloor  {n\over k}\rfloor}\sum_{j=1}^{\lfloor {m \over k}\rfloor}[gcd(i,j)=1]\\
因为gcd|i,gcd|j，且莫反式子\sum_{d|n}\mu(d)=[n=1]\\
所以：\sum_{k=1}^{up}{k\choose B}\sum_{i=1}^{ \lfloor  {n\over k}\rfloor}\sum_{j=1}^{\lfloor {m \over k}\rfloor}\sum_{d|i,d|j}\mu(d)\\
又分块：\sum_{k=1}^{up}{k\choose B}\sum_{d=1}^{up'}\mu(d)\sum_{i=1}^{ \lfloor  {n\over dk}\rfloor}\sum_{j=1}^{\lfloor {m \over dk}\rfloor}\\
设T=dk\\
有\sum_{T=1}^{up}\sum_{k|T}{k\choose B}\mu({T\over k}){ \lfloor{n\over T}\rfloor}{\lfloor {m \over T}\rfloor}
$$
然后预处理$\mu$整除分块即可（bushi
这样你就有$30$分（滑稽
#  T2 
~~可以用*异或的妙用* 艹过去~~
正解：في ذلك النظر في بنقطة واحدة منك تحديد والده نقطة نهاية الأيسر مؤخرا جعل يشكلون في نطاق الشرعية، حسنا، هذا يجب أن يكون ضئيلة للغاية بين المناطق وسيلة شريفة ثقـة، وعـلى تابعتين نطاق المشروع العظيم هذا غير قانوني دوكوس ثقـة، وعـلى نطاق إما التاليين المشروعة ومشروع العظيم، إما ضئيلة للغاية المشروعة ثقـة، وعـلى واحد.. اذن مثل هاواي الخطط المتكاملة للرصد والتقييم في مسار لمنفعة الأجيال القادمة، أسلافنا أي تطابق نطاق الشرعية، في الحقيقة عن عمق LCA. في أسلوب التعامل مع الاشتراطات، إنه مجرد سؤال بسيط. الأسئلة الأساسية
#  T3 
不可做不可做，溜了溜了

# 11-8
~~mdzz~~被嘲讽了？？？
#  T1 $pts~60$
的确是一道高考题，可以用构造等比数列的方法做，$O(log(n))$
再后一点NOIP姿势，矩阵快速幂优化递推系数，$O(2^3log(n))$
其次是很容易卡常的$O(n)$递推系数emmmm
#  T2 $pts~25$

>第一数组开小了
第二数组忘清空了
第三以为$J$号牌一定出现过（其实出题人还算良心，大样例有卡，但是数组没清空就……）

#  T3 $pts~20$
不可做，但是暴力分拿满了还是不错
（抱紧流泪的自己）

# 11-9
~~正常正常~~
#  T1 $pts~100$
稍稍奇妙的分组背包
**思考的时候冷静点**会更有效，不要打晃
#  T2 $pts~50$
考场上脑子乱成了一团……结果清空大脑就蹦出了一个正确的结论（从重构算法到想到结论不到2min）
成功证明了我上面的话
#  T3 $pts~0$
额……$45^{\omicron}$旋转那个万恶的正方形……我还是太菜了，扫描线都不会

> 固定端点求线段交等价于逆序对问题

# 11-11
#  T1 $pts~100$
树状数组or二分or双指针
#  T2 $pts~100$
发现wjs那一坨的方法很有意思
因为对于一个决策点，他后面一定空2的倍数个格子，所以就相当于$\lfloor{n-m\over 2}\rfloor$个小球，$m$个隔板。
由隔板法可得

$$
ans={{n+m\over 2}\choose m} 
$$
#  T3 $pts~60$
不开long long见祖宗
用线段树区间合并思想搞一搞，注意下细节（挺多的）

#  T4 留坑
等着某位童鞋搞懂

# 11-12

~~今天睡意浓郁~~差点爆0

#  T1 $pts~10$

本来照着70的trie去的，vanvan没想到自己的处理答案挂了：
对于目标串和当前串，枚举的是哪个串的位置就应该处理**好**哪个位置，而不是把这个地方的数处理好，这样才是有正确性的。

> 拓展开来看，对于一类问题，我们在需要询问一些信息的时候，应该确定信息和目标的状态，不能“感觉”确定了或者“用不着完全”确定

#  T2 $pts~60$
这数论算法很牛逼

#  T3 $pts~0$

我 Too young，Too simple，naive again

对于加号的处理，是枚举某一个数后面的数空了加号的个数，但这就有一个问题：最后一个数之后不能放加号，但使得$10^i$的贡献打满，所以此时组合数内不能是$10^i * {n-i-2\choose m-1}$而是$10^i * {n-i-1\choose m}$

> 怎么说呢，今天的状态是有问题的，真没什么好说的，参考意义呢说大也不大，说没有又不是，不往心里去就好了，心态最重要

md困死我了



我们是占位符
。
。
。
。
。
。
。
。
。
。
