---
title: 二分答案P1316温习
date: 2018-07-26 10:11:30 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

```cpp
# include <iostream>
# include <algorithm>
using namespace std;
int A,B;
int caps[100000+1];
bool judge(int dis){
    int last = caps[1];
    int now,cnt = 1;
    for(int i = 2;i<=A;i++){
        if(caps[i]-last>dis){
            last = caps[i];
            cnt++;
        }
        if(cnt>B)true;//如果满足当前距离的点过多，说明距离过小，应增大，即区间应该更新到[mid,last]之间
    }
    return cnt>=B;
}
int main() {
    cin>>A>>B;
    for(int i = 1;i<=A;i++){
        cin>>caps[i];
    }
    sort(caps+1,caps+A+1);
    int l,r;
    l = 0;
    r = caps[A];
    while(l<r){
        int mid = (l+r)/2;
        if(judge(mid)==true){//说明距离过小，调整区间(mid,last]
            l = mid+1;
        }else{//区间合适或者过大，调整区间[0,mid]包含mid
            r = mid;
        }
    }
    cout<<l;//l即是找到的答案，因为二分答案就是搜索所有的可能情况，找到最符合的一个。骚！
    return 0;
}
```