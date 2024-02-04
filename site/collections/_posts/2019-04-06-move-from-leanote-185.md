---
title: fhq treap
date: 2019-04-06 15:38:17 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 非旋treap
fhq是天才！
先放板子
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