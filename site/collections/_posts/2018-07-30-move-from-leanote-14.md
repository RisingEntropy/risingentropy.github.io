---
title: 线性筛选质数
date: 2018-07-30 15:40:40 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 埃式筛法
原理：
质数的倍数一点不是质数
代码：
```cpp
int prime[10000001];
bool judge[10000001];
int tot = 0;
void ph(int N){
    memset(judge,true, sizeof(judge));
    judge[1] = false;
    for(int i = 2;i<=N;i++){
        if(judge[i]){//如果i是质数
           prime[++tot] = i;
        }
        for(int j = 1;i*prime[j]<=N&&j<=tot;j++){
            judge[i*prime[j]] = false;
            if(i%prime[j]==0)break;//这一段是为了判重，即比一个合数大的质数和该合数的乘积可用一个更大的合数和比其小的质数相乘得到。若这里条件成立，说明之前或之后会被判断一次，这以后的合数也可以不管了
        }
    }
}
```