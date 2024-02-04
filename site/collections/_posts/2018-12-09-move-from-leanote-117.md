---
title: Treap
date: 2018-12-09 11:29:39 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

为了省事，我已不择手段
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