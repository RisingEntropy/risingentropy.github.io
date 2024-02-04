---
title: 【日后重点复习】搜索专题测试
date: 2019-09-14 13:26:07 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

感觉这是一个乱搞考试。
#  T1Cryptcowgraphy 解密牛语
农民Brown和John的牛们计划协同逃出它们各自的农场。它们设计了一种加密方法用来保护它们的通讯不被他人知道。

如果一头牛有信息要加密，比如"International Olympiad in Informatics"，它会随机地把C，O，W三个字母插到到信息中（其中C在O前面，O在W前面），然后它把C与O之间的文字和 O与W之间的文字的位置换过来。这里是两个例子：

International Olympiad in Informatics -> CnOIWternational Olympiad in Informatics

International Olympiad in Informatics -> International Cin InformaticsOOlympiad W

为了使解密更复杂，牛们会在一条消息里多次采用这个加密方法（把上次加密的结果再进行加密）。一天夜里，John的牛们收到了一条经过多次加密的信息。请你写一个程序判断它是不是这条信息经过加密（或没有加密）而得到的：

Begin the Escape execution at the Break of Dawn

PROGRAM NAME:cryptcow

输入
一行,不超过75个字符的加密过的信息。

输出
一行，两个整数. 如果能解密成上面那条逃跑的信息，第一个整数应当为1，否则为0；如果第一个数为1，则第二个数表示此信息被加密的次数，否则第二个数为0。

样例输入
```
Begin the EscCution at the BreOape execWak of Dawn
```
样例输出
```
1 1
```
标签
USACO Training Section 4.1
# 解答
就是搜索剪枝。有以下剪枝

 1. 如果C与O之间的字符串在"Begin the Escape execution at the Break of Dawn"中没有出现过，说明不可能  
 2. 哈希记忆化
 3. 优化搜索顺序，先找O再找C和W，虽然我也不知道为啥这样可以
 4. C之前的和W之后的必须和原串相同
 
代码：
```cpp
# include <iostream>
# include <cstring>
# include <cstdio>
using namespace std;
const int base = 29;
const int mod = 100007;
bool exist[10][mod+10];
char *str = " Begin the Escape execution at the Break of Dawn";
int slen = strlen(str)-1;
int pw[70],hash[100];
int getHash(int l,int r){
	return ((hash[r]-(1LL*hash[l-1]*pw[r-l+1]%mod))%mod+mod)%mod;
}
bool shown(int h,int len){
	for(int i = len;i<=slen;i++){
		if(getHash(i-len+1,i)==h)return true;
	}
	return false;
}
bool check(char *s){
	for(int i = 1;i<=slen;i++)if(s[i]!=str[i])return false;
	return true;
}
bool flag;
int step;
void dfs(int pos,char *s,int len){
	if(pos>step){
		if(check(s))flag = true;
		return;
	}
	int ret = 0;
	for(int i = 1;i<=len;i++)ret = (1LL*ret*base + s[i])%mod;
	if(exist[pos][ret])return;
	exist[pos][ret] = true;
	ret = 1;
	while(s[ret]!='C'&&s[ret]!='O'&&s[ret]!='W'){
		if(s[ret]!=str[ret])return;
		++ret;
	}
	if(ret!=len+1&&s[ret]!='C')return;
	ret = 0;
	while(s[len-ret]!='C'&&s[len-ret]!='O'&&s[len-ret]!='W'&&ret<len){
		if(s[len-ret]!=str[slen-ret])return;
		++ret;
	}
	if(ret!=len&&s[len-ret]!='W')return;
	
	int pre = 1;
	for(int i = 1;i<=len;i++){
		if(s[i]=='C'||s[i]=='O'||s[i]=='W'){
			if(pre<i){
				ret = 0;
				for(int j = pre;j<i;j++)ret = (1LL*ret*base+s[j])%mod;
				if(!shown(ret,i-pre))return;
			}
			pre = i+1;
		}
	}
	char to[77];
	for(int c = 1;c<=len;c++){
		if(s[c]=='C'){
			for(int o = c+1;o<=len;o++){
				if(s[o]=='O'){
					for(int w = o+1;w<=len;w++){
						if(s[w]=='W'){
							int cnt = 0;
							for(int i = 1;i<c;i++)to[++cnt] = s[i];
							for(int i = o+1;i<w;i++)to[++cnt] = s[i];
							for(int i = c+1;i<o;i++)to[++cnt] = s[i];
							for(int i = w+1;i<=len;i++)to[++cnt] = s[i];
							dfs(pos+1,to,cnt);
							if(flag)return;
						}
					}
				}
			}
		}
	}
}
char ss[100];
int main(){
	gets(ss+1);
	int len = strlen(ss+1);
	pw[0] = 1;
	for(int i = 1;i<=69;i++)pw[i] = pw[i-1]*base%mod;
	for(int i = 1;i<=slen;i++)hash[i] = (hash[i-1]*base+str[i])%mod;
	int cntc = 0,cnto = 0,cntw = 0;
	for(int i = 1;i<=len;i++){
		if(ss[i]=='C')cntc++;
		if(ss[i]=='O')cnto++;
		if(ss[i]=='W')cntw++;
	}
	if(cntc!=cnto||cntc!=cntw||cnto!=cntw){
		puts("0 0");return 0;
	}
	if((len-slen)%3!=0){
		puts("0 0");return 0;
	}
	step = cntc;
	dfs(1,ss,len);
	if(flag){
		printf("1 %d",cntc);
	}else puts("0 0");
	return 0;
}
```
# T2 火力网
在一个n*n的阵地中，有若干炮火不可摧毁的石墙，现在要在这个阵地中的空地上布置一些碉堡。假设碉堡只能向上下左右四个方向开火，由于建筑碉堡的材料挡不住炮火，所以任意一个碉堡都不能落在其它碉堡的火力范围内，请问至多可建造几座碉堡？

输入
第一行一个整数n(n<=10)。

下面n行每行为一个由n个字符构成的字符串，表示阵地的布局，包括空地('.')，和石墙('X')。

输出
一个整数，即最多可建造的碉堡数。

样例输入
```
4
.X..
....
XX..
....
```
样例输出
```
5
```
# 解答
wjs tql，神仙脑子
dp[line][s]表示第$line$行，前面所有行对这一行的影响是$s$,对这个进行记忆化。然后记录一下当前行前面的炮火覆盖的格子，我们特别规定我们一次只处理下一个格子，然后还要记录一个ne，表示当前行加上前面所有的行对下一行的影响，为什么要记录呢？因为当前行可能会有石墙，导致前面行的影响传递不到下一行。
代码有细节：
```cpp
# include <iostream>
# include <cstdio>
# include <cstring>
using namespace std;
const int MAXN = 1024+10;
int dp[11][MAXN];
int n;
char map[11][11];
int dfs(int line,int k,int now,int ne,int last){
	if(line>n){
		return 0;
	}
	if(k==1&&dp[line][last])return dp[line][last];
	if(map[line][k]=='.'&&(last&1<<(k-1)))ne|=1<<(k-1);//如果这一个是石墙，前面行的状态就覆盖不到下一行
	if((now&1<<(k-1))||(last&1<<(k-1))){//如果这一个不能放
		if(k==n)return dp[line+1][ne] = dfs(line+1,1,0,0,ne);
		else return dfs(line,k+1,(now&1<<(k-1))&&(map[line][k]=='.')?now|1<<(k):now,ne,last);
	}else{//如果没有炮火覆盖
		if(map[line][k]=='X'){//不能放，本行前面的炮火就不会蔓延到下一个格子，就不用刷新下一个格子
			if(k==n)dp[line+1][ne] = dfs(line+1,1,0,0,ne);
			else return dfs(line,k+1,now,ne,last);
		}else{//继续大判断
			if(k==n){
				int s1 = 1+dfs(line+1,1,0,0,ne|1<<(k-1)),s2 = dfs(line+1,1,0,0,ne);
				dp[line+1][ne|1<<(k-1)] = s1-1;
				dp[line+1][ne] = s2;
				return max(s1,s2);
			}else{
				return max(dfs(line,k+1,now|1<<k,ne|1<<(k-1),last)+1,dfs(line,k+1,now,ne,last));
			}
		}
	}
}
int main(){
	scanf("%d",&n);
	for(int i = 1;i<=n;i++){
		scanf("%s",map[i]+1);
	}
	printf("%d",dfs(1,1,0,0,0));
	return 0;
}
```
# T3 long
汉诺塔升级了：现在我们有N个圆盘和N个柱子，每个圆盘大小都不一样，大的圆盘不能放在小的圆盘上面，N个柱子从左到右排成一排。每次你可以将一个柱子上的最上面的圆盘移动到右边或者左边的柱子上（如果移动之后是合法的话）。现在告诉你初始时的状态，你希望用最少的步数将第i大的盘子移动到第i根柱子上，问最小步数。

输入
第一行一个正整数T，代表询问的组数。

接下来T组数据，每组数据第一行一个整数N。

接下来一行每行N个正整数，代表每个柱子上圆盘的大小。

输出
输出共T行，代表每次的答案。如果方案不存在，输出“-1”。

样例输入 [复制]
```
4
3
2 1 3
2
7 8
2
10000 1000
3
97 96 95
```
样例输出 [复制]
```
4
0
-1
20
```
提示
对于70%的数据，N的值都是相等的。

对于100%的数据，1≤T≤6×〖10〗^3,1≤N≤7。
# 解答
暴力的一道题，暴力从合法的状态开始bfs，把所有能走到的状态全部标记一下就完了。top[i]表示i根柱子最上面的那个的大小，pos[i]表示第i个圆盘的位置。
然后暴力枚举长度为1-7的可能，暴力做
```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# pragma GCC optimize("O3")
using namespace std;
const int MAXN  = 10000000;
const int N = 10;
int top[N],pos[N],bit[N];
int a[N],b[N];
queue<int> q;
int ans[MAXN],vis[MAXN];
inline char nc(){
    static char buf[100000],*p1=buf,*p2=buf;
    return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
inline int read(){
    char ch=nc();int sum=0;
    while(!(ch>='0'&&ch<='9'))ch=nc();
    while(ch>='0'&&ch<='9')sum=sum*10+ch-48,ch=nc();
    return sum;
}
void bfs(int s){
	int x  = 0,state = s;
	for(int i = 1;i<=7;i++)top[i] = 0;
	while(state){
		pos[++x] = state%10;
		state/=10;
	}
	reverse(pos+1,pos+x+1);
	for(int i = x;i>=1;i--)top[pos[i]] = i;
	for(int i = 1;i<=x;i++){
		if(i==top[pos[i]]){
			int p = pos[i];
			if(p!=1&&(i<top[p-1]||!top[p-1])){
				int nxt = s-bit[x-i];
				if(!vis[nxt])q.push(nxt),ans[nxt] = ans[s]+1,vis[nxt] = true;
			}
			if(p!=x&&(i<top[p+1]||!top[p+1])){
				int nxt = s+bit[x-i];
				if(!vis[nxt]){
					q.push(nxt);
					vis[nxt] = true,ans[nxt] = ans[s]+1;
				}
			}
		}
	}
	
}

bool cmp(int x,int y){
	return a[x]<a[y];
}
int main(){
	int T;
	T = read();
	int s = 0;bit[0] = 1;
	for(int i = 1;i<=7;i++){
		bit[i] = bit[i-1]*10;
		s = s*10+i;q.push(s);vis[s] = true;
	}
	while(!q.empty()){
		s = q.front();q.pop();
		bfs(s);
	}
	while(T--){
		int n = read();
		for(int i = 1;i<=n;i++)a[i] = read(),b[i] = i;
		sort(b+1,b+n+1,cmp);
		s = 0;
		for(int i = 1;i<=n;i++)s = s*10+b[i];
		if(!vis[s])puts("-1");
		else printf("%d\n",ans[s]);
	}
	return 0;
}
```
# T4 来自风平浪静的明天
冬眠了五年，光终于从梦中醒来。

千咲、要，大家都在。

隐约记得“昨天”的海船祭，爱花意外成为贡女，沉入海底。

海面冰封，却有丝丝暖流在冰面之下涌动。

此时，爱花沉睡在祭海女神的墓地。她的胞衣在一点点脱落，化作一簇簇暖流，夹杂着她的 感情，向海面上涌去。

爱花，你在哪里？

五年之后，纺已经成为海洋学研究科的大学生。

在纺的帮助下，光得知了海面下海流的情况。

纺告诉光，暖流一旦产生，就会不断地向四周扩散，直到遇到海中的岩石。

红腹海牛，快告诉光，爱花在哪里。

纺帮你绘制了一张海流情况图，长度为 N，宽度为 M。

海很大，一边有沙滩，一边一望无际，但长度和宽度都不会超过 300。沙滩是金黄色的，所 以用 Y 表示。海是蓝色的，所以用 B 表示。暖流很暖和，所以用 H 表示 海中有大大小小的石头。石头很危险，所以用 X 表示 光相信自己一定能找到爱花（爱花的位置只有一种可能）

输入
第一行包括两个整数 N,M。

接下来 N 行，每行 M 个字符

输出
仅一行，表示爱花的位置（如果你无能为力，请输出 -1 ， 只要你尽力，光不会责怪你）

样例输入 [复制]
```cpp
5 5
YYYHB
YYHHH
YHHXB
BBHBB
BBBBB
```
样例输出 [复制]
```
2 3
```
提示
【数据范围】
对于 30%的数据， n,m<=10
对于 70%的数据， n,m<=100
对于 100%的数据， n,m<=300
【样例解释】
在(2,3)出现第一个 H 后，经过 3s 后，出现样例输入的地图。
标签
# 解答
这是一个屑题，垃圾题面，害我没看懂这玩意在干嘛。草。
就是暴力枚举每个点作为起点，按照bfs的floodfill方式，标记一遍，看一下是否走过了海洋（就是海洋和乱流都入队，沙滩和岩石都不管，最后看队列里是不是有海洋）
屑题代码：
```cpp
# include <iostream>
# include <cstdio>
# include <queue>
# include <cstring>
# define clean(x) memset(x,0,sizeof(x))
using namespace std;
typedef pair<int,int> pii;
const int MAXN = 310;
char map[MAXN][MAXN];
void file(){
	freopen("calm.in","r",stdin);
	freopen("calm.out","w",stdout);
}
int dep[MAXN][MAXN];
bool vis[MAXN][MAXN];
int mv[4][2] = {{1,0},{0,1},{0,-1},{-1,0}};
int n,m;
vector<pii> v[MAXN];
int tot;
bool bfs(int x,int y){
	v[1].push_back(make_pair(x,y));
	int layer = max(m,n);
	int cnt = 0;clean(vis);
	vis[x][y] = 1; 
	for(int i = 1;i<=layer;i++){
		for(int j = 0;j<v[i].size();j++){
			int tx = v[i][j].first,ty = v[i][j].second;
			if(map[tx][ty]=='B')return false;
			for(int k = 0;k<4;k++){
				int nx = tx+mv[k][0],ny = ty+mv[k][1];
				if(nx<1||nx>n||ny<1||ny>m||vis[nx][ny]||map[nx][ny]=='Y'||map[nx][ny]=='X')continue;
				vis[nx][ny] = true;v[i+1].push_back(make_pair(nx,ny));
			}
		}
		cnt+=v[i].size();
		if(tot==cnt)return true;
	}
	return false;
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i = 1;i<=n;i++){
		scanf("%s",map[i]+1);
		for(int j = 1;j<=m;j++)if(map[i][j]=='H')tot++;
	}
	for(int i = 1;i<=n;i++){
		for(int j = 1;j<=m;j++){
			if(map[i][j]=='H'){
				for(int i = 1;i<=max(m,n);i++)v[i].clear();
				if(bfs(i,j))return printf("%d %d",i,j)*0;
			}
		}
	}
	return 0;
}
/* 
*/
```