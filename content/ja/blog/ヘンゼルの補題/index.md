---
aliases: []
author: Yuki Wada
categories:
- mathematical-model
date: '2025-01-03'
description: ヘンゼルの補題
draft: true
math: true
slug: hensel-testing
title: Newton 法からヘンゼルの補題を導出してみる
weight: 999
---

## 概要

- この記事で伝えたいこと ← ★重要★
- 記事の対象者

久しぶりに AtCoder をやってみました。自分がメインで AtCoder をやっていた時期は 2021 年ごろでそれ以降はコンテストに参加することはありませんでした。
最近では形式的べき級数を使うテクニックが増えてきているというところで、なぜこれが増えてきているのだろうかというところが気になったので調べてみました。



## そもそも形式的べき級数とは何か

多項式とは、有限個の項からなる代数式のことですが、これを無限に拡張したものを**べき級数（power series）**と呼びます。

べき級数は多項式の自然な一般化であり、直感的には「項数が無限にある多項式」と捉えることができます。ただし、通常のべき級数では収束半径という概念があり、級数が実際に値として意味を持つのは、ある範囲内に限られます。

一方で、「収束するかどうか」をまったく考慮せず、単に係数付きの無限項の多項式として記号的に扱うものが**形式的べき級数（formal power series）**です。

ここで「形式的」という言葉が使われているのは、この級数を数値的に収束するものとしてではなく、純粋に代数的な対象として扱うことを意味しています。つまり、関数として値を取るかどうかは考慮せず、項の並びとその演算規則だけを重視するのが形式的べき級数です。



適切な条件の下で、形式的べき級数は局所体と呼ばれるクラスに属する。局所体は整数論でよく使われる \\( p \\) 進数体と

形式的べき級数に追加の代数構造を付与することで Witt 環と呼ばれる数学的対象が定義でき、



## 形式的べき級数を使いたくなるタイミング

形式的べき級数を使われるのは母関数による数え上げです。

- 組合せ
- \\( k \\) 乗和公式
- 分割の数え上げ
- 多項式の剰余計算
- 母関数



#### 多項式の剰余計算







## 上記を計算するために何が必要か
- 畳み込み
- 逆数



## 本文2 ― 具体例 (example) 


## 結論 (conclusion or point)



#### 



逆元を



- 本文1 ― 詳細 (reason)
  - 解決したい課題 ← ★重要★
  - 課題の背景
  - 課題を解決する技術・手法の概要
  - 技術・手法の効果、課題がどう解決されるか
  - 留意点、デメリット

#### 形式的べき級数とは何か



