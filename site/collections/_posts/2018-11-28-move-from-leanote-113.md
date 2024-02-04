---
title: 打表
date: 2018-11-28 17:04:52 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

关于看到这个东西的小伙伴，如果你没看懂的话，可以加鄙人QQ1724458359，我一定会尽我所能解答你的问题。今天上课我讲的可能语速快了一点，我的锅。

# 打表
# 前置技能
1.前缀和
2.估算复杂度
# 前缀和
我们先看一下一个问题：
给定一个序列，支持一下操作
1:给某个数加上`x`
2:查询区间`[l,r]`的和
我们应该怎么做呢？首先可以考虑暴力~~暴力怎么可能过？别想了~~，暴力可以骗到部分分，但是我们应该想一个更好的算法。我们发现如果我们把这个序列全部加起来，用`sum[x]`表示 $\sum_i^x$ 那么对于每个查询`[l,r]`，我们就可以使用`sum[r]-sum[l-1]`来计算这个区间的数的和。我再详细的解释一下：
查询`[l,r]`的和那么$sum[r]=a[1]+a[2]+a[3]...+a[r]$
同理$sum[l-1] = a[1]+a[2]+a[3]...+a[l-1]$那么$sum[r]-sum[l-1]=a[1]-a[1]+a[2]-a[2]+a[3]-a[3]...+a[l-1]-a[l-1]+a[l+1]+a[l+2]+...a[r]$
那么对于修改操作我们该怎么解决呢？其实也非常简单，只需要把`sum[x]到sum[n]`全部加上要修改的值`val`就行啦！
这就是所谓的前缀和。它主要用于单点修改，区间查询的操作。每次查询复杂度为$O(n)$修改复杂度为$O(1)$.它明显适用于修改少，查询多的问题。如果要平均一下修改和查询，那么我们可以使用树状数组(以后gsj大佬讲)，做到修改和查询均是$O(log n)$的复杂度。如果不知道修改和查询谁多的话，就无法选择使用的算法，那么我们会用到另一骗分神器：以后会讲的：分块！

# 估算复杂度
知道一个复杂度的式子，带入数据范围，算出来的值不超过1e8，大概率可以过。
# 打表
我粗略的分为2种，分块打表和裸的打表
# 打表
看一下这道题[反素数](https://www.luogu.org/problemnew/show/P1463)，作为一个垃圾，我真的不会呀。搜索剪枝？智商不够，做不来。那我只好打一个表了，到时候直接就在表里面查，吊打标算！
经过计算，我们可以得到以下一个表：(怎么来的待会说)
```
{1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040,7560,10080,15120,20160,25200,27720,45360,50400,55440,83160,110880,166320,221760,277200,332640,498960,554400,665280,720720,1081080,1441440,2162160,2882880,3603600,4324320,6486480,7207200,8648640,10810800,14414400,17297280,21621600,32432400,36756720,43243200,61261200,73513440,110270160,122522400,147026880,183783600,245044800,294053760,367567200,551350800,698377680,735134400,1102701600,1396755360,2001000000};
```
然后直接查就行了。
那这个怎么表怎么计算呢？好像也很难！但是我会暴力啊！直接暴力算好了。
先算一下$1-500000000$.
当打出了 0 0 到 $5×10^8$
  范围的表之后，我们可以发现打出来的数很少，也就是说此题可以通过打表解。然后，我们可以求出这次打表打出来的最后一个数的约数个数，于是我们可以知道，约数个数不会超过short的范围。
由于short最大可以开到5e8（本机），那么我们可以分四次将表打全。我们可以将上次打表所求出的最后一个数的约数个数作为此次打表的maxn。
附上打表代码：
```cpp
# include<cstdio>
using namespace std;
short a[500000001];
int main()
{
    for(int i=1;i<=1000000000;++i)
        for(int j=(500000000/i)*i+i;j<=1000000000;j+=i)
            a[j-500000000]++;
    short maxn=1152;
    for(int i=1;i<=500000000;++i) if(a[i]>maxn) {maxn=a[i];printf("%d,",i+500000000);}
    return 0;
}
```
感谢文庙校区黄逸大佬提供的题解。~~这道题我写的正解，懒得写暴力了~~
# 分块打表
以一道例题的形式讲
# 题面
# 题目描述
windy定义了一种windy数。不含前导零且相邻两个数字之差至少为2的正整数被称为windy数。 windy想知道，在A和B之间，包括A和B，总共有多少个windy数？
# 输入输出格式
#  输入格式：
包含两个整数，A B。

#  输出格式：
一个整数

# 输入输出样例
#  输入样例# 1： 
```
1 10
```
#  输出样例# 1： 
```
9
```
#  输入样例# 2： 
```
25 50
```
输出样例# 2： 
```
20
```
说明
100%的数据，满足 1 <= A <= B <= 2000000000 。

# 解答
数位dp，但是我又不会。做前缀和一样的打表，分成每100000个数打一次表，统计从1到这个点的windy数的总和，打表程序：
```cpp
# pragma GCC optimize("Ofast")
# include <fstream>
# include <stdlib.h>
# include <cstdio>//打表程序
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
inline bool judge(int x){
        int w=x%10;x/=10;
        while(x)
        {
            if(abs(w-(x%10))<2) return false;
            w=x%10;
            x/=10;
        }
        return true;
}
int main(void){
    ofstream out("data");
    int cnt = 0;
    int round = 0;
    for(int i = 1;i<=2000000000;i++){
        if(judge(i)){
            cnt++;
        }
        round++;
        if(round==1000000){
            round = 0;
            out<<cnt<<',';
        	printf("%.2lf\n",(double)i/(double)2000000000);
		}
    }
    out.close();
    return 0;
}
```


然后就是难度在计算上，如何利用这个前缀和计算呢？我画了一张图(字丑，见谅)
![图片标题](https://cdn.risingentropy.top/images/posts/bda8b02ab644127f6001a4a.png)


AC代码：
```cpp
# pragma GCC optimize("Ofast")
# include <fstream>
# include <stdlib.h>
# include <cstdio>//打表程序
using namespace std;
inline int read(){
    char ch = getchar();
    int f = 1 ,x = 0;
    while(ch > '9' || ch < '0'){if(ch == '-')f = -1; ch = getchar();}
    while(ch >= '0' && ch <= '9'){x = (x << 1) + (x << 3) + ch - '0';ch = getchar();}
    return x * f;
}
inline bool judge(int x){
    int w=x%10;x/=10;
    while(x)
    {
        if(abs(w-(x%10))<2) return false;
        w=x%10;
        x/=10;
    }
    return true;
}
const int block_length = 1000000;

int table[2000000] = {202174,338305,476808,615022,753274,891526,1029740,1168243,1304374,1459689,
1459689,1459689,1459689,1597903,1736155,1874407,2012621,2151124,2287255,2442570,
2597885,2597885,2597885,2597885,2736137,2874389,3012603,3151106,3287237,3442552,
3597867,3733998,3733998,3733998,3733998,3872250,4010464,4148967,4285098,4440413,
4595728,4731859,4870362,4870362,4870362,4870362,5008576,5147079,5283210,5438525,
5593840,5729971,5868474,6006688,6006688,6006688,6006688,6145191,6281322,6436637,
6591952,6728083,6866586,7004800,7143052,7143052,7143052,7143052,7279183,7434498,
7589813,7725944,7864447,8002661,8140913,8279165,8279165,8279165,8279165,8434480,
8589795,8725926,8864429,9002643,9140895,9279147,9417361,9417361,9417361,9417361,
9572676,9708807,9847310,9985524,10123776,10262028,10400242,10538745,10538745,10538745,
10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,
10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,
10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,10538745,
10694060,10830191,10830191,10830191,10830191,10968443,11106657,11245160,11381291,11536606,
11691921,11828052,11966555,11966555,11966555,11966555,12104769,12243272,12379403,12534718,
12690033,12826164,12964667,13102881,13102881,13102881,13102881,13241384,13377515,13532830,
13688145,13824276,13962779,14100993,14239245,14239245,14239245,14239245,14375376,14530691,
14686006,14822137,14960640,15098854,15237106,15375358,15375358,15375358,15375358,15530673,
15685988,15822119,15960622,16098836,16237088,16375340,16513554,16513554,16513554,16513554,
16668869,16805000,16943503,17081717,17219969,17358221,17496435,17634938,17634938,17634938,
17634938,17634938,17773441,17911655,18049907,18188159,18326373,18464876,18601007,18756322,
18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,
18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,
18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,18756322,
18911637,19047768,19186271,19186271,19186271,19186271,19324485,19462988,19599119,19754434,
19909749,20045880,20184383,20322597,20322597,20322597,20322597,20461100,20597231,20752546,
20907861,21043992,21182495,21320709,21458961,21458961,21458961,21458961,21595092,21750407,
21905722,22041853,22180356,22318570,22456822,22595074,22595074,22595074,22595074,22750389,
22905704,23041835,23180338,23318552,23456804,23595056,23733270,23733270,23733270,23733270,
23888585,24024716,24163219,24301433,24439685,24577937,24716151,24854654,24854654,24854654,
24854654,24854654,24993157,25131371,25269623,25407875,25546089,25684592,25820723,25976038,
25976038,25976038,25976038,26114252,26252504,26390756,26528970,26667473,26803604,26958919,
26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,
26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,
26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,26958919,
27114234,27250365,27388868,27527082,27527082,27527082,27527082,27665585,27801716,27957031,
28112346,28248477,28386980,28525194,28663446,28663446,28663446,28663446,28799577,28954892,
29110207,29246338,29384841,29523055,29661307,29799559,29799559,29799559,29799559,29954874,
30110189,30246320,30384823,30523037,30661289,30799541,30937755,30937755,30937755,30937755,
31093070,31229201,31367704,31505918,31644170,31782422,31920636,32059139,32059139,32059139,
32059139,32059139,32197642,32335856,32474108,32612360,32750574,32889077,33025208,33180523,
33180523,33180523,33180523,33318737,33456989,33595241,33733455,33871958,34008089,34163404,
34318719,34318719,34318719,34318719,34456971,34595223,34733437,34871940,35008071,35163386,
35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,
35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,
35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,35163386,
35318701,35454832,35593335,35731549,35869801,35869801,35869801,35869801,36005932,36161247,
36316562,36452693,36591196,36729410,36867662,37005914,37005914,37005914,37005914,37161229,
37316544,37452675,37591178,37729392,37867644,38005896,38144110,38144110,38144110,38144110,
38299425,38435556,38574059,38712273,38850525,38988777,39126991,39265494,39265494,39265494,
39265494,39265494,39403997,39542211,39680463,39818715,39956929,40095432,40231563,40386878,
40386878,40386878,40386878,40525092,40663344,40801596,40939810,41078313,41214444,41369759,
41525074,41525074,41525074,41525074,41663326,41801578,41939792,42078295,42214426,42369741,
42525056,42661187,42661187,42661187,42661187,42799439,42937653,43076156,43212287,43367602,
43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,
43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,
43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,43367602,
43522917,43659048,43797551,43935765,44074017,44212269,44212269,44212269,44212269,44367584,
44522899,44659030,44797533,44935747,45073999,45212251,45350465,45350465,45350465,45350465,
45505780,45641911,45780414,45918628,46056880,46195132,46333346,46471849,46471849,46471849,
46471849,46471849,46610352,46748566,46886818,47025070,47163284,47301787,47437918,47593233,
47593233,47593233,47593233,47731447,47869699,48007951,48146165,48284668,48420799,48576114,
48731429,48731429,48731429,48731429,48869681,49007933,49146147,49284650,49420781,49576096,
49731411,49867542,49867542,49867542,49867542,50005794,50144008,50282511,50418642,50573957,
50729272,50865403,51003906,51003906,51003906,51003906,51142120,51280623,51416754,51572069,
51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,
51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,
51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,51572069,
51727384,51863515,52002018,52140232,52278484,52416736,52554950,52554950,52554950,52554950,
52710265,52846396,52984899,53123113,53261365,53399617,53537831,53676334,53676334,53676334,
53676334,53676334,53814837,53953051,54091303,54229555,54367769,54506272,54642403,54797718,
54797718,54797718,54797718,54935932,55074184,55212436,55350650,55489153,55625284,55780599,
55935914,55935914,55935914,55935914,56074166,56212418,56350632,56489135,56625266,56780581,
56935896,57072027,57072027,57072027,57072027,57210279,57348493,57486996,57623127,57778442,
57933757,58069888,58208391,58208391,58208391,58208391,58346605,58485108,58621239,58776554,
58931869,59068000,59206503,59344717,59344717,59344717,59344717,59483220,59619351,59774666,
59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,
59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,
59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,59774666,
59929981,60066112,60204615,60342829,60481081,60619333,60757547,60896050,60896050,60896050,
60896050,60896050,61034553,61172767,61311019,61449271,61587485,61725988,61862119,62017434,
62017434,62017434,62017434,62155648,62293900,62432152,62570366,62708869,62845000,63000315,
63155630,63155630,63155630,63155630,63293882,63432134,63570348,63708851,63844982,64000297,
64155612,64291743,64291743,64291743,64291743,64429995,64568209,64706712,64842843,64998158,
65153473,65289604,65428107,65428107,65428107,65428107,65566321,65704824,65840955,65996270,
66151585,66287716,66426219,66564433,66564433,66564433,66564433,66702936,66839067,66994382,
67149697,67285828,67424331,67562545,67700797,67700797,67700797,67700797,67836928,67992243,
67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,
67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,
67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,67992243,
67992243,67992243,68130746,68268960,68407212,68545464,68683678,68822181,68958312,69113627,
69113627,69113627,69113627,69251841,69390093,69528345,69666559,69805062,69941193,70096508,
70251823,70251823,70251823,70251823,70390075,70528327,70666541,70805044,70941175,71096490,
71251805,71387936,71387936,71387936,71387936,71526188,71664402,71802905,71939036,72094351,
72249666,72385797,72524300,72524300,72524300,72524300,72662514,72801017,72937148,73092463,
73247778,73383909,73522412,73660626,73660626,73660626,73660626,73799129,73935260,74090575,
74245890,74382021,74520524,74658738,74796990,74796990,74796990,74796990,74933121,75088436,
75243751,75379882,75518385,75656599,75794851,75933103,75933103,75933103,75933103,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,76088418,
76088418,76088418,76226921,76365135,76503387,76641639,76779853,76918356,77054487,77209802,
77209802,77209802,77209802,77348016,77486268,77624520,77762734,77901237,78037368,78192683,
78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,
78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,
78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,78192683,
78347998,78484129,78622632,78760846,78760846,78760846,78760846,78899349,79035480,79190795,
79346110,79482241,79620744,79758958,79897210,79897210,79897210,79897210,80033341,80188656,
80343971,80480102,80618605,80756819,80895071,81033323,81033323,81033323,81033323,81188638,
81343953,81480084,81618587,81756801,81895053,82033305,82171519,82171519,82171519,82171519,
82326834,82462965,82601468,82739682,82877934,83016186,83154400,83292903,83292903,83292903,
83292903,83292903,83431406,83569620,83707872,83846124,83984338,84122841,84258972,84414287,
84414287,84414287,84414287,84552501,84690753,84829005,84967219,85105722,85241853,85397168,
85552483,85552483,85552483,85552483,85690735,85828987,85967201,86105704,86241835,86397150,
86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,
86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,
86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,86397150,
86552465,86688596,86827099,86965313,87103565,87103565,87103565,87103565,87239696,87395011,
87550326,87686457,87824960,87963174,88101426,88239678,88239678,88239678,88239678,88394993,
88550308,88686439,88824942,88963156,89101408,89239660,89377874,89377874,89377874,89377874,
89533189,89669320,89807823,89946037,90084289,90222541,90360755,90499258,90499258,90499258,
90499258,90499258,90637761,90775975,90914227,91052479,91190693,91329196,91465327,91620642,
91620642,91620642,91620642,91758856,91897108,92035360,92173574,92312077,92448208,92603523,
92758838,92758838,92758838,92758838,92897090,93035342,93173556,93312059,93448190,93603505,
93758820,93894951,93894951,93894951,93894951,94033203,94171417,94309920,94446051,94601366,
94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,
94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,
94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,94601366,
94756681,94892812,95031315,95169529,95307781,95446033,95446033,95446033,95446033,95601348,
95756663,95892794,96031297,96169511,96307763,96446015,96584229,96584229,96584229,96584229,
96739544,96875675,97014178,97152392,97290644,97428896,97567110,97705613,97705613,97705613,
97705613,97705613,97844116,97982330,98120582,98258834,98397048,98535551,98671682,98826997,
98826997,98826997,98826997,98965211,99103463,99241715,99379929,99518432,99654563,99809878,
99965193,99965193,99965193,99965193,100103445,100241697,100379911,100518414,100654545,100809860,
100965175,101101306,101101306,101101306,101101306,101239558,101377772,101516275,101652406,101807721,
101963036,102099167,102237670,102237670,102237670,102237670,102375884,102514387,102650518,102805833,
102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,
102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,
102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,102805833,
102961148,103097279,103235782,103373996,103512248,103650500,103788714,103788714,103788714,103788714,
103944029,104080160,104218663,104356877,104495129,104633381,104771595,104910098,104910098,104910098,
104910098,104910098,105048601,105186815,105325067,105463319,105601533,105740036,105876167,106031482,
106031482,106031482,106031482,106169696,106307948,106446200,106584414,106722917,106859048,107014363,
107169678,107169678,107169678,107169678,107307930,107446182,107584396,107722899,107859030,108014345,
108169660,108305791,108305791,108305791,108305791,108444043,108582257,108720760,108856891,109012206,
109167521,109303652,109442155,109442155,109442155,109442155,109580369,109718872,109855003,110010318,
110165633,110301764,110440267,110578481,110578481,110578481,110578481,110716984,110853115,111008430,
111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,
111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,
111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,111008430,
111163745,111299876,111438379,111576593,111714845,111853097,111991311,112129814,112129814,112129814,
112129814,112129814,112268317,112406531,112544783,112683035,112821249,112959752,113095883,113251198,
113251198,113251198,113251198,113389412,113527664,113665916,113804130,113942633,114078764,114234079,
114389394,114389394,114389394,114389394,114527646,114665898,114804112,114942615,115078746,115234061,
115389376,115525507,115525507,115525507,115525507,115663759,115801973,115940476,116076607,116231922,
116387237,116523368,116661871,116661871,116661871,116661871,116800085,116938588,117074719,117230034,
117385349,117521480,117659983,117798197,117798197,117798197,117798197,117936700,118072831,118228146,
118383461,118519592,118658095,118796309,118934561,118934561,118934561,118934561,119070692,119226007,
119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,
119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,
119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,119226007,
119226007,119226007,119364510,119502724,119640976,119779228,119917442,120055945,120192076,120347391,
120347391,120347391,120347391,120485605,120623857,120762109,120900323,121038826,121174957,121330272,
121485587,121485587,121485587,121485587,121623839,121762091,121900305,122038808,122174939,122330254,
122485569,122621700,122621700,122621700,122621700,122759952,122898166,123036669,123172800,123328115,
123483430,123619561,123758064,123758064,123758064,123758064,123896278,124034781,124170912,124326227,
124481542,124617673,124756176,124894390,124894390,124894390,124894390,125032893,125169024,125324339,
125479654,125615785,125754288,125892502,126030754,126030754,126030754,126030754,126166885,126322200,
126477515,126613646,126752149,126890363,127028615,127166867,127166867,127166867,127166867,127322182,
127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,
127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,127322182,};
int cal(int a,int b){
    int ta = a/block_length;
    int tb = b/block_length;
    if(tb-ta<=1){
        int cnt = 0;
        for(int i = a;i<=b;i++){
            if(judge(i))cnt++;
        }
        return cnt;
    }else{
        int up = b/block_length;
        int down = a/block_length;
        int sum1 = 0,sum2 = 0;
        for(int i = down*block_length+1;i<=a-1;i++)if(judge(i))sum1++;
        if(a>=block_length)sum1+=table[down-1];
        for(int i = up*block_length+1;i<=b;i++)if(judge(i))sum2++;
        sum2+=table[up-1];
        return sum2-sum1;
    }

}
int main(void){
    int a,b;
    a = read(),b = read();
    printf("%d",cal(a,b));
    return 0;
}
```
至此，这道题也就完啦，相信你已经学会了分块打表的技能，快来找两道习题练习一下吧！
# 练习题
#  单身数
我自己出了一道题，暴力就别想了。数位dp我应该也给你卡死了，乖乖打表吧！
[单身数](https://www.luogu.org/problemnew/show/U54177)
#  A%B problem
正解是[算术基本定理](https://baike.baidu.com/item/%E7%AE%97%E6%9C%AF%E5%9F%BA%E6%9C%AC%E5%AE%9A%E7%90%86)+暴搜。但是这道题也可以打表过，你可以用它来练习打表
[P1865 A % B Problem](https://www.luogu.org/problemnew/show/P1865)
# 拓展练习
如果你把上面的题给AC了，你可以看一下这一道题，思维难度较大，打表也不是上面讲的打表，这种打表办法在WC2017的挑战里面也用到了
[浏览器](https://www.luogu.org/problemnew/show/P4932)