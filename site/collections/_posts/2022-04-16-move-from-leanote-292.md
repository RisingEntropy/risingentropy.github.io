---
title: unknown title
date: 2022-04-16 23:45:11 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

We used SOTA architecture to demonstrate that the improvement is due to the deployment of TCJA rather than a change in network design.

On DVS128, we utilized PLIF\cite{citefang2021incorporating} and remain the hyper-parameters the same. Dropout rate is set to 0.5 in accordance with the original network.  Following origin model, bias is set false. In the last layer, we ditched the LIF model in favor of a 1-D average pooling voting layer, which yielded a ten-dimensional vector as the vote outcome. This is because this architecture simulates a longer timestep (T=20), so that the robustness of the network can be impoved.


On CIFAR10-DVS, we adopt VGG architecture introduced in TET\cite{deng2021temporal}. There's no dropout on set. In this network,bias is enabled following the origin one. Voting layer is the same as DVS128.

On NCaltech 101,we combined two architectures together. First, we reserved a pooling for each layer,which comes from DVS128. Then, through the process, resolution is reduced while channel number is increased.The structure comes from VGG-2 and on CALTECH101,we set dropout rate to 0.8. Bias is disabled.


In those networks,compared with TET\cite{deng2021temporal},to support Fully-Spike, we choose to use MSE Loss rather than cross entropy. 
