---
title: AC自动机板子洛谷P3808
date: 2018-09-14 23:43:57 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
//
// Created by dhy on 18-9-14.
//
# include <iostream>
# include <string>
# include <queue>
using namespace std;
struct trie{
    int fail;
    int son[27];
    int cnt;
}ACtree[1000000];
int top = 0;
void build_tree(string str){
    int n = str.size()-1;
    int ch = 0;
    for(int i = 0;i<=n;i++){
        if(ACtree[ch].son[str[i]-'a']==0){
            ACtree[ch].son[str[i]-'a'] = ++top;
        }
        ch = ACtree[ch].son[str[i]-'a'];
    }
    ACtree[ch].cnt+=1;
}
void build_fail(){
    queue<int> q;
    for(int i = 0;i<26;i++){
        if(ACtree[0].son[i]!=0) {
            ACtree[ACtree[0].son[i]].fail = 0;
            q.push(ACtree[0].son[i]);
        }
    }
    while(!q.empty()){
        int u = q.front();
        q.pop();
        for(int i = 0;i<26;i++){
            if(ACtree[u].son[i]!=0){
                ACtree[ACtree[u].son[i]].fail = ACtree[ACtree[u].fail].son[i];//
                q.push(ACtree[u].son[i]);
            }else{
                ACtree[u].son[i] = ACtree[ACtree[u].fail].son[i];;
            }
        }
    }
}
int query(string str){
    int n = str.size()-1;
    int ans = 0;
    int ch = 0;
    for(int i = 0;i<=n;i++){
        ch = ACtree[ch].son[str[i]-'a'];
        for(int j = ch;ACtree[j].cnt!=-1;j = ACtree[j].fail){
            ans+=ACtree[j].cnt;
            ACtree[j].cnt = -1;
        }
    }
    return ans;
}
int main(void){
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    string s;
    for(int i = 1;i<=n;i++){
        cin>>s;
        build_tree(s);
    }
    build_fail();
    cin>>s;
    cout<<query(s)<<endl;
    return 0;
}
```