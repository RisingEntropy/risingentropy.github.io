---
title: 【NOIP专题】NOIP2017
date: 2019-09-15 10:36:32 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

#  NOIP2017
评价:质量还不错的一年，难度适中，没有16年的毒瘤，也没有18年的日怪。
#  T1
[题面](https://www.luogu.org/problem/P3951)
#   解答
神仙结论题，其实考试的时候打表也可以找出规律。注意开`long long`
结论是$a\times b-a-b$
```cpp
# include<bits/stdc++.h>
using namespace std;
int main()
{
	long long i,j,k;
	cin>>i>>j;
	k=i*j-i-j;
	cout<<k;
	return 0;
 } 
```
#   T2
算是一道适中的模拟题吧，注意一下细节就行。
我代码写的丑
```cpp
// luogu-judger-enable-o2
# include <cstring>
# include <iostream>
# include <stack>
# include <fstream>
# include <queue>
# include <string>
# include <sstream>
# include <set>
using namespace std;
struct F{
    char var;
    int x,y;
};
struct E{
    int tag;//没啥用，就是标记一个结束而已 
};
int p;

bool O1=false;
const int ERR = 0x9897;
const int YES = 0x7467;
const int NO = 0x545a;
inline int to_int(string s,int b,int e){
    int x = 0,f = 1;;
    int i = b;
    if(s[i]=='-')f = -1,i=-~i;
    for(;i<=e;i=-~i){
        x = (x<<3)+(x<<1)+s[i]-'0';
    }
    return x*f;
}
int check(queue<string> q){
    bool vars[27];//是否在栈里面 
    memset(vars,false,sizeof(vars));
    stack<char>var_stack;//变量栈
    stack<F> f_stack;//用于储存f语句的栈 
    int depth = 0;//如果有不执行的循环，那么嵌套的深度 
    bool deadloop = false;//是否有不执行的循环 
	int act_p = 0;
    int num = 0;//常数复杂度 
    int pow = 0;//指数复杂度 
    while(!q.empty()){
        string top = q.front();
        q.pop();
        string temp;
        if(top[0]=='F'){//F语句 
            F f;
            temp = q.front();
            q.pop();
            if(vars[temp[0]-'a']){
                return ERR;
            }else{
                vars[temp[0]-'a'] = true;
                var_stack.push(temp[0]);               
                f.var = temp[0];
            }
            int x,y;
			temp = q.front();
			q.pop();
			if(temp[0]=='n')x=999;else x = to_int(temp,0,temp.size()-1);
			temp = q.front();
			q.pop();
			if(temp[0]=='n')y = 999;else y = to_int(temp,0,temp.size()-1);//x,y分别看看是不是n，如果是的话就执行 
			if(x>y){
				deadloop = true;
				depth++;
			}else{
				depth++;
				if(deadloop){
					//do nothing
				}else{
					if(x<=100&&y>=999){
						pow++;
					}else{
						num++;
					}
				}
			}
			f.x = x,f.y = y;
			f_stack.push(f);
        }else{
        	act_p = max(act_p,pow);
        	if(f_stack.empty()){
        		return ERR;
        	}
        	depth--;
				if(depth == 0){
					deadloop = false;

					pow=0;
				}
			F t = f_stack.top();
			f_stack.pop();
			vars[t.var-'a'] = false;
			var_stack.pop();
			if(t.x<=100&&t.y>=999&&depth!=0){
				pow--;
			}
        }
    }
    	if(act_p==0){
    		if(O1)return YES;
    		else return NO;
    	}else{
    		if(act_p==p)return YES;
    	}
    	return NO;
}
int main(void){
    int t;
    cin>>t;
    while(t--){
    	p = 0;
    	O1 = false;
        queue<string> q;
        int L;
        cin>>L;
        string temp;
        int cf = 0,ce = 0;
        cin>>temp;
        if(temp[2]=='n'){
            p = to_int(temp,4,temp.size()-2);
        }else{
            O1=true;
        }
        while(L--){
            cin>>temp;
            if(temp[0]=='F'){
            	cf++;
                q.push(temp);
                cin>>temp;//var
                q.push(temp);
                cin>>temp;//x
                q.push(temp);
                cin>>temp;//y
                q.push(temp);
            }else{
                q.push(temp);
                ce++;
            }
        }
        if(ce!=cf){
        	cout<<"ERR"<<endl;
        	continue;
        }
        switch(check(q)){
            case YES:
                cout<<"Yes"<<endl;
                break;
            case NO:
                cout<<"No"<<endl;
                break;
            case ERR:
                cout<<"ERR"<<endl;
                break;
            default:
                cout<<"ERR"<<endl;
                break;
        }
    }
    return 0;
}
```
#  T3
[逛公园](https://www.luogu.org/problem/P3953)
#   解答
记忆化搜索,看到k<=50，就会发现其实是一个与k有关的DP，压到状态里面去，dp[x][k]表示走到k这个点，与最短路长度差为k的路径条数，那么答案就是$\sum dp[1][i]$对于有0环的情况就记录一个是否入栈，如果搜到已经在栈里面的点，且长度还不变，则说明有0环，输出-1好了。
代码如下：
```cpp
// luogu-judger-enable-o2
# include <iostream>
# include <queue>
# include <cstring>
# include <cstdio>
using namespace std;
const int MAXK = 51;
const int MAXN = (int)1e5+10;
int mod;
int n,m,p,k;
struct edge{int t,w,next;};
bool vis[MAXN],mark[MAXN][MAXK];
int dp[MAXN][51];
int read(){
    int x = 0,f = 1;
    static char c = getchar();
    while(c<'0'||c>'9'){ if(c=='-')f = -1;c = getchar(); }
    while(c>='0'&&c<='9'){ x = x*10+(c^'0');c = getchar(); }
    return x*f;
}
struct graph{
    edge edges[MAXN<<1];
    int dis[MAXN],head[MAXN],top;
    void add(int f,int t,int w){
        edges[++top].next = head[f];
        edges[top].t = t;
        edges[top].w = w;
        head[f] = top;
    }
    void init(){
        top = 0;memset(head,0,sizeof(head));
        memset(dis,0x3f,sizeof(dis));
    }
}G,rG;
void spfa(graph &g,int S){
    queue<int> q;
    memset(vis,false,sizeof(vis));
    vis[S] = true;q.push(S);g.dis[S] = 0;
    while(!q.empty()){
        int top =  q.front();q.pop();
        vis[top] = false;
        for(int i = g.head[top];i;i = g.edges[i].next){
            int t = g.edges[i].t;
            if(g.dis[t]>g.dis[top]+g.edges[i].w){
                g.dis[t] = g.dis[top]+g.edges[i].w;
                if(!vis[t]){
                    vis[t] = true;
                    q.push(t);
                }
            }
        }
    }
}
bool flag = false;
int dfs(int x,int know){
    if(mark[x][know]){
        flag = true;//flag是用来判0环的
        return 0;
    }
    if(dp[x][know]!=-1)return dp[x][know];
    if(flag)return 0;
    mark[x][know] = true;
    int sum = 0;
    for(int i = G.head[x];i;i = G.edges[i].next){
        int t = G.edges[i].t;
        int delta = know-(rG.dis[t]-rG.dis[x]+G.edges[i].w);
        if(delta<0||delta>k)continue;
        sum = (sum + dfs(t,delta))%mod;
        if(flag)return 0;
    }
    if(x==n&&know==0)sum = 1;
    mark[x][know] = false;
    return dp[x][know] = sum;
}
void init(){
    G.init();rG.init();
    flag = false;
    memset(dp,-1,sizeof(dp));
}
int main(){
    int T = read();
    while(T--){
        init();
        n = read(),m = read(),k = read(),mod = read();
        int f,t,w;
        for(int i = 1;i<=m;i++){
            f = read(),t = read(),w = read();
            G.add(f,t,w);rG.add(t,f,w);
        }
        spfa(rG,n);
        int ans = 0;
        for(int i = 0;i<=k;i++){
            memset(mark,false,sizeof(mark));
            ans = (ans+dfs(1,i))%mod;
        }
        printf("%d\n",flag?-1:ans);
    }
    return 0;
} 
```
#  T4
[题面](https://www.luogu.org/problem/P3958)
#   解答
并查集的签到题。
```cpp
# include <iostream>
# include <time.h>
# include <algorithm>
# include <stdlib.h>
using namespace std;
const int MAXN = 1010;
int fa[MAXN];
int find(int x){
    while(fa[x]!=x){x = fa[x];}
    return fa[x];
}
bool judge(int x,int y){ return find(x)==find(y);}
void unionn(int x,int y){fa[find(y)]=find(x);}
struct hole{
    long long x,y,z;
    int id;
    bool operator<(const hole &h2)const{
        return z<h2.z;
    }
}holes[MAXN];
long long n,r,h;
bool connect(hole h1,hole h2){
    return 4*r*r>=(h1.x-h2.x)*(h1.x-h2.x)+(h1.y-h2.y)*(h1.y-h2.y)+(h1.z-h2.z)*(h1.z-h2.z);//是否联通
}
hole top[MAXN],bottom[MAXN];
int top_cnt,bottom_cnt;
int main(void){
    ios::sync_with_stdio(false);
    int T;
    cin>>T;

    while(T--){
        cin>>n>>h>>r;
        top_cnt = 0;
        bottom_cnt = 0;
        bool connected = false;
        for(int i = 1;i<=n;i++)fa[i] = i;
        for(int i = 1;i<=n;i++){
            cin>>holes[i].x>>holes[i].y>>holes[i].z;
            holes[i].id = i;
            if(holes[i].z+r>=h&&holes[i].z-r<h){
                if(holes[i].z-r<=0&&holes[i].z+r>0){//既联通上面又联通下面，整个蛋糕都空了
                    connected = true;
                }else{
                    top[++top_cnt] = holes[i];
                }
            }else if(holes[i].z-r<=0&&holes[i].z+r>=0){
                bottom[++bottom_cnt] = holes[i];
            }
        }
        if(connected)goto tag;
        for(int i = 2;i<=n;i++){
            for(int j = 1;j<i;j++){
                if(connect(holes[i],holes[j])){
                    unionn(holes[i].id,holes[j].id);
                }
            }
        }
       for(int i = 1;i<=top_cnt;i++){
           for(int j = 1;j<=bottom_cnt;j++){
               if(judge(top[i].id,bottom[j].id)){
                   connected = true;
                   goto tag;
               }
           }
       }
        tag:
        if(connected){
            cout<<"Yes"<<endl;
        }else{
            cout<<"No"<<endl;
        }
    }
    return 0;
}
```
#  T5
[题面](https://www.luogu.org/problem/P3959)
#   解答
仔细观察发下这就是一个旅行商问题的改版。状压DP。$dp[x][s]$表示走到x这个点，走过的点的状态是s的时候的最小花费，然后搜索的时候还要记录一个深度，回溯的时候要恢复，如果搜到更短的点，就要去更新答案。
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# define clear(x) memset(x,0,sizeof(x))
# define set(x,v) memset(x,v,sizeof(x))
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAXN = 13;
int map[MAXN][MAXN];
int dp[1<<13];
int dep[MAXN];
int n,m;
void dfs(int S){
	for(int i = 1;i<=n;i++){
		if(S&1<<i-1){
			for(int j = 1;j<=n;j++){
				if((S&1<<j-1)==0&&map[i][j]!=INF){
					if(dp[S|1<<j-1]>dp[S]+dep[i]*map[i][j]){
						int ori_dep = dep[j];
						dp[S|1<<j-1]=dp[S]+dep[i]*map[i][j];
						dep[j] = dep[i]+1;
						dfs(S|1<<j-1);
						dep[j] = ori_dep;
					}
				}
			}
		}
	}
}
int main(){
	scanf("%d%d",&n,&m);
	int f,t,w;
	memset(map,0x3f,sizeof(map));
	for(int i = 1;i<=m;i++){
		scanf("%d%d%d",&f,&t,&w);
		map[f][t] = map[t][f] = min(map[t][f],w);
	}
	int ans = INF;
	for(int i = 1;i<=n;i++){
		set(dp,0x3f);clear(dep);
		dp[1<<i-1] = 0;
		dep[i] = 1;dfs(1<<i-1);
		ans = min(dp[(1<<n)-1],ans);
	}
	printf("%d\n",ans);
	return 0;
}
```
#  T6
[题面](https://www.luogu.org/problem/P3960)
#   解答
很不错额一道线段树的好题，前两天才学了线段树分治以及动态开点的线段树，刚好来写一下这道题。听大佬们说可以`splay`水过，但是我太弱了，太久没有写`spay`这种一写一下午的东西了。我们建立$n+1$个线段树，分别维护$n$行及最后一列。每次操作就从相应的一行中找到第y个数，如果第y个数的下标大雨了了n，说明已经出去了超过那么多人了，只有从那个节点所代表的的vector里面找出$pos-m$个数，对于最后一列，同样使用一个vector维护，查询的时候如果线段树里面的人数已经少于要查询的人数了，就从vector里面取那么多个人粗来就好啦。
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
# include <vector>
using namespace std;
const int MAXN = (int)3e5+10;
int tree[MAXN*20][2],sum[MAXN*20],cnt,root[MAXN];
int pos;
int n,m,q,mx;
vector<long long> v[MAXN*20];
int query(int k,int l,int r,int w){
	if(l==r){return l;}
	int mid = l+r>>1;int tmp = mid-l+1-sum[tree[k][0]];
	if(tmp>=w)return query(tree[k][0],l,mid,w);
	else return query(tree[k][1],mid+1,r,w-tmp);
}
void modify(int &k,int l,int r,int pos){
	if(!k)k = ++cnt;
	sum[k]++;
	if(l==r)return;
	int mid = l+r>>1;
	if(pos<=mid)modify(tree[k][0],l,mid,pos);
	else modify(tree[k][1],mid+1,r,pos);
}
long long work1(int x,long long y){
	pos = query(root[n+1],1,mx,x);
	modify(root[n+1],1,mx,pos);
	long long ans = pos<=n?(long long)pos*m:v[n+1][pos-1-n];
	v[n+1].push_back(y?y:ans);
	return ans;
}
long long work2(int x,int y){
	pos = query(root[x],1,mx,y);
	modify(root[x],1,mx,pos);
	long long ans = pos<m?(long long)(x-1)*m+pos:v[x][pos-m];
	v[x].push_back(	work1(x,ans));
	return ans;
}
int main(){
	scanf("%d%d%d",&n,&m,&q);
	mx = max(m,n)+q;
	int x,y;
	while(q--){
		scanf("%d%d",&x,&y);
		if(y==m)printf("%lld\n",work1(x,0));
		else printf("%lld\n",work2(x,y));
	}
	return 0;
}
```