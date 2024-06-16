---
title: '進競程大觀園'
excerpt: '紀錄一下人生第一次認真打的競程趣味賽'
index_img: /assets/cover/my-first-cpp.avif
banner_img: /assets/banner/my-first-cpp.avif
tags:
  - program
  - life
date: 2023-09-24 00:00:00
updated: 2023-09-24 14:00:00
keywords: 清大, nthu, 競程, competitive programming
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

> 欸不是為什麼換臉後看起來那麼醜呀qq

&emsp;&emsp;雖然筆者曾經在[以前的文章中][hate_cpp]表明自己不太喜歡競程（以下簡稱 CPP），而這次比下來的結果也大多是如此，但因為是人生中第一次認真打的比賽，也學到了一些咚咚，也有跟室友合作解決了一些瓶頸，所以還是來記錄一下 uwu。

## 正文

&emsp;&emsp;先打劑強心針：筆者上次碰 CPP 是高二，而且也是去當個花瓶，至今都還沒真正學過 CPP。所以如果某位 CPP 大佬路過看到快要吐血，還請見諒 owo。

&emsp;&emsp;筆者進 NTHU CS 後發現系上竟然有像資訊社的社團－NTHU TS（[NTHU Tech Society][nthuts]），而且社費也很便宜（高中時的快 $1/3$），所以馬上就選擇加進去惹 uwu。而因為筆者覺得自己現在最缺乏的是資安相關咚咚，對它初次印象也比 CPP 好，所以之後就先進資安小組從 0 開始學學看。

&emsp;&emsp;之所以會參加這次 `NTHUTS 競程組入組考` 是因為在期初社員大會時看到介紹；而室友原本也是想要進 CPP 組，所以問我要不要也來寫寫看。筆者想說碰一下應該不會有問題，反正頂多也是寫了前一兩題就放棄 ~~後來證明大錯特錯~~，所以就去寫寫看了。

> 這次考試規則有明寫可以討論，只要不抄 code 就好了

### p1

&emsp;&emsp;是個簡單版的 1A2B，應該是沒問題。

{% fold success @AC Code %}

```cpp
#include <iostream>

using namespace std;

#define SIZE 4

int main() {
    int a[SIZE], b[SIZE];

    for (int i = 0; i < 4; i++) cin >> a[i];
    for (int i = 0; i < 4; i++) cin >> b[i];

    int A = 0, B = 0;

    for (int i = 0; i < 4; i++) {
        if (a[i] == b[i]) A++;
        else {
            for (int j = 0; j < 4; j++) {
                if (i == j) continue;
                if (a[i] != b[j]) continue;
                
                B++;
                break;
            }
        }
    }

    cout << A << "A" << B << "B" << endl;
}
```

{% endfold %}


### p2

&emsp;&emsp;筆者一開始就把這題想太難了，直接把黑白灰編碼成 `1, -1, 0` 然後開始用數學的角度來看，事後發現其實只要把灰視為黑白都是就好了。到這邊心情已經`--`。

{% fold success @AC Code %}

```cpp
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M, N;
    cin >> M >> N;

    char c;
    int wseq = 0, bseq = 0;
    bool null;
    for (int i = 0; i < M; i++) {
        bool wfound = 0, bfound = 0;
        for (int j = 0; j < N; j++) {
            cin >> c;

            if (c == 'W' || c == 'G') wfound = 1;
            if (c == 'B' || c == 'G') bfound = 1;
            null = (c == '.');

            if (wfound && (c == 'B' || null)) {
                wfound = 0;
                wseq++;
            }

            if (bfound && (c == 'W' || null)) {
                bfound = 0;
                bseq++;
            }
        }
        if (wfound) wseq++;
        if (bfound) bseq++;
    }

    cout << wseq << " " << bseq;
}
```

{% endfold %}

### p3

&emsp;&emsp;這題筆者心態完全炸掉，起初寫了個 `3` 維 dp，果不其然 TLE。後來隔了一天多才抓到可能的降維方式重點，但全觀來看還是沒對。後來是室友直接教筆者這題的 2 維 dp 要怎麼分才過（筆者自己的 2 維 dp 定義爛了，所以做不出來）。室友自己是寫了個 1 維 dp，簡直是鬼，筆者到現在都還沒去想那個 1 維 dp 要怎麼定義。

{% fold success @AC Code %}

```cpp
#include <iostream>

#define MOD (int)(1e9 + 7)
#define size 3000 + 1

using namespace std;

int S, M;  // sum & max

int dp[size][size];

int run_dp(int m, int n) {
    if (m < 0) return 0;
    if (m < n) return run_dp(m, m);

    if (dp[m][n] == -1) {
        dp[m][n] = ((run_dp(m - n, n) % MOD) + (run_dp(m, n - 1) % MOD)) % MOD;
    }
    return dp[m][n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> S >> M;

    for (int i = 0; i <= S; i++) {
        for (int j = 0; j <= M; j++) {
            dp[i][j] = -1;
        }
    }

    dp[0][0] = 1;
    for (int i = 1; i <= S; i++) dp[i][0] = 0;

    cout << run_dp(S, M) << "\n";
}
```

{% endfold %}

### p4 part.1

&emsp;&emsp;筆者一開始寫了個 $O(N^2)$ 的演算法，完全 TLE 毫不意外（因為測資會到 $10^6$）。但暫時沒想到這題優化方式，先到下一題。

### p5

&emsp;&emsp;這題筆者終於是用自己想出來的演算法解掉了，但前前後後想了至少 2 天。起初是挑前 $k$ 大的數丟到後面，錯；再來是在一定區間內挑前 $k$ 大的數丟到後面，幾乎對了（但關鍵想法還是錯的）；再來是優化找區間的方式，還是錯。到這邊筆者其實心情還是沒有很差，有一部分可能是因為筆者比較喜歡這題，做起來不會很躁 owo。

&emsp;&emsp;最後想出來正確演算法時，是筆者在凌晨 1. 實作完上面最後一個版本但還是錯後就跑去準備睡覺時。如果區間搜尋已經優化了麼多次，那挑選的方式肯定還是有問題，所以就直接在腦中把問題模擬成 Minecraft 情境開始想像，把問題轉成 「如何讓山的正面看起來最為平緩」。

&emsp;&emsp;後來筆者才想到重點：一定要極力避免把後面有大數字的小數字移掉，否則數字整體一定會變大。所以筆者最後就想到了**空置域演算法**[^1]。只要把過程想像成在爬山，並且遇到下坡時，就回頭把任何高於目前這步地勢還要高的山移掉，直到遇到相同高度的土塊停下，再回到原本位置繼續下山/爬山。這可以確保以爬山者為中心的左區間永遠會是非遞減數列。在往回走的時候，也可以把原本用來存大數的 array 裡面用負數標示移走山體之後造成的空隙會有多長，把複雜度從 $O(k^2)$ 降到 $O(k\log k)$。這個新的演算法也不用額外的 $O(N\log N)$ 時間 & $O(N)$ 空間來算什麼奇怪的區間了，非常直覺，應該才是正常好的演算法會有的樣子 uwu。

&emsp;&emsp;筆者在凌晨 2. 確定想法後才去睡（而且隔天是**早八**，**非常刺激**）。明天一早起來看室友還沒想出來，就把這個想法告訴室友；我們當天下午就開始實作這個演算法。結果室友 AC 了，筆者還因為實作能力爛掉導致程式也跟著爛掉，後來發現是有 legacy code 沒刪掉還有記憶體邊界覆寫問題導致檢查失敗的鍋，順利 AC。

> 寫出這題的成就感比前幾題大多了，但實作不出來的感覺還是很躁 ##。

{% fold success @AC Code %}

```cpp
#include <bits/stdc++.h>

#define MAX (int)(1e5 + 1)

using namespace std;

short n[MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    scanf("%d", &T);

    while (T--) {
        char c;
        int cur_pos = 0;
        queue<int> desc;
        while (true) {
            c = getchar();

            if (c == ' ')
                break;
            else if (c == '\n')
                continue;

            n[cur_pos] = c - 48;
            if (cur_pos > 0 && n[cur_pos - 1] > n[cur_pos])
                desc.push(cur_pos);

            cur_pos++;
        }
        desc.push(cur_pos);
        n[cur_pos] = 10;

        int k;  // ops can do
        scanf("%d", &k);
        k = min(cur_pos, k);

        int sel[10] = { 0 };

        int l, r;
        while (!desc.empty() && k) {
            r = desc.front();
            desc.pop();

            for (l = r - 1; l >= 0; l--) {
                if (n[l] < 0) {  // hop across gaps
                    l += n[l];
                    if (l < 0) break;
                }
                if (n[l] <= n[r]) break;

                sel[n[l]]++;

                if (n[l] < n[cur_pos])
                    n[cur_pos] = n[l];

                n[l] = -1;
                if (!(--k)) break;
            }
            // indicates gap width
            if (l != r - 1) n[r - 1] = l - (r - 1);
        }

        for (int i = 0; i < cur_pos; i++) {
            if (n[i] > 0) printf("%d", n[i]);
        }

        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < sel[i]; j++) printf("%d", i);
        }
        printf("\n");
    }
}

```

{% endfold %}

### p4 part.2

&emsp;&emsp;筆者寫完 p5 的隔天才來想這題，但用錯了想法，只想到一個更爛的 $O(N^2\log N)$ 的演算法。雖然感覺可以用線段樹做，但因為筆者完全沒能力用它所以就先算了。後來室友也跟筆者說了可能的另外一個想法：把能攻擊的 ll 和沒辦法攻擊的 ll 分開看，直接把複雜度壓到 $O(N\log N)$。筆者想了一下之後把其中一些步驟優化變成線性複雜度，但整體來說還是讚讚的 $O(N\log N)$。順利 AC。

&emsp;&emsp;唯獨筆者室友那邊 p4 還是 TLE，後來筆者發現只是 I/O 優化的問題，傳給他筆者之前看 CPP 朋友常用的兩行神奇程式碼就過了，他超氣 w。

{% fold success @AC Code %}

```cpp
#include <bits/stdc++.h>

#define MAX (int)(1e6 + 1)
#define pii pair<int, int>

using namespace std;

class Compare {
   public:
    bool operator()(pii a, pii b) const { return a.first < b.first; }
};

pii ll_waiting[MAX];
priority_queue<pii, vector<pii>, Compare> mana;

bool cmp_courage(pii a, pii b) {
    return a.second > b.second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    int m, c;
    for (int i = 0; i < N; i++) {
        cin >> m >> c;
        ll_waiting[i] = { m, c };
    }
    sort(ll_waiting, ll_waiting + N, cmp_courage);

    int avail_pos = 0, ll_counter = 0;
    while (M > 0) {
        while (avail_pos < N && ll_waiting[avail_pos].second >= M) {
            mana.push(ll_waiting[avail_pos]);
            avail_pos++;
        }

        if (mana.empty()) break;  // no ll avail

        M -= mana.top().first;
        mana.pop();
        ll_counter++;
    }

    if (M > 0)
        cout << -1;
    else
        cout << ll_counter;
}
```

{% endfold %}

## 後記

&emsp;&emsp;總之，筆者人生第一次 5 題都解出來了[^2]，在這邊大感謝室友 & TW54，被我問了一堆問題。反正筆者最後還是會去資安小組，這次的 CPP 小旅程也差不多就到這邊 uwu。

那麼，就醬。

![](fin.avif)

## 參考
[^1]: 沒錯，筆者甚至有閒情逸致幫演算法取名稱。
[^2]: 雖然前前後後花了五天多，這顯然不是正常上機 CPP 的時間。

[hate_cpp]: https://phantom0174.github.io/2023/06/origin/#fn:15
[nthuts]: https://taplink.cc/nthuts
