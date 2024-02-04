---
title: 数学复习总结
date: 2019-11-05 18:54:35 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

# 数学复习总结
人生中最后一篇OI总结
# 数论分块
- [] [余数求和](http://192.168.110.251/problempage.php?problem_id=3138# ) 数论分块的板子，拆式子：$ans=\sum k-\lfloor \frac{k}{i}\rfloor\\=n*k -\sum\lfloor\frac{k}{i}\rfloor$然后我们发现$\lfloor \frac{k}{i}\rfloor$这个东西很多都是一样的，也就是说如果一个点l是一样的，那么最后一个一样的就是$\lfloor\frac{k}{l}\rfloor$，于是直接从1开始枚举每个l，计算区间的值,计算方法如下:当前块的 $t \times$ 当前块元素个数 $\times$ 当前块 $i$ 的平均值 = $t \times (r-l+1) \times (l+r) \div 2$
# 欧拉函数
计算公式：$\varphi(N) = N*\prod_{p|N}(1-\frac{1}{p})$
线性筛计算代码：
```cpp
void getprime(int n){
	phi[1] = 1;
	for(int i = 2;i<=n;i++){
		if(!vis[i]){phi[i] = i-1;prime[++cnt] = i;}
		for(int j = 1;j<=cnt&&i*prime[j]<=n;j++){
			vis[i*prime[j]] = true;
			if(i%prime[j]==0){
				phi[i*prime[j]] = phi[i]*prime[j];
				break;
			}else
				phi[i*prime[j]] = phi[i]*phi[prime[j]];
		}
	}
}
```
