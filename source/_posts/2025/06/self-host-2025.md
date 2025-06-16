---
title: 'self-hosting 初體驗'
excerpt: '也是讓我玩上這東西了捏'
index_img: /assets/cover/self-host-2025.avif
banner_img: /assets/banner/self-host-2025.avif
tags:
  - program
  - life
hide: false
date: 2025-06-15 12:00:00
keywords:
---

<!-- Latex Protector: Remove "@" before use -->
<!-- lp:skip-all -->
<!--@lp:skip-some-->

<!-- EMSP Replacer: Auto replacement of double full-width white-space with &emsp;&emsp; -->

<!-- Spoiler Replacer: Replace ||text||  with {% spoiler text %} -->
<!--@sprp:skip-all-->

<!-- Footnote Reposer: Auto repositioning of all the footnotes in post -->
<!--@ft:skip-all-->

## 小小前言

呼－許久沒有寫文了。上次的文還停留在開學時期的日本旅遊文，而如今已逼近學期終末之時。

與前幾學期相同，這中間也是發生了種種大小事，一直讓我[^1]忙到了現在才真正能在心中放下各科大石，悠悠哉哉地來寫文。這些東西就等再晚點有空的時候來細說吧。

## 正文

### Server 的誕生

要從哪談起 Self-hosting 這東西呢？從字面上來說就是「在私人伺服器跑網路服務，取代大公司提供的網路服務。」[^2]

私人伺服器又從何而來呢？完全就是因為某天心血來潮，覺得高中時期用的舊筆電放在倉庫生灰太浪費，就把它挖出來了嘿。對這台螢幕背板要裂不裂、少掉一個 `S` 鍵鍵帽的 `Lenovo T450s`，用酒精擦掉上面陳年的灰塵和霉斑後，一台省電又有著健康 `SSD` 的小 server 就誕生啦！

### 要跑甚麼呢

最先想到的，是之前逛著 Github 時恰好喵到的 [Immich][immich_link]：一個生態相對成熟、功能齊全的自架相簿服務。

> 在此點名開發到一半又跑路的 SpaceDrive，為什麼我會說**又**呢？

在 Google Photos 於 3, 4 年前取消了免費備份功能後的這幾年間，一直沒有找到可以替代它的方案。`Synology Photos` 在只用幾個禮拜後也能客觀地感受到其功能相當之爛：縮圖載入效率低、有問題的功能比比皆是、甚至要額外裝 plugin 才能產生縮圖，完全用不下去。這正好是 Immich 大顯身手的機會！

囫圇吞棗地啃完 `docker` & `docker compose` 相關教學，還有幾部 YouTube 上的自架教學影片後，這小小的 Immich 也是成功地跑起來了。

但過程中的坑仍然沒少踩，其中一個坑是在處裡分離式 `library` 時踩到的。由於儲存貴重資料其實不太適合存在要壞就全壞給你看的 SSD 上；壞也通常只會壞單一磁區的 HDD 比較勝任這份工作。因此花了大把時間想把 `library` 部分的資料夾用 SMB 服務連到家中的 `Synology DS224+` 上，結果折騰了老半天還是沒弄成功，就先擱著了。

大力出奇蹟，既然早晚都要移到 NAS，最後乾脆把整個 Immich Docker instance 丟到 `DS224+` 上跑了，這台 `T450s` 後來就拿來跑別的服務。

### 一些小改動

跑起 Immich 之後，才發現這東西真的是太好用了，順勢就想把它當作國中群出遊時的雲端照片儲存空間。在這之前，我們每次出遊的照片都是統一上傳到 Line 相簿，但 Line 上傳的照片品質又受到很多因素影響，我給它的評價是能不用就不要用，寧願傳到 Google Drive 上也不要去用（哼。

但問題馬上就迎面而來了：當時是用 Zerotier 內網穿透來辦到從外網存取內網服務的行為，如果要公開的話就要弄 reverse proxy，但去哪找這個服務呢？經過一番調查後，我找到了 Cloudflared Tunnel。這也是 Immich 的 Discord 討論區所建議的其中一種 expose 方式。

因為 Cloudflared Tunnel 需要自備域名，特地為此去 `Namecheap` 買了個自己的專屬域名 `phantom0174.online`。當時的購買價格換算過後只要 35 NTD，超便宜的！

這域名目前是供這個 blog 與一些需要公開的 self-host 服務用。屬實是為了一碟醋包了一盤餃子 owo。

> 再過將近 2 個禮拜就是下一次出團了，不知道到時候用起來如何捏。

### 很喜歡的點

Immich 這個服務有幾個我很喜歡的地方：

- 乾淨簡潔且現代化的介面
- 高度的客製化設定
- 智慧搜尋功能
- 地圖功能

前兩個就由讀者來日有機會自行體驗。智慧搜尋如其字面意思，可以通過搜尋圖片描述來找到相關的照片。iOS 貌似有同樣的功能，不過除了平板之外都是 Android 用戶的我沒體驗過。平常不會用來拍照片的 iPad 就算有這功能好像也用不太到捏。

像是－如果想找到上次國中團去綠島吃的藍柑橘冰，只要打上「藍色刨冰」就會顯示相關結果了。

![左上角的那一張](blue_ice.avif)

這個功能底層是用 CLIP model 進行實現，會在上傳照片時順便交給模型分析（特徵崁入），之後就可以依照描述在向量空間中搜尋。CLIP model 還有分英文限定與多語言版本。

我用的 model 是 `ViT-L-16-SigLIP2-256__webli`，用起來比快速且低運算需求的 `XLM-Roberta-Large-Vit-B-16Plus` 來得好，因為後者簡直就是把黑色/大部分黑色的圖片當成 wildcard character 在處理，每次搜尋結果中肯定少不了它們，相當之煩。

而 `DS224+` 想當然爾如果要長年跑這個模型肯定吃不消，所以就把這部分丟到了 `T450s` 上跑，平衡一下 loading。具體而言是跑 `immich-remote-ml`，也就是前面提到的「跑別的服務」。我還測試了在最新的 Mac Mini M4 上跑這個模型的效率，簡直就是天差地遠，每秒可處裡的照片張數可以差到 10 幾張之多。不愧是最新的 M4 晶片。

可惜這台 Mac Mini 終究還是要為其他東西服務，沒辦法長期當作 server，最終還是用回了舊舊的 `T450s`。

而地圖功能就會直接在世界地圖上顯示哪些照片是在哪個地方拍的，讓獲取回憶的渠道除時間外又多了地區上的方式。

> 希望有了這幾個功能之後可以多多紀錄點生活，不要一直窩在宿舍正常發揮宅宅本領。

### Barries 網的茁壯

小小提個：自從這台 `T450s` 與 Mac Mini 新加入後，原本只有 2 台裝置的 Zerotier 網路（barries 網）已經成長成如今的狀態了，開心開心 uwu。

![](barries.avif)

## 新服務加入

### Jellyfin

某個正值期末考周的周末晚上，突然手癢想要在 NAS 上跑更多服務，於是就選中了 `Jellyfin`，一個多媒體串流服務。

架這個服務的主要原因之一，是某天突然萌生的懷舊感推動著我找回了六年前正值國二時期聽的音樂。大部分，非常意外地，在 Spotify 上都找得到；反手就存進了歌單之中。其餘是只存在於 YouTube 上的稀有生物，所以要想辦法找個地方存放它們。

若當今要再用國中那種把音檔全放在 SD Card 裡再放進隨身錄音筆聽的方法未免也太過時了，所以當然是要把音檔全部存到 NAS，再用 Jellyfin 的 web 或是 mobile client 收聽。再次感嘆時代差異吶。

> 推薦可以修點著作權法，從各方面來說都很有用的。

> 順帶一提，著作權法成績順利地拿了個班上第一 uwu。

### Minecraft server

因某 Wo 老朋友在學期尾聲，一個我仍處於水生火熱的時間點，提議了想玩 Minecraft 一事。直到上禮拜終於從最後一個報告中解脫後，便想到了為何不在這台大部分時間仍處於低負載狀態的 `T450s` 上架個 Minecraft 伺服器呢 owo？

在經過了幾番調適後，簡單易架設的 MC server 就順利地開始跑在 `T450s` 上了，真是多虧了之前的架設經驗。目前幾乎每天都狂玩，前幾天甚至出現了一天猛玩 8 小時的情形，簡直就在重現兩年前的 Terraria 事蹟。目前伺服器內時間已經過了快半年了，不知道會不會有新朋朋加入呢？

## 後記

雖然目前老老的 `T450s` 跑 MC server 在生成 chunks 的時候 CPU 使用率還是會飆到 100%，且處理大量機器學習的部分也相當慢；不過現在有了 homelab 後，總算可以辦到之前做不到的許多事了，相當方便吶。在玩 docker 的過程中也間接地幫助了這學期的專案開發。

最後面的 MC server 也是無意中的又一個新結果，真是無心插柳柳橙汁。

那就，先醬 owob。

---

<!-- ## 參考 -->

[^1]: 把自稱從「筆者」換成這個試試看，第一人稱感++;
[^2]: https://ivonblog.com/posts/why-should-you-self-host/

[immich_link]: https://immich.app
