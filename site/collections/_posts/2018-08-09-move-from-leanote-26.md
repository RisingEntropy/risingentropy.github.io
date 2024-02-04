---
title: P2580 字典树
date: 2018-08-09 22:12:29 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
//
// Created by dhy on 18-8-8.
//
# include <iostream>
# include <cstring>
using namespace std;
const int OK = 1;
const int REPEAT = 2;
const int WRONG = 3;
struct node{
    int son[27];
    int exist = false;
    bool visited = false;
}nodes[1000000];
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
int main(void){
    int n,m;
    ios::sync_with_stdio(false);
    cin>>n;
    string str;
    memset(nodes,0,sizeof(nodes));
    for(int i = 1;i<=n;i++){
        cin>>str;
        insert(str);
    }
    cin>>m;
    for(int i = 1;i<=m;i++){
        cin>> str;
        int state = search(str);
        if(state==OK)cout<<"OK"<<endl;
        if(state==WRONG)cout<<"WRONG"<<endl;
        if(state==REPEAT)cout<<"REPEAT"<<endl;
    }
    return 0;
}

```