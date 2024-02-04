---
title: 【种类并查集】食物链
date: 2019-05-03 14:17:19 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
动物王国中有三类动物A,B,C，这三类动物的食物链构成了有趣的环形。A吃B， B吃C，C吃A。
现有N个动物，以1－N编号。每个动物都是A,B,C中的一种，但是我们并不知道它到底是哪一种。
有人用两种说法对这N个动物所构成的食物链关系进行描述：
第一种说法是“1 X Y”，表示X和Y是同类。
第二种说法是“2 X Y”，表示X吃Y。
此人对N个动物，用上述两种说法，一句接一句地说出K句话，这K句话有的是真的，有的是假的。当一句话满足下列三条之一时，这句话就是假话，否则就是真话。
1） 当前的话与前面的某些真的话冲突，就是假话；
2） 当前的话中X或Y比N大，就是假话；
3） 当前的话表示X吃X，就是假话。
你的任务是根据给定的N（1<=N<=50,000）和K句话（0<=K<=100,000），输出假话的总数。
#  输入
第一行是两个整数N和K，以一个空格分隔。 以下K行每行是三个正整数 D，X，Y，两数之间用一个空格隔开，其中D表示说法的种类。 若D=1，则表示X和Y是同类。 若D=2，则表示X吃Y。
#  输出
只有一个整数，表示假话的数目。
#  样例输入
```
100 7
1 101 1 
2 1 2 
2 2 3 
2 3 3 
1 1 3 
2 3 1 
1 5 5
```
#  样例输出
```
3
```
# 解答
种类并查集板子题！并查集开3倍大小，分别表示某个动物的`同类` `猎物` `天敌`。然后考虑维护，如果A是B的同类，那么A的同类也是B的同类。A是B的天敌，那么A的同类也是B的天敌，A的猎物也是B的猎物。如果A是B的猎物，那么A的同类也是B的猎物，A的天敌是B的同类，A的猎物是B的天敌。完事！
代码：
```cpp
# include <iostream>
using namespace std;
const int MAXN = 50100;
int fa[MAXN*3];
int find(int x){return x==fa[x]?x:fa[x] = find(fa[x]);}
void unionn(int x,int y){fa[find(x)] = find(y);}
bool judge(int x,int y){return find(x)==find(y);}//1 同类 2猎物 3 天敌 
int main(){
    int n,T;cin>>n>>T;
    for(int i = 1;i<=n*3;i++)fa[i] = i;
    int opt,x,y;
    int ans = 0;
    while(T--){
        cin>>opt>>x>>y;
        if(x>n||y>n){ans++;continue;}
        if(opt==1){
            if(find(x+n)==find(y)||find(x+2*n)==find(y)){ans++;continue;}
            unionn(x,y);unionn(x+n,y+n);unionn(x+n+n,y+n+n);
        }else{
            if(find(x)==find(y)||find(x+n+n)==find(y)){ans++;continue;}
            unionn(x,y+n+n);unionn(x+n,y);unionn(x+n+n,y+n);
        }
    }
    cout<<ans;
    return 0;
}
```