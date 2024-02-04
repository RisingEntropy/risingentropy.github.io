---
title: bzoj 3916
date: 2018-10-25 16:04:17 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目描述
有三个好朋友喜欢在一起玩游戏,A君写下一个字符串S,B君将其复制一遍得到T,C君在T的任意位置(包括首尾)插入一个字符得到U.现在你得到了U,请你找出S.
# 输入输出格式
#  输入格式
第一行一个数N,表示U的长度.
第二行一个字符串U,保证U由大写字母组成
#  输出格式
输出一行,若S不存在,输出"NOT POSSIBLE".若S不唯一,输出"NOT UNIQUE".否则输出S.
# 样例
#  样例1
#  输入
```
7
ABXCABC
```
#  输出
```
ABC
```
#  样例2
#  输入
```
6
ABCDEF
```
#  输出
```
NOT POSSIBLE
```
#  样例三
#  输入
```
9
ABABABABA
```
#  输出
```
NOT UNIQUE
```
# 解答
其实就是~~乱搞~~哈希，枚举每一位，看看这一位是不是加进去的，判断方法是：这一位以前的和以后的hash是不是和另一半相等.
至于这个一半是什么意思呢？其实就是如果这个字符串的长度是偶数的话，明细是不可能的。如果是奇数的话，那么原来串S的长度就是$\lfloor \frac{N}{2}\rfloor$这道题要注意哈希的长度的开始与结束点
代码：
```cpp
# include <iostream>
using namespace std;
const int MAXN = 2000001+10;
unsigned long long Hash[MAXN];
int n;
const int base = 37;//基数
char str[MAXN];
unsigned long long pow[MAXN];//基数的n次方mod mod的值
void work_pow(){
    pow[0] = 1;
    for(int i = 1;i<=n;i++){
        pow[i] = pow[i-1]*base;
    }
}
void calHash(){
    Hash[0] = 0;
    for(int i = 1;i<=n;i++){
        Hash[i] = Hash[i-1]*base+str[i]-'A'+1;//这里还是注意一下每个字母代表的值，如果A代表0的话A不了，不知道为什么
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin>>n;
    cin>>str+1;
    work_pow();
    calHash();
    if(!n&1){
        cout<<"NOT POSSIBLE";
        return 0;
    }
    unsigned long long x = 0;
    unsigned long long y = 0;
    bool found = false;
    unsigned  long long ans ;
    int pos = 0;
    for(int i = 1;i<=n;i++){//枚举每一位
        if(i<=n/2) x = Hash[n/2+1]-Hash[i]*pow[n/2-i+1]+Hash[i-1]*pow[n/2-i+1];
        else x = Hash[n/2];
        if(i<=n/2+1){
            y = Hash[n]-Hash[n/2+1]*pow[n/2];
        }else y = Hash[n] - Hash[i]*pow[n-i]+(Hash[i-1] - Hash[n/2]*pow[i-n/2-1])*pow[n-i];
        if(x==y){
            if(found&&ans!=x){
                cout<<"NOT UNIQUE"<<endl;
                return 0;
            } else{
                pos = i;
                found = true;
                ans = x;
            }
        }
    }
    if(found) {
        if (pos <= (n >> 1)+1) {//原串在后面
            for (int i = (n >> 1) + 2; i <= n; i++) {
                cout << str[i];
            }
        } else {
            for (int i = 1; i <= n >> 1; i++) {
                cout << str[i];
            }
        }
    }else {
        cout<<"NOT POSSIBLE"<<endl;
    }
    return 0;
}
```