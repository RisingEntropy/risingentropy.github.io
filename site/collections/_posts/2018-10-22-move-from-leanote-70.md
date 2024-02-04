---
title: luogu P4932
date: 2018-10-22 19:23:04 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
__stdcall给了你n个点，第i个点有权值x[i]，对于两个点u和v，如果x[u] xor x[v]的结果在二进制表示下有奇数个1，那么在u和v之间连接一个Edge，现在__stdcall想让你求出一共有多少个Edge。

如果你没能成功完成任务，那么__stdcall会让你痛苦一下，你这个测试点就没分了。
# 输入输出格式
#  输入格式：
一行六个整数，n，a，b，c，d，x[0]。
n是点的个数，每个点的权值需要用如下的方式生成。
你需要使用a，b，c，d和x[0]生成一个数组x，生成方式是这样的。
$X_i=(a*X_{i-1}^2+bX_i-1+c)\ mod\ d$
x[i]就是第i个点的权值，点的标号是1到n。

# 输出格式：
输出一个整数，表示一共有多少个Edge。
#  样例1
```
8 98 24 20 100 44
```
#  输出1
```
12
```
#  样例2
```
1000 952537 601907 686180 1000000 673601
```
#  输出2
```
249711
```
# 解答
首先要生成一个x数组对吧？该取模取模。但是注意取模的式子应该是这样的：((a%d*x[i-1]%d*x[i-1]%d+b*x[i-1]%d+c%d)%d+d)%d 就是为了防止它变成负数。
然后注意观察,a xor b中1的个数的奇偶性与a和b中1的个数的奇偶性有关，**当且仅当** a和b中1的个数为奇数时，a xor b中的1的个数是奇数，否则为偶数。对此的解释：
>我们考虑两种情况，a中的1和b中的1是否在同一位置(能否对上)。
1.如果能对上的个数为奇数，如果a中1的个数为奇数，b中个数为偶数，我们先把对上的1的个数忽略。如果a中1的个数为奇数，那么忽略以后a中1的个数为偶数，b中也为偶数，所有a xor b中1的个数为偶数。如果a中1的个数为偶数，b中也为偶数，忽略掉以后，a中1的个数为奇数，b中也为奇数，那么a xor b中的1的个数为偶数。用这种思想，可以得到以上结论

~~语文不太好，如果说的不清楚见谅~~不懂可以私信问我
然后，就简单了，只需要把含有1的个数为奇数的数统计出来，用这个数量乘以含有1为偶数的数的数量想乘，就是答案。这样做复杂度是O(nlogv)。楼下也提到过。但是还是会T掉。那么怎么办呢？经过冥思苦想，我们发现可以把一个数拆了，拆成高低各16位，这样，把这$2^{16}$个数打表，打出来以后，就直接把一个数拆了，然后分别查询高低位里面的1的个数，最后加起来(获得高16位可以直接右移16，获得低16位可以&0xFFFF这个应该能理解吧，不能理解问我)。然后乘一下就行。
以下是AC代码：
```cpp
// luogu-judger-enable-o2
# include <iostream>
using namespace std;
int n,a,b,c,d;
long long x[(int)1e7+50];
int bits_table[69545];
inline int popbit(long long k){//用lowbit计算有多少个1
    int ans = 0;
    while(k){
        ans++;
        k-=(k&-k);
    }
    return ans;
}
void gen(){
    for(int i = 1;i<=n;i++)x[i]=((a%d*x[i-1]%d*x[i-1]%d+b*x[i-1]%d+c%d)%d+d)%d;

    for(int i = 1;i<=65535;i++){
        bits_table[i] = popbit(i);//高低16位中1的个数
    }
}
int main(void){
    ios::sync_with_stdio(false);
    cin>>n>>a>>b>>c>>d>>x[0];
    gen();
    long long single = 0;
    long long even = 0;
    for(int i = 1;i<=n;i++){
        int t = 0;
        t += bits_table[x[i]>>16];//高16位 
        t += bits_table[x[i]&0xFFFF];//低16位 
        if(t&1)single++;
        else even++;
    }
    cout<<single*even<<endl;
    return 0;
}
```