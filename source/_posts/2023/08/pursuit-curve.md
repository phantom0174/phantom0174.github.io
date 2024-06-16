---
title: '有關追蹤曲線'
excerpt: '從 Terraria 發想的小研究'
index_img: /assets/cover/pursuit-curve.avif
banner_img: /assets/banner/pursuit-curve.avif
tags:
  - mafs
  - life
  - program
date: 2023-08-27 00:00:00
updated: 2023-09-10 11:20:00
keywords: 追蹤曲線, pursuit curve, radiodrome, differential equation, euler method, rk4 method, laplace transform, terraria, wall of flesh
---

<!-- Latex Protector: Remove "@" before use -->
<!--@lp:skip-all-->
<!--@lp:skip-some-->

<!-- EMSP Replacer: Auto replacement of double full-width white-space with &emsp;&emsp; -->

<!-- Spoiler Replacer: Replace ||text||  with {% spoiler text %} -->
<!--sprp:skip-all-->

<!-- Footnote Reposer: Auto repositioning of all the footnotes in post -->
<!--@ft:skip-all-->


## 前言

&emsp;&emsp;筆者這個暑假有段時間沉迷於開放世界型遊戲（典型的報復性沉迷 uwu），其中包含了知名的 Terraria。先說個題外話：這是筆者第一次破關（打完 Moonlord），花了成噸的時間在上面，不過娛樂性相當值得 \\^~^。

{% gi 2 1-1 %}
	![Home sweet home](terraria-house.avif)
	![精神時光屋](terraria-save.avif)
{% endgi %}

&emsp;&emsp;玩過的人應該知道，Terraria 中有一個叫 [Wall Of Flesh (WoF)][wof] 的 Boss。WoF 有一種特殊的 debuff - 狂卷之舌：當你在距離牠太遠時會伸出舌頭把你拉回去。

&emsp;&emsp;筆者在玩的時候就想到，如果玩家利用魔鏡傳送回地表後馬上開始被拉回去地獄時，玩家的軌跡 **真正來說** 會長怎樣呢[^1]？因為在拉的過程中 WoF 並不會靜止不動，而是邊拉著玩家邊前進，造成軌跡會有一定程度的彎曲。而這個東西，讓筆者想起來了之前有看過但沒有詳細研究[^2]的追蹤曲線 - [pursuit curve][pursuit_curve]，研究正式開始。

![spoiler: 會長醬](curve-spoiler.avif)

## 正文

### 摸索

&emsp;&emsp;在實際狀況下，玩家是被拉著前進；但其實可以把問題看成是：玩家以等速向著 WoF 追去；WoF 以等速前進，讓這個問題符合 pursuit curve 的定義。更準確來說，是 [Radiodrome][radiodrome] 的定義，也就是追蹤的目標會以等速前進的狀況。

&emsp;&emsp;筆者列了些基本的式子：

<p>
$$
\textbf{H}_t = v_h\ \frac{\textbf{W} - \textbf{H}}{|\textbf{W} - \textbf{H}|},\ \textbf{W} = (x_W - v_w\,t,\ y_W)
$$
</p>

其中 H 是玩家（human）；W 是 WoF； $\textbf{H}$ 是玩家的位置向量；$\textbf{W}$ 是 WoF 的位置向量；$v_i$ 就代表各自的移動速度。

&emsp;&emsp;筆者一開始想要從這個微分方程解 time-dependent path，結果發現怎麼解都解不出來，把那條向量微分方程式換元也只能得到一條裡面有 unit vector 的 DE。筆者還特地去問了台大物理系的朋朋，結果他也不知道要怎麼處理那個鬼東西 qq。

&emsp;&emsp;最後翻到 radiodrome 的 wiki page 時才發現這個東西根本沒辦法解 time-dependent，光解 x-y functional relation 的步驟就夠難了。

&emsp;&emsp;接下來，筆者基本上就是先照著 wiki page 上面的解法一步步嘗試理解 {% spoiler 真的有點難 owo %}，理解完後再用自己的符號習慣重新解了 x-y 軸翻轉後的版本（因為 Terraria 的世界是橫向），最後再把解出來的結果放進 Desmos 中模擬進行結果驗證。以下是解出來的路徑結果與 [Desmos 模型][desmos_version_1]：

<p>
$$
x\left(y\right) = H_x + \int_{0}^{y}\sinh\left(c + V\ln\left(1 - \frac{Y}{W_y}\right)\right)\,dY \\
c = \sinh^{-1}\left(\frac{W_x - H_x}{W_y - H_y}\right),\ V = \frac{v_w}{v_h}
$$
</p>

其中 $H,\ W$ 下標 $x,\ y$ 是兩個體的初始位置（initial value）。

> 這個積分其實寫得出封閉形式，但因為有點小長所以還是寫積分式比較漂亮 uwu。

---

### 延伸

&emsp;&emsp;光解出這個 pursuit curve 的筆者並不滿足，畢竟這只是其中一個特殊狀況：目標要等速，移動方向要平行兩軸之一且只能是直線。所以筆者去找了些 paper，像是在 [Pursuit Curves and Ordinary Differential Equations][paper1] 這篇裡面就教你怎麼解 multi-pursuer 的狀況，這也是筆者在文章前面說「曾經看過」的東西，在下一段**小提**一下。

&emsp;&emsp;筆者在高中時候曾經看過 multi-pursuer 的問題，但那時候的筆者顯然是完全不知道為什麼這個問題的路徑會是 **對數螺線**，所以跑去問補習班的物理老師。結果那位老師就百般刁難筆者的問題敘述方式[^3]，完全脫離了筆者問問題的本意[^4]；所以筆者就氣到直接把這個東西擺在旁邊，回去乖乖學物理。

&emsp;&emsp;現今，在大一下學了工程數學中的 Laplace transform 之後的筆者剛好看得懂這篇 paper 中的解法，所以理解起來並無大礙，也算是攻克了一個長年疑問。

---

### 結尾

&emsp;&emsp;此外，筆者在翻更多資料時也發現了這個[紀載了巨多曲線資訊的網站][mathcurve]。其中關於 pursuit-curve 的介紹 & 另一篇 paper 讓筆者知道 pursuit-curve 確實不是這麼好解的東西。

> 筆者記得在 general-form 下會是一個 $\partial_2$ Non-linear DE，可以先不用嘗試求解了 owo。

&emsp;&emsp;所以，筆者又自己在 Desmos 中建了一個 [Simulator of general-form pursuit curve 的模型][desmos_version_2]，有興趣的人也歡迎去玩玩看！（還支持軌跡功能呦 ^~^）

---

### 2023/9/9 更新：模擬方式

&emsp;&emsp;筆者一開始進行模擬時（也就是用數值法求解 DE）是用 Euler method，今天在看這個影片時候學到了名為 **RK4** 的新方法！

<!-- Building a Physics Engine with C++ and Simulating Machines -->
{% youtube TtgS-b191V0 %}

普通的 Euler method 在逼近時只用了一步，但 RK4 代表在逼近時前前後後用了總共 4 步，最後再取平均來獲得更精確的估計值。而 total accumulated error 的複雜度會是 $O(\text{dt}^p)$，其中 $p$ 為更新步數，$\text{dt}$ 為更新時間差。

所以 RK4 會比 Euler method 還要再更精確許多，如上影片中 3:32 左右講述的：使用 Euler method 要求出不發散的解需要以 600KHz 進行模擬；但使用 RK4 只需要 300Hz 就可得出穩定解。

筆者去找了些 RK4 的教學影片後，也嘗試利用看看在暑假學了一些的 Unity 去寫了 pursuit-curve 的模擬器，並在裡面實現 Vector DE 版本的 RK4 更新，如下：

{% fold info @Unity code %}

```csharp
void RK4UpdatePos()
{
    Vector3 k1 = dP(targetClass.T_total, trans.position),
        k2 = dP(targetClass.T_total + dt / 2, trans.position + dt / 2 * k1),
        k3 = dP(targetClass.T_total + dt / 2, trans.position + dt / 2 * k2),
        k4 = dP(targetClass.T_total + dt, trans.position + dt * k3);

    Vector3 avr = (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    trans.position += dt * avr;
}

Vector3 dP(float t, Vector3 p)
{
    return moveSpeed * (targetClass.PathPos(t) - p).normalized;
}
```

{% endfold %}

也放上一張模擬的結果owo：

![$T(t) = (\cos(t), \cos(t)^3)$](simu0.avif)

總地來說，Desmos 和 Unity 在效能上真的差超多；但或許是因為追蹤曲線的 DE 過於簡單，Euler & RK4 之間的模擬只有在 Target path 非常極端的狀況下才會有微小差異。

反正學到新東西就是爽爽的uwu。

---

### 2023/9/10 更新：鬼抓人模型模擬

&emsp;&emsp;繼昨天的模擬之後，筆者在晚上時突然想到了可以把鬼抓人的行為描述成微分方程，如下：

<p>
$$
\left\{\begin{matrix}
    \begin{align*}
        \frac{dP}{dt} &= V_P \cdot \Lambda (T-P)\\
        \frac{dT}{dt} &= V_T \cdot \Lambda \left[\Lambda (T-P)(1-\alpha)+R_{\theta}\,\hat{\tau}(t)\alpha \right]
    \end{align*}
\end{matrix}\right.
$$
</p>

其中 $P$ 擔任鬼的角色；$T$ 就是人。$\Lambda(v)$ 代表 $\hat{v}$ {% spoiler 因為對於很長的 $v$ 來說只有個小 hat 太不明顯了，所以寫成 function 型態 %}。

也順便解釋一下各個式子的意義：$P_t$ 沒甚麼好講，跟 pursuit curve 的狀況一樣；$T_t$ 的意思是：人除了會往反方向逃離（$\Lambda (T-P)$），同時也會受想要逃離鬼的心理作祟，亦或者是受場地大小限制而拐彎（$R_{\theta}\,\hat{\tau}(t)$）。而 $\alpha$ 就是作為這兩者心理因素的加權平均值，最後再將向量合 normalize 之後乘上 $V_T$ 即為人的逃跑微分方程。

其中 $R_{\theta}$ 是用來修正坐標系的旋轉矩陣，$\theta$ 是以下函數：

<p>
$$
\theta=\text{atan2}\left(T-P\right)
$$
</p>

但要用 RK4 解這組向量微分方程組的話，就必須要把這個方程組合併，並鑲入 $\mathbb{R}^5$ 中（在 Unity 裡實作時其實是 $\mathbb{R}^7$），如下：

<p>
$$
\begin{align*}
    S &= (P,T)\\
    S_t &= (P_t,T_t)\\
        &= (f_1(t,P,T),\ f_2(t,P,T))\\
        &= (f_1(t,S),\ f_2(t,S))
\end{align*}
$$
</p>

$S$ 代表 System，描述整個系統。而有了這個複合向量之後，我們就可以用 RK4 去模擬這個問題了！以下為核心 code：

{% fold info @Unity code %}

```csharp
private void UpdatePos()
{
    if (pTrans == null || tTrans == null) return;

    Sys delta = RK4DESolver(new Sys(pTrans.position, tTrans.position));
    pTrans.position += delta.P;
    tTrans.position += delta.T;
}

private Sys RK4DESolver(Sys s)
{
    Sys k1 = dS(tTotal, s),
        k2 = dS(tTotal + dt / 2, s + k1 * (dt / 2)),
        k3 = dS(tTotal + dt / 2, s + k2 * (dt / 2)),
        k4 = dS(tTotal + dt, s + k3 * dt);

    Sys avr = (k1 + (2 * k2) + (2 * k3) + k4) / 6;

    return avr * dt;
}

private Sys dS(float t, Sys s)
{
    Vector3 dirVec = (s.T - s.P).normalized;
    return new Sys(
        vP * dirVec,
        vT * (
            dirVec * (1-alpha) + XYRotation(tiltVector(t), Mathf.Atan2(dirVec.y, dirVec.x)) * alpha
        ).normalized
    );
}
```

{% endfold %}

> 其中 Sys 實作是利用 struct + operator overload。

說了一堆奇怪的數學術語，是時候來看一些模擬圖了！

> 參數使用：

<p>
$$
\begin{align*}
    A(k) &= \frac{k\pi}{180}\\
    \hat{\tau}(t,k) &= \left(\cos(x), \sin(x)\right),\ x = \cos(t)A(k)
\end{align*}
$$
</p>

$A(k)$ 是角度範圍修正量。

> 紅色是人，藍色是鬼

![$\hat{\tau}(t, 45)$](simu45.avif)
![$\hat{\tau}(t, 30)$](simu30.avif)

人稍微跑慢一點就變醬了qq：

![$V_T/V_P = 0.9$](too_slow.avif)

從上面模擬結果可知：跑的時候不要亂擺來擺去，跑直線最好 owo。

<!-- Simulation of Tag game model -->
{% youtube pIOTvZjVlv0 %}

## 後記

在這邊特別感謝那位台大物理朋朋，被我硬塞了一堆奇怪的東東 owo。
> 也要感謝新室友，也被我塞了一堆奇怪的東東 uwu。

總之，就是一個寫紀錄文寫到一半時突然想起某個氣死人的事情並對其狂酸的筆者。

那麼，就醬 uwu（心情舒爽多了。

## 註腳

[^1]: 假設玩家可以存活到被拉到 WoF 身旁，且拉的速度為等速。
[^2]: 其實有想詳細研究過，但被打斷了，詳細原因等等再說。
[^3]: 簡述一下那位物理老師的話：「你連怎麼說這個情況都會說不清楚那還解甚麼題目，但老師還是幫你看一下，**看了 1 分鐘多**，啊這個老師也不知道怎麼解要想一下。」直接笑死，根本不會解；不過完全不意外，蠻多筆者遇過的補習班老師在問同領域的課外問題時的回應幾乎都是「要想一下」，那時早就習慣了##。
[^4]: 我是來學習不是來聽文不對題的廢話。

[wof]: https://terraria.wiki.gg/zh/wiki/血肉墙
[pursuit_curve]: https://zh.wikipedia.org/wiki/追踪曲线
[radiodrome]: https://en.wikipedia.org/wiki/Radiodrome

[paper1]: https://www.researchgate.net/publication/298480827_Pursuit_Curves_and_Ordinary_Differential_Equations
[desmos_version_1]: https://www.desmos.com/calculator/yspi1pjjkn?lang=zh-TW
[desmos_version_2]: https://www.desmos.com/calculator/pz1rfnm4ol?lang=zh-TW
[mathcurve]: https://mathcurve.com/courbes2d.gb/poursuite/poursuite.shtml
