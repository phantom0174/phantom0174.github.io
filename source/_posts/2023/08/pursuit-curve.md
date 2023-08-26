---
title: '有關追蹤曲線'
excerpt: '從 Terraria 發想的小研究'
index_img: /assets/cover/pursuit-curve.avif
banner_img: /assets/banner/pursuit-curve.avif
tags:
  - mafs
  - life
date: 2023-08-27 00:00:00
keywords: 追蹤曲線, pursuit curve, radiodrome, differential equation, laplace transform, terraria, wall of flesh
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

&emsp;&emsp;筆者這個暑假有段時間沉迷於開放世界型遊戲（典型的報復性沉迷 uwu），其中包含了知名的 Terraria。先說個題外話：這是筆者第一次破關（打完 Moonlord），花了成噸的時間在上面，不過娛樂性相當值得 \\^~^。

![Home sweet home](/assets/contents/pursuit-curve/terraria-house.avif)
![精神時光屋](/assets/contents/pursuit-curve/terraria-save.avif)

&emsp;&emsp;有玩過的人應該知道，Terraria 中有一個叫 [Wall Of Flesh (WoF)][wof] 的 Boss。WoF 有一種特殊的 debuff - 狂卷之舌：當你在距離牠太遠時會伸出舌頭把你拉回去。

&emsp;&emsp;筆者在玩的時候就想到，如果玩家利用魔鏡傳送回地表後馬上開始被拉回去地獄時，玩家的軌跡 **真正來說** 會長怎樣呢[^1]？因為在拉的過程中 WoF 並不會靜止不動，而是邊拉著玩家邊前進，造成軌跡會有一定程度的彎曲。而這個東西，讓筆者想起來了之前有看過但沒有詳細研究[^2]的追蹤曲線 - [pursuit curve][pursuit_curve]，研究正式開始。

![spoiler: 會長醬](/assets/contents/pursuit-curve/curve-spoiler.avif)

## 正文

&emsp;&emsp;在實際狀況下，玩家是被拉著前進；但其實可以把問題看成是：玩家以等速向著 WoF 追去，且 WoF 以等速前進來讓這個問題符合 pursuit curve 的定義。更準確來說，是 [Radiodrome][radiodrome] 的定義，也就是追蹤的目標以等速前進的狀況。

&emsp;&emsp;筆者列了些基本的式子：

<p>
$$
\textbf{H}_t = v_h\ \frac{\textbf{W} - \textbf{H}}{|\textbf{W} - \textbf{H}|},\ \textbf{W} = (x_W - v_w\,t,\ y_W)
$$
</p>

其中 H 是玩家（human）；W 是 WoF； $\textbf{H}$ 是玩家的位置向量；$\textbf{W}$ 是 WoF 的位置向量；$v_i$ 就代表各自的移動速度。

&emsp;&emsp;筆者一開始是想要從這個微分方程解 time-dependent path，結果發現怎麼解都解不出來，把那條向量微分方程式換元也只能得掉一條裡面有 unit vector 的 DE，筆者還特地去問了台大物理系的朋朋，結果他也不知道要怎麼 handle 那個鬼東西 qq。

&emsp;&emsp;最後翻到 radiodrome 的 wiki page 時才發現這個東西根本沒辦法解 time-dependent，光解 x-y functional relation 的步驟就夠難了。

&emsp;&emsp;接下來筆者基本上就是先照著 wiki page 上面的解法一步步嘗試理解（噢真的有點難 owo），理解完後再用自己的符號習慣重新解了 x-y 軸翻轉的版本（因為 Terraria 的世界是橫向），最後再把解出來的結果放進 Desmos 中模擬進行結果驗證。以下是解出來的路徑結果與 Desmos 模型：

<p>
$$
x\left(y\right) = H_x + \int_{0}^{y}\sinh\left(c + V\ln\left(1 - \frac{Y}{W_y}\right)\right)\,dY \\
c = \sinh^{-1}\left(\frac{W_x - H_x}{W_y - H_y}\right),\ V = \frac{v_w}{v_h}
$$
</p>

其中 $H,\ W$ 下標 $x,\ y$ 是兩個體的初始位置（initial value）。

> 這個積分可以寫出來，但因為太長所以還是寫積分式比較漂亮 uwu。

[**Desmos 模型在這！**][desmos_version_1]

&emsp;&emsp;但解出這個 pursuit curve 的筆者並不滿足，畢竟這只是其中一個特殊狀況：目標要等速，移動方向要平行兩軸之一且只能是直線。所以筆者去找了些 paper，像是在 [Pursuit Curves and Ordinary Differential Equations][paper1] 這篇裡面就教你怎麼解 multi-pursuer 的狀況，這也是筆者在文章前面說「曾經看過」的東西，以下解釋一下。

&emsp;&emsp;筆者在高中時候曾經看過這個問題，但那時候的筆者顯然是完全不知道為什麼這個 multi-pursuer 的路徑會是 **對數螺線**，所以跑去找補習班的老師問。結果補習班的物理老師就百般刁難筆者的問題敘述方式[^3]，完全脫離了筆者問問題的本意[^4]；所以筆者就超氣，氣到直接把這個東西擺在旁邊回去乖乖學物理。

&emsp;&emsp;現今，在大一下學了工程數學中的 Laplace transform 之後的筆者剛好看得懂這篇 paper 中的解法，所以理解起來並無大礙，也算是攻克了一個長年疑問。

&emsp;&emsp;此外，筆者在翻更多資料時也發現了這個[紀載了巨多曲線資訊的網站][mathcurve]。其中關於 pursuit-curve 的介紹 & 另一篇 paper 讓筆者知道 pursuit-curve 確實不是這麼好解的東西。

> 筆者記得在 general-form 下會是一個 $\partial 2$ Non-linear DE，可以先不用嘗試求解了 owo。

&emsp;&emsp;所以，筆者又自己在 Desmos 中建了一個 Simulator of general-form pursuit curve 的模型，有興趣的人也歡迎去玩玩看！（還支持軌跡功能呦 ^~^）

[**另一個 Desmos 模型在這！**][desmos_version_2]

## 後記

在這邊特別感謝那位台大物理朋朋，被我硬塞了一堆奇怪的東東 owo。

總之，就是一個寫紀錄文寫到一半時突然想起某個氣死人的事情並對其狂酸的筆者。

那麼，就醬 uwu（心情舒爽多了。

## 註腳

[^1]: 假設玩家可以存活到被拉到 WoF 身旁，且拉的速度為等速。
[^2]: 其實有想詳細研究過，但被打斷了，詳細原因等等再說。
[^3]: 簡述一下那位物理老師的話：「你連怎麼說這個情況都會說不清楚那還解甚麼題目，但老師還是幫你看一下，**看了1分鐘多**，啊這個老師也不知道怎麼解要想一下。」直接笑死，根本不會解；不過完全不意外，蠻多筆者遇過的補習班老師在問同領域的課外問題時的回應幾乎都是「要想一下」，那時早就習慣了##。
[^4]: 我是來學習不是來聽文不對題的廢話。

[wof]: https://terraria.wiki.gg/zh/wiki/血肉墙
[pursuit_curve]: https://zh.wikipedia.org/wiki/追踪曲线
[radiodrome]: https://en.wikipedia.org/wiki/Radiodrome

[paper1]: https://www.researchgate.net/publication/298480827_Pursuit_Curves_and_Ordinary_Differential_Equations
[desmos_version_1]: https://www.desmos.com/calculator/yspi1pjjkn?lang=zh-TW
[desmos_version_2]: https://www.desmos.com/calculator/pz1rfnm4ol?lang=zh-TW
[mathcurve]: https://mathcurve.com/courbes2d.gb/poursuite/poursuite.shtml
