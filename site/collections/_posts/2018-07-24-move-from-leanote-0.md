---
title: C++杂记
date: 2018-07-24 18:12:20 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 设置小数精度
```cpp
cout<<setiosflags(ios::fixed)<<setprecision(3)<<ans;
```

# 1.优化流输出，使其与scanf/printf一样快
>ios::sync_with_stdio(false);//关闭iostream输入输出缓存，使其和printf等函数相差无几

# 2.格式化输出:
I/O流常用控制符：
使用控制符时，在程序开头加投文件# include `<`iomanip`>` C++有两种方法控制格式输出：1、用格式控制符；2、用流对象的成员函数 格式控制符：
dec                                 设置基数为10
hex                                 设置基数为16
oct                                 设置基数为8
setfill(c)                          设置填充字符c
setprecision(n)                     设置显示小数精度为n位
setw(n)                             设置域宽为n个字符
setiosflags(ios::fixed)             固定的浮点显示
 setiosflags(ios::scientific)        指数表示
setiosflags(ios::left)              左对齐
setiosflags(ios::right)             右对齐
setiosflags(ios::skipws)            忽略前导空白
setiosflags(ios::uppercase)         16进制数大写输出
setiosflags(ios::lowercase)         16进制小写输出
成员函数：
flags(10)                           设置基数为10
flags(16)                           设置基数为16
flags(8)                            设置基数为8
flags(c)                            设置填充字符c
precision(n)                        设置显示小数精度为n位
width(n)                            设置域宽为n个字符
 在新版本的c++中头文件已经用iomanip取代了iomanip.h。
　　以下是一些常用的函数:
　　dec 置基数为10 相当于"%d"
　　hex 置基数为16 相当于"%X"
　　oct 置基数为8 相当于"%o"
　　setfill(c) 设填充字符为c
　　setprecision(n) 设显示小数精度为n位
　　setw(n) 设域宽为n个字符
　　setiosflags(ios::fixed) 固定的浮点显示
　　setiosflags(ios::scientific) 指数表示
　　setiosflags(ios::left) 左对齐
　　setiosflags(ios::right) 右对齐
　　setiosflags(ios::skipws 忽略前导空白
　　setiosflags(ios::uppercase) 16进制数大写输出
　　setiosflags(ios::lowercase) 16进制小写输出
　　setiosflags(ios::showpoint) 强制显示小数点
　　setiosflags(ios::showpos) 强制显示符号
可以不使用# include<iomanip>的
cout.precision()设置小数点后精确度，
cout.width()设置宽度，
cout.setf()设置显示格式，比如
cout.setf(ios::left)左对齐
cout.setf(ios::showpoint)不管是否有小数位，显示小数点
cout.fill();不足宽度则填充，如cout.fill('0');
cout.precision(6);
cout.width(8);
cout.setf(ios::left);
cout.setf(ios::showpoint);
cout.fill('0');
仅仅cout.precision(6)和cout.setf(ios::showpoint)时，不知何原因如果为0只显示到小
数点后5位，所以为了在最后加个0,要加上其它3项补充（部分是iomanip里的）：
long flags( ) const 返回当前的格式标志。
long flays(long newflag) 设置格式标志为newflag，返回旧的格式标志。
long setf(long bits) 设置指定的格式标志位，返回旧的格式标志。
long setf(long bits,long field)将field指定的格式标志位置为bits，返回旧的格式标志
long unsetf(long bits) 清除bits指定的格式标志位，返回旧的格式标志。
long fill(char c) 设置填充字符，缺省条件下是空格。
char fill( ) 返回当前填充字符。
int precision(int val) 设置精确度为val，控制输出浮点数的有效位，返回旧值。
int precision( ) 返回旧的精确度值。
int width(int val) 设置显示数据的宽度(域宽),返回旧的域宽。
int width( )只返回当前域宽，缺省宽度为0。这时插入操作能按表示数据的最小宽度显示
数据
dec 十进制的输入输出
hex 十六进制的输入输出
oct 八进制的输入输出
例如用cout<<hex<<i<<endl; 即可以让变量i以16进制的格式输出。
ws 提取空白字符
flush 刷新流
resetiosflags(long) 请除特定的格式标志位
setiosflags(long) 设置特定的格式标志位
setfill(char) 设置填充字符
setprecision(int) 设置输出浮点数的精确度
setw(int) 设置域宽格式变量

# 3.优先队列小根堆
```cpp
priority_queue<int,vector<int>,greater<int>> q;
```
自定义结构体放入优先队列：
重载<运算符