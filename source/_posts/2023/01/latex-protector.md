---
title: 'LaTeX 保護者'
excerpt: '功能更加齊全的解析器套件，協助你在 hexo 上渲染輕量型 KaTeX'
date: 2023-01-28 16:38:53
updated: 2023-1-30 02:06:00
index_img: /assets/cover/latex-protector-cover.webp
banner_img: /assets/banner/latex-protector-banner.webp
tags:
    - program
    - hexo
    - mafs
---

<!--lp:skip-all-->

## 前言

上篇內容，是有關於怎麼輕量型渲染 hexo-posts 中的 LaTeX (KaTeX) 語法。在某個段落中[^1]，筆者放了一個簡易版的 `latex-protector.py` 程式碼，但這短短的程式碼顯然不具有任何語法檢查功能，跑起來效能也很差。

所以筆者用另一個邏輯重新寫了 `latex-protector` 並將其打包起來，相比舊程式有著以下 **4 大特點**：

1. 支持語法檢查
2. 可插入 **忽略部分區塊** 或 **忽略全部內容** 的語法
3. 過程快速
4. 輸出美化

## 所以說那個程式碼呢

請見 Github:
https://github.com/phantom0174/latex-protector

## 實作

### 名詞定義

先提一下奇怪的名詞

> p.s. 因為 characteristics 太長了，縮寫又會變成 `char`，所以乾脆把數學中的 `eigen` 前綴借來用 owo。

- `$$` 稱為 特徵字串（eigenstring）
- 特徵區塊（eigenblock）是由一個前導 `$$` 與後導 `$$` 封閉起來的區塊，兩兩為一對，稱為 特徵對（eigenpair）。

### 流程

整體分為5大部分，括弧中為在程式碼中用的代號。

1. 特徵化（`eigenize`）
    將 md 檔案內容讀入，並將每一行中有多少 eigenstring 記錄下來；同時將 **忽略語法** 編碼為 `-1`。
    此過程得到的東西稱為特徵資訊（`eigeninfo`）

2. 忽略自訂區塊（`ignore_eigeninfo`）
    將使用者以 **忽略語法** 包起來的區塊從 eigeninfo 中移除。
    同時檢查忽略語法有沒有成雙成對。

3. 檢查特徵語法（`check_eigen_info`）
    特徵語法有可能會出錯，像是：
    1. 同行中出現超過兩個 eigenstring
    2. 檔案中 eigenstring 的數目為奇數，也就是至少有一個 eigenpair 出問題了。

4. 檢查特徵區塊（`check_eigen_block`）
    檢查一個 eigenpair 中間是否有被 **單行eigenpair**（一行中有兩個 eigenstring）擋住。

5. 取得插入位置與標記（`get_insertion_cmd`）
    從 eigeninfo 中最後決定要在哪裡插入 `<p>`；哪裡插入 `</p>`，並將行數與要插入的字串回傳。

## 後記

總之用起來就是又快又開心 \\^~^/。

然後因為筆者程式超爛，所以有出 bug 的話請直接發 issues，有時間的話會來修。

---

Photo by [Markus Winkler](https://unsplash.com/@markuswinkler?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/3LVhSjCXRKc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

## 參考

[^1]: https://phantom0174.github.io/2023/01/lightweight_hexo_latex_rendering/#實作過程
