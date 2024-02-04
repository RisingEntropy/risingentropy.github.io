---
title: CF977D Divide by three multipy by two 
date: 2018-10-24 14:44:03 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

#   题目描述
有一个长度为 $n$ 的数列 $a_i$，要求你将这个数列重排成一个排列 $p_i$，使得对于任意的 $p_i(1 \le i < n)$：

- $p_i \times 2 = p_{i+1}$，或者
- 当 $p_i$ 可以被 $3$ 整除时，$p_i \div 3 = p_{i+1}$。

保证答案存在。

#   输入输出格式

**输入格式：**

输入包含两行。

第一行一个整数 $n(2 \le n \le 100)$，表示数列中的元素个数。  
第二行包含 $n$ 个整数 $a_1, a_2, \dots, a_n (1 \le a_i \le 10^{18})$，描述这个数列。

**输出格式：**

输出应包含 $n$ 个整数 $p_1, p_2, \dots, p_n$，表示你的答案。

#   说明

在第一个样例中，一种可能的合法排列为 $[9,3,6,12,4,8]$。
# 解答
#  法1：乱搞
就是取2个随机数，然后把这两个随机数所代表的的位置的数交换，每交换一次就判断一下是不是符合题意。这样可以过3个点。大概就是小于20左右的数据范围可以过吧。多了就过不了啦
代码：
```cpp
# include <iostream>
# include <time.h>
# include <stdlib.h>
using namespace std;
int n;
long long a[101];
bool judge(){
    for(int i = 1;i<n;i++){
        if(!(a[i]*2ll==a[i+1]||a[i+1]*3ll==a[i])){
            return false;
        }
    }
    return true;
}
void work(){
    int x=0,y = 0;
    srand((int)time(0));
    while(!judge()){
        x=0,y = 0;
        while(x==y) {
            while (x == 0||x==y)x = rand()%(n+1);
            while (y == 0||x==y)y = rand()%(n+1);
        }
        swap(a[x],a[y]);   //as
        x = y = 0;
    }
}
int main(void){
    ios::sync_with_stdio(false);
    cin>>n;
    for(int i = 1;i<=n;i++){
        cin>>a[i];
    }
    work();
    for(int i = 1;i<=n;i++)cout<<a[i]<<' ';
    return 0;
}
```
#  法2：老实地搜索吧
没有什么难度，复杂度也很低，直接搜就行
```cpp
# include <iostream>
# include <time.h>
# include <stdlib.h>
using namespace std;
int n;
long long a[101];
int used[101];
long long ans[101];
inline void print(){
    for(int i = 1;i<=n;i++)cout<<ans[i]<<' ';
    exit(0);
}
void dfs(int pos){
    if(pos>n){
        print();
    }
    for(int i = 1;i<=n;i++){
        if(!used[i]){
            if(a[i]==ans[pos-1]*2||a[i]*3==ans[pos-1]){
                used[i] = true;
                ans[pos] = a[i];
                dfs(pos+1);
                used[i] = false;
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(false);
    cin>>n;
    for(int i = 1;i<=n;i++){
        cin>>a[i];
    }
    for(int i = 1;i<=n;i++){
        ans[1] = a[i];
        used[i] = true;
        dfs(2);
        used[i] = false;
    }
    return 0;
}
```