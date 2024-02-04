---
title: 树状数组维护前缀和
date: 2018-08-10 09:37:25 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 构造
1.构造一个序列c,  $c_i$ = $\sum^i_{j=i-2^k+1}a_j$,其中k表示i的二进制表示中末尾连续的0的个数，记lowbit(i) = $2^k$,特别地，记lowbit(0)=0
例如i = $11000_{(2)}$,则k=3，lowbit(i) = $2^3$=8
如何求lowbit(i)? lowbit(i)=i&-i;
即c[i] = a[i-lowbit(i)+1...i]
#  求前缀和
a[i...k]=c[k...k-lowbit(k)+1(>0)]
代码：
```cpp
int sum(int x){
    int cur = x;
    int ans = 0;
    while(cur>0){
            ans+=c[cur];
            cur-=lowbit(cur);
    }
    return ans;
}
```
#  单点修改
```cpp
void add(int x,int y){
    for(;x-n;x+=lowbit(x))c[x]+=y;
}
```
# 可维护运算
1.被操作代数系是交换群(+* xor )满足交换律，结合律，有逆元
不可操作的运算
or - / max

# 多维树状数组
复杂度$O(log^mn)$
代码
```cpp
void add(int x,int y,int value){
    int i = x;
    while(x<=n){
        int j = y;
        while(y<=m){
            c[x][y] += value;
            j+=lowbit(y);
        }
        x+=lowbit(x);
    }
}
```

老师的讲义：
这个公式是区间维护的公式，自己看看应能懂
$$\sum_{i=1}^{k}a_i=\sum_{i=1}^{k}\sum_{j=1}^{i}b_j=\sum_{j=1}^{k}b_j(k+1-j)$$

```cpp
sum[]
for(int i = 1; i <= n; i++) {
  sum[i] = sum[i - 1] + a[i];
}
while(q--) {
  int l, r;
  scanf("%d %d", &l, &r);
  printf("%d\n", sum[r] - sum[l - 1]);
}

--------------------------------

b[]
for(int i = 1; i <= n; i++) {
  b[i] = a[i] - a[i - 1];
}
while(q--) {
  int l, r, x;
  scanf("%d %d %d", &l, &r, &x);
  b[l] += x, b[r + 1] -= x;
}
for(int i = 1; i <= n; i++) {
  b[i] += b[i - 1];
}
// b[i]

--------------------------------
//分块的代码
c[]
int size = (int)sqrt(n);
int getBlock(int x) { // 1-based
  return (x - 1) / size + 1;
}
int getStart(int b) {
  return (b - 1) * size + 1;
}
int getEnd(int b) {
  return min(n, getStart(b + 1) - 1);
}
for(int i = 1; i <= n; i++) {
  c[getBlock(i)] += a[i];
}
while(q--) {
  int opt;
  scanf("%d", &opt);
  if(opt == 1) {
    int p, x;
    scanf("%d %d", &p, &x);
    // a[p] += x
    a[p] += x;
    c[getBlock(p)] += x;
  } else {
    int l, r;
    scanf("%d %d", &l, &r);
    if(getBlock(l) == getBlock(r)) {
      int ans = 0;
      for(int i = l; i <= r; i++) {
        ans += a[i];
      }
      printf("%d\n", ans);
    } else {
      int ans = 0;
      for(int i = getBlock(l) + 1; i <= getBlock(r) - 1; i++) {
        ans += c[i];
      }
      for(int i = l; i <= getEnd(getBlock(l)); i++) {
        ans += a[i];
      }
      for(int i = getStart(getBlock(r)); i <= r; i++) {
        ans += a[i];
      }
      printf("%d\n", ans);
    }
  }
}

--------------------------------

sum[]
for(int i = 1; i <= n; i++) {
  sum[i] = sum[i - 1] + a[i];
}
vector<pair<int, int> > modify;
int C = (int)sqrt(q);
while(q--) {
  int opt;
  scanf("%d", &opt);
  if(opt == 1) {
    int p, x;
    scanf("%d %d", &p, &x);
    // a[p] += x
    modify.push_back(make_pair(p, x));
    if(modify.size() > C) {
      for(int i = 0; i < modify.size(); i++) {
        a[modify[i].first] += modify[i].second;
      }
      for(int i = 1; i <= n; i++) {
        sum[i] = sum[i - 1] + a[i];
      }
      modify.clear();
    }
  } else {
    int l, r;
    scanf("%d %d", &l, &r);
    int ans = sum[r] - sum[l - 1];
    for(int i = 0; i < modify.size(); i++) {
      if(modify[i].first >= l && modify[i].first <= r) {
        ans += modify[i].second;
      }
    }
    printf("%d\n", ans);
  }
}

--------------------------------
//二维前缀和
sum[][]

for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    sum[i][j] = a[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
  }
}

for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    sum[i][j] = a[i][j];
  }
}
for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    sum[i][j] += sum[i - 1][j];
  }
}
for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    sum[i][j] += sum[i][j - 1];
  }
}

int query(int x1, int y1, int x2, int y2) {
  return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1];
}

--------------------------------//二维区间修改
sum[][]
vector<pair<pair<int, int>, int> > modify;
int query(int x1, int y1, int x2, int y2) {
  return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1];
}
for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    sum[i][j] = a[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
    // a[i][j] = sum[i][j] + sum[i - 1][j - 1] - sum[i][j - 1] - sum[i - 1][j];
  }
}
int C = (int)sqrt(n * m);
while(q--) {
  int opt;
  scanf("%d", &opt);
  if(opt == 1) {
    int x1, y1, x2, y2;
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    int ans = query(x1, y1, x2, y2);
    for(int i = 0; i < modify.size(); i++) {
      int curX = modify[i].first.first;
      int curY = modify[i].first.second;
      if(curX >= x1 && curX <= x2 && curY >= y1 && curY <= y2) {
        ans += modify[i].second;
      }
    }
  } else {
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);
    modify.push_back(make_pair(make_pair(x, y), z));
    if(modify.size() > C) {
      for(int i = 0; i < modify.size(); i++) {
        int curX = modify[i].first.first;
        int curY = modify[i].first.second;
        a[curX][curY] += modify[i].second;
      }
      for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
          sum[i][j] = a[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
        }
      }
      modify.clear();
    }
  }
}

--------------------------------
b[][]
for(int i = 1; i <= n; i++) {
  for(int j = 1; j <= m; j++) {
    b[i][j] = a[i][j] + a[i - 1][j - 1] - a[i - 1][j] - a[i][j - 1];
  }
}

--------------------------------
# include <bits/stdc++.h>

using namespace std;

const int MAXN = 500005;

int n, m;
long long c[MAXN], a[MAXN];

int lowbit(int x) {
  return x & -x;
}

// 单次操作复杂度： O(logn)

long long sum(int x) {
  long long res = 0;
  for(; x >= 1; x -= lowbit(x)) res += c[x];
  return res;
}

void add(int x, int y) {
  for(; x <= n; x += lowbit(x)) c[x] += y;
}

int main() {
  scanf("%d %d", &n, &m);
  for(int i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
    add(i, a[i]);
  }
  while(m--) {
    int opt, x, y;
    scanf("%d %d %d", &opt, &x, &y);
    if(opt == 1) {
      add(x, y);
    } else {
      printf("%lld\n", sum(y) - sum(x - 1));
    }
  }
  return 0;
}

--------------------------------
a[]
while(q--) {
  int opt;
  scanf("%d", &opt);
  if(opt == 1) {
    int x;
    scanf("%d", &x);
    if(a[x] == 1) {
      a[x] = 0;
      add(x, -1);
    } else {
      a[x] = 1;
      add(x, 1);
    }
  } else {
    int l, r;
    scanf("%d %d", &l, &r);
    printf("%d\n", sum(r) - sum(l - 1));
  }
}

--------------------------------
c[]
void add(int x, int y) { // a[x] ^= y
  for(; x <= n; x += lowbit(x)) c[x] ^= y;
}
int sum(int x) { // XOR()
  int res = 0;
  for(; x >= 1; x -= lowbit(x)) res ^= c[x];
  return res;
}

--------------------------------//线段树
struct Node {
  int val;
  Node *ls, *rs;
  void pushup() {
    val = max(ls->val, rs->val);
  }
}pool[MAXN];

Node *newNode() {
  static int cnt = 0;
  return &pool[cnt++];
}

Node *build(int l, int r) {
  Node *cur = newNode();
  if(l < r) {
    int mid = (l + r) / 2;
    cur->ls = build(l, mid);
    cur->rs = build(mid + 1, r);
  }
  return cur;
}

int query(Node *cur, int l, int r, int a, int b) {
  if(a <= l && b >= r) {
    return cur->val;
  } else {
    int mid = (l + r) / 2;
    int res = 0;
    if(a <= mid) res = max(res, query(cur->ls, l, mid, a, b));
    if(b > mid) res = max(res, query(cur->rs, mid + 1, r, a, b));
    return res;
  }
}

void modify(Node *cur, int l, int r, int p, int v) {
  if(l == r) {
    cur->val = v;
  } else {
    int mid = (l + r) / 2;
    if(p <= mid) modify(cur->ls, l, mid, p, v);
    else modify(cur->rs, mid + 1, r, p, v);
    cur->pushup();
  }
}

--------------------------------
//区间维护（树状数组）
namespace BIT {
  ll c0[MAXN], c1[MAXN];
  void add(ll *c, int x, ll k) {
    for(; x <= n; x += x & -x) c[x] += k;
  }
  ll sum(ll *c, int x) { 
    ll r = 0; 
    for(; x; x -= x & -x) r += c[x];
    return r;
  }
  void add(int l, int r, ll k) {
    add(c0, l, k); add(c0, r + 1, -k);
    add(c1, l, (l - 1) * k); add(c1, r + 1, -r * k);
  }
  ll sum(int l, int r) {
    return sum(c0, r) * r - sum(c1, r) - sum(c0, l - 1) * (l - 1) + sum(c1, l - 1);
  }
}
```