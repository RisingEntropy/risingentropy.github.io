---
date: 2024-2-4 20:24:56 +0800
name: Scholar Homepage Spider
intro: A spder that claw and draw relation among scholars
image: https://cdn.risingentropy.top/images/posts/20240204214135.png
description: This spider claw data from google scholar or cnki and draw a relation graph among scholars
tags: [NCNN, YOLO, Deployment]
---

![20240204214358](https://cdn.risingentropy.top/images/posts/20240204214358.png)

代码：[code](https://github.com/RisingEntropy/scholar-spider)
一年一度的套磁季快到了，准备开始海投简历找老师了。写了个爬虫，爬取google scholar 和cnki 上面的老师的合作关系，绘制关系图。代码包括python和js，实际demo在本页展示

## 使用方法
直接粘贴谷歌学术连接或者cnki学者主页就行。深度不建议设置超过2，超过2会非常卡且半天爬不完。

## Demo
<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
    <script defer src="https://cdn.risingentropy.top/scholar_spider.js" type="text/javascript" charset="utf-8"></script>
    <link rel="stylesheet" href="https://cdn.risingentropy.top/scholar_spider.css">
    <div id="google_spider_area" class="spider_area">
        <div class="input_area">
            <div class="inputbox">
                <input type="text" required="required" id="home_page_url">
                <span>Homepage URL</span>
            </div>
            <div class="inputbox">
                <input type="number" required="required" id="depth" step="1" min="0">
                <span>Depth</span>
            </div>
        </div>
        <div id="button-wrapper">
            <p class="submit" >Submit</p>
            <div class="loader-wrapper">
                <span class="loader yellow"></span>
                <span class="loader pink"></span>
            </div>
            <span class="loader orange"></span>
            <div class="check-wrapper">
                <svg width="65px" height="38px" viewBox="0 0 64.5 37.4">
                    <polyline class="check" points="5,13 21.8,32.4 59.5,5 "/>
                </svg>
            </div>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg">  <defs>    <filter id="goo">      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />      <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="goo" />      <feBlend in="SourceGraphic" in2="goo" />    </filter>  </defs></svg>
        <div class="gradient-border" id="box">
            <div id="graph"></div>
        </div>
    </div>