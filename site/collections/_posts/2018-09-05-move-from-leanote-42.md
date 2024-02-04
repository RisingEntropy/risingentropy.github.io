---
title: 双向bfs
date: 2018-09-05 17:09:35 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

其实很简单，就是两边一起搜。板子如下luogu UVA439
```cpp
# include <iostream>
# include <algorithm>
# include <queue>
# include <cstring>
using namespace std;
queue<pair<int,int>> qs[2];
int dx ={ 1,2,2,1,-1,-2,-2,-1};
int dy = {2,1,-1,-2,-2,-1,1,2};
bool ma[2][9][9];
int ans = 0;
int distance[2][9][9];
bool expand(int k){
	int x,y,tx,ty;
	x = qs[k].top().first;
	y = qs[k].top().second;
	int d = distance[k][x][y];
	for(int i = 0;i<8;i++){
		tx = x+dx[i];
		ty = y+dy[i];
		if(tx>0&&tx<=9&&ty>0&&ty<=9&&!ma[k][tx][ty]){
			ma[k][tx][ty] = true;
			qs[k].push(make_pair(tx,ty));
			dis[k][tx][ty] = d+1;
			if(ma[1-k][tx][ty]){
				ans = distance[k][tx][ty]+distance[1-k][tx][ty];
				return 1;
			}
		}
	}
	return 0;
}
int main(void){
	int x,gx,gy,y;
	ios::sync_with_stdio(false);
	cin>>x>>y>>gx>>gy;
	qs[0].push(make_pair(x,y));
	qs[1].push(make_pair(gx,gy));
	while(qs[0].size()>0||qs[1].size>0){
	    pair<int,int> p;
	    if(qs[0].size()>qs[1].size()){
	        if(expand(1)){return;}
	    }else{
	    if(expand(0))return;
	    }
	}
	return 0;
}
```