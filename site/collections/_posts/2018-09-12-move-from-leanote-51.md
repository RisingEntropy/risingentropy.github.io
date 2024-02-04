---
title: Trie 数组版
date: 2018-09-12 16:42:18 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
const N = 50000;
const sigmaSize = 26;//字符集大小 
int trie[N][sigmaSize];
int total = 1;
bool endOfWords[N];
void insert(char * str){
	int n = strlen(str);
	int p = 1;
	int ch ;
	for(int i = 0;i<n;i++){
		ch = str[i]-'a';
		if(trie[p][ch]==0){
			trie[p][ch] = ++total;
		}
		p = trie[p][ch];
	}
	endOfWords[p] = true;
}
bool search(char * str){
	int n = strlen(str);
	int p = 1;
	int ch = 0;
	for(int i = 0;i<n;i++){
		ch = str[i]-'a';
		if(trie[p][ch]==0)return false;
		p = trie[p][ch];
	}
	return false;
}
```