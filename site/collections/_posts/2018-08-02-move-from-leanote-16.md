---
title: STL
date: 2018-08-02 12:06:36 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# map/multimap    set/multiset
multi 表示可以放重复元素

#  set
头文件:<set>
操作：
加入insert(a)
删除erase(a)
查找find(a)//worst:O(n) avg:O（log n)
最小元素*s.begin() 最大*s.end()
元素个数s.size
清空clear
返回大于某元素的第一个元素的迭代器:upper_bound
小于:lower_bound

遍历：
```cpp
for(set<typename>::iterator i = s.begin();i!=s.end();i++){
    do something
}
```

#  map
散列表
声名
```cpp
map<key,value>
```
查找map.find();如果没有找到，就应该是map.find()==map.end;找到就返回pair对象

#  alogorithm
```cpp
lower_bound[b,e),k; 在b-e之间小于k的第一个元素(不属于)
```