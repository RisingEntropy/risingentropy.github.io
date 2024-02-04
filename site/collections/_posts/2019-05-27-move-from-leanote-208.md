---
title: fhq treap
date: 2019-05-27 15:38:17 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# fhq treap(神仙数据结构)
前置知识：treap平衡树 BST
# 开始
首先说一下
这个东西可以搞一切bst，treap，splay所能搞的东西
这个东西的学名应该是叫做fhq treap，应该是treap的强化版。
整个数据结构中只有两个操作：
  1.分离（split） 就是把一棵树分成两个树(有按排名分裂和权值分裂两种，下面都有代码)
  2.合并（merge）把两棵树合成一棵树
# 操作
1.插入：
```
split(root,a,x,y);
root=merge(merge(x,new_node(a)),y);
```
这个比较好理解，我们先把树分为x,y两部分，然后把新的节点a看做是一棵树，先与x合并，合并完之后将合并的整体与y合并
2.删除
```
split(root,a,x,z);
split(x,a-1,x,y);
y=merge(ch[y][0],ch[y][1]);
root=merge(merge(x,y),z);
```
首先我们把树分为x和z两部分

那么x树中的最大权值为a

再把x分为x和y两部分。

此时x中的最大权值为a-1，且权值为a的节点一定是y的根节点。

然后我们可以无视y的根节点，直接把y的左右孩子合并起来，这样就成功的删除了根节点，

最后再把x，y，z合并起来就好

3.查询a的排名
```
 split(root,a-1,x,y);
printf("%d\n",siz[x]+1);
root=merge(x,y);
```
我们首先按照a-1的权值把树分开。

那么x树中最大的应该是a-1。

那么a的排名就是siz[x]+1

4.查询排名为a的数

 1 printf("%d\n",val[kth(root,a)]); 

直接调用查找排名的函数即可，

这个函数应该比较好理解。。
5.求x的前驱(前驱定义为小于a，且最大的数)
```cpp
split(root,a-1,x,y);
printf("%d\n",val[kth(x,siz[x])]);
root=merge(x,y);
```
因为要小于a，那么我们按照a-1的权值划分，

x中最大的一定是<=a-1的，

所以我们直接输出x中最大的数就好，

（这里有一个小技巧，因为siz储存的是节点的数目，然后根据二叉查找树的性质，编号最大的就是值最大的）

6.求x的后继(后继定义为大于x，且最小的数)
```
split(root,a,x,y);
printf("%d\n",val[kth(y,1)]);
root=merge(x,y);
```

# 附
按排名分裂
当我们遍历到一个节点时，如果它的权值小于k，那么它的左子树会被分到左边的树里，然后我们遍历它的右儿子，如果大于k，则把它的右子树分到右边的树里。如果到达递归边界now==0怎么办呢？这里会有两种情况：
1.root=0（即第一次split），很明显要给x和y初始化，即x=y=0。
2.split到了叶子节点，此时无法继续split了，只能返回。此时的x=y=0没什么用，因为x和y会在回溯的时候通过地址符号改变。
```cpp
void split(int now,int k,int &x,int &y)
{
    if(!now)
        x=y=0;
    else
    {
        if(k<=siz[ch[now][0]])
        {
            y=now;
            split(ch[now][0],k,x,ch[now][0]);
        }
        else
        {
            x=now;
            split(ch[now][1],k-siz[ch[now][0]]-1,ch[now][1],y);
        }
        update(now);
    }
}
```
按权值分裂
与按权值分裂类似
```cpp
void split(int now,int k,int &x,int &y)
{
    if(!now)
        x=y=0;
    else if(val[now]<=k)
    { 
        x=now;
        split(ch[now][1],k,ch[now][1],y);
    }
    else
    {
        y=now;
        split(ch[now][0],k,x,ch[now][0]);
    }
    update(now);//update(i)为更新size[i]大小的函数
}
```
完整fhq代码：
```cpp
    # include <iostream>
    # include <cstdlib>
    using namespace std;
    struct node{
        int val,rnd,l,r,size;
    }tree[100010];int top,root;
    void pushup(int x){
        tree[x].size = tree[tree[x].l].size+tree[tree[x].r].size+1;
    }
    int newnode(int x){
        tree[++top].val = x;tree[top].size  = 1;tree[top].rnd = rand();
        return top;
    }
    int merge(int x,int y){//x<y
        if(!x||!y)return x+y;//已经空了
        if(tree[x].rnd<tree[y].rnd){
            tree[x].r = merge(tree[x].r,y);
            pushup(x);return x;
        }else {
            tree[y].l = merge(x,tree[y].l);
            pushup(y);return y;
        }
    }
    void split(int now,int k,int &x,int &y){//以x为权值分为两棵树
        if(!now) x=y=0;//
        else {
            if(tree[now].val<=k)
            x = now,split(tree[now].r,k,tree[now].r,y);
            else 
                y = now,split(tree[now].l,k,x,tree[now].l);
            pushup(now);
        }
    }
    int kth(int now,int k){
        while(true){
            if(k<=tree[tree[now].l].size){
                now = tree[now].l;
            }else {
                if(k==tree[tree[now].l].size+1)return now;
                else{
                   k-=tree[tree[now].l].size+1;
                   now = tree[now].r;
                }
            }
        }
    }
    int main(){
        srand(19260817);
        int T,op,x,y,z,a,b;cin>>T;
        while(T--){
            cin>>op>>a;
            if(op==1){
                split(root,a,x,y);
                root = merge(merge(x,newnode(a)),y);
            }else if(op==2){
                split(root,a,x,z);split(x,a-1,x,y);
                y = merge(tree[y].l,tree[y].r);
                root = merge(merge(x,y),z);
            }else if(op==3){
                split(root,a-1,x,y);
                cout<<tree[x].size+1<<endl;
                root = merge(x,y);
            }else if(op==4){
                cout<<tree[kth(root,a)].val<<endl;
            }else if(op==5){
                split(root,a-1,x,y);
                cout<<tree[kth(x,tree[x].size)].val<<endl;
                root = merge(x,y);
            }else if(op==6){
                split(root,a,x,y);
                cout<<tree[kth(y,1)].val<<endl;
                root = merge(x,y);
            }
        }
        return 0;
    }
```
# 文末彩蛋
treap模板
```cpp
//
// Created by dhy on 18-12-2.
//
# include <cstdlib>
# include <cstdio>
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+c-'0';c = getchar(); }
    return x*f;
}
const int SIZE = 100010;
struct Treap{
    int l,r;
    int val,dat;//key code and weight
    int cnt,size;//
}tree[SIZE];
int tot,root,INF = 0x7fffffff;
int New(int val){
    tree[++tot].val = val;
    tree[tot].dat = rand();
    tree[tot].cnt = tree[tot].size = 1;
    return tot;
}
void update(int p){//左旋右旋以后，要更新一下
    tree[p].size = tree[tree[p].l].size+tree[tree[p].r].size+tree[p].cnt;
}
void build(){
    New(-INF),New(INF);
    root = 1;
    tree[1].r = 2;
    update(root);
}
int getRankByVal(int p,int val){
    if(p==0)return 0;//
    if(val==tree[p].val)return tree[tree[p].l].size+1;
    if(val<tree[p].val)return getRankByVal(tree[p].l,val);
    return getRankByVal(tree[p].r,val)+tree[tree[p].l].size+tree[p].cnt;
}
int getValByRank(int p,int rank){
    if(p==0)return INF;
    if(tree[tree[p].l].size>=rank)return getValByRank(tree[p].l,rank);
    if(tree[tree[p].l].size+tree[p].cnt>=rank)return tree[p].val;
    return getValByRank(tree[p].r,rank-tree[tree[p].l].size-tree[p].cnt);
}
void zig(int &p){//turn to right
    int q = tree[p].l;
    tree[p].l = tree[q].r,tree[q].r = p,p = q;
    update(tree[p].r);update(p);
}
void zag(int &p){//turn to left
    int q = tree[p].r;
    tree[p].r = tree[q].l;
    tree[q].l = p;
    p = q;
    update(tree[p].l);
    update(p);
}
void insert(int &p,int val){
    if(p==0){
        p = New(val);
        return;
    }
    if(val == tree[p].val){
        tree[p].cnt++;
        update(p);
        return;
    }
    if(val<tree[p].val){
        insert(tree[p].l,val);
        if(tree[p].dat<tree[tree[p].l].dat)zig(p);//就是插入节点以后，右旋上来
    }else{
        insert(tree[p].r,val);
        if(tree[p].dat<tree[tree[p].r].dat)zag(p);//插入到右子树，左旋上来
    }
    update(p);
}
int getPre(int val){
    int ans = 1;
    int p = root;
    while(p){
        if(val==tree[p].val){
            if(tree[p].l>0){
                p = tree[p].l;
                while(tree[p].r>0)p = tree[p].r;//找到val，然后从val的左节点开始，一路向右走
                ans = p;
            }
            break;
        }
        if(tree[p].val<val&&tree[p].val>tree[ans].val)ans = p;//找前驱，不断更新ans
        p = val<tree[p].val?tree[p].l:tree[p].r;//左走右走
    }
    return tree[ans].val;
}
int getNext(int val){
    int ans = 2;
    int p = root;
    while(p){
        if(val==tree[p].val){
            if(tree[p].r>0){
                p = tree[p].r;
                while(tree[p].l>0)p = tree[p].l;//后继，和上面一样的
                ans = p;
            }
            break;
        }
        if(tree[p].val>val&&tree[p].val<tree[ans].val)ans = p;
        p = val<tree[p].val?tree[p].l:tree[p].r;
    }
    return tree[ans].val;
}
void remove(int &p,int val){
    if(p==0)return;
    if(tree[p].val==val){
        if(tree[p].cnt>1){
            tree[p].cnt--;
            update(p);
            return;
        }
        if(tree[p].l||tree[p].r){//左右子树有一个不为0
            if(tree[p].r==0||tree[tree[p].l].dat>tree[tree[p].r].dat)
                zig(p),remove(tree[p].r,val);
            else
                zag(p),remove(tree[p].l,val);
            update(p);
        }
        else
            p = 0;
        return;
    }
    val<tree[p].val?remove(tree[p].l,val):remove(tree[p].r,val);
    update(p);
}
int main(){
    build();
    int n = read();
    while(n--){
        int opt,x;
        opt = read(),x = read();
        switch (opt){
            case 1:
                insert(root,x);
                break;
            case 2:
                remove(root,x);
                break;
            case 3:
                printf("%d\n",getRankByVal(root,x)-1);
                break;
            case 4:
                printf("%d\n",getValByRank(root,x+1));
                break;
            case 5:
                printf("%d\n",getPre(x));
                break;
            case 6:
                printf("%d\n",getNext(x));
                break;
        }
    }
    return 0;
}
```
splay 模板(无区间反转)
```cpp
    # include <iostream>
    # include <cstdio>
    using namespace std;
    const int MAXN = 100010;
    int a[MAXN];
    int root;
    inline void swap(int &x,int &y){x = x^y;y = y^x;x = x^y;}
    int tree[MAXN][2];int sze[MAXN];int cnt[MAXN];
    int val[MAXN];int lzy[MAXN];int tot;int fa[MAXN];
    int n;
    inline void pushup(int x){sze[x] = sze[tree[x][0]]+sze[tree[x][1]]+cnt[x];}
    int which(int x){return tree[fa[x]][1]==x;}
    void rotate(int x){
        int y = fa[x];int z = fa[y],d = which(x),w = tree[x][d^1];
        tree[y][d] = w;fa[w] = y;
        tree[z][which(y)] = x;fa[x] = z;
        tree[x][d^1] = y;fa[y] = x;
        pushup(y);pushup(x);
    }
    void splay(int x,int tar = 0){
        while(fa[x]!=tar){
            int y = fa[x];int z = fa[y];
            if(z!=tar){
                if(which(x)==which(y))rotate(y);
                else rotate(x);
            }
            rotate(x);
        }
        if(!tar)root = x;
    }
    void pushdown(int x){
        if(lzy[x]){
            swap(tree[x][1],tree[x][0]);
            lzy[tree[x][0]]^= 1;lzy[tree[x][1]]^=1;
            lzy[x] = 0;
        }
    }
    int kth(int rank){
        int curr = root;
        while(1){
            pushdown(curr);
            if(tree[curr][0]&&rank<=sze[tree[curr][0]]){
                curr = tree[curr][0];
            }else if(rank>sze[tree[curr][0]]+cnt[curr]){
                rank-=sze[tree[curr][0]]+cnt[curr];
                curr = tree[curr][1];
            }else return curr;
        }
    }
    void insert(int x){
        int curr = root;int p = 0;
        while(curr&&val[curr]!=x){
            if(x>val[curr])p = curr,curr = tree[curr][1];else p = curr,curr = tree[curr][0];
        }
        if(curr){
            cnt[curr]++;
        }else{
            curr = ++tot;
            if(p)tree[p][x>val[p]] = curr;
            tree[curr][0] = tree[curr][1] = 0;
            fa[curr] = p;val[curr] = x;
            cnt[curr] = sze[curr] = 1;
        }
        splay(curr);
    }
    void find(int x){
        int curr = root;
        while(tree[curr][x>val[curr]]&&val[curr]!=x){
            curr = tree[curr][x>val[curr]];
        }
        splay(curr);
    }
    void reverse(int l,int r){
        int x = kth(l), y =kth(r+2);
        splay(x);
        splay(y,x);
        lzy[tree[y][0]]^=1;
    }
    int pre(int x){
        find(x);
        if(val[root]<x)return root;
        int curr = tree[root][0];
        while(tree[curr][1])curr = tree[curr][1];
        return curr;
    }
    int succ(int x){
        find(x);
        if(val[root]>x)return root;
        int curr = tree[root][1];
        while(tree[curr][0])curr = tree[curr][0];
        return curr;
    }
    void output(int x){
        pushdown(x);
        if(tree[x][0])output(tree[x][0]);
        if(val[x]&&val[x]<=n)printf("%d ",val[x]);
        if(tree[x][1])output(tree[x][1]);
    }
    int main(){
        int m;
        scanf("%d%d",&n,&m);
        int x,y;
        for(int i = 0;i<=n+1;i++)insert(i);
        while(m--){
            scanf("%d%d",&x,&y);
            reverse(x,y);
        }
        output(root);
        return 0;
    }
```
# 参考文献
Chanis博客[传送门](https://www.luogu.org/blog/Chanis/fhq-treap)
范浩强 浅谈数据结构[地址](https://wenku.baidu.com/view/a5f6fefe0066f5335a8121fa.html)