---
title: '文字コード'
description: '文字コード'
date: '2025-01-03'
categories: []
weight: 999
math: true
---

## 文字コードとは

「文字コード」とは、文字をコンピューターで表現する際にどのようなバイト表現にするかを定めるもので、下記の概念を持ちます。

| 用語           | 説明                                                         |
| :------------- | :----------------------------------------------------------- |
| **文字集合**   | **符号化文字集合**(CCS:Coded Character Set)、**キャラクタセット** とも呼びます。文字に番号を割り振ります。主な文字集合として **JIS X 0208** や **Unicode** があります。これらの規約では、文字に「**群・面・区・点**」の番号を割り振ります。群は 0～127、面・区・点は 0～255 の数値をとります。すべて使用すると 128×256×256×256＝2,147,483,648文字を表すことができますが、JIS X 0208 では1～94区×1～94点のみの 94×94＝8,836文字、Unicode では 0～16面×0～255区×0～255点の 17×256×256＝1,114,112文字の範囲で文字を定義しています。例えば文字の「あ」は、JIS X 0208 では「4区1点」、Unicodeでは「0面48区66点」の番号を割り振っています。 |
| **符号化方式** | **文字符号化方式**(CES:Character Encoding Scheme)、**エンコーディングルール** とも呼びます。文字集合で定義した「群・面・区・点」の番号を、どのようなバイト列に変換するかのルールを決めます。JIS X 0208 を符号化する方式としては、**ISO-2022-JP**(俗にいうJISコード)、**Shift_JIS**、**EUC** など、Unicode を符号化する方式としては、**UTF-8**, **UTF-16** などがあります。 |

## 主な文字集合と符号化方式

#### 環境依存文字

機種依存文字ともいう。狭義には JIS X 0208 の私用拡張部分に登録した文字列が異なるため、OS レベルで表示文字の対応が違う現象をさす。

![image-20240824151615346](G:\マイドライブ\writings\.images\image-20240824151615346.png)

関連用語：

#### SJIS

#### Unicode

- [サロゲートペア](https://www.tohoho-web.com/ex/charset.html#surrogates)
- [バイトオーダー](https://www.tohoho-web.com/ex/charset.html#byte-order)
- [BOM](https://www.tohoho-web.com/ex/charset.html#bom)
  byte order mark
  リトルエンディアン、ビッグエンディアン
- [合字](https://www.tohoho-web.com/ex/charset.html#ligature)
- [異体字](https://www.tohoho-web.com/ex/charset.html#variant)
- [正規化](https://www.tohoho-web.com/ex/charset.html#normalization)
- Unicode 正規化

### あ

- デバイスからの入力
- 画面上での表示

#### データ分析用の正規化

- 半角・全角
  - 英数字
  - 記号
  - スペース（タブ・改行も含む）
  - ひらがな
  - カタカナ
- 大文字・小文字
- 



----



## 並列処理・並行処理

- threading と multiprocessing
- concurrent.futures
- joblib

Python は GIL の仕様があるため、multithread を並列処理用途で利用はできない 

- 

## 非同期処理

- asyncio

eventloop
