---
title: Trie Tree 
date: 2018-08-11 09:37:07 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
struct node{
    int son[27];
    int exist = false;
    bool visited = false;
}nodes[900000];
int top = 0;
void insert(string str){
    int num,root = 1;
    for(int i = 0;str[i];i++){
        num = str[i] - 'a';
        if(nodes[root].son[num]==0)//no son
            nodes[root].son[num] = ++top;
        root = nodes[root].son[num];
    }
    nodes[root].exist = true;
}
int search(string str){
    int num = 0,root = 1;
    for(int i = 0;str[i];i++){
        num = str[i]-'a';
        if(nodes[root].son[num]==0)return WRONG;
        root = nodes[root].son[num];
    }
    if(!nodes[root].exist)return WRONG;
    else if(nodes[root].visited)return REPEAT;
    nodes[root].visited = true;
    return OK;

}
```