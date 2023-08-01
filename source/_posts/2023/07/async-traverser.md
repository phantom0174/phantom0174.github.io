---
title: 'Async Traverser 小介紹'
excerpt: '解放筆者寫文章的雙手！'
index_img: /assets/banner/async-traverser.avif
banner_img: /assets/banner/async-traverser.avif
tags:
  - program
  - hexo
date: 2023-07-19 22:57:41
updated: 2023-07-31 22:30:00
keywords: tool, program, python, hexo
---

<!-- Latex Protector: Remove "@" before use -->
<!--lp:skip-all-->
<!--@lp:skip-some-->

<!-- EMSP Replacer: Auto replacement of double full-width white-space with &emsp;&emsp; -->

<!-- Spoiler Replacer: Replace ||text||  with {% spoiler text %} -->
<!--sprp:skip-all-->

<!-- Footnote Reposer: Auto repositioning of all the footnotes in post -->
<!--ft:skip-all-->

{% note info %}
此文章待潤色
{% endnote %}

## 前言

&emsp;&emsp;繼上次的 `latex-protector` 之後，因為筆者又多了一些需要針對每篇文章的原始 `.md` 檔自動修正的程序；所以該脆直接把這個過程模組化，做成高階的 `async-traverser`，只需要專注在撰寫處理檔案內容的程式碼與狀態回應的部分上即可。

[**程式碼點我**][async_traverser_url]

## 正文

> 這篇文會專注在介紹 `async-traverser` 的運作原理與架構上

### 前提

&emsp;&emsp;其實這個東西筆者上學期就已經有想法了，也有寫出來一些東西；但那時的想法還不是很成熟，一直沒辦法決定底層的架構、實作方式、以及到底要實現什麼功能。考完轉學考後來寫只花了差不多 1 小時就把之前模模糊糊的實作方式確定下來了。

### 架構

&emsp;&emsp;`async-traverser` 使用 `python` 撰寫，主要由兩個類別組成：`Traverser` 與 `Response`。前者負責遍歷 `.md` 的過程；後者負責紀錄遍歷檔案過程中的狀況回報（像是成功、警告、或是錯誤，以及個別的詳細訊息）。

> 其實應該是要命名為 `Responser` 的，但筆者好懶，不想改 owo

&emsp;&emsp;`Traverser` 有以下幾個可自訂的 attributes: `name`, `target_folder_root`, `workflow_function`: `name` 即是這個 `Traverser` 負責的流程名稱；`target_folder_root` 是從舊版 `Protector` 移植過來的東西，就是需要遍歷的根資料夾相對路徑；而 `workflow_function` 是自訂的 `.md` 檔案處理函數。其中 `workflow_function` 有一定的格式，如下：

```py
def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    ...
```

### 流程

1. `Traverser` 開始計時（in ms）

2. `Traverser` 會遞迴下去搜 `target_folder_root` 底下的所有檔案，將其開好之後（mode: r+），將檔案本身與 `Response` 一起丟給 `workflow_function`，讓其可以將單一檔案的回應訊息儲存進 `Response`。

3. `workflow_function` 開始運作，對檔案內容進行自定義的修改。

4. 等到所有檔案都被遍歷完之後，停止計時；並調用 `Response` 底下的 `output_result()` 輸出美化版的錯誤訊息（各種層級的回應訊息會有不同顏色作為標示）。

有關流程的更詳細底層邏輯，請自行前往 repo 看囉～

## 後記

&emsp;&emsp;寫完這個東西後筆者就迫不及待地加進一堆神奇的功能，開始解放雙手的旅程了！目前有以下幾個小功能：

1. 全形空格替換器
2. latex-protector（移植後的版本）
3. spoiler syntax replacer
4. 腳註自動排序器
	> 近期加的一個超好用工具，省略了超多慢慢打字的時間！

之後肯定會再出現一些有趣的功能，敬請期待 owo。

那麼，就先醬。

---

Photo by [Hunter Harritt][hunter_harritt] on [Unsplash][unsplash].


[async_traverser_url]: https://github.com/phantom0174/phantom0174.github.io/tree/master/utils/traverse/async_traverser
[hunter_harritt]: https://unsplash.com/@hharritt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
[unsplash]: https://unsplash.com/photos/Ype9sdOPdYc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
