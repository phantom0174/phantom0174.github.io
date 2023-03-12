---
title: 放點新奇的數學東西
excerpt: 就是數學大雜燴
index_img: /assets/cover/mafs_mixture.webp
banner_img: /assets/cover/mafs_mixture.webp
date: 2023-01-21 21:38:00
tags:
    - mafs
---


## 前言

因為這個 blog 實在太空了，所以放一些自己碰過的一些 **數學大雜燴**。

## 正文

#### 羅密歐與茱麗葉微分方程

<p>
$$
\begin{bmatrix}
\dot{R} \\ \dot{J}
\end{bmatrix}
=\textbf{M}
\begin{bmatrix}
R \\ J
\end{bmatrix} 
$$
</p>

#### 牛頓冷卻定律

<p>
$$
\frac{dT}{dt}=-k\left(T-E(t)\right)
$$
</p>

#### 費馬小定理

<p>
$$
a^{p-1}\equiv 1\quad (\bmod\ p)
$$
</p>

#### 歐拉定理

<p>
$$
a^{\varphi(n)}\equiv 1\quad (\bmod\ n),\ \gcd(a,n)=1
$$
</p>

#### 未命名 M5

<p>
$$
F\left(x\right)=\left(m\left(x\right)-\frac{1}{x}\int_{0}^{x}m\left(u\right)du\right)
$$
</p>

<p>
$$
M_{5}\left(x\right) = \int_{0}^{x}m\left(n\right)\cdot\left(1+F\left(n\right)\cdot sgn\left(m\left(n\right)\right)^{sgn\left(n\right)}\right)e^{\frac{l}{2}\left(x^{2}-n^{2}\right)}dn
$$
</p>

#### 花瓣

<p>
$$
\left( x^2 + y^2 \right)^{\frac{n+1}{2}} = \sum_{k=0}^{\left \lfloor \frac{n}{2}\right \rfloor} \binom{n}{2k}\ (-1)^k\ x^{n-2k}\ y^{2k}
$$
</p>

#### 奇怪積分

<p>
$$
\int_0^{x}u^udu=\sum_{n=0}^{\infty}\left(\frac{x^{n+1}}{n+1}\left(\sum_{m=0}^{n}\left(\frac{-1}{n+1}\right)^{n-m}\frac{\ln(x)^m}{m!}\right)\right)
$$
</p>

<p>
$$
\int_0^x(u\ln(u))^cdu=\frac{x^{c+1}}{c+1}\left(\sum_{n=0}^{c}\left(\frac{-1}{c+1}\right)^{c-n}\frac{c!}{n!}\ln(x)^n\right)
$$
</p>

#### 優秀的符號混用

<p>
$$
\int ddd=\frac{d^2}{2}+C
$$
</p>

#### Gamma 雜燴

<p>
$$\Gamma(z)=\int_0^\infty x^{z-1}e^{-x}dx$$
</p>

<p>
$$\Gamma(z)=(z-1)!$$
</p>

<p>
$$\int_{0}^{\infty}e^{-x^t}dx=\Gamma\left(\frac{1}{t}+1\right)$$
</p>

#### Laurent Series

<p>
$$
f(z)=\sum_{n=-\infty}^\infty a_n(z-c)^n
$$
</p>

#### 留數定理

<p>
$$
\oint_\gamma f(z)\, dz = 2\pi i \sum_{f_a} \operatorname{Res}(f, a_k)
$$
</p>

#### 超難積分雜燴

<p>
$$
\int \frac{dx}{x^n+1}=\frac{-1}{n}\sum_{\omega^n+1=0}\omega\ln(x-\omega)+C
$$
</p>

<p>
$$
\int\frac{dx}{x^{\frac{q}{p}}+1}=p\int \textbf{Q}\left[\frac{u^{p-1}}{u^q+1}\right]\left(x^{\frac{1}{p}}\right)dx-\frac{p}{q}\sum_{\omega^q+1=0}\omega^{p}\ln\left(x^{\frac{1}{p}}-\omega\right)+C
$$
</p>

#### 複數線積分雜燴

<p>
$$\int_0^\infty \frac{\sin(x)}{x}dx = \frac{\pi}{2}$$
</p>

<p>
$$\int_0^\infty \frac{dx}{x^n+1} = \frac{\pi}{n\cdot \sin\left(\frac{\pi}{n}\right)}$$
</p>

<p>
$$\int_0^\infty \sin\left(x^n\right)dx = \frac{1}{n}\sin\left(\frac{\pi}{2n}\right)\Gamma\left(\frac{1}{n}\right)$$
</p>

<p>
$$\int_0^\infty \frac{\sin\left(x^n\right)}{x}dx = \frac{\pi}{ 2|n| },\ n\neq 0$$
</p>

#### 單擺

<p>
$$
T=4\sqrt{\frac{L}{g}}K\left(\frac{\theta_0}{2}\right),\ K(x)=\int_0^{\frac{\pi}{2}}\frac{d\theta}{\sqrt{1-x^2\sin^2(\theta)}}
$$
</p>

#### 相撞

<p>
$$
t_{collision}=\frac{1}{\sqrt{2G(M+m)}}\left(\sqrt{r_ir_f(r_i-r_f)}+\sqrt{r_i^3}\cos^{-1}\left(\sqrt{\frac{r_f}{r_i}}\right)\right)
$$
</p>

#### 神奇數學大雜燴

<p>
$$D^{z}x^n=\frac{\Gamma(n+1)}{\Gamma(n-z+1)}x^{n-z}$$
</p>

<p>
$$D^{z}e^{nx}=n^{z}e^{nx}$$
</p>

<p>
$$D^{z}\cos(n\theta)=n^z\cos\left(n\theta+\frac{\pi}{2}z\right)$$
</p>

<p>
$$e^{D^z}(e^{nx})=e^{n^z+nx}$$
</p>

<p>
$$e^D(x^n)=(x+1)^n$$
</p>

<p>
$$sin(D)e^{nx}=e^{nx}\sin(n)$$
</p>

<p>
$$\sin(D)\sin(\theta)=\cos(x)\sinh(1)$$
</p>

<p>
$$
\sin(D)\ln(x) = \begin{cases}
\tan^{-1}\left(\frac{1}{x}\right)
    & \text{ if } x \geq 1 \\
\infty
    & \text{ if } 0 \lt x \lt 1
\end{cases}
$$
</p>

<p>
$$
\ln(D)e^{nx}=2\ln(n)e^{nx},\ n>0
$$
</p>

<p>
$$
\ln(D)\sin(x)=\pi\cos(x)
$$
</p>

<p>
$$
\frac{f(x)}{(D-a)^m}=e^{-ax}\int^{(m)}f(x)e^{ax}dx^{(m)}
$$
</p>

<p>
$$
\int_{0}^\infty \frac{f\left(x^n\right)}{x}dx
= \frac{1}{ |n| } \int_{0}^\infty \frac{f(t)}{t}dt,\ n\neq 0
$$
</p>

## 後記

推薦在無聊時可以去看看這些東西：

- 介紹影片
    - [Inter-universal Teichmüller theory via Fumiharu Kato w/English subtitles \[PROPER\]](https://www.youtube.com/watch?v=kq4jbNl4lJk)

- 論文連結
    1. [Part I](http://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf)
    2. [Part II](http://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1757.pdf)
    3. [Part III](http://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1758.pdf)
    4. [Part IV](http://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1759.pdf)
