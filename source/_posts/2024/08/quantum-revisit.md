---
title: 'Re:從零開始的量子生活'
excerpt: '戴上非常現代的線代視鏡來重新觀察量運'
index_img: /assets/cover/quantum-revisit-2024.avif
banner_img: /assets/banner/quantum-revisit-2024.avif
tags:
  - quantum
  - life
date: 2024-08-17 21:45:56
keywords: quantum computing
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

> 欸好久沒看 re:zero 了，等等寫完來看 

在高中時期，筆者曾經在只有一絲絲線代知識下自學過量子運算（Quantum Computing, QC），還順便想出了以下這量子態的製備演算法（Quantum State Preparation, QSP），量子核心部分複雜度粗估 $O(\log^2N)$。{% spoiler 隨手算的，60% 會錯(?) %}

<p>
$$
\ket{\psi} = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1}\ket{k},\ N \in \mathbb{Z}^+
$$
</p>

但在沒有完備數學底子之下，那時候的能力已經達到瓶頸了，所以之後數年都沒有再認真碰過。直到大二上學完線代。

## 正文

原本預計大二下來看之前的上課影片的計畫被打亂後，終於可以在平靜的暑假來實現這項事情了。

量運基本上整個基底都是由線代 + 量物相輔而成的 {% spoiler 幸好量運沒有太多量物(?) %}。所以扎扎實實學完線代再來挑戰量運，在理解速度上顯然是有很大差距。

### 筆記分享

{% note info %}
在學 Dirac Notation、Quantum Mechanics postulates and measurements 這幾個章節時因為還沒入手平板，所以沒留下筆記痕跡。
{% endnote %}

> [筆記連結](https://drive.google.com/drive/folders/1rRyHE9to2wZODhvhZ-U_Lv1r56FOMNON?usp=sharing)

### 一些心得

1. 測量的數學定義比預期中還要難很多，種類也很多種，到現在可能還不太熟練

2. 密度算子部分又遇到了機率老朋友，真的很難轉回來

3. 在密度算子證明偶而會遇到黑魔法，雖然已經問過一遍了但還是沒很懂，開學後再去問問

4. Arbitrary unitary gate 的造價也太昂貴，$O(n^2 2^{2n})$ 是甚麼鬼，$O(n^2 2^{2n})$ 耶

5. Permutation chain 的概念是好咚咚，說不定之後會用到

6. Simon's 意外地難，但相同概念也可以套到 Order finding 的第二種看法上，習慣啦

7. QFT 之後又出現一堆黑魔法了，還有一堆不知名的 theorem & lemma

8. Shor 比想像中還要簡單非常多，基本上要做的事都由 classical 做完了，只是用 quantum 來加速一下 order finding 的部分而已

## 後記

截至寫這篇文的現在，筆者還剩下大約兩個禮拜的課要看，基本上開學後一開始都可以先看看要不要看 paper 或是拿來讀其他科的咚咚了，大歡喜。

但有些東西感覺學太快所以還沒打好基礎，反正筆者學習習慣都是先碰然後放置消化，所以也沒啥大不了。

反正開學後班上有人要組團學，筆者的台大物理朋朋好像也要來學，到時候再去抱大腿uwu。

至於暑假旅行文...再看看嚕，太不習慣寫這種咚咚了，說不定拖到開學才會出來也說不定。

那就，先醬 owob。
