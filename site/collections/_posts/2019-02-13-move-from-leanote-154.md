---
title: luoguP4147 玉蟾宫
date: 2019-02-13 21:50:40 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
#  题目背景
有一天，小猫rainbow和freda来到了湘西张家界的天门山玉蟾宫，玉蟾宫宫主蓝兔盛情地款待了它们，并赐予它们一片土地。

#  题目描述
这片土地被分成N*M个格子，每个格子里写着'R'或者'F'，R代表这块土地被赐予了rainbow，F代表这块土地被赐予了freda。

现在freda要在这里卖萌。。。它要找一块矩形土地，要求这片土地都标着'F'并且面积最大。

但是rainbow和freda的OI水平都弱爆了，找不出这块土地，而蓝兔也想看freda卖萌（她显然是不会编程的……），所以它们决定，如果你找到的土地面积为S，它们每人给你S两银子。

#  输入输出格式
#  输入格式：
第一行两个整数N,M，表示矩形土地有N行M列。

接下来N行，每行M个用空格隔开的字符'F'或'R'，描述了矩形土地。

#  输出格式：
输出一个整数，表示你能得到多少银子，即(3*最大'F'矩形土地面积)的值。

#  输入输出样例
#  输入样例# 1： 
```
5 6 
R F F F F F 
F F F F F F 
R R R F F F 
F F F F F F 
F F F F F F
```
输出样例# 1： 
```
45
```
# 解答
lyd和shy真的秀啊，我为什么要在2月13号做这种题？情人节预热？FA♂Q！
悬线法的题。所谓的悬线法就是针对这种题，我们用一根从上到下的线，从左到右扫描，这根线可长可短，每个点左右可以追溯到的最远的的方也可以计算到。然后就可以计算出面积了。预处理up,left,right数组表示(i，j)这个点左右上下的追溯点(up表示的是长度)，然后计算就行了。类似于dp。
代码
```cpp
//
// Created by dhy on 19-2-13.
//
# include <cstring>
# include <cstdio>
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const int MAXN = 1010;
int up[MAXN][MAXN],left[MAXN][MAXN],right[MAXN][MAXN];
char map[MAXN][MAXN];
char s[5];
inline int max(int a,int b){return a>b?a:b;}
inline int min(int a,int b){return a<b?a:b;}
int main(){
    int n = read(),m = read();
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=m;j++){
            scanf("%s",s);
            map[i][j] = s[0];
            up[i][j] = 1;right[i][j] = left[i][j] = j;
        }
    }
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=m;j++){
            if(map[i][j] == 'F'&&map[i][j-1]=='F'){
                left[i][j] = left[i][j-1];
            }
        }
    }
    for(int i = 1;i<=n;i++){
        for(int j = m-1;j>=1;j--){
            if(map[i][j] == 'F'&&map[i][j+1]=='F'){
                right[i][j] = right[i][j+1];
            }
        }
    }
    int ans = 0;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=m;j++){
            if(i>1&&map[i][j]=='F'&&map[i-1][j]=='F'){
                right[i][j] = min(right[i-1][j],right[i][j]);
                left[i][j] = max(left[i-1][j],left[i][j]);
                up[i][j] = up[i-1][j]+1;
            }
            ans = max(ans,up[i][j]*(right[i][j]-left[i][j]+1));
        }
    }
    printf("%d",ans*3);
    return 0;
}
```
最后，吐槽一句洛谷的数据，水啊！我把`map[i][j+1]=='F'`打成了`map[i][j+1=='F']`居然TM过了4个点。