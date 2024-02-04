---
title: SDOI2007线性方程组
date: 2019-03-29 21:56:46 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
已知 n 元线性一次方程组。
其中： n < = 50 ．系数是整数,绝对值<=100 , bi(方程右边)的值都是正整数且<300
根据输入的数据，编程输出方程组的解的情况。
#  输入
n
a11 a12 ... a1n b1

........

an1 an2 ... ann bn

输出
如果方程组无实数解输出-1 ; 　　 如果有无穷多实数解，输出 0 ; 　　 如果有唯一解,则输出解（小数点后保留两位小数，如果解是0,则不保留小数）

样例输入
```
3
2 -1 1 1
4 1 -1 5
1 1 1 0
```
样例输出
```
x1=1.00
x2=0
x3=-1.00
```
高斯消元板题
判断无解看代码
代码：
```cpp
# include <iostream>
# include <cmath>
# include <cstdio>
using namespace std;
double a[110][110],ans[110];
int n;
void deal(int k){
	double p;int x = k;
	for(int i = k+1;i<=n;i++)if(abs(a[i][k])>abs(a[x][k]))x = i;
	if(x!=k)for(int i = k;i<=n+1;i++)swap(a[x][i],a[k][i]);
	for(int i = k+1;i<=n;i++){
		if(a[k][k]!=0){
			p = a[i][k]/a[k][k];
			for(int j = k;j<=n+1;j++){a[i][j]-=p*a[k][j];}
		}
	}
}
bool check(){
	int i,j;
	for(i = 1;i<=n;i++){
		for(j = 1;j<=n;j++)if(a[i][j]!=0)break;
		if(j>n){
			if(a[i][n+1]!=0){//所有系数都为0，但常数不为0无解
				cout<<-1<<endl;return false;
			}else{
				cout<<0<<endl;return false;//有无数解
			}
		}
	}
	return true;
}
void OutAns(){
	for(int i = n;i>0;i--){
		for(int j = n;j>i;j--)a[i][n+1]-=a[i][j]*ans[j];
		if(a[i][i]==0){
			if(a[i][n+1]==0)
				cout<<0<<endl;else cout<<-1<<endl;
			return;
		}
		ans[i] = a[i][n+1]/a[i][i];
	}
	for(int i = 1;i<=n;i++){
		if(ans[i]!=0)
			printf("x%d=%.2f\n",i,ans[i]);
		else printf("x%d=0\n",i);
	}
}
void guass(){
	for(int i = 1;i<=n;i++)deal(i);
	if(check())OutAns();
}
int main(){
	cin>>n;
	for(int i = 1;i<=n;i++)for(int j = 1;j<=n+1;j++)cin>>a[i][j];
	guass();
	return 0;
}
```