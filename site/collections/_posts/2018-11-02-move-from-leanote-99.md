---
title: 省事板子
date: 2018-11-02 15:18:20 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
const int MAXN = 101;
struct edge{
    int t,w,next;
}edges[MAXN<<1];
int head[MAXN];
int top;
void add(int f,int t,int w) {
    edges[++top].next = head[f];
    edges[top].t = t;
    edges[top].w = w;
    head[f] = top;
}
```
SPFA
```cpp
void spfa(){
	memset(dis,-1,sizeof(dis));
	memset(vis,false,sizeof(vis));
	queue<int> q;
	int s = 0;
	vis[s] = true;
	dis[s] = 0;
	q.push(s);
	while(!q.empty()){
		int top = q.front();
		q.pop();
		vis[top] = false;
		for(int i = head[top];i!=0;i = edges[i].next){
			int t = edges[i].t;
			if(dis[t]<dis[top]+edges[i].w){
				dis[t] = dis[top]+edges[i].w;
				if(!vis[t]){
					vis[t] = true;
					q.push(t);
				}
			}
		}
	}
}
```
dijkstra自己多写dij，免得写错
```cpp
struct node{
	int f,w;
	bool operator<(const node &n2)const{
		return w>n2.w;
	}
};
void dijkstra(){
	priority_queue<node> q;
	memset(dis,-0x3f,sizeof(dis));
	memset(vis,false,sizeof(vis));
	node temp;
	temp.f = 0;
	dis[0] = 0;
	temp.w = 1;
	q.push(temp);
	while(!q.empty()){
		node top = q.top();
		q.pop();
		if(vis[top.f])continue;
		vis[top.f] = true;
		for(int i = head[top.f];i!=0;i = edges[i].next){
			int t = edges[i].t;
			if(dis[t]<dis[top.f]+edges[i].w){
				dis[t]=dis[top.f]+edges[i].w;
				temp.f = t;
				temp.w = dis[top.f]+edges[i].w;
				q.push(temp);
			}
		}
	}
}
```
```
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = (x<<1)+(x<<3)+(c^'0');c = getchar(); }
    return x*f;
}
```
dzyo读优
```
inline char nc() {
	static char ibuf[RLEN],*ib,*ob;
	(ib==ob) && (ob=(ib=ibuf)+fread(ibuf,1,RLEN,stdin));
	return (ib==ob) ? -1 : *ib++;
}
inline int rd() {
	char ch=nc(); int i=0,f=1;
	while(!isdigit(ch)) {if(ch=='-')f=-1; ch=nc();}
	while(isdigit(ch)) {i=(i<<1)+(i<<3)+ch-'0'; ch=nc();}
	return i*f;
}
```
```

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
```