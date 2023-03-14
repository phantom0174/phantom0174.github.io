---
title: '關於中國剩餘定理'
excerpt: '終於搞懂這千年遺恨啦！'
index_img: /assets/cover/about-chinese-remainder-theorem.webp
banner_img: /assets/banner/about-chinese-remainder-theorem.webp
tags:
  - mafs
  - life
date: 2023-03-13 23:35:00
keywords: 中國剩餘定理, 中國餘式定理, CRT, 同餘, 數論, 數學, 自學
---

## 前言

筆者在高中時候有段時間跑去學基礎數論，當時候基礎運算、費馬小定理甚麼的都懂了，就是不懂中國剩餘定理，遺恨千年 qwq。

剛剛恰好讀到跟數論有關的東西，就想起以前這個小遺憾，所以給自己 `1` 小時的時間重新複習同餘運算並挑戰弄懂中國剩餘定理。結果真的成功了！

## 正文

### 預備知識

以下是我這 `1` 小時內看的東東（依照時間排序），對我理解非常有幫助：

- 同餘基本運算
  1. [Day 14:[離散數學]同餘（Mod）是什麼](https://ithelp.ithome.com.tw/articles/10205727)

- 中國剩餘定理
  1. [Day 15:[離散數學] 中國餘式定理](https://ithelp.ithome.com.tw/articles/10205772)（文章）
  2. [The Chinese Remainder Theorem made easy](https://www.youtube.com/watch?v=ru7mWZJlRQg)（影片）
  3. [The Chinese Remainder Theorem (Solved Example 1)](https://www.youtube.com/watch?v=e8DtzQkjOMQ)（影片）

不過對於 `Day 14:[離散數學]同餘（Mod）是什麼` 中的 `同餘的相乘性質`，筆者有不同的見解。從文章中的講解來看，初學者（像是正在複習N年前學的東西的筆者）並不會知道第一式要乘上 $c$；第二式要乘上 $b$ 來證明這個東東，因此筆者臨時想出了另外一個感覺比較簡單的證明流程（基於變數變換）：

Statement:
<p>
$$
\begin{align*}
a &\equiv b \pmod k,\\
c &\equiv d \pmod k\\
\Rightarrow ac &\equiv bd \pmod k
\end{align*}
$$
</p>

Proof:
<p>
$$
\begin{align*}
c &= kp + r,\\
d &= kq + r\\
\Rightarrow c-d &= k(p-q) = kn\\
\Rightarrow c &= d+kn \tag{1}
\end{align*}
$$
</p>

<p>
$$
\begin{align*}
ac &\equiv bc \pmod k \tag{known fact}\\
\Rightarrow bc &\equiv b(d+kn) \equiv bd \pmod k \tag{by (1)}\\
\Rightarrow ac &\equiv bd \pmod k\ _\blacksquare
\end{align*}
$$
</p>

### 過程理解

> p.s. 筆者原本想把整個理解過程都打下來，但這樣會變成超長篇大論，因此理解過程就請讀者自行觀看上述文章與影片囉 \\^~^/

其實就是影片中的東西以筆者的理解語言複述一遍，以下是筆者自己理解的步驟：

1. 將 $x$ 構造出 $k$ 個部分，每個部分將會在同餘 $m_i$ 之下時顯現出獨立特性。
    > 在這一步定義 $M,\ M_i$，並先令每個部分都是 $M_i$。

2. 將獨立部分暫時湊出理想值
    > 在這一步將每個部分前方乘上 $a_i$

3. 利用反元素進行修正
    > 在這一步將每個部分後方乘上 $M_i^{-1}(m_i)$

4. 將所有部分合起來

<p>
$$
x = \sum a_i\cdot M_i\cdot M_i^{-1}(m_i)
$$
</p>

5. 加上週期修正項
    > 有點解基礎偏微分聯立方程時偏積分後要加上缺少項的感覺 owo

<p>
$$
x = \sum a_i M_i M_i^{-1}(m_i) + Mk,\enspace k\in\mathbb{Z}
$$
</p>

6. 完成！\\^~^/

## 後記

現在看整個過程在視覺化的幫助下其實應該蠻簡單的，只是筆者早期有陋習 - 甚麼東西都去 wiki 看。而 wiki 上中國剩餘定理頁面中的證明又寫得又亂又長（氣），所以筆者當時才會花了幾乎一整天盯著那個頁面看，結果最後還是靠直覺理解，然後隔天就忘掉了（所以到頭來根本沒有弄懂 owo）。

不過現在弄懂就是超級開心的啦 \\^~^/ \\^~^/ （灑花！

那就先醬。
