---
date: 2023-7-25 19:23:56 +0800
name: 智能数控电源
intro: 数控buck-boost电源
image: https://cdn.risingentropy.top/images/posts/integratedcircuitsics.png
description: 输出电压可调buck-boost电源，输入电压2.7-12V，最大输出电流2A，最大输入电流4A。
tags: [Power, Stm32]
---

仓库连接：[Code](https://github.com/RisingEntropy/SmartPower)

这是一个以MP8862为电源芯片，外加stm32l051 MCU为主控的可调数控电源。控制方式为：旋转EC11编码盘调整输出电压大小（步长0.1V），按下编码盘输出/关闭。具有锁定参数功能（按下右方按钮设置锁定/解锁）。参数锁定后，无法调节输出电压大小和输出状态，防止误触导致电压过高系统烧毁。经过测量，该电源纹波小于10mV（我使用的示波器信噪比较低，只能大概看出小于10mV，没法再精确测量）。同时，MCU未使用的引脚均引出，方便电子设计竞赛时使用。系统待机功率0.01W（取下OLED显示屏，插上OLED显示屏功率0.015W）。UI部分由u8g2库实现，此库对内存要求稍高，几乎占满了stm32l051的所有flash，若需该电源同时完成一些较为复杂的任务，可以修改源代码。

## 实物展示：
![实物](https://cdn.risingentropy.top/images/posts/5ce8a666b2b55bc662fe89bb308c28a4.jpeg)

## 仓库说明：
PCB docs为Altium Designer的PCB文件。

L051MAX77857.ioc为stm32cubemx 的配置文件

其余为stm32cubemx生成的代码，ide为clion，构建系统为cmake。

## 注意事项
PCB打板推荐华秋PCB，嘉立创样板工艺太差！