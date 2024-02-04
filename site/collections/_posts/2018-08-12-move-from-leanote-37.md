---
title: 线段树
date: 2018-08-12 15:28:53 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 构造普通线段树
```cpp
//用数组来做
int mins[];
void build(int k,int l,int r){//k代表编号
    if（l==r){
        nodes[k].val = a[l];
        return;
    }
    int mid = (l+r)/2;
    build(k*2,l,mid);
    build(k*2+1,mid+1,r);
    mins[k] =  min(mins[2*k].val,mins[2*k+1].val);//当前节点的值，根据实际情况改
}
```
# 区间查询
```cpp
int query(int k,int l,int r,int x,int y){//l是标号,xy是询问区间，lr是当前区间
    if(x>r||y<l)return inf;//查询区间不在该节点的范围内
    if(x<=l&&r<=y)return//只有真包含才会执行 nodes[k].val;
    int mind = (l+r)/2;
    return min(query(k*2,l,mid,x,y),query(k*2+1,mid+1,r,x,y);
}

```
# 单点修改
```cpp
void change(int k,int l,int r,int x,int v){
    if(x<l||x>r)return ;//不在区间内，不管
    if(l==r&&x==l){//不要忘了l==r
        mi[k] = v;
        return;
    }
    int mid = (l+r)/2;
    change(k*2,l,mid,x,v);
    change(k*2+1,mid+1,r,x,v);
    mi[k] = min(mi[k*2],mi[k*2+1]);//回来的路上把值更新了
}
```
# 区间修改，单点查询
```cpp
addsum[];
int query(int k,int l,int r,int pos){
    if(l==r)return addsum[k];
    int mid = (l+r)>>1;
    if(pos<=mid)return query(2*k,l,mid,pos)+addsum[k];
    else return query(k*2+1,mid+1,r,pos)+addsum[k];
}
void modify(int k,int l,int r int x int y,int v){//区间[x,y]内所有数加上v
        if(l>y||r<x)return;
        if(l>=x&&r<=y){//完全包含
            addsum[k]+=v;//标记上
            return;
        }
        int mid = l+r>>1;
        modify(k*2,l,mid,x,y,v);
        modify(k*2+1,mid+1,r,x,y,v);
}
```
# 标记下传
```cpp
void Add(int k,int l,int r,intv){
    add[k] +=v;
    sum[k]+=(r-l+1)*v;
    retrun;
}
void pushdown(int k,int l,int r,int mid){//标记下传
    if(add[k]==0)return;//如果当前节点没有标记，就不管
    Add(k*2,l,mid,add[k]);
    Add(k*2+1,mid+1,r,add[k]);
    add[k] = 0;//清空标记
}
void modify(int k,int l,int r,int x,int y,int v){
    if(l>=x&&r<=y)return Add(k,l,r,v);//包含
    int mid = l + r>>1;
    pushdown(k,l,r,mid);//每一个节点都向下穿标记
    if(x<=mid)modify(k*2,l,mid,x,y,v);
    if(mid<y)modify(k*2+1,mid+1,r,x,y,v);
    sum[k] = sum[k*2]+sum[k*2+1];//下传后更新当前正确的sum值
}
int query(int k,int l,int r,int x,int y){//查询[l,r]的和
    if(l>=x&&r<=y)return sum[k];
    int mid = l+r>>1;
    int ans = 0;
    pushdown(k,l,r,mid);
    if(x<=mid)res+=query(k*2,l,mid,x,y);
    if(mid<y)res+=query(k*2+1,mid+1,r,x,y);
    return res;
}

```
# 标记永久化
```cpp
void modify(int k,int l,int r,int x,int y,int v){
    if(l>=x&&r<=y){
        add[k]+=v;
        return ;
    }
    sum[k]+=(min(r,y)-max(l,x)+1)*v;//计算子节点对当前节点的影响
    int mid = l+r>>1;
    if(x<=mid)modify(k*2,l,mid,x,y,v);
    if(mid<y)midfy(k*2+1,mid+1,r,x,y,v);
    sum[k]=sum[k*2]+sum[k*2+1]//千万不要忘了
}

int query(int k,int l,int r,int x,int y){
    if(l>=x&&r<=y)return sum[k]+(r-l+1)*add[k];
    int mid = l+r>>1;
    int res = (min(r,y)-max(l,x)+1)*add[k];
    if(x<=mid)res+=query(k*2,l,mid,x,y);
    if(mid<y)res+=query(k*2+1,mid+1,r,x,y);
    return res;
}
```
# 小优化

 1. a/2 ->a>>1
 2. a*2  ->a<<1
 3. a*2+1 ->a<<1|1;