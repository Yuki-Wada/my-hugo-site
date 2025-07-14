---
title: 'アルゴリズム'
description: '統計的仮説検定、とくに一様再強力検定について'
date: '2025-01-03'
slug: 'alg-testing'
categories:
    - mathematical-model
    - データ構造・数理最適化
math: true
---

## アルゴリズム

#### 方針を検討

- まずは愚直に求められるアルゴリズムがないかを探す
- 次に高速化する方法を検討する
  - アルゴリズムの計算量が直感と異なるケースがあるので、適切な計算量解析が要求される場合もある

#### 探索

- 探索対象
  - bit 全探索
  - 順列全探索
- 探索順序
  - 深さ優先探索
  - 幅優先探索

#### データ構造

- コレクション
  - vector
  - stack
  - queue
  - priority queue
  - set, multiset
  - map
- グラフ
  - トポロジカルソート
    - 閉路検出を含む
  - 強連結成分分解
- 木構造
  - 最長共通祖先
- Union-Find
- Segment tree
  - Segment tree (in usual form)
  - Binary Indexed tree
  - Segment tree with lazy propagation
- **計算幾何**
- **文字列**
  - Trie 木
  - Wavelet matrix


#### アルゴリズム

- 便利関数
  - 

- ソート
- 最長増加部分列
- 剰余関連
  - 最大公約数の計算
  - 素数判定
- 最短距離計算
  - ダイクストラ
- 最小全域木
  - クラスカル法
- 最大フロー
  - 最小カット
    - Project selection problem
  - 二部マッチング
- **文字列**
  - Rolling hash
  - 最長共通接頭辞の長さ
    - Z algorithm
  - Suffix array: 接尾辞の辞書順配列
    - Longest common prefix
- 離散フーリエ変換
  - 複素数バージョン
  - 剰余バージョン


#### 実高速化・計算量削減

- 二分探索
- べき乗計算
  - 行列
  - ダブリング
- 計算結果をキャッシュ
  - 累積和
  - 動的計画法

- 座標圧縮
- データ分割
  - 平方分割
  - 半分全列挙
- 枝刈り

#### その他

- Grundy 数



## 詳細

#### Sement tree

##### Segment tree 

以下が可能となる。

- 一点更新
- 区間取得

##### Segment tree with lazy propagation

日本語では「遅延評価付き segment tree」と呼ばれる。

以下が可能となる。

- 区間更新
- 区間取得

保持する値を $ x $、区間更新時の作用を $m$ で表す。

- $ x $ には演算 $ \cdot $ 、$ m $ には演算 $ \times $ をそれぞれ monoid になるように定義する。
  - とくに $ (x, \cdot) $ と $ (m, \times) $ は結合律を満たすようにとる必要がある。
    - $ (𝑥_{1} \cdot 𝑥_{2}) \cdot 𝑥_{3} = 𝑥_{1} \cdot (𝑥_{2} \cdot 𝑥_{3})$
    - $ (𝑚_{1} \times 𝑚_{2}) \times 𝑚_{3} = 𝑚_{1} \times (𝑚_{2} \times 𝑚_{3}) $
- このとき、$ [l, r] $ の区間取得で得られる値は $ x_{l} \cdot x_{l+1} \cdots x_{r-1} \cdot x_{r} $ となる。
- $ x $ の $ m $ への作用を以下の準同型性を満たすように定義する。これを $ x @ m $ と書くことにする。
  - $ x @ m $ が $ (x, \cdot) $ 上の準同型であること: $ (𝑥_{1} \cdot 𝑥_{2} ) @ 𝑚 = (𝑥_{1} @ 𝑚) \cdot (𝑥_{2} @ 𝑚) $
  - $ (m, \times) \rightarrow \mathrm{End} ((x, \cdot)) $ の射が準同型であること: $ (𝑥 @ 𝑚_{1}) @ 𝑚_{2} ＝ 𝑥 @ (𝑚_{1} \times 𝑚_{2}) $



##### Segment tree beats

https://smijake3.hatenablog.com/entry/2019/04/28/021457