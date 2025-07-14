---
title: '推定量の性質'
description: '推定量の性質'
date: '2025-01-03'
categories: []
weight: 20
math: true
---

## 推定量

数理モデルにはハイパーパラメータが必要です。

推定量が真のパラメータに近いことを表す性質として以下の二つがあります。

- 不偏性
- 一致性

推定量が不偏性を持つ場合に関する性質

- 一様最小分散不偏推定量 = 有効性

～～～～

代表的な推定量として以下が挙げられます。

- 標本平均
- 標本分散・不変分散
- 最尤推定量

## 統計量の性質

- 十分性



## バイアスバリアンス分解

$ T (X) $ を $ \theta $ の推定量とする。このとき、

推定量の良さを計算するために、推定量と真値の二乗誤差をとると、
$$
\begin{align}
& \mathbb{E} \left( \left( T(X) - \theta) \right)^{2} \right) \\
= & \mathbb{E} \left( \left( T(X) - \mathbb{E}(T(X))
+ \mathbb{E}(T(X)) - \theta \right)^{2} \right) \\
= & \mathbb{E} \left( \left( T(X) - \mathbb{E}(T(X)) \right)^{2}
+ \left(\mathbb{E}(T(X)) - \theta \right)^{2}
+ 2 \left( T(X) -\mathbb{E}(T(X) ) \right) \left( \mathbb{E} (T(X)) - \theta \right) \right) \\
= & \underbrace{\mathbb{E} \left( \left( T(X) - \mathbb{E}(T(X)) \right)^{2} \right)}_{variance}
+ \underbrace{\left(\mathbb{E}(T(X)) - \theta \right)^{2}}_{bias^{2}}
\end{align}
$$
variance は推定量の値自体がどの程度ばらつきがあるかを、bias は推定量の平均値が真値とどの程度ずれているかを表している。

とはいえ、どっちを重視するべきかと言われると難しいところもあるし、基本的に $ T(X) $ は実際のデータから 1 つしか計算できないため、

## 