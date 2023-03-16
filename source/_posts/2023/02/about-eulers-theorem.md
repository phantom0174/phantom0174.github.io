---
title: '有關歐拉定理'
excerpt: '記錄一下自己複習的歐拉定理證明流程'
index_img: ''
banner_img: ''
tags:
  - mafs
  - life
date: 2023-03-16 23:46:01
keywords: 歐拉定理, Euler's theorem, 同餘, 數論, 數學, 自學
---

## 前言

如副標，只是記錄一下自己複習的歐拉定理證明流程 owo。

> 所以才沒有專屬放上精美的封面

## 正文

創建兩個集合，$S$ 包含所有小於且與 $n$ 互質的不重複的數；$S_a$ 則是 $S$ 中的所有元素都乘上一個與 $n$ 互質的數 $a$。

<p>
$$
\begin{align*}
&\text{let}\quad S = \set{e\mid \forall\, e(e\ \bot\ n) \wedge (0 < e < n)};\ \Rightarrow |S|=\varphi(n)\\
&\text{let}\quad S_a=\set{a\cdot e\mid \forall\,e\in S},\enspace a\ \bot\ n
\end{align*}
$$
</p>

證明：$S_a$ 中的元素在模 $n$ 之下跟 $S$ 中的元素是完全相同且不重複的。

<p>
$$
\begin{align*}
&\text{Notice that if}\quad ae_1\equiv ae_2 \pmod n\\
&\Rightarrow a(e_1-e_2)\equiv 0 \pmod n\\
\end{align*}
$$
</p>

然而，因為 $a$ 與 $n$ 互質、$e_1 - e_2$ 也不可能大於 $n$，因此唯一可能的就只有 $e_1 = e_2$。

但因為 $S$ 中的元素不重複，故此條件不可能符合，進而導致此假設不可能成立。因此在 $S_a$ 中的元素在模 $n$ 之下是完全不重複$^{(1)}$、小於 $n$ $^{(2)}$、且與 $n$ 互質的$^{(3)}$。

如要符合 (1) & (2) & (3)，代表 $S_a$ 中的元素會完全與 $S$ 中的一樣。因此得出：

<p>
$$
\begin{align*}
\prod_{e\ \in\ S}e &\equiv \prod_{\varepsilon\ \in\ S_a}\varepsilon \pmod n\\
&= \prod_{e\ \in\ S}ae\\
&= a^{|S|}\prod_{e\ \in\ S}e\\
&= a^{\varphi(n)}\prod_{e\ \in\ S}e\\
\end{align*}
$$
</p>

通過消去左右兩邊元素的乘積（因為 $\prod e$ 仍與 $n$ 互質），得出證明：

<p>
$$
\begin{align*}
\prod_{e\ \in\ S}e &\equiv a^{\varphi(n)}\prod_{e\ \in\ S}e \pmod n\\
\Rightarrow a^{\varphi(n)} &\equiv 1 \pmod n\ _\blacksquare
\end{align*}
$$
</p>

---
