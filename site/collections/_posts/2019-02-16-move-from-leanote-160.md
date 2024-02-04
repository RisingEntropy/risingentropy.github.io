---
title: 分块
date: 2019-02-16 11:29:32 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 分块思想
这种算法会将序列（序列长度为N）进行分块，通常设置一个上限K，每一块有至多K个元素。在序列分块问题上，一般会严格要求每个块都要有K个元素，这样就会分成约N/K块。（最后一个块除外） 一般取块大小为$\sqrt N$证明如下：
设每一块大小为$k$,那么一共分为$\frac{N}{k}$块。那么假设一共查询$M$次，每一次最坏情况大约是$k+\frac{N}{k}$则总复杂度为$M(k+\frac{N}{k})$又因为$M$是定值，所以只需要$k+\frac{N}{k}$最小即可，由均值不等式：$a\times b\ge 2\sqrt{ab}$(当且仅当$a=b$时取等)可知，当$k=\frac{N}{k}$时，复杂度最优，那么此时，$k$等于$\sqrt{N}$总复杂度：$M(2\sqrt N)=Θ(M\sqrt N)$
# 例题
至于没什么好讲的，就上例题。
T1[2440](oi.cdshishi.net:8000/problempage.php?problem_id=2440# )
给出一个长为n的数列，以及n个操作，操作涉及区间加法，询问区间内小于某个值x的元素个数。
解答：就是分块，然后每一块排个序，维护一个`lazy tag`，块间查找的时候就是lower_bound查找出来就行了。然后两边跑暴力。注意有些时候`lazy tag`不要忘了。
代码：
```cpp
# include <cstdlib>
# include <iostream>
# include <vector>
# include <cmath>
# include <algorithm>
# include <cstdio>
using namespace std;
const int INF = 0x7f3f3f3f;
const int MAXN = 100010;
int tag[MAXN];
vector<int> blocks[500];
int idx[MAXN];
int block_len,block_cnt;
int a[MAXN];
int n;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
void init(){
    block_len = sqrt(n);
    block_cnt = (n-1)/block_len+1;
    for(int i = 1;i<=n;i++){
        int id = (i-1)/block_len+1;
        idx[i] = id;
        blocks[id].push_back(a[i]);
    }
    for(int i = 1;i<=block_cnt;i++){
        sort(blocks[i].begin(),blocks[i].end());
    }
}
void modify(int l,int r,int v){
    for(int i = l;i<=min(r,block_len*idx[l]);i++){
        a[i]+=v;
    }
    blocks[idx[l]].clear();
    for(int i = block_len*(idx[l]-1)+1;i<=min(block_len*idx[l],n);i++){
        blocks[idx[l]].push_back(a[i]);
    }
    sort(blocks[idx[l]].begin(),blocks[idx[l]].end());
    if(idx[l]!=idx[r]){
        for(int i = idx[l]+1;i<idx[r];i++){
            tag[i]+=v;
        }
        for(int i = block_len*(idx[r]-1)+1;i<=r;i++){
            a[i]+=v;
        }
        blocks[idx[r]].clear();
        for(int i = block_len*(idx[r]-1)+1;i<=min(block_len*idx[r],n);i++){
            blocks[idx[r]].push_back(a[i]);
        }
        sort(blocks[idx[r]].begin(),blocks[idx[r]].end());
    }
}
int query(int l,int r,int x){
    int ans = 0;
    for(int i = l;i<=min(idx[l]*block_len,r);i++){
        if(a[i]<x-tag[idx[l]])ans++;
    }
    if(idx[l]!=idx[r]){
        for(int i = idx[l]+1;i<idx[r];i++){
            int temp = lower_bound(blocks[i].begin(),blocks[i].end(),x-tag[i])-blocks[i].begin();
            ans+=temp;
        }
        for(int i = block_len*(idx[r]-1)+1;i<=r;i++){
            if(a[i]<x-tag[idx[i]])ans++;
        }
    }
    return ans==-INF?-1:ans;
}
int main(){
    n = read();int m = read();
    for(int i = 1;i<=n;i++)a[i] = read();
    init();
    int op,x,y,z;
    for(int i = 1;i<=m;i++){
        op = read(),x = read(),y = read(),z = read();
        if(op==1){
            modify(x,y,z);
        }else{
            printf("%d\n",query(x,y,z));
        }
    }
    return 0;
}
```
T2[2441](oi.cdshishi.net:8000/problempage.php?problem_id=2441)
给出一个长为n的数列
接下来有m次操作，操作有2种
1 x y z 表示修改区间[x,y]增加数z
2 x y z 表示查询区间[x,y]比z小且最大的数，如果都比z大，输出-1
解答：和上一道题一样，维护同样的信息。
```cpp
# include <cstdlib>
# include <iostream>
# include <vector>
# include <cmath>
# include <algorithm>
# include <cstdio>
using namespace std;
const int INF = 0x7f3f3f3f;
const int MAXN = 100010;
int tag[MAXN];
vector<int> blocks[500];
int idx[MAXN];
int block_len,block_cnt;
int a[MAXN];
int n;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
void init(){
    block_len = sqrt(n);
    block_cnt = (n-1)/block_len+1;
    for(int i = 1;i<=n;i++){
        int id = (i-1)/block_len+1;
        idx[i] = id;
        blocks[id].push_back(a[i]);
    }
    for(int i = 1;i<=block_cnt;i++){
        sort(blocks[i].begin(),blocks[i].end());
    }
}
void modify(int l,int r,int v){
    for(int i = l;i<=min(r,block_len*idx[l]);i++){
        a[i]+=v;
    }
    blocks[idx[l]].clear();
    for(int i = block_len*(idx[l]-1)+1;i<=min(block_len*idx[l],n);i++){
        blocks[idx[l]].push_back(a[i]);
    }
    sort(blocks[idx[l]].begin(),blocks[idx[l]].end());
    if(idx[l]!=idx[r]){
        for(int i = idx[l]+1;i<idx[r];i++){
            tag[i]+=v;
        }
        for(int i = block_len*(idx[r]-1)+1;i<=r;i++){
            a[i]+=v;
        }
        blocks[idx[r]].clear();
        for(int i = block_len*(idx[r]-1)+1;i<=min(block_len*idx[r],n);i++){
            blocks[idx[r]].push_back(a[i]);
        }
        sort(blocks[idx[r]].begin(),blocks[idx[r]].end());
    }
}
int query(int l,int r,int x){
    int ans = -INF;
    for(int i = l;i<=min(idx[l]*block_len,r);i++){
        if(a[i]<x-tag[idx[l]]&&a[i]+tag[idx[l]]>ans)ans = a[i]+tag[idx[l]];
    }
    if(idx[l]!=idx[r]){
        for(int i = idx[l]+1;i<idx[r];i++){
            int temp = lower_bound(blocks[i].begin(),blocks[i].end(),x-tag[i])-blocks[i].begin()-1;
            int val;
            if(temp==-1)continue;
            else val = blocks[i][temp]+tag[i];
            if(val>ans){
                ans = val;
            }
        }
        for(int i = block_len*(idx[r]-1)+1;i<=r;i++){
            if(a[i]<x-tag[idx[i]]&&a[i]+tag[idx[i]]>ans)ans = a[i]+tag[idx[i]];
        }
    }
    return ans==-INF?-1:ans;
}
int main(){
    n = read();int m = read();
    for(int i = 1;i<=n;i++)a[i] = read();
    init();
    int op,x,y,z;
    for(int i = 1;i<=m;i++){
        op = read(),x = read(),y = read(),z = read();
        if(op==1){
            modify(x,y,z);
        }else{
            printf("%d\n",query(x,y,z));
        }
    }
    return 0;
}
```
T3 woj 1685
给出一个长为n的数列，以及m个操作，操作涉及区间加法，区间求和。
裸的分块，直接维护块的和与`lazy tag`就好了
```cpp
# include<bits/stdc++.h>
using namespace std;
# define N 100010
# define LL long long
LL lazy[N]={0},v[N],idx[N],sum[N]={0};
//v是原数组，lazy是分块标记， idx记录每个点的块编号,sum是每块的总和 
LL n,m,k;

inline void read(LL &x){
	 x=0;int f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
   	x*=f;
}

void add(LL x,LL y,LL z){
	for(LL i=x;i<=min(idx[x]*k,y);i++){//sqrt(n)
		v[i]+=z;sum[idx[x]]+=z; 
	}

	if(idx[x]!=idx[y]){
		for(LL i=(idx[y]-1)*k+1;i<=y;i++){
			v[i]+=z;sum[idx[y]]+=z; 
		}	
	}	
	for(LL i=idx[x]+1;i<=idx[y]-1;i++) //sqrt(n)
		lazy[i]+=z;
}
LL query(LL x,LL y){
	LL ans=0;
	for(LL i=x;i<=min(idx[x]*k,y);i++){
		ans+=v[i]+lazy[idx[x]];
	}		
	if(idx[x]!=idx[y])
		for(LL i=(idx[y]-1)*k+1;i<=y;i++)
			ans+=v[i]+lazy[idx[y]];
			
	for(LL i=idx[x]+1;i<=idx[y]-1;i++) {//sqrt(n)
		ans+=sum[i]+k*lazy[i];
	}	
	return ans;
}
int main(){
	read(n);read(m);k=sqrt(n);
	for(LL i=1;i<=n;i++)	read(v[i]);
	for(LL i=1;i<=n;i++){	
		idx[i]=(i-1)/k+1;//分块 
		sum[idx[i]]+=v[i];
	}

	while(m--){//n
		LL op,x,y,z;
		read(op);read(x);read(y);
		if(op==1){
			read(z);
			add(x,y,z);			
		} 
		else
			printf("%lld\n",query(x,y));

	}
	return 0;
} 
```
T4woj 3109
给出一个长为n的数列，以及m个操作，操作涉及单点插入，单点询问，数据随机生成。
其实就是用`vector`存每一块中的数，然后动态插入，如果某一块大小超过某个值(比如规定块大小的20倍)，那么直接重构~~替罪羊树~~。
```cpp
# include <cstdio>
# include <algorithm>
# include <stdio.h>
# include <vector>
# include <iostream>
using namespace std;
const int MAXN = 1000010;
vector<int> blocks[10100];
int block_len,block_cnt;
int temp[MAXN],top;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
int query(int pos){
    int i = 1;
    for(;pos>blocks[i].size();i++){
        pos-=blocks[i].size();
    }
    return blocks[i][pos-1];
}
void rebuild(){
    top = 0;
    for(int i = 1;i<=block_cnt;i++){
        for(int j = 0;j<blocks[i].size();j++)temp[++top] = blocks[i][j];
        blocks[i].clear();
    }
    block_len = sqrt(top);
    block_cnt = (top-1)/block_len+1;
    for(int i = 1;i<=top;i++){
        int id = (i-1)/block_len+1;
        blocks[id].push_back(temp[i]);
    }
}
void insert(int pos,int val){
    int i = 1;
    for(;pos>blocks[i].size();i++)pos-=blocks[i].size();
    blocks[i].insert(blocks[i].begin()+pos-1,val);
    if(blocks[i].size()>20*block_len)rebuild();
}
int main(){
    int n = read();
    block_len = sqrt(n);
    block_cnt = (n-1)/block_len+1;
    int t;
    for(int i = 1;i<=n;i++){
        t = read();
        blocks[(i-1)/block_len+1].push_back(t);
    }
    int opt,l,r,c;
    for(int i = 1;i<=n;i++){
        opt = read(),l = read(),r = read(),c = read();
        if(!opt)insert(l,r);
        else printf("%d\n",query(r));
    }
    return 0;
}
```
T5 woj2443
给出一个长为n的数列，以及m个操作，操作涉及询问区间内出现偶数次的数的数量。
这个题，分块真的不好做，直接上莫队就行了。
```cpp
# include <cstdio>
# include <algorithm>
# include <stdio.h>
# include <vector>
# include <iostream>
using namespace std;
const int MAXM = 100010;
const int MAXN = 100010;
int block_len;
struct Q{int l,r,id;bool operator<(const Q&q1){int x = (l-1)/block_len+1;int y = (q1.l-1)/block_len+1;return x==y?r<q1.r:x<y;}}querys[MAXM];
int top;
int a[MAXN],cnt[MAXN],ans;
int anss[MAXM];
void add(int pos){
    cnt[a[pos]]++;
    if(cnt[a[pos]]%2==0)ans++;
    else if(cnt[a[pos]]%2==1&&cnt[a[pos]]!=1)ans--;
}
void del(int pos){
    cnt[a[pos]]--;
    if(cnt[a[pos]]%2==0&&cnt[a[pos]]!=0)ans++;
    else if(cnt[a[pos]]%2==1)ans--;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int n,c,m;cin>>n>>c>>m;
    int l = 0,r = 0;
    for(int i = 1;i<=n;i++){
        cin>>c;a[i] = c;
    }
    block_len = sqrt(n);
    for(int i = 1;i<=m;i++){
        cin>>l>>r;
        querys[++top].l = l,querys[top].r = r,querys[top].id = i;
    }
    sort(querys+1,querys+1+top);
    l = 1,r = 1;cnt[a[1]]++;
    for(int i = 1;i<=m;i++){
        while(l>querys[i].l)add(--l);
        while(r<querys[i].r)add(++r);
        while(l<querys[i].l)del(l++);
        while(r>querys[i].r)del(r--);
        anss[querys[i].id] = ans;
    }
    for(int i = 1;i<=m;i++)cout<<anss[i]<<endl;
    return 0;
}
```