---
title: 二分陷阱
date: 2018-08-20 16:46:17 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 范围缩小时，对mid值的改变
前提while(l `<` r)
1.缩小范围时，r = mid,l = mid+1 ,则，mid = (l+r)>>1;
2.缩小范围时，l = mid,r = mid-1,则，mid = (l+r+1)>>1;
<font color="red">注意,有负数解的时候，只能用>>1而不能/2因为除法向0取整，会导致漏解</font>

# 二分判无解
因为mid = (l+r)>>1不会取到r这个值，mid(l+r+1)>>1不会取到l这个值所以可以利用这一性质判断无解，把二分区间[1,n]扩大到[1,n+1]和[0,n]，把a数组的一个越界下表包含进来。如果二分终于扩大后的这个越界下标上，则说明a不存在所求的数。
# 实数域上二分
超简单，直接判断while(l+精度`<`r)就行
或者 for(int i = 0;i<=100;i++){
    //do sth
    //这种方法精度比楼上高Orz
}