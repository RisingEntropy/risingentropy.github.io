---
title: 几种快读效率比较
date: 2019-02-15 20:11:15 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 几种读入方式效率比较
测试人：成都石室中学 邓皓宇
测试平台：Ubuntu 18.04 
测试如下读入方式(所有代码均附在文末)：

 - cin(cin.cpp)
 - cin(关闭捆绑)(cin(close sync).cpp)
 - cin(管捆绑 tie(0))(cin(close sync tie(0)))
 - scanf (scanf.cpp)
 
数据生成器:gen.cpp
测试时间器：judge.cpp
# 测试1 整数读入
范围 10000000 个int类型读入，运行50次，比较运行时间求平均值。为了模拟最真实的情况，从程序加载时开始计时，程序结束运行时，结束计时
测试结果如下：
|项目名|T1|T2|T3|T4|T5|T6|T7|T8|T9|T10|AVERAGE|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|cin|526 ms|516 ms|504 ms|530 ms|489 ms|494 ms|438 ms|602 ms|532 ms|515 ms|514.6
|cin_close_sync|428 ms|420 ms|392 ms|444 ms|395 ms|405 ms|428 ms|416 ms|476 ms|632 ms|443.6
|cin_close_sync_tie0|489 ms|584 ms|467 ms|413 ms|417 ms|397 ms|389 ms|418 ms|404 ms|594 ms|457.2
|scanf|10411 ms|9816 ms|9820 ms|10414 ms|9725 ms|10081 ms|9922 ms|9594 ms|10289 ms|9956 ms|10002.8

我不这道怎么回事，为什么会出现这种结果，但这是真实的测试结果，我只能选择尊重客观事实。。。~~事实就是dhy太弱了~~

代码：
cin:
```cpp
# include <iostream>
using namespace std;
const int MAXN = 10000000;
int a[MAXN+1];
int main(){
	for(int i = 1;i<=MAXN;i++){
		cin>>a[i];
	}
	return 0;
}
```
cin__close_sync:
```cpp
# include <iostream>
using namespace std;
const int MAXN = 10000000;
int a[MAXN+1];
int main(){
	ios::sync_with_stdio(false);
	for(int i = 1;i<=MAXN;i++){
		cin>>a[i];
	}
	return 0;
}
```
cin tie(0)
```cpp
# include <iostream>
using namespace std;
const int MAXN = 10000000;
int a[MAXN+1];
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	for(int i = 1;i<=MAXN;i++){
		cin>>a[i];
	}
	return 0;
}
```
scanf
```cpp
# include <cstdio>
const int MAXN = 10000000;
int a[MAXN+1];
int main(){
	for(int i = 1;i<=MAXN;i++){
		scanf("%d",&a[i]);
	}
	return 0;
}
```
judge:
```cpp
# include <cstdlib>
# include <cstdio>
# include <ctime>
# include <fstream>
using namespace std;
int main(){
	int T = 10;
	ofstream out("res");
	long long start,end;
	system("./gen>in");
	int tot = 0;
	/*******cin*******/
	printf("%s\n","Start new test");
	out<<"|cin|";
	for(int i = 1;i<=T;i++){
		start = clock();
		system("./cin<in");
		end = clock();
		out<<end-start<<" ms|";
		tot+=end-start;
		printf("%s%d\n","test item:",i);
	}
	out<<double(tot)/double(10)<<endl;
	/*******cin close sync*******/
	tot = 0;
	printf("%s\n","Start new test");
	out<<"|cin_close_sync|";
	for(int i = 1;i<=T;i++){
		start = clock();
		system("./cin_close<in");
		end = clock();
		out<<end-start<<" ms|";
		tot+=end-start;
		printf("%s%d\n","test item:",i);
	}
	out<<double(tot)/double(10)<<endl;

	/*******cin_tie0*******/
		printf("%s\n","Start new test");
	tot = 0;
	out<<"|cin_close_sync_tie0|";
	for(int i = 1;i<=T;i++){
		start = clock();
		system("./cin_close_sync_tie0<in");
		end = clock();
		out<<end-start<<" ms|";
		tot+=end-start;
		printf("%s%d\n","test item:",i);
	}
	out<<double(tot)/double(10)<<endl;
	/*******scanf*******/
		printf("%s\n","Start new test");
	tot = 0;
	out<<"|scanf|";
	for(int i = 1;i<=T;i++){
		start = clock();
		system("./scanf<in");
		end = clock();
		out<<end-start<<" ms|";
		tot+=end-start;
		printf("%s%d\n","test item:",i);
	}
	out<<double(tot)/double(10)<<endl;
	printf("Done");
	return 0;
}
```
gen:
```cpp
# include <cstdlib>
# include <cstdio>
const int MAXN = 10000000;
int main(){
	srand(19260817);
	for(int i = 1;i<=MAXN;i++)printf("%d",rand());
}
```