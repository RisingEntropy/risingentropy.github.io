---
title: bzoj3620
date: 2018-10-26 20:52:24 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
# 题目
“Madoka,不要相信 QB！”伴随着 Homura 的失望地喊叫,Madoka 与 QB 签订了契约.
这是 Modoka 的一个噩梦,也同时是上个轮回中所发生的事.为了使这一次 Madoka 不再与 QB签订契约,Homura 决定在刚到学校的第一天就解决 QB.然而,QB 也是有许多替身的(但在第八话中的剧情显示它也有可能是无限重生的),不过,意志坚定的 Homura 是不会放弃的——她决定
消灭所有可能是 QB 的东西.现在，她已感受到附近的状态,并且把它转化为一个长度为 n 的字符串交给了学 OI 的你.
现在你从她的话中知道 , 所有形似于 A+B+A 的字串都是 QB 或它的替身 , 且len(A)>=k,len(B)>=1 （位置不同其他性质相同的子串算不同子串,位置相同但拆分不同的子串算同一子串）,然后你必须尽快告诉 Homura 这个答案——QB 以及它的替身的数量.
# 输入输出格式
#  输入格式
第一行一个字符串,第二行一个数 k
#  输出格式
仅一行一个数 ans,表示 QB 以及它的替身的数量
#  样例
#  样例输入1
```
aaaaa
1
```
#  样例输出1
```
6
```
#  样例输入2
```
abcabcabc
2
```
#  样例输出2
```
8
```
# 解答
其实还是比较裸的kmp的题。主要是理解清楚kmp的fail的含义**当前失配以后去哪里** 通过这个含义，我们可以想到用它来解决A+B+A的问题。若对于后面的串A，我们发现其实对于A[1]要找到它在前面的A中的对应位置只需要求得fail[i]就行了
对于当前的j来说，只要j!=pos(pos是枚举的开始位置)并且(j-pos+1)*2>=i-pos+1,就是说明两个A串的长度加起来都大于等于(取等是因为len(B)>=1目前枚举到的pos-i串的长度了，肯定不可能构成一个A+B+A型的串，所以要把j向前调整，就是向前跳。最后判断一下如果(j-pos+1)*2>=k,就说明这里找到匹配了，计数加一个。因为这道题说的是只要位置不同就行，即只要对于每一个pos，只要符合条件的j取到的时候，i与之前不同，就不同。所以这里直接ans++一下就行。快写有问题，输出是一样的，但是交上去却死活过不了
以下是代码
```cpp
# include <cstdio>
# include <cstdlib>
# include <time.h>
# include <vector>
# include <cstring>
using namespace std;
int read(){
	int x = 0,f = 1;
	static char c = getchar();
	while(c<'0'||c>'9'){if(c=='-') f = -1;c = getchar();}
	while(c>='0'&&c<='9')x = x*10+c-'0',c = getchar();
	return x*f;
}
const int MAXN = 15010;
int nxt[MAXN];
char str[MAXN];
int n,k;
int ans = 0;
void kmp(int pos){
	int j = 0;
	nxt[pos] = pos-1;
	for(int i = pos+1;i<=n;i++){
		j = nxt[i-1];
		while(j!=pos-1&&str[i]!=str[j+1]) j = nxt[j];
		if(str[i] == str[j+1])j++;
		nxt[i] = j;
	}
	j = nxt[pos];
	for(int i = pos+1;i<=n;i++){
		while(j!=pos-1&&str[i]!=str[j+1])j = nxt[j];
		if(str[i]==str[j+1])j++;
		while((j-pos+1)*2>=(i-pos+1))
			j = nxt[j];
		if((j-pos+1)>=k)
			ans++;
	}
}
int main(void){
	scanf("%s",str+1);
	k = read();
	n = strlen(str+1);
	for(int i = 1;i<=n;i++)kmp(i);//枚举以i作为开头
	printf("%d",ans);
	return 0;
}
```