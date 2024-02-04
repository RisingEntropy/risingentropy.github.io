---
title: 【贪心】购买书籍
date: 2019-10-06 10:50:44 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
L的书籍被M偷了以后伤心欲绝，决定再购买一些回来，现在有 N 本书可以买，每本书的价格是 a[i]元。
现在L总共有 M 元，以及 K 张优惠券。 对于每本书，如果使用一张优惠券，则可以用b[i]的优惠价格购买。 注意每本书只能使用一张优惠券，只能购买一次。
L想知道自己最多可以购买几本书？
#  输入
第一行三个整数 N, K, M
接下来 N 行，每行两个整数，表示 a[i]和 b [i]。
#  输出
一个整数表示答案。
#  样例输入
```
4 1 7
3 2
2 2
8 1
4 3
```
#  样例输出
```
3
```
提示
【解释】
选择第 1、 2、 3 本书，其中第3本使用优惠券。总共 5 元。
【数据规模】
对于 20%：N<=10
对于 50%：N<=100
对于另外 20%：K = 0
对于 100%：1<=N<=100000，0<=K<=N，M<=1014，1<=b[i]<=a[i]<=109
标签
# 解答
感谢熊姐姐的题解Orz，太聚了。贪心题，不算特别难想，但是我也想不到。。。。于是随机化贪心过了。。。。。。。。。zxy的hack数据也没hack掉(~~蒟蒻光环~~)
先说随机化贪心的方法，先按照优惠价排序，按照优惠价购买，买完以后如果有剩余的钱就按照原价最小买Orz。然后由于我感觉不太稳，把原序列`random_shuffle`一下，再多跑几遍，跑的时候2种策略计算答案，就A了。~~你来卡我啊~~
贴随机化贪心代码：前面还有一通乱搞乱排序
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <ctime>
using namespace std;
const int MAXN = 100010;
long long n,m,k;
struct book{
	long long a,b;
}bs[MAXN];
bool cmp1(book &b1,book &b2){
	return b1.a<b2.a;
}
bool cmp2(book &b1,book &b2){
	return b1.b<b2.b;
}
bool cmp3(book &b1,book &b2){
	return b1.a-b1.b<b2.a-b2.b;
}
bool cmp4(book &b1,book &b2){
	return b1.a*b1.b<b2.a*b2.b;
}
bool cmp5(book &b1,book &b2){
	return b1.a/b1.b<b2.a/b2.b;
}
long long work(){
	long long sum = m,tot = 0,used = 0;
	for(int i = 1;i<=n;i++){
		if(sum>=bs[i].a)tot++,sum-=bs[i].a;
		else if(used<k&&sum>=bs[i].b)used++,sum-=bs[i].b,tot++;
	}
	long long ret = tot;
	sum = m,tot = 0,used = 0;
	for(int i = 1;i<=n;i++){
		if(sum>=bs[i].b&&used<k)tot++,sum-=bs[i].b,used++;
		else if(sum>=bs[i].a)used++,sum-=bs[i].a,tot++;
	}
	return max(tot,ret);
}
int main(){
	# ifdef BEYONDSTARS
		freopen("testdata.in","r",stdin);
	# endif
	srand(time(0));
	scanf("%lld %lld %lld",&n,&k,&m);
	for(int i = 1;i<=n;i++){
		scanf("%lld %lld",&bs[i].a,&bs[i].b);
	}
	long long ans = work();
	sort(bs+1,bs+1+n,cmp1);ans = max(ans,work());
	sort(bs+1,bs+1+n,cmp2);ans = max(ans,work());
	sort(bs+1,bs+1+n,cmp3);ans = max(ans,work());
	sort(bs+1,bs+1+n,cmp4);ans = max(ans,work());
	sort(bs+1,bs+1+n,cmp5);ans = max(ans,work());

	if(n>5000){
		for(int i = 1;i<=200;i++){
			random_shuffle(bs+1,bs+1+n);ans = max(ans,work());
		}
	}else{
		for(int i = 1;i<=5000;i++){
			random_shuffle(bs+1,bs+1+n);ans = max(ans,work());
		}
	}
	printf("%lld",ans);
	return 0;
}

```
正解：还是贪心，就是优先购买优惠价低的，然后对于剩下的东西，从原价最小开始枚举，看看是把之前用了券的退掉，这个东西用优惠价便宜还是直接买便宜。于是3个set维护差值，优惠价，原价就好了。Orz wtcl
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# include <set>
using namespace std;
typedef pair<int,int> pii;
const int MAXN = 100010;
long long a[MAXN],b[MAXN],id[MAXN];
set<pii> s1,s2,s3;
bool cmp(int x,int y){return b[x]<b[y];}
int main(){
	int n,k;long long m;scanf("%d %d %lld",&n,&k,&m);
	for(int i = 1;i<=n;i++)scanf("%lld %lld",&a[i],&b[i]),id[i] = i;
	sort(id+1,id+1+n,cmp);
	int ans = 0;
	if(k==0){
		sort(a+1,a+1+n);
		for(int i = 1;i<=n;i++){
			if(m>a[i])ans++,m-=a[i];
			else break;
		}
		printf("%d",ans);return 0;
	}
	long long now = 0;
	for(int i = 1;i<=k;i++){
		now+=b[id[i]];if(now>m){printf("%d",ans);return 0;}
		ans++;
		s1.insert(make_pair(a[id[i]]-b[id[i]],id[i]));
	}
	for(int i = k+1;i<=n;i++){
		s2.insert(make_pair(b[id[i]],id[i]));
		s3.insert(make_pair(a[id[i]],id[i]));
	}
	while(s2.size()){
		long long f1 = s1.begin()->first+s2.begin()->first,f2 = s3.begin()->first;
		if(f1<f2){
			now+=f1;
			if(now>m)return 0*printf("%d",ans);
			ans++;
			int id_ = s2.begin()->second;
			s1.erase(s1.begin());s2.erase(s2.begin());
			s3.erase(s3.find(make_pair(a[id_],id_)));
			s1.insert(make_pair(a[id_]-b[id_],id_));
		}else{
			now+=f2;if(now>m)return 0*printf("%d",ans);
			ans++;
			int id_ = s3.begin()->second;
			s2.erase(s2.find(make_pair(b[id_],id_)));s3.erase(s3.begin());
		}
	}
	printf("%d",ans);
	return 0;
}

```
