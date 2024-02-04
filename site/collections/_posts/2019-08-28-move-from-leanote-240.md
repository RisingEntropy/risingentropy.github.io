---
title: FFT
date: 2019-08-28 15:19:19 +0800
image: '/images/posts/OI.png'
tags: [OI, former blog]
---

FFT过程（n items）
$$
F(x) = FL(x^2)+x*FR(x^2)\\
F(w_n^k) = FL((w_{n}^k)^2)+w_n^kFR((w_{n}^k)^2)\\
F(w_n^k) = FL(w_{n/2}^k)+w_n^kFR(w_{n/2}^k)\\
solve:w_n^0...w_n^{n/2-1}\\
to: w_n^{n/2-1}...w_n^{n-1}\\
$$
假设$k<n/2$,由于：
$$
w_n^k = w_n^{k\%n}
$$
所以可以做如下转化
$$
F(w_n^{k+n/2}) = FL((w_n^{k+n/2})^2)+w_n^{k+n/2}FR((w_n^{k+n/2})^2)\\
bacause\\
(w_n^k)^j = w_n^{kj}\\
therefore\\
=FL(w_n^{2k+n})+w_n^{k+n/2}FR(w_n^{2k+n})\\
w_n^k = w_n^{k\%n}\\
= FL(w_n^{2k})+w_n^{k+n/2}FR(w_n^{2k})\\
w_{2n}^{2k} = w_n^k\\
= FL(w_{n/2}^k)+w_n^{k+n/2}FR(w_{n/2}^k)\\
w_n^{k+n/2} = -w_n^{k}\\
therefore \\
FL(w_{n/2}^k)-w_n^{k}FR(w_{n/2}^k)
$$
DFT OK!

IDFT
$$nF[k] = \sum\limits_{i = 0}^{n-1}(\omega_n^{-k})^iY[i]$$