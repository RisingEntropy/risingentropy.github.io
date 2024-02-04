---
title: woj3205 送礼物
date: 2019-02-23 10:21:51 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 题面
作为惩罚，GY被遣送去帮助某神牛给女生送礼物(GY：貌似是个好差事)但是在GY看到礼物之后，他就不这么认为了。某神牛有N个礼物，且异常沉重，但是GY的力气也异常的大(-_-b)，他一次可以搬动重量和在w(w<=2^31-1)以下的任意多个物品。GY希望一次搬掉尽量重的一些物品，请你告诉他在他的力气范围内一次性能搬动的最大重量是多少。
#  输入
第一行两个整数，分别代表W和N。
以后N行，每行一个正整数表示G[i],G[i]<= 2^31-1。
#  输出
仅一个整数，表示GY在他的力气范围内一次性能搬动的最大重量。
#  样例输入 
```
20 5
7
5
4
18
1
```
#  样例输出 
```
19
```
#  提示
对于20%的数据 N<=26
对于40%的数据 W<=2^26
对于100%的数据 N<=45 W<=2^31-1
# 解答
把整个区间排序，分成2部分，对于前面一部分，把可以凑出来的体积全部丢到一个数组里面。然后后面一部分枚举每个 选或不选，看看与前面的最大可以凑出来的体积是多少，能不能更新答案就行了。
代码:
```cpp
# include<bits/stdc++.h>

using namespace std;
struct IO
{
    streambuf *ib,*ob;
    int buf[50];
    inline void init()
    {
        ios::sync_with_stdio(false);
        cin.tie(NULL);cout.tie(NULL);
        ib=cin.rdbuf();ob=cout.rdbuf();
    }
    inline int read()
    {
        char ch=ib->sbumpc();int i=0,f=1;
        while(!isdigit(ch)){if(ch=='-')f=-1;ch=ib->sbumpc();}
        while(isdigit(ch)){i=(i<<1)+(i<<3)+ch-'0';ch=ib->sbumpc();}
        return i*f;
    }
    inline void W(int x)
    {
        if(!x){ob->sputc('0');return;}
        if(x<0){ob->sputc('-');x=-x;}
        while(x){buf[++buf[0]]=x%10,x/=10;}
        while(buf[0])ob->sputc(buf[buf[0]--]+'0');
    }
}io;
const int MAXN = 45;
int G[MAXN+10];
long long n;int m;
vector<long long> wghs;
long long ans = -999;
bool fid;
void dfs1(int pos,long long tot){
    if(tot>n)return;
    if(pos>m/2){
        wghs.push_back(tot);
        return;
    }
    dfs1(pos+1,tot);dfs1(pos+1,tot+G[pos]);
}
void dfs2(int pos,long long tot){
    if(tot+wghs[0]>n)return;
    if(pos==m+1){
        if(tot>n)return;
        int pos = lower_bound(wghs.begin(),wghs.end(),n-tot)-wghs.begin();
        if(pos==0&&wghs[0]>n-tot)return;
        if(pos==0&&wghs[0]==n-tot){
            ans = n;
            fid = true;
            return;
        }
        if(tot+wghs[pos-1]<=n)
            ans = max(ans,tot+wghs[pos-1]);
        return ;
    }
    if(!fid)
        dfs2(pos+1,tot+G[pos]),dfs2(pos+1,tot);
}
int main(){
    io.init();
    n = io.read(),m = io.read();
    for(int i = 1;i<=m;i++)G[i] = io.read();
    sort(G+1,G+m+1);
    dfs1(1,0);
    sort(wghs.begin(),wghs.end());
    dfs2(m/2+1,0);
    printf("%lld",ans);
    return 0;
}
```