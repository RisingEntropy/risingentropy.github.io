---
title: 左偏树
date: 2019-02-23 15:50:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 左偏树
左偏树是可并堆得一种实现方式。

 - 定义一个树的斜深度为从根节点开始一直向右走走到叶子节点的步数
 - 左偏树是一种特殊的堆，满足左儿子的斜深度大于等于右儿子。
 - 左偏树的基本操作：合并
 
# 左偏树的性质
 - 满足左偏的性质：左儿子斜深度大于右孩子斜深度
 - 堆性质：键值满足堆性质
 
# 左偏树的结论
 - 每个节点的左右子树都是一颗左偏树
 - 当前节点的斜深度=右孩子斜深度+1
 - 一颗斜深度为k的左偏树，至少有$2^{k+1}-1$个节点
 - 一棵N个结点的左偏树，斜深度最大为$log(N+1)-1$
 
# 支持的操作
 - 初始化一颗空树
 - 加入一个元素
 - 合并两颗树
 - 查询最大最小节点
 - 删除最大最小节点

# 操作
合并(核心操作)
```cpp
int merge(int k1,int k2){
	if(k1==0||k2==0)return k1+k2;//k1 或 k2至少有一颗是空树
	if(tree[k1].w>tree[k2].w)swap(k1,k2);//满足左边根的边权大于右边
	tree[k1].r = merge(k2,tree[k1].r);//合并，左偏树在右节点合并
	if(tree[tree[k1].l].d<tree[tree[k2]].d)swap(tree[k1].l,tree[k1].r);//维护左偏的性质 
	tree[k1].d = tree[tree[k1].r].d+1;//父节点的斜深度等于右儿子的斜深度+1 
	return k1; 
}
```
# 例题
woj2161 国王游戏
题意：2个操作
1.合并2个集合
2.查询1个点所在集合的最小值，并删除该点，如果这个点已经被删除则输出0
# 解答
左偏树板子题。合并集合：并查集。最大最小值：左偏树.数组vis记录是否被杀死。杀人就是把它的子树合并起来。代码(这题卡常)
```cpp
# include <cstring>
# include <vector>
# include <queue>
# include <algorithm>
# include <cstdio>
using namespace std;
const int MAXN = 1000010;
int fa[MAXN],root[MAXN],tree[MAXN][2],dep[MAXN];
bool vis[MAXN];
int val[MAXN];
int find(int x){return fa[x]==x?x:fa[x] = find(fa[x]);}
int merge(int k1,int k2){
	if(k1==0||k2==0)return k1+k2;//k1 或 k2至少有一颗是空树
	if(val[k1]>val[k2])swap(k1,k2);//满足左边根的边权大于右边
	tree[k1][1] = merge(k2,tree[k1][1]);//合并，左偏树在右节点合并
	if(dep[tree[k1][0]]<dep[tree[k1][1]])swap(tree[k1][0],tree[k1][1]);//维护左偏的性质 
	dep[k1] = dep[tree[k1][1]]+1;//父节点的斜深度等于右儿子的斜深度+1 
	return k1; 
}
void del(int &x){
	x = merge(tree[x][0],tree[x][1]);
}
int main(){
    int n;scanf("%d",&n);
    for(int i = 1;i<=n;i++){
    	scanf("%d",&val[i]);fa[i] = i;root[i] = i;
    }
    int m;scanf("%d",&m);
    char c[5];int x,y;
	while(m--){
    	scanf("%s",c);
    	if(c[0]=='M'){
    		scanf("%d%d",&x,&y);
    		if(vis[x]||vis[y])continue;
    		x = find(x),y = find(y);
    		if(x == y)continue;
    		fa[x] = y;
    		root[y] = merge(root[x],root[y]);
    	}else{
    		scanf("%d",&x);
    		if(vis[x]){
    			printf("0\n");
    		}else{
    			x = find(x);
    			printf("%d\n",val[root[x]]);
    			vis[root[x]] = true;
    			del(root[x]);
    		}
    	}
    }
    return 0;
}
```

