---
title: OI技巧总结及例题
date: 2019-10-11 21:04:16 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# OI技巧总结及例题
#  动态规划
#  概率期望
- [] 许多概率期望都是倒着推，有一类概率期望的状态定义是还剩i个的期望步数 ，然后递推。例题[CF398B Painting The Wall](https://www.luogu.org/problem/CF398B)$\ \ \ \ \ \ \ $ [题解](http://blog.leanote.com/post/denghaoyu/8a76b7a5a11b)
#  斜率优化
- [] 一般（但不限于）能把转移方程抽象成这样的形式： $$dp[i]=min/max(a*dp[j]^b+k*W[i]*S[j]+c*K[j]^d+f*L[i]^g)$$
其中$a,b,c,d,f,g,k\in R$ 且 $a,b,c,d,f,g,k\not=0$。
#  计数类问题
- [] 状态定义为还剩a,b,c,d...
# 线段覆盖的妙用
- [] 有些题可以转化为线段覆盖的模型。例题[引水入城](http://192.168.110.251/problempage.php?problem_id=1838) [poj1328]()
# 倍增
#  倍增优化
- [] 倍增不仅可以用来求LCA，还可以用来优化一些不方便维护的东西，比如在有些实在是不好用其他方法(比如数学方法)优化的题。例题：[01 串](http://192.168.110.251/problempage.php?problem_id=4079) [题解](http://blog.leanote.com/post/denghaoyu/%E3%80%90%E5%80%8D%E5%A2%9E%E3%80%9101%E4%B8%B2)
# 数学
- [] n*m的方格从(1,1)走向(n,m)，只能走右或者下的方案数为$C_{n+m-2}^{n-1}$注意MAXN的范围就是m+n而不是MAXN
- [] 递推逆元 `inv[i] = (p-p/i)*inv[p%i]%p`
- [] 表示形如kkkkkk这种数：$k*(10^{x+1}-1)/9$
# 杂七杂八的技巧
- [] 涉及到2个数组交换后相同的题，有可能是逆序对。[例题](http://192.168.110.251/problempage.php?problem_id=1806)
- [] 有些不好处理的线段问题，或许可以拆成2个点来处理，不好处理的矩形问题，或许可以拆成线段再拆成点处理。
# 数据结构
- [] 有一类题，就是想个稍微高级点的做法，然后就上数据结构优化，说白了就是数据结构优化暴力乱搞。[例题](http://192.168.110.251/problempage.php?problem_id=4768)
- [] 对于区间某个数出现次数的问题，可以离线，单独对每一个数进行处理，把这个数的影响全部计算出来。
- [] 
# 图论
- [] 对于某些有多个状态的题，可以考虑spfa的时候加一维状态 [例题](http://192.168.110.251/problempage.php?problem_id=3841) 
- [] 有些最小生成树相关的题，是以kruskal的过程变化来做的，不妨从kruskal的过程方面来考虑
- [] 如果树上两条链相交，那么一条链一定过另一条链的的最浅的点。
- [] dijkstra的重载（>符号）
```
struct node{
	int u;
	ll c,t;
	const bool operator >(const node &b)const{//像这样重载 
		if(c==b.c)return t>b.t;
		return c>b.c;
	}
};
priority_queue<node,vector<node>,greater<node> >q;
```

# 枚举子集
```cpp
for(int y = S;y;y = (y-1)&S)
```
# 应试&答题技巧
#  检查时应记住的一些事项
- [] 一些非MAXN、MAXM数组的空间
- [] 相似的变量名
- [] long long的一系列操作
- [] 数组千万清零，尤其是用第0个元素记录长度的，一定清零
#  关于重构代码
- [] 在自己思维混乱，在原来代码上修改数次后
- [] 修改算法或完全推翻算法时应将相关部分重构
#  考试注意事项
- [] 不要用size做变量名
- [] 头文件,比如`cstdio`
- [] 老版本编译器在结构体内定义比较大小运算符重载记得后面加`const` 在结构体外定义cmp函数时也要写成`const [name] &[varname]`的形式
- [] m和n变量名不要反
- [] 保证暴力不要挂
- [] 卡常暴力超级读优不要写挂
- [] 循环变量ij不要打反
- [] 注意模数是多少，不要多打个0，也不要少打个0eg:$10^8+7$
- [] 对于一类在环上DP的问题，下一个坐标通过取模处理的时候千万要注意是![title](https://cdn.risingentropy.top/images/posts/db243bdab64417d4300004c.png)