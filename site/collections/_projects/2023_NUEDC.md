---
date: 2023-12-3 00:17:23 +0800
name: 2023年全国大学生电子设计竞赛H题FPGA部分
intro: 国一作品
image: https://cdn.risingentropy.top/images/posts/20231203004200.png
description: 2023年全国大学生电子设计竞赛H题FPGA部分，包含ADC、DAC、SPI、寄存器组，DDS部分
tags: [verilog, Vivado]
---
[Code](https://github.com/RisingEntropy/2023EEDesignContest)


![20231203002321](https://cdn.risingentropy.top/images/posts/20231203002321.png)
这是2023年全国大学生电子设计竞赛H题《信号分离装置》我们的方案。该仓库为FPGA部分电路设计代码。我们的方案分为三个部分，模拟电路部分，MCU部分，FPGA部分。[MCU部分代码](https://github.com/Duanyll/h743_2023h)


FPGA选用XilinxXC7K70TFBG484-2芯片，高速ADC选用AD9269，DAC选用AD9744芯片。FPGA电路主要分成三个部分，ADC输入部分、寄存器组和输出部分。ADC 的采样率被设置为40.960. Msps，这样的数据速率超过了stm32单片机SPI总线的速度，故设计了一个缓冲区来缓存数据并发送给stm32单片机以供其分析计算。同时ADC部分还会维护一个触发计时，当计时结束时，会在下一个ADC的过零点产生一个触发信号来复位DDS的相位，以减少频率误差的积累。

在寄存器组中，一共存在13个寄存器，地址从0x00到0x0D，其功能被列在表1中。通过
SPI 读写寄存器组的方式，STM32单片机可以灵活地配置FPGA电路的输入输出和表现。寄存
器主要负责配置DDS重置周期、两个通道的输出波形、频率及其初始相位。
寄存器表格如下：
![20231203002642](https://cdn.risingentropy.top/images/posts/20231203002642.png)