---
title: temp
date: 2018-11-09 12:16:08 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <cstdio>
# include <algorithm>
# include <cstring>
# include <ctime>
# include <cmath>
# include <cstdlib>
using namespace std;
template<typename T>
void read(T &a){
	T x = 0,f = 1;static char c = getchar();
	while(c<'0'||c>'9'){if(c=='-')f = -1;c = getchar();}
	while(c>='0'&&c<='9'){x = (x<<1)+(x<<3)+c-'0';c = getchar();}
	a =  x*f;
}
const int MAXN = 5e3+10;
struct enemy{
	long long w;
	int x,y,z;
}enemies[MAXN];
int n;
double cal(double x,double y,double z){
	double ans = 0;
	for(int i = 1;i<=n;i++){
		double dis = sqrt((x-enemies[i].x)*(x-enemies[i].x)+(y-enemies[i].y)*(y-enemies[i].y)+(z-enemies[i].z)*(z-enemies[i].z));
		ans+=enemies[i].w*dis;
	}
	return ans;
}
const double T = 1926;
const double delta = 0.998;
double best_x,best_y,best_z,best_ans;
void simulate_annealing(){
	double curr_T = T;
	while(curr_T>0.001){
		double curr_x = best_x + (rand()*2-RAND_MAX)*curr_T;
		double curr_y = best_y + (rand()*2-RAND_MAX)*curr_T;
		double curr_z = best_z + (rand()*2-RAND_MAX)*curr_T;
		double curr_ans = cal(curr_x,curr_y,curr_z);
		double DE = curr_ans - best_ans;
		if(DE<0){
			best_x = curr_x;
			best_y = curr_y;
			best_z = curr_z;
			best_ans = curr_ans;
		}else if(exp(-DE/curr_T)*RAND_MAX>rand()){
			best_x = curr_x;
			best_y = curr_y;
			best_z = curr_z;
			best_ans = curr_ans;
		}
		curr_T*=delta;
	}
}
void SA(){
	long long s = clock();
//	while(double(clock()-s)/(double)CLOCKS_PER_SEC<0.8){
		simulate_annealing();
		simulate_annealing();
		simulate_annealing();
//	}
}
int main(){
	read(n);
	for(int i = 1;i<=n;i++){
		read(enemies[i].x);
		read(enemies[i].y);
		read(enemies[i].z);
		read(enemies[i].w);
	}
	SA();
	printf("%.2lf\n%.2lf\n%.2lf\n%.2lf\n",best_x,best_y,best_z,best_ans);	
	return 0;
}
```