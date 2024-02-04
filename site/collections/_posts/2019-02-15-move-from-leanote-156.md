---
title: 20190215日考试
date: 2019-02-15 13:03:24 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

T1：
一句话题意：给你一个序列，判断他能否通过栈变得有序且从小到大。
就是个判断出栈顺序是否合法。
# 解答
我太弱了，居然连判断出栈顺序是否合法都不会了。基础太差了，我太弱了。
代码:
```cpp
# include <cstdio>
# include <algorithm>
# include <stdio.h>
# include <vector>
using namespace std;
const int MAXN = 100010;
int a[MAXN],b[MAXN];
int stack[MAXN];int top;
int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        for(int i = 1;i<=n;i++)scanf("%d",&a[i]),b[i] = a[i];
        sort(a+1,a+1+n);
        int A = 1,B = 1;
        bool flag = true;
        while(B<=n){
            if(a[A]==b[B])A++,B++;
            else if(top&&stack[top]==b[B])top--,B++;
            else if(A<=n)stack[++top] = a[A++];
            else {
                flag = false;
                break;
            }
        }
        if(flag)printf("Y\n");else printf("J\n");
    }
    return 0;
}
```
# T2
在平面上有N个点，L需要你选取四个点出来，要求4个点构成一个正方形
 问：有多少中不同的方案（2个方案不同当且仅当所用点不全相同，坐标相同的2个点视为不同的点）
大水题，但是我却只有30分，因为正方形四个顶点坐标公式推错了。。怪不得考不起好高中。。。我太撇了。
md公式搞错了一个地方
```cpp
# include <cstdio>
# include <algorithm>
# include <iostream>
# include <stack>
# include <set>
# include <queue>
# include <cstring>
# include <vector>
using namespace std;
const int MAXN = 20010;
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
vector<pair<int,int> > point;
multiset<pair<int,int> > map;
int main(){
    int n = read();
    int x,y;
    for(int i = 1;i<=n;i++){
        x = read(),y = read();
        point.push_back(make_pair(x,y));
        map.insert(make_pair(x,y));
    }
    int ans = 0;
    sort(point.begin(),point.end());
    for(int i = 0;i<n;i++){
        for(int j = i+1;j<n;j++){
            int x1 = point[i].first,y1 = point[i].second;
            int x2 = point[j].first,y2 = point[j].second;
            if(i==j)continue;
            int x3,x4,y3,y4;
            int sum = x1+x2,delta = y2-y1;
            x3 = (sum+delta)/2;x4=sum-x3;
            if(x3*2!=sum+delta)continue;//卡上精度了，坐标不可能是小数
            sum = y1+y2,delta = x2-x1;
            y4 = (sum+delta)/2,y3 = sum-y4;
            if(y4*2!=sum+delta)continue;
            if(map.find(make_pair(x3,y3))!=map.end()&&map.find(make_pair(x4,y4))!=map.end()){
                ans+=1;
            }
        }
    }
    printf("%d",ans/2);
    return 0;
}

```
# T3
初始有一个空集，依次插入个数 。有 次询问 ，表示询问第 个数加入集合后的排名为的数是多少
权值线段树，但是我没写过，只好把treap拿来抄。。。。太弱了
```cpp
# include <cstdio>
# include <algorithm>
# include <iostream>
# include <stack>
# include <set>
# include <queue>
# include <cstring>
# include <vector>
using namespace std;
const int MAXN = 60010;
struct node{
    int l,r,dat,size,cnt;
    long long val;
}tree[MAXN<<1];
int tot,root;
const  long long INF = 0x7f7f7f7f7f7f;
int NEW(long long val){
    tree[++tot].val = val;
    tree[tot].dat = rand();
    tree[tot].size = tree[tot].cnt = 1;
    return tot;
}
void update(int p){
    tree[p].size = tree[tree[p].l].size+tree[tree[p].r].size+tree[p].cnt;
}
void build(){
    NEW(-INF),NEW(INF);
    tree[1].r = 2;
    root = 1;
    update(root);
}
long long getValByRank(int p,int rank){
    if(p==0)return INF;
    if(tree[tree[p].l].size>=rank)return getValByRank(tree[p].l,rank);
    if(tree[tree[p].l].size+tree[p].cnt>=rank)return tree[p].val;
    return getValByRank(tree[p].r,rank-tree[tree[p].l].size-tree[p].cnt);
}
void zig(int &p){
    int q = tree[p].l;
    tree[p].l = tree[q].r;tree[q].r = p;p = q;
    update(tree[p].r);update(p);
}
void zag(int &p){
    int q = tree[p].r;
    tree[p].r = tree[q].l,tree[q].l = p,p =q;
    update(tree[p].l);update(p);
}
void rotate(int &p){
    if(tree[p].dat<tree[tree[p].l].dat)zig(p);
    if(tree[p].dat<tree[tree[p].r].dat)zag(p);
}
void insert(int &p,long long val){
    if(p==0) {
        p = NEW(val);
        return;
    }
    if(val==tree[p].val){
        tree[p].cnt++;update(p);return;
    }
    if(val<tree[p].val){
        insert(tree[p].l,val);
        rotate(p);
    }else{
        insert(tree[p].r,val);
        rotate(p);
    }
    update(p);
}
long long a[MAXN];
int main(){
    int n,m;scanf("%d %d",&n,&m);
    srand(19260817);
    int maxm = 0;
    for(int i = 1;i<=n;i++)scanf("%lld",&a[i]);
    build();
    for(int i = 1;i<=m;i++){
        int bj;scanf("%d",&bj);
        if(maxm>=bj){
            printf("%lld\n",getValByRank(root,i+1));
        }else{
            for(int j = maxm+1;j<=bj;j++)insert(root,a[j]);
            maxm = bj;
            printf("%lld\n",getValByRank(root,i+1));
        }
    }
    return 0;
}
```
总得分:230。哎，要不是T2多打了个abs，我就可以AK人生第一场比赛了。。。。。。。。。。