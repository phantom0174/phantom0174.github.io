---
title: '線代小筆記'
excerpt: '一堆線代咚咚'
index_img: /assets/cover/about-linear-algebra.avif
banner_img: /assets/banner/about-linear-algebra.avif
tags:
  - mafs
  - life
date: 2023-12-06 16:00:00
keywords:
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

&emsp;&emsp;筆者這學期初實在是被課業完全追著跑，都已經好幾個月沒寫文了QQ。今天上完線代後才實際用學到的東東來算之前想要算的東西。這篇文章就留著給線代相關的咚咚吧。{% spoiler  還有一篇線代的文難產中owo  %}

## 咚咚們

### k 次重複彈碰通式

> eigen 對角化後取冪再化簡

<p>
$$
\begin{align*}
  V^{+} &= \frac{1}{m+M}\begin{pmatrix}
    M-m & -2M\\
    2m & M-m\\
  \end{pmatrix}\\ \\
  \Rightarrow (V^+)^k &= \frac{1}{2}\begin{pmatrix}
    l^+ + l^- & (l^+ - l^-)\sqrt{\frac{M}{m}}i\\
    (l^- - l^+)\sqrt{\frac{m}{M}}i & l^+ + l^-\\
  \end{pmatrix} \\ \\ 
  \text{where } l^{\pm} &= e^{\pm ik\theta},\ \theta = \text{atan2}\left( M-m, \sqrt{4mM} \right) \\ \\
  \Rightarrow (V^+)^k &= \begin{pmatrix}
    \cos(k\theta) & -\sin(k\theta)\sqrt{\frac{M}{m}}\\
    \sin(k\theta)\sqrt{\frac{m}{M}} & \cos(k\theta)\\
  \end{pmatrix}
\end{align*}
$$
</p>

---

<!-- ## 參考 -->
