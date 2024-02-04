---
title: Poj 2559
date: 2019-01-19 11:31:40 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# Description

A histogram is a polygon composed of a sequence of rectangles aligned at a common base line. The rectangles have equal widths but may have different heights. For example, the figure on the left shows the histogram that consists of rectangles with the heights 2, 1, 4, 5, 1, 3, 3, measured in units where 1 is the width of the rectangles: 
![图片标题](https://cdn.risingentropy.top/images/posts/c429a7cab644154ed0006ba.png)

Usually, histograms are used to represent discrete distributions, e.g., the frequencies of characters in texts. Note that the order of the rectangles, i.e., their heights, is important. Calculate the area of the largest rectangle in a histogram that is aligned at the common base line, too. The figure on the right shows the largest aligned rectangle for the depicted histogram.
Input

The input contains several test cases. Each test case describes a histogram and starts with an integer n, denoting the number of rectangles it is composed of. You may assume that 1<=n<=100000. Then follow n integers h1,...,hn, where 0<=hi<=1000000000. These numbers denote the heights of the rectangles of the histogram in left-to-right order. The width of each rectangle is 1. A zero follows the input for the last test case.
Output

For each test case output on a single line the area of the largest rectangle in the specified histogram. Remember that this rectangle must be aligned at the common base line.
# Sample Input
```
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
```
# Sample Output
```
8
4000
```
# 解答
单调栈的做法
我们考虑一个一个地向这个栈里面加入矩形，有两种情况：

 1. 新加入的一块矩形比当前栈顶的矩形高，那么当然选择加入它啦！
 2. 如果当前加入的矩形，比栈顶的矩形矮，那怎么办？我们就要考虑计算一下目前栈里面的矩形可以围成的面积大小了。计算的时候统计一下宽度，如下图所解释：![图片标题](https://cdn.risingentropy.top/images/posts/c429a7cab644154ed0006ba.png)
 
最后，我们需要在后面加一块高为0的矩形，目的是为了防止最后栈里面还有一些矩形。
代码如下
```cpp
# include <iostream>
# include <stack>
# include <cstdio>
using namespace std;
const int MAXN = 100010;
long long a[MAXN];
long long stk[MAXN];
long long w[MAXN];
int p;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
int main(){
	int n;
	ios::sync_with_stdio(false);//poj卡常
	while(cin>>n&&n){
		for(int i = 1;i<=n;i++)cin>>a[i];
		p = 0;
		a[++n] = 0;//插入一块高度为0的矩形
		long long ans = 0;
		for(int i = 1;i<=n;i++){
		    if(stk[p]<a[i])stk[++p] = a[i],w[p] = 1;//如果插入的矩形高度高于，那么直接加
		    else{//如果不高于，那么计算一组解
		        int wei = 0;
		        while(stk[p]>a[i]){
                    wei+=w[p];
                    ans = max(ans,wei*stk[p]);
                    p--;
		        }
		        stk[++p] = a[i],w[p] = wei+1;
		    }
		}
		cout<<ans<<endl;
	}
	return 0;
}
```