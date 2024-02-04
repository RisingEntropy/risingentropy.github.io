---
title: KMP Loj 剪花布条
date: 2018-09-09 16:16:16 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
# include <queue>
# include <algorithm>
# include <string>
using namespace std;
int next[1010];
string A,B;
int m,n;
void nex(){
	int j = 0;
	next[1] = 0;
	for(int i = 1;i<m;i++){
		while(j>0&&B[j+1]!=B[i+1])j = next[j];
		if(B[j+1]==B[i+1])j++;
		next[i+1]=j;
	}
}
int kmp(){
	int ans = 0,j = 0;
	for(int i = 0;i<n;i++){
		while(j>0&&B[j+1]!=A[i+1])j = next[j];
		if(B[j+1]==A[i+1])j++;
		if(j==m){
			ans++;
			j = 0;
		}
	}
	return ans;
}
int main(void){
	ios::sync_with_stdio(false);
	cin>>A;
	while(A!="# "){
		cin>>B;
		m = B.size();
		n = A.size();
		A.insert(0,1,1);
		B.insert(0,1,1);
		nex();
		cout<<kmp()<<endl;
		cin>>A;
	}
	return 0;
}
```