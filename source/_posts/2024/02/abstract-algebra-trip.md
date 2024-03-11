---
title: '抽象代數小旅行'
excerpt: '寒假期間了解了三等分角與倍立方問題的不可作證明'
index_img: /assets/cover/abstract-algebra-trip.avif
banner_img: /assets/banner/abstract-algebra-trip.avif
tags:
  - mafs
  - life
date: 2024-02-28 18:00:00
keywords: abstract algebra, field theory, angle trisection
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

&emsp;&emsp;筆者寒假時從書堆裡挖出來了很久以前買已經生灰塵的《數學女孩：伽羅瓦理論》，決定重看一遍之前一直卡關的地方{% spoiler  說不定有機會看完整本？  %}。筆者之前在體論的部分就卡得死死的了，後面的群論也只是掃過去根本沒看懂。如今來測試看看筆者的理解能力到哪裡了 owo。

&emsp;&emsp;直接跳結論：最後還是沒看完 QQ，但至少體論的部分概念已經懂了；群論因為有點小難所以最近還在從基礎看起（但時間又被量子運算搶走了）。不過在過程中也讀懂了在高中時期從來沒學過證明的兩個有名問題的證明：三等分角與倍立方，算是頗有收穫。

## 正文

{% note info %}
因為筆者太懶了，所以下文會跳過體&體擴張的概念 owo
{% endnote %}

### 尺規作圖支援的體態

&emsp;&emsp;因為尺規作圖可以支援加減乘除（用某些神奇的方式）與開根號運算，所以其支援的體 $\mathbb{F}$ 即為：

<p>
$$
\mathbb{F} = \mathbb{Q}\left ( \sqrt{\cdot} \right ) = \mathbb{Q}(\sqrt{n_1})(\sqrt{n_2}) \cdots (\sqrt{n_\infty})\\
\text{denote } \mathbb{Q}_0=\mathbb{Q},\, \mathbb{Q}_k = \mathbb{Q}_{k-1}(\sqrt{n_k})\\
\text{where } \mathbb{Q}_k \neq \mathbb{Q}_{k-1}\, \forall\, k \geq 1
$$
</p>

根據 Finite Extension Theorem[^1]，我們可以得知 $\left [ \mathbb{F}:\mathbb{Q} \right ]$（也就是這個體相對於 $\mathbb{Q}$ 的擴張度數）為 $2^n$，證明如下：

<p>
$$
\begin{align*}
\left[ \mathbb{Q}_k:\mathbb{Q} \right] &= \prod_{i=1}^{k}\left[ \mathbb{Q}_i:\mathbb{Q}_{i-1} \right]\\
&= \prod_{i=1}^{k}2\\
&= 2^k
\end{align*}
$$
</p>

### 任意三等分角的解屬於的體態

我們可以使用 $\cos$ 或是 $\sin$ 的三倍角公式來反推出 $\cos(\theta/3)$ 所在的解集體態為何：

<p>
$$
\begin{align*}
\cos(3\theta) &= 4\cos(\theta)^3 - 3\cos(\theta)\\
\Rightarrow \cos(\theta) &= 4\cos\left(\frac{\theta}{3}\right)^3 - 3\cos\left(\frac{\theta}{3}\right)
\end{align*}
$$
</p>

其中的 $\cos(\theta)$ 為已得知的數；而 $\cos(\frac{\theta}{3})$ 不知，令個別為 $a,\ x$ 得出方程式：

<p>
$$
4x^3-3x-a=0
$$
</p>

因此，如果我們能用尺規作圖創造出 $\mathbb{Q}\left(\cos(\frac{\theta}{3}) \right) = \mathbb{Q}(x)$ 這個體，即可用尺規作圖表達這個解。在這之前，我們先試算一下 $\left[ \mathbb{Q}(x):\mathbb{Q} \right]$ 為何。

為此，需要用到上面的方程式。注意到這個方程式在 $\mathbb{Q}$ 中是不可約的，因此它為解 $x$ 的最小多項式。因此，我們可以將

<p>
$$
B = \left\{ 1, x, x^2 \right\}
$$
</p>

作為基底，對 $\mathbb{Q}$ 進行擴張。為此，需要提到一下如何從上方的最小多項式提取出線性代數中的「線性獨立」資訊；我們先將這條方程式改變一下樣貌：

<p>
$$
(-a)\cdot 1 + (-3)\cdot x + 0\cdot x^2+4\cdot x^3=0
$$
</p>

這即符合「線性相依」的概念；而如果在**度數不到 3 之前**都沒有符合的方程式（因不可約），代表：

<p>
$$
\nexists\ a_{i's} \neq 0\ni \sum a_i\textbf{b}_i=0,\ \textbf{b}_i \in B
$$
</p>

因此，$B$ 為線性獨立。

回歸此擴張的度數：因 $|B| = 3$，因此 $\left[ \mathbb{Q}(x):\mathbb{Q} \right] = 3$。

如果我們可以用尺規作圖做出這個體，代表

<p>
$$
\mathbb{Q}(x) = \mathbb{F}
$$
</p>

然而

<p>
$$
\left[ \mathbb{Q}(x):\mathbb{Q} \right] = 3\\
\left[ \mathbb{F}:\mathbb{Q} \right] = 2^k
$$
</p>

<p>
$$
\text{Since } \nexists\ k \in \mathbb{Z} (2^k = 3)\, \rightarrow\leftarrow\\
\Rightarrow \mathbb{Q}(x) \neq \mathbb{F}\ _\blacksquare
$$
</p>

因此，尺規作圖無法做出這個解，因而無法實現任意三等分角。

### 倍立方的解屬於的體態

這個跟三等分角的差別只有這個問題的最小多項式為

<p>
$$
x^3-2=0
$$
</p>

遵循跟上面一樣的步驟就可得出解集體的擴張度數也為 3，同樣帶向矛盾。因此無法作圖。

## 後記

&emsp;&emsp;感謝物理系朋朋教我商群還有推薦給我群論的 yt 影片，前者的 Corollary 實屬 N 年前完全搞不懂的東東，但現在懂了就爽爽的 uwu。

那就，先醬。

---

[^1]: 其實筆者不確定這個定理的名稱是不是這個，甚至不確定它有沒有名字 owo，但因為頗符合的就先用(?)

<!-- ## 參考 -->
