---
title: '某古早積分的隱藏結構'
excerpt: '我們小學二年級就學過的東西啊'
index_img: /assets/cover/strange_integral_old.webp
banner_img: /assets/banner/strange_integral_old.webp
tags:
  - mafs
  - life
date: 2024-11-09 19:03:50
keywords: math, integral, residue
hide: false
---

<!-- Latex Protector: Remove "@" before use -->
<!--@lp:skip-all-->
<!--@lp:skip-some-->

<!-- EMSP Replacer: Auto replacement of double full-width white-space with &emsp;&emsp; -->

<!-- Spoiler Replacer: Replace ||text||  with {% spoiler text %} -->
<!--@sprp:skip-all-->

<!-- Footnote Reposer: Auto repositioning of all the footnotes in post -->
<!--@ft:skip-all-->


## 前言

在許久之前，筆者曾寫過一篇利用某奇怪公式對某函數強制做部分分式展開，[以解其積分的文章][prev_pos]。

然而，某奇怪公式寫出來後與**留數**的定義不謀而合，困擾了筆者許久。

在向數學系雙主資工電神朋朋請教後，得到了想要的解答，如下：

## 正文

注意到所有留數都是一階的，強制對 $f(z) = \frac{1}{z^n+1}$ 展開成部分分式：

<p>
$$
\sum_{\omega^n+1=0} \frac{c_k}{z-\omega}
$$
</p>

為顯現其中 $c_k$ 即為 $f(z)$ 在 $\omega_k$ 的留數，我們引進留數的定義/留數定理：

<p>
$$
\text{Res}(f,\omega_k) = \frac{1}{2\pi i} \oint_{C_k}f(z)dz \equiv \frac{I}{2\pi i}
$$
</p>

其中 $C_k$ 為以 $\omega_k$ 為圓心的一半徑極小逆時針圓曲線。將此線積分分成包圍住 $\omega_k$ 與落在外圍的 $\omega_j$ 部分：

<p>
$$
I = \lim_{r \rightarrow 0} \oint_{C_k}\frac{c_k}{z-\omega_k} + \sum_{j \neq k}\oint_{C_k}\frac{c_j}{z-\omega_j} \equiv I_1 + I_2
$$
</p>

接下來做參數化以求解線解積分：

<p>
$$
\begin{align*}
  z &= \omega_k + re^{i\theta}\\
  dz &= ire^{i\theta}d\theta
\end{align*}
$$
</p>

<p>
$$
\begin{align*}
I_1 &= \lim_{r \rightarrow 0} \int_0^{2\pi}\frac{c_k \cdot ire^{i\theta}}{re^{i\theta}} d\theta= 2\pi i c_k\\ \\
I_2 &= \lim_{r \rightarrow 0} \sum_{j \neq k}\int_0^{2\pi} \frac{c_j \cdot ire^{i\theta}}{\omega_k + re^{i\theta} -\omega_j}d\theta = \lim_{r \rightarrow 0} \sum_{j \neq k} r \left(\int_0^{2\pi} \frac{c_j \cdot ie^{i\theta}}{\omega_k + re^{i\theta} -\omega_j}d\theta \right) = 0
\end{align*}
$$
</p>

<p>
$$
\text{Res}(f,\omega_k) = \frac{1}{2\pi i} \left( I_1 + I_2 \right) = \frac{1}{2\pi i} (2\pi i c_k + 0) = c_k\ _\blacksquare
$$
</p>

## 後記

這樣就不用依賴某奇怪公式，可以從複變的角度去解釋這一現象了，也可以推廣到其它積分上。

感謝 @meep，解惑了一個大大大疑問，果然數學還是要問數學系 uwub。

[prev_pos]: <https://phantom0174.github.io/2023/01/compute-that-strange-integral/#所以要怎麼解這個積分呢？>