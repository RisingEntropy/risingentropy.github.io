---
date: 2024-4-8 16:23:56 +0800
name: Cell Scope
intro: An AI enpowered medical stain sample viewer
image: 'https://cdn.risingentropy.top/images/20240408172839.png'
description: To make it easier for doctors to examine patient samples, I developed the Cell Scope. Cell Scope is equipped with functions such as whole slide image (WSI) image browsing, neural network segmentation, and lesion cell counting.
tags: [NCNN, Qt, Medical-Image]
---
## Cell Scope
This is a software intended to automatic segment steined cells.

Code link: [Code](https://github.com/RisingEntropy/CellScope)

Functions: View, AI Powered Segmentation, Cell Count
## Install
```bash
git clone https://github.com/RisingEntropy/CellScope
xmake .
xmake install
```

## Demonstrate
View a WSI image:
![20240412155621](https://cdn.risingentropy.top/images/20240412155621.png)

Segment a WSI image using GPU:
![20240412155835](https://cdn.risingentropy.top/images/20240412155835.png)

View the segmentation and cell count:
![20240412155943](https://cdn.risingentropy.top/images/20240412155943.png)