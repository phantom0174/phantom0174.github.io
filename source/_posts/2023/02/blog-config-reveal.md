---
title: 'Blog 設定公開'
excerpt: '公開我對這個 hexo fluid blog 的客製化設定'
date: 2023-02-16 17:06:00
updated: 2023-02-22 12:55:00
index_img: /assets/cover/blog-config-reveal.webp
banner_img: /assets/banner/blog-config-reveal.jpg
tags:
  - hexo
keywords: hexo, theme, fluid, 美化, 客製化, blog, canvas-nice.js, toc
---

<!--lp:skip-all-->

## 前言

筆者開始用 hexo 作為部落格生成器之後，常常遇到想要但沒有的功能；也找不到類似的 plugins，所以只能自己來弄。筆者大多都在研究數學&程式，所以做的修改大多都是有助於撰寫這方面的東西。

大部分功能的實現是依賴 hexo 本身的注入器與 fluid 主題的增強注入器[^1]。

## 正文

### 修改了什麼

以下為主要增強點：

1. 數學式渲染（KaTeX）
    > 必需的吧 OwO，沒有這個就甚麼都做不了惹。

2. 文章推薦（disqus recommendations）

3. 動態背景
    > 舊用 canvas-nest.js，現已切換到筆者自己開發的優化版套件 canvas-noice.js[^2]。

4. 自動生成 Table Of Contents
    > 筆者覺得 hexo fluid 本身的側欄 toc 不太好用

5. 客製化字體
    > 英文：PT Serif, 中文：Noto Serif TC, 程式語法：Fira Code

### 其他東西

除了以上幾點外，筆者也弄了一些小動畫、調整了一些元素的大小、優化了一些文件的載入順序、設定了一些會影響 SEO 評分的東西。總而言之，就是要讓這個部落格好看一點 \\^~^/。

### 公開的地點

請看 [這個網頁的原始碼](https://github.com/phantom0174/phantom0174.github.io)。主要為 `./scripts/` 和 `./source/css/` 底下的東西。

## 後記

網路上看很多人都有公開自己的 hexo blog 設定與客製化設定，想說等弄完基本修改之後就來公佈自己的。如果你也想要公開自己的設定（注意不要讓敏感資料外洩），可以參考這篇[教學文章](https://guiblogs.com/hexo30-23/)。

希望這篇文章可以幫助到想要客製化自己部落格的人。

那就先醬。

---

Photo by [Josh Redd](https://unsplash.com/@joshredd?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/zBtM8P2OaeA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

## 參考

[^1]: [注入器 Documentation](https://fluid-dev.github.io/hexo-fluid-docs/advance/)
[^2]: 詳情請見[此文](https://phantom0174.github.io/2023/02/introduce-canvas-noice.js/)
