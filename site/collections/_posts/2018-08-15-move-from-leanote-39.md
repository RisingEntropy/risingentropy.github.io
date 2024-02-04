---
title: unknown title
date: 2018-08-15 15:51:27 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
//
// Created by dhy on 18-8-15.
//
# include <iostream>
# include <algorithm>
using namespace std;
int n,m,p;
struct SegmentNode{
    long long val,add,mul = 1;
}segTree[100000*4+1];
long long a[100000*4];
void buildTree(int k,int l,int r){
    if(l==r){
        segTree[k].val = a[l]%p;
        return;
    }
    int mid = l+r>>1;
    buildTree(k*2,l,mid);
    buildTree(k*2+1,mid+1,r);
    segTree[k].val = (segTree[k*2].val+segTree[k*2+1].val)%p;
}
void pushdown(int k,int l,int r){
    //更新子节点的值，先称后加更方便，子节点的新值=子节点的值*父节点的乘法数+加法的套路
    int mid = l+r>>1;
    segTree[k*2].val = (segTree[k*2].val*segTree[k].mul+segTree[k].add*(mid-l+1))%p;
    segTree[k*2+1].val = (segTree[k*2+1].val*segTree[k].mul+segTree[k].add*(r-mid))%p;

    segTree[k*2].mul = (segTree[k].mul*segTree[k*2].mul)%p;
    segTree[k*2+1].mul = (segTree[k].mul*segTree[k*2+1].mul)%p;
    segTree[k*2].add = (segTree[2*k].add*segTree[k].mul+segTree[k].add)%p;
    segTree[k*2+1].add = (segTree[2*k+1].add*segTree[k].mul+segTree[k].add)%p;
    segTree[k].add = 0;
    segTree[k].mul = 1;
}
long long query(int k,int l,int r,int x,int y){
    if(r<x||l>y)return 0;
    if(l>=x&&r<=y)return segTree[k].val;
    pushdown(k,l,r);
    long long ans = 0;
    int m = l+r>>1;
    ans += query(k*2,l,m,x,y);
    ans += query(k*2+1,m+1,r,x,y);
    return ans%p;
}
void modifyMul(int k,int l,int r,int x,int y,long long v){
    if(y<l||x>r)return;
    if(l>=x&&r<=y){
        segTree[k].mul = (segTree[k].mul*v)%p;
        segTree[k].add = (segTree[k].add*v)%p;
        segTree[k].val = (segTree[k].val*v)%p;
        return;
    }
    pushdown(k,l,r);
    int mid = l+r>>1;
    modifyMul(k*2,l,mid,x,y,v);
    modifyMul(k*2+1,mid+1,r,x,y,v);
    segTree[k].val = (segTree[k*2].val+segTree[k*2+1].val)%p;
}
void modifyAdd(int k,int l,int r,int x,int y,long long v){
    if(r<x|l>y)return;
    if(l>=x&&r<=y){
        segTree[k].val = (segTree[k].val+(r-l+1)*v)%p;
        segTree[k].add = (segTree[k].add+v)%p;
        return;
    }
    int mid = l+r>>1;
    pushdown(k,l,r);
    modifyAdd(k*2,l,mid,x,y,v);
    modifyAdd(k*2+1,mid+1,r,x,y,v);
    segTree[k].val = (segTree[k*2].val+segTree[k*2+1].val)%p;
}
int main(void){
    ios::sync_with_stdio(false);
    cin>>n>>m>>p;
    for(int i = 1;i<=n;i++){
        cin>>a[i];
    }
    buildTree(1,1,n);
    int op,x,y,k;
    for(int i = 1;i<=m;i++){
        cin>>op>>x>>y;
        switch(op){
            case 2:
                cin>>k;
                modifyAdd(1,1,n,x,y,k);
                break;
            case 1:
                cin>>k;
                modifyMul(1,1,n,x,y,k);
                break;
            default:
                cout<<query(1,1,n,x,y)<<endl;
        }
    }
    return 0;
}
```