---
title: 關於我怎麼算出那個奇怪積分的
excerpt: 如何解開那個令超多人為之苦惱的積分
date: 2023-01-16 00:00:00
updated: 2023-01-18 14:41:00
index_img: /assets/cover/strange_integral.webp
banner_img: /assets/banner/strange_integral.webp
tags:
    - mafs
---

## 簡單版的積分（正整數）

### 這個積分的由來

學會積分的第一件事，就是試著解解看各式各樣的積分。
一開始看到這個問題時可能會想：這超簡單的啦！（$n\in\mathbb{Z}^+$）

<p>
$$
\int \frac{dx}{x^n}
$$
</p>

但如果它偷偷幫自己在分母 $+1$ 的話：

<p>
$$
\int \frac{dx}{x^n + 1}
$$
</p>

你會發現，用部份積分、變數變換、費曼積分法、複數線積分都做不出來。
> p.s. 用複數線積分當然做不出來，因為那是解瑕積分時才會用到的，當時不知道的筆者還特地為了這個問題去碰了複變 OwO。

用泰勒展開固然可以解，但那會變成非封閉形式的解，身為數學完美主義者的筆者當然是想要得到封閉形式的解。

### 所以要怎麼解這個積分呢？

這時候，就要回歸到最初的技巧 - **部份分式**！
特地觀察這個積分的分母 $x^n + 1$ 後，會發現它如果要拆解成數個 $x-\omega_i$ （$\omega_i$ 是 $x^n + 1 = 0$ 的第 $i$ 個根，總共 $n$ 個） 相乘的型式的話，其中的 $\omega_i$ 幾乎都是複數。
所以，我們可以導出以下等式：

<p>
$$
\begin{align*}
\frac{1}{x^n + 1}&=\prod_{i=1}^{n}\frac{1}{x-\omega_i}\\
&=\sum_{i=1}^{n}\frac{c_i}{x-\omega_i}
\end{align*}
$$
</p>

但這時我們並不知道其中的 $c_i$ 甚麼，因此需要先引進一個我稱之為 **一階部份分式封閉型式展開式** 的超級有用公式：

<p>
$$
\frac{f}{g} = \sum_{\omega\in \mathbb{Z}_g}\left(\frac{f(u)}{g'(u)}\biggm\vert_{u=\omega}\cdot\frac{1}{x-\omega}\right)
$$
</p>

不過使用它的條件也很嚴苛：

<p>
$$
\begin{align*}
&1.\quad \partial f < \partial g \\
&2.\quad \forall\ \omega\in \mathbb{Z}_g,\ \partial\omega = 1 \\
&3.\quad \mathbb{Z}_f\ \cap\ \mathbb{Z}_g = \emptyset \\
\end{align*}
$$
</p>

這邊的 $\mathbb{Z}_f,\ \mathbb{Z}_g$ 指的就是 $f,\ g$ 的零點集（就是所有不重複的根所形成的集合）。
用白話文說明一下這三點：

1. $f$ 的次方要小於 $g$ 的次方
2. 用部份分式所展開 $g$ 的所有根的都不可以是一以上的重根
3. $f$ 和 $g$ 不行有相同的根

以下是 **一階部份分式封閉型式展開式** 的推導，覺得太長可以跳過。

{% note secondary %}

首先，規則 1. 要成立，因為如果 $f$ 的次方大於 $g$ 的次方的話就應該會有一個商式，要另外處裡。
接下來就是普通部份分式的第一步（這邊假設 $g$ 的次數是 $n$）：

<p>
$$
\frac{f(x)}{\prod_{i=1}^{n}(x-\omega_i)} = \sum_{i=1}^{n}\frac{c_i}{x-\omega_i}
$$
</p>

將兩邊分母約分，並比較之後可得：

<p>
$$
f(x) = \sum_{i=1}^{n}\left(c_i\prod_{j\neq i}(x-\omega_j)\right)
$$
</p>

我們將要解的目標設定為係數 $c_k$，所以先把不相關的全部移到左邊去（這邊容許筆者偷懶簡寫下標與上標）：

<p>
$$
f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j) = c_k\prod_{j\neq k}(x-\omega_j)
$$
</p>

這時，右邊看起來很醜，所以我們將兩邊同乘 $x-\omega_k$：

<p>
$$
\begin{align*}
(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right) &= c_k(x-\omega_k)\prod_{j\neq k}(x-\omega_j)\\
&=c_k\cdot g(x)
\end{align*}
$$
</p>

這時右邊好看多了。為了解 $c_k$，將 $g$ 除到左邊下面：

<p>
$$
c_k = \frac{(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)}{g(x)}
$$
</p>

但現在還有奇怪的東西：

<p>
$$
\sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)
$$
</p>

注意：每一個 $\prod_{j\neq i}(x-\omega_j)$ 中都有 $x-\omega_k$。
因此要讓這個東西消失的話，我們可以玩個把戲：把兩邊的 $x$ 都趨近於 $\omega_k$

<p>
$$
\lim_{x\to \omega_k} c_k = \lim_{x\to \omega_k} \frac{(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)}{g(x)}
$$
</p>

但有個問題，右邊的 $(x-\omega_k)$ 與 $g(x)$ 在 $x\to \omega_k$ 時都會變成 $0$。
因此這個極限也是 $\frac{0}{0}$ 的形式，這時候就可以引進羅必達法則了！

<p>
$$
\begin{align*}
\lim_{x\to \omega_k} \frac{(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)}{g(x)} \overset{L'Hôpital}{=}& \lim_{x\to \omega_k} \frac{\left((x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)\right)'}{g'(x)}\\
=& \lim_{x\to \omega_k} \frac{(x-\omega_k)'\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)+(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)'}{g'(x)}\\
=& \lim_{x\to \omega_k} \frac{\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)+(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)'}{g'(x)}
\end{align*}
$$
</p>

其中分子左方的 $\sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)$ 與右方的 $(x-\omega_k)$ 在 $x\to \omega_k$ 時都會變成 $0$。
所以這個極限值等於

<p>
$$
\begin{align*}
&= \lim_{x\to \omega_k} \frac{\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)+(x-\omega_k)\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)'}{g'(x)}\\
&= \lim_{x\to \omega_k} \frac{\left(f(x) - 0\right)+0\cdot\left(f(x) - \sum_{i\neq k}c_i\prod_{j\neq i}(x-\omega_j)\right)'}{g'(x)}\\
&= \lim_{x\to \omega_k} \frac{f(x)}{g'(x)}
\end{align*}
$$
</p>

而依照規則 3.，$f(\omega_k)$ 不會是 $0$，因為 $f,\ g$ 沒有共同根。
另外，依照規則 2. $g$ 的每個根都是一階根，因此 $g'(\omega_k)$ 也不會是 $0$。我們得到：

<p>
$$
\begin{align*}
\lim_{x\to \omega_k} c_k &= \lim_{x\to \omega_k} \frac{f(x)}{g'(x)}\\
&=\frac{f(u)}{g'(u)}\biggm\vert_{u=\omega_k}
\end{align*}
$$
</p>

左邊顯然不被 $x$ 極限取值影響，因此以下就是針對單個係數 $c_k$ 的結果，而對於任意其他的係數也是相同結果：

<p>
$$
c_k =\frac{f(u)}{g'(u)}\Big|_{u=\omega_k}
$$
</p>

最終，將這個結果塞回原本的展開式中，得到：

<p>
$$
\frac{f}{g} = \sum_{\omega\in \mathbb{Z}_g}\left(\frac{f(u)}{g'(u)}\biggm\vert_{u=\omega}\cdot\frac{1}{x-\omega}\right)_\blacksquare
$$
</p>

{% endnote %}

回到正題。<del>早上好台灣，</del>現在我們有 **一階部份分式封閉型式展開式**，可以來準備解這題積分了。

<p>
$$
\begin{align*}
\frac{1}{x^n + 1} &= \sum_{\omega^n + 1 = 0}\frac{1}{\left(u^n+1\right)'}\biggm\vert_{u=\omega}\frac{1}{x-\omega}\\
&=\sum_{\omega^n + 1 = 0}\frac{1}{n\omega^{n-1}}\cdot \frac{1}{x-\omega}
\end{align*}
$$
</p>

而由已知條件 $\omega^n+1 = 0$，我們可以進一步化簡 $n\omega^{n-1}$：

<p>
$$
\begin{align*}
\omega^n+1&=0\\
\omega^n&=-1\\
\omega^{n-1}&=\frac{-1}{\omega}
\end{align*}
$$
</p>

所以，

<p>
$$
\sum_{\omega^n + 1 = 0}\frac{1}{n\omega^{n-1}}\cdot \frac{1}{x-\omega} = \frac{-1}{n}\sum_{\omega^n + 1 = 0}\omega\cdot \frac{1}{x-\omega}
$$
</p>

最後，只要把這個東西積分起來就好了：

<p>
$$
\begin{align*}
\int \frac{dx}{x^n+1}&=\int \frac{-1}{n}\sum_{\omega^n + 1 = 0}\omega\cdot \frac{1}{x-\omega}dx\\
&=\frac{-1}{n}\sum_{\omega^n + 1 = 0}\omega \int \frac{1}{x-\omega}dx\\
&=\frac{-1}{n}\sum_{\omega^n + 1 = 0}\omega\ln(x-\omega)+C\ _\blacksquare
\end{align*}
$$
</p>

### 簡單驗證與要點

在大一學微積分的時候，通常老師都會告訴你 $\int\frac{dx}{x-k}$ 積分後要加絕對值，變成

<p>
$$
\ln\left|x-k\right|+C
$$
</p>

但在這邊，算出來的結果卻不行加絕對值，因為我們處裡的東西有 **複數**。
不信的話，我們可以用 $n=2$ 驗證看看（結果應該會是 $\tan^{-1}(x)+C$）：

{% note success %}

不加絕對值的版本

<p>
$$
\begin{align*}
\frac{-1}{2}\sum_{\omega^2 + 1 = 0}\omega\ln(x-\omega)+C &= -\frac{1}{2}\left(i\cdot\ln(x-i)+(-i)\cdot\ln(x-(-i)) \right)+C\\
&=-\frac{i}{2}\left( \ln(x-i)-\ln(x+i)\right)+C\\
&=\frac{i}{2}\left( \ln(x+i)-\ln(x-i)\right)+C\\
&=\frac{i}{2}\ln\left(\frac{x+i}{x-i}\right)+C\\
&=\frac{i}{2}\ln\left(\frac{i+x}{i-x}\right)+C'\\
\end{align*}
$$
</p>

{% endnote %}

{% note warning %}

加絕對值的版本

<p>
$$
\begin{align*}
\frac{-1}{2}\sum_{\omega^2 + 1 = 0}\omega\ln|x-\omega|+C &= -\frac{1}{2}\left(i\cdot\ln|x-i|+(-i)\cdot\ln|x-(-i)| \right)+C\\
&=-\frac{i}{2}\left( \ln|x-i|-\ln|x+i|\right)+C\\
&=\frac{i}{2}\left( \ln|x+i|-\ln|x-i|\right)+C\\
&=\frac{i}{2}\ln\left|\frac{x+i}{x-i}\right|+C\\
&=\frac{i}{2}\ln\left|\frac{i+x}{i-x}\right|+C\\
\end{align*}
$$
</p>

{% endnote %}

最後，我們把 $\tan^{-1}(x)$ 在複變分析中的定義[^1]拿出來比對：

<p>
$$
\tan^{-1}(x)=\frac{i}{2}\ln\left(\frac{i+x}{i-x}\right)
$$
</p>

很明顯可以看出來，沒有加絕對值的結果才跟這個一樣。

或者也可以從反證的方式思考：
現在假設加絕對值的結果是對的，並代入任一實數，會變成兩個複數做運算後取絕對值（也就是取模長），這樣 $\ln$ 項就會變成一個實數。
任意實數乘上前面的 $\frac{i}{2}$ 結果都會是複數（除了如果那個實數是 $0$）。
但我們知道 $\tan^{-1}(x)$ 的值在代入實數時應該也要是實數，而這跟我們的結果矛盾，因此一開始的假設是錯的，也就是加絕對值後的結果並不是對的。

## 困難版的積分（有理數）

### 過程大綱

1. 變數變換
2. 引入一階部份分式封閉型式展開式
3. 分別處理餘與商函數
4. 將結果合併
5. 用已知條件進行簡化

### 詳細過程

要解這個積分：

<p>
$$
I(x)=\int\frac{dx}{x^{\frac{q}{p}}+1},\quad q,\ p\in\mathbb{Z}^+,\ \gcd(q, p) = 1
$$
</p>

的話，首先要引進以 $u=x^{\frac{1}{p}}$ 為核心的變數變換：

<p>
$$
\begin{align*}
u&=x^{\frac{1}{p}}\\
\Rightarrow \frac{du}{dx}&=\frac{1}{p}\cdot x^{\frac{1}{p}-1}\\
\Rightarrow p\cdot x^{1-\frac{1}{p}}du&=dx\\
\overset{u^p=x}{\Rightarrow}pu^{p-1}du&=dx
\end{align*}
$$
</p>

變換的結果：

<p>
$$
p\int\frac{u^{p-1}}{u^q+1}du
$$
</p>

觀察分子與分母都是一個有理多項式，此時便可引進在簡單版時同樣有用到的 **一階部份分式封閉型式展開式**。
但注意這邊的 $p-1$ 有可能會 $\geq$ $q$，會不滿足第一條規則，所以要分開討論：

<p>
$$
\int\frac{f(x)}{g(x)}dx=\int Q(x)\, dx + \sum_{\omega\in\mathbb{Z}_g}\frac{R(\omega)}{g'(\omega)}\ln(x-\omega)+C
$$
</p>

其中 $Q(x)$ 和 $R(x)$ 就是商式與餘式。

{% note info %}

其一，當 $p-1 \lt q$ 時，$Q(x) = 0$，便可直接引進公式得到結果：

<p>
$$
\begin{align*}
\int\frac{u^{p-1}}{u^q+1}du&=p\sum_{\omega^{q}+1=0}\frac{\omega^{p-1}}{q\omega^{q-1}}\ln(u-\omega)+C,\ u=x^{\frac{1}{p}}\\
&=\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p-q}\ln(x^{\frac{1}{p}}-\omega)+C\\
&=-\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p}\ln(x^{\frac{1}{p}}-\omega)+C\\
\end{align*}
$$
</p>

{% endnote %}

{% note warning %}

其二，當 $p-1 \ge q$ 時，我們便要計算 $Q(x),\ R(x)$ 分別是甚麼，最後再對其進行積分。
然而，對於 $Q(x),\ R(x)$，筆者目前除了用最簡單的慢慢除方式，想不到其他可行的方法。

> p.s. 之前筆者有寫出來一個要解 $n$ 維複數逆矩陣的解法，但那顯然太難了。

為簡化運算過程，我們令 $p-1 = b,\ q = a$，這是我們的目標：

<p>
$$
x^b=(x^a+1)Q(x)+R(x)
$$
</p>

以下為過程：

<p>
$$
\begin{align*}
x^b&=(x^a+1)\cdot x^{b-a}-x^{b-a},\ b-a > a,\\
x^{b-a}&=(x^a+1)\cdot x^{b-2a}-x^{b-2a},\ b-2a> a,\\
&...\\
x^{b-(n-1)a}&=(x^a+1)\cdot x^{b-na}-x^{b-na},\ b-na\geq a,\\
x^{b-na}&=(x^a+1)\cdot x^{b-(n+1)a}-x^{b-(n+1)a},\ b-(n+1)a < a,\\
\end{align*}
$$
</p>

這過程就是對每次試除一次之後的餘式繼續試除，直到最後沒辦法再除的時候（假設除了共 $n$ 次）停下。
而把這些試除之後得到的商全部加起來，可以得到下面的式子：

<p>
$$
\Rightarrow x^b=(x^a+1)\left(x^{b-a}-x^{b-2a}+...+(-1)^{n}x^{b-(n+1)a}\right )-(-1)^{n}x^{b-(n+1)a}
$$
</p>

而用 **沒辦法再除** 的這個條件，又可以得到自然限制，並解出 $n$：

<p>
$$
\begin{alignat*}{3}
b-(n+1)a &< a &&\leq b-na,\ a \neq 0\\
\Rightarrow \frac{b}{a}-(n+1) &< 1 &&\leq \frac{b}{a}-n\\
\Rightarrow \frac{b}{a}-1 &< n+1 &&\leq \frac{b}{a}\\
\end{alignat*}\\
\Rightarrow n+1=\left \lfloor \frac{b}{a}\right \rfloor\\
$$
</p>

解出 $n$ 後，便可把上面的 $Q(x),\ R(x)$ 寫成封閉形式：

<p>
$$
\begin{align*}
Q(x)&=\sum_{k=1}^{n+1}(-1)^{k-1}x^{b-ka},\\
R(x)&=-(-1)^{n}x^{b-(n+1)a}\\
\end{align*}
$$
</p>

最後，先把 $n+1$ 換回來：

<p>
$$
n+1 = \left \lfloor \frac{b}{a}\right \rfloor = \left \lfloor \frac{p-1}{q}\right \rfloor = m
$$
</p>

再解最後的積分：

<p>
$$
\begin{align*}
p\int\frac{u^{p-1}}{u^q+1}du&=p\left[\int\sum_{k=1}^{m}(-1)^{k-1}u^{(p-1)-kq}du+\sum_{\omega^{q}+1=0}\frac{(-1)^{m}x^{(p-1)-mq}}{\left(u^q+1\right)'}\biggm\vert_{u=\omega}\ln(u-\omega)\right]+C\\
&=p\left[\sum_{k=1}^{m}(-1)^{k-1}\frac{u^{p-kq}}{p-kq}+(-1)^m\frac{1}{q}\sum_{\omega^q+1=0}\omega^{p-(m+1)q}\ln(u-\omega)\right]+C\\
&=p\sum_{k=1}^{m}(-1)^{k-1}\frac{u^{p-kq}}{p-kq}+(-1)^m\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p-(m+1)q}\ln(u-\omega)+C,\ u=x^{\frac{1}{p}}\\
&=p\sum_{k=1}^{m}(-1)^{k-1}\frac{x^{1-k\frac{q}{p}}}{p-kq}+(-1)^m\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p-(m+1)q}\ln(x^{\frac{1}{p}}-\omega)+C\\
&=p\sum_{k=1}^{m}(-1)^{k-1}\frac{x^{1-k\frac{q}{p}}}{p-kq}-\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p}\ln(x^{\frac{1}{p}}-\omega)+C
\end{align*}
$$
</p>

{% endnote %}

將上面兩個情況整合起來，就可以得到這個問題的最終答案：

<p>
$$
\begin{align*}
I(x)&=\int\frac{dx}{x^{\frac{q}{p}}+1}\\ \\
&=\begin{cases}p\sum_{k=1}^{m}(-1)^{k-1}\frac{x^{1-k\frac{q}{p}}}{p-kq}-\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p}\ln(x^{\frac{1}{p}}-\omega)+C,\ m=\left \lfloor \frac{p-1}{q} \right \rfloor & \text{ if } p\geq q+1\\
-\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p}\ln(x^{\frac{1}{p}}-\omega)+C & \text{ if } p< q+1\ _\blacksquare\end{cases}
\end{align*}
$$
</p>

恭喜，現在你也會解這兩個積分了！

---

p.s. 寫到手快斷掉owo

## 參考

[^1]: https://zh.m.wikipedia.org/zh-tw/反正切#定義
