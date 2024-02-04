---
title: KMP真宗好看的板子
date: 2018-09-10 15:24:42 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# KMP板子
```cpp
void next(){
    j=0;
    for (int i=2;i<=lb;i++)
       {     
       while(j&&b[i]!=b[j+1])
       //此处判断j是否为0的原因在于，如果回跳到第一个字符就不 用再回跳了
       j=kmp[j];    
        //通过自己匹配自己来得出每一个点的kmp值 
       if(b[j+1]==b[i])j++;    
       kmp[i]=j;
        //i+1失配后应该如何跳 
       }
}
void kmp(){
    int j;
    j=0;//j可以看做表示当前已经匹配完的模式串的最后一位的位置 
    //如果楼上看不懂，你也可以理解为j表示模式串匹配到第几位了 
    for(int i=1;i<=la;i++)
       {
          while(j&&b[j+1]!=a[i])j=kmp[j];
          //如果失配 ，那么就不断向回跳，直到可以继续匹配 
          if (b[j+1]==a[i]) j++;
          //如果匹配成功，那么对应的模式串位置++ 
          if (j==lb) 
          {
          cout<<i-lb+1<<endl;
          j=kmp[j];
          //继续匹配 
          }
       }
}
```