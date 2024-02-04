---
title: AC自动机
date: 2018-09-12 16:43:55 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

NOIP好像不考，介于时间紧，学的比较匆忙，日后复习
# 用途
就是用于多模式串的匹配问题
# 步骤
1.所有的模式串构建一棵trie树。
2.对Trie上的所有节点构造前缀指针。
3.利用前缀指针对主串进行匹配。
# 算法流程
树上KMP，见板子