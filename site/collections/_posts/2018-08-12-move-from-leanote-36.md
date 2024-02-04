---
title: ST快速查询区间最值板子
date: 2018-08-12 14:23:50 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
int max = ....;
int logN = 20;//自己改，值是log2 N
int a[],F[max][logN],int log2[];
cin>>a;
log2[0] = -1;
for(1...N){
    log[i] = log[i/2]+1;
    F[i][0] = a[i];
}
for(int j :1...logN)
    for(int i = 1;i+(1<<j)-1<=N;i++)
        F[i][j] = max(F[i][j-1],F[i+(1<<j-1)][j-1]);
    for(每个询问){
        int s,e;
        cin>>s>>e;
        int tem = logN[e-s+1];// log2(e-s+1)的向下取整的值
        cout<<max(f[s][tem],F[e-(1<<tem)+1][tem]);
        }
```