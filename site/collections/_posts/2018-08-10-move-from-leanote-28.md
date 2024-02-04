---
title: 树状数组板子
date: 2018-08-10 16:03:59 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 一维：
```cpp
c[];//
int lowbit(int x){
    return x&-x;//自证不难个屁
}
void add(int x,int value){
    while(x<=n){
    c[x]+=value;//*=  ^  
    x+=lowbit(x);
    }
}
int sum(int x){
    int ans = 0;
    int i = x;
    while(x>0){
        ans+=c[i];
        i -= lowbit[i];
    }
}
```
# 二维
```cpp
c[][];
void add(int x,int y,int value){
    int i = x;
    while(x<=n){
        int j = y;
        while(y<=m){
            c[x][y] += value;
            j+=lowbit(y);
        }
        x+=lowbit(x);
    }
}
int sum(int x,int y){
    int ans;
    while(x>0){
    int j = y;
    while(j>0){
        ans+=c[x][j];
        j-=lowbit(j);
    }
    x-=lowbit(x);
    }
}
```
# 高维：和二维一样，自己推