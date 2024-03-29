---
date: 2024-2-4 20:24:56 +0800
name: Scholar Homepage Spider
intro: A spder that claw and draw relation among scholars
image: https://cdn.risingentropy.top/images/posts/20240204232209.png
description: This spider claw data from google scholar or cnki and draw a relation graph among scholars
tags: [Network Spider, Python, JavaScript]
---

![20240204214358](https://cdn.risingentropy.top/images/posts/20240204214358.png)

代码：[Github](https://github.com/RisingEntropy/scholar-spider)

Code: [Github](https://github.com/RisingEntropy/scholar-spider)

一年一度的套磁季快到了，准备开始海投简历找老师了。为了更好地海投，我写了个爬虫，爬取 google scholar 和 cnki 上面的老师的合作关系，绘制关系图。代码包括 python 和 js，demo 在本页下方。

Time for applying for 2025 fall Ph.D is soon. To facilitate getting in contact, I write this network spider to draw the relation among mentors. The code includes python and javascript. A demon can be seen at the bottom this page.

## 使用方法 Usage
直接粘贴谷歌学术连接或者cnki学者主页就行。深度不建议设置超过2，超过2会变卡。由于谷歌学术不支持 CORS，所以我用了 cloudflare worker 进行代理转发。

Directly paste the google scholar homepage link or cnki homepage link into the text box. The suggested depth is no deeper than 2, otherwise it will get super slow. Google scholar doesn't support CORS, so I use the cloudflare worker as an agent to forward the request.

例如，我爬电子科技大学邓良剑老师的主页：

A successful demo is:
![20240204221953](https://cdn.risingentropy.top/images/posts/20240204221953.png)

图中，圆圈的颜色表示学校，大小表示影响因子（知网是下载量）。

In the figure, color of the circle is affiliation while the size is citation.
## Demo
<iframe src="https://risingentropy.top/single_pages/demo/scholar_spider.html" width="800" height = "850" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen> </iframe>