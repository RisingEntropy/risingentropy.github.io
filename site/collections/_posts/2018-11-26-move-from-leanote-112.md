---
title: 平衡树Treap
date: 2018-11-26 14:39:59 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 二叉查找树
给定一颗二叉树，树上每个节点都带有一个数值，称为该节点的“关键码”，所谓“BST性质”指的是：
1.该节点的关键码不小于它的左子树中任意节点的关键码；
2.该节点的关键码不大于它的右子树中任意节点的关键码。
满足上述性质的二叉树就是一颗“二叉查找树(BST)”。显然，二叉查找树的中序便利是一个关键码单调递增的节点序列
# BST的建立
为了避免月结，减少边界情况的特殊判断,一般在一个关键码为正无穷(一个很大的正整数)和一个关键码为负无穷的节点，仅由这两个节点构成的BST就是一颗初始的空BST。
```cpp
const int MAXN = 99;
struct BST{
	int l,r;
	int val;
}tree[MAXN];
int tot,root,INF = 1<<30;
int New(int val){
	tree[++tot].val = val;
	return tot;	
}
void build(){
	New(-INF),New(INF);
	root = 1;
	tree[1].r = 2;
}
```
 # BST检索
 在BST中检索是否存在关键码为val的节点。
 设变量p为根节点root，执行以下过程：
 1.若p的关键码等于val，则已经找到
 2.若p的关键码大于val
 (1)若p的左节点为空，则说明不存在
 (2)若p的做节点不为空，则在p的子树中递归检索
 3.若p的关键码小于val
  (1)若p的右节点为空，则说明不存在
 (2)若p的右节点不为空，则在p的子树中递归检索
```cpp
 int search(int p,int val){
	if(p==0)return 0;
	if(val==tree[p].val)return p;
	return val<tree[p].val?search(tree[p].l,val):search(tree[p].r,val;
}
```
# BST插入
在BST中插入一个新的值val，(假设目前BST中不存在关键码为val的节点)。
与BST的检索过程类似
在发现要走向的p的子节点为空，说明val不存在时，直接建立关键码为val的新节点作为p的子节点。
```cpp
void insert(int &p,int val){
	if(p==0){
		p = New(val);
		return;
	}
	if(val==tree[p].val)return;
	if(val<tree[p].val)insert(tree[p].l,val);
	else insert(tree[p].r,val);
}
```
# 求BST的前驱/后继
val的后继是指在BST的关键码大于val的前提下，关键码最小的节点。
初始化ans为具有正无穷关键码的那个节点的编号。然后，在BST中检索val。在检索的过程中，每经过一个节点，就检查该节点的关键码，判断能否跟新所求的后继ans；
检索完成后可能有三种结果:
1.没有找到val.
此时val的后继就在已经经过的
2.找到了关键码为val的节点p，但是p没有右子树。与上一种情况相同，ans就是所求找到了关键码为val的节点p，且p有右子树，那么从p的右子树出发，一直向左走，就找到了val的后继
```cpp
int getNext(int val){
	int ans = 2;//tree[2] = INF
	int p = root;
	while(p){
		if(val==tree[p].val){
			if(tree[p].r>0){
				p = tree[p].r;
				while(tree[p].l>0)p = tree[p].l;
				ans = p;
			}
			break;
		}
		if(tree[p].val>val&&tree[p].val<tree[ans].val)ans = p;
		p = val<tree[p].val?tree[p].l:tree[p].r;
	}
	return ans;
}
```
# BST的节点删除
从BST中删除关键码为val的节点
首先，在BST中检索val，得到节点p。
若p的子节点个数小于2，则直接删除p，并令p的子节点代替p的位置，与p的父节点相连。
若p既有左子树，又有右子树，则在BST中求出val的后即节点next，因为next，没有左子树。最后让next节点代替p节点，删除p即可。
```cpp
void remove(int val){
	int &p = root;
	while(p){
		if(val==tree[p].val)break;
		p = tree[p].val>val?tree[p].l:tree[p].r;
	}
	if(p==0)return;
	if(tree[p].l==0){//没有左子树，用右子树代替p的位置 
		p = tree[p].r;		
	}else if(tree[p].r==0){
		p = tree[p].l;//没有右子树，左子树代替p的位置 
	}else{
		int next = tree[p].r;
		while(tree[next].l>0)next = tree[next].l;
		remove(tree[next].val);//next一定没有左子树，直接删除
		tree[next].l = tree[p].l,tree[next].r  = tree[p].r;//next 代替p的位置 
		p = next;
	}
}
```
# Treap
#  左旋(zig)右旋(zag)
#  右旋zig
注意：这里因为实现的原因，没有记录父节点，为方便起见，把作用对象改为旋转前处于父节点位置的节点
假设$x$是$y$的左子节点，$A$和$B$分别是$x$的左右子树，$C$是$y$的右子树。
"右旋"操作是指在保持BST的性质的基础上，**把$x$变为$y$的父节点**。因为$x$的关键码小于$y$的关键码，所以$y$应该作为$x$的右子节点。
当$x$变成$y$的父节点后，$y$的左子树就空了出来，于是$x$原来的右子树$B$就恰好作为$y$的左子树。
代码：
```cpp
void zig(int &p){
    int q = tree[p].l;
    tree[p].l = tree[p].r,tree[q].r = p;
    p = q;
}
void zag(int &p){
    int q = tree[p].r;
    tree[p].r = tree[q].r,tree[q].l = p;
    p = q;
}
```
# 如何平衡
我们发现如果数据是随机的，那么BST将趋于平衡。Treap的思想就是利用随机来创造平衡条件。
Treap在插入新节点的时候，给节点随机生成一个额外的权值。然后就像二叉堆的插入过程一样，自底向上检查，当某个节点不满足大根对的性质的时候，就执行单旋转，使他与父节点的关系对调。
对于删除操作，，我们就先找到要删除的节点，并把它向下旋转成叶节点，最后直接删除。这样就避免了采取类似普通BST的删除方法可能导致的节点信息更新、堆性质的维护等复杂问题。
For short，treap通过单旋转，**在维持关键码满足BST性质的同时，还使每个节点上随机生成的额外权值满足大根对的性质。**检索，查找，删除，求前驱后继及删除节点的时间复杂度都是$O(log N)$

eg:bzoj3224
# 有问题的代码
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
void update(int p){
    tree[p].size = tree[tree[p].l].size+tree[tree[p].r].size+tree[p].cnt;
}
void build(){
    New(-INF),New(INF);
    root = 1;
    tree[1].r = 2;
    update(root);
}
int getRankByVal(int p,int val){
    if(p==0)return 0;
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
        if(tree[p].dat<tree[tree[p].l].dat)zig(p);//TODO
    }else{
        insert(tree[p].r,val);
        if(tree[p].dat<tree[tree[p].r].dat)zag(p);//TODO
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
                while(tree[p].r>0)p = tree[p].r;//TODO
                ans = p;
            }
            break;
        }
        if(tree[p].val<val&&tree[p].val>tree[ans].val)ans = p;//TODO
        p = val<tree[p].val?tree[p].l:tree[p].r;
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
                while(tree[p].l>0)p = tree[p].l;//TODO
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
    if(tree[p].l||tree[p].r){//TODO
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