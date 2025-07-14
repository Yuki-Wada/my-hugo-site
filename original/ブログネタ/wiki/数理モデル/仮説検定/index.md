---
title: '仮説検定'
description: '統計的仮説検定、とくに一様再強力検定について'
date: '2025-01-03'
slug: '/hypothesis-testing'
categories:
    - mathematical-model
weight: 50
math: true
---



## 仮説検定の手順

#### 実際に仮説検定を実施するまでの設定

1. 確率モデルを設定する。
2. 帰無仮説 \\( H _ {0} \\) と対立仮説 \\( H _ {1} \\) を設定する。
3. 検定統計量を設定する。
4. 検定統計量に対して帰無仮説 \\( H _ {0} \\) の棄却域を設定する。

上記の問題設定に基づいて、実際にデータを取得する。取得したデータから検定統計量を計算し、帰無仮説 \\( H _ {0} \\) が棄却（= 対立仮説 \\( H _ {1} \\) ）できるかを判定する。





## 仮説検定の用語

- 帰無仮説（データ (実現値) から否定しようとする仮説, あるいは, 誤って正しいと判定した場合の損害が大きい仮説）、対立仮説（帰無仮説が正しくないと判定される場合に採用される仮説）、帰無仮説と対立仮説（確率モデルのパラメータを \\( \Theta := \\) に限定していることに注意する。）
- 単純仮説（仮説が成り立つパラメータがただひとつであるような仮説）、複合仮説（仮説が成り立つパラメータが複数あるような仮説）帰無仮説： データ (実現値) から否定しようとする仮説, あるいは, 誤って正しいと判定した場合の損害が大きい仮説.
- 棄却： 仮説を正しくないと判定すること
- 第一種の過誤、第二種の過誤





## 主張（一様最強力検定が存在すること）

「確率モデルが単調尤度比を持ち」、「帰無仮説:  \\( \theta = \theta _ {0} \\)、対立仮説: \\( \theta > \theta _ {0} \\)」であるときに一様最強力検定が存在するという以下の主張を示そう。



**Theorem**

確率モデルが単調尤度比を持つとし、\\( \alpha \\) を \\( 0 < \alpha < 1 \\) を満たす実数とする。
このとき、「帰無仮説:  \\( \theta = \theta _ {0} \\)、対立仮説: \\( \theta > \theta _ {0} \\)」となる仮説検定に対して、有意水準 \\( \alpha \\) の一様最強力検定が存在する。





**Proposition**

確率モデルが単調尤度比も持つとし、\\( \theta _ {1} \\) を \\( \theta _ {1} > \theta _ {0} \\) を満たす実数とする。
このとき、検定統計量 \\( T(x) \\) に関する片側検定 \\( \phi \\) に対して、ある実数 \\( k _ {0} \\) が存在して、\\( \mathbb{R}^{N} \\) 上の関数
\\[ \\begin{aligned}  g(x) := f (x; \\theta _ {1}) - k _ {0} f (x; \\theta _ {0})  \\end{aligned} \\]
が以下の条件を満たすようにできる。
\\[ \\begin{aligned}      T(x) > a \\Longrightarrow g (x) > 0 \\\\     T(x) = a \\Longrightarrow g (x) = 0 \\\\     T(x) < a \\Longrightarrow g (x) < 0  \\end{aligned} \\]




## 主張（一様最強力不偏検定が存在すること）

「確率モデルが指数型分布族」であり、「帰無仮説:  \\( \theta = \theta _ {0} \\)、対立仮説: \\( \theta \neq \theta _ {0} \\)」であるときに一様最強力不偏検定が存在するという以下の主張を示そう。



**Theorem**

確率モデルが指数型分布族であるとし、\\( \alpha \\) を \\( 0 < \alpha < 1 \\) を満たす実数とする。
このとき、「帰無仮説:  \\( \theta = \theta _ {0} \\)、対立仮説: \\( \theta \neq \theta _ {0} \\)」となる仮説検定に対して、有意水準 \\( \alpha \\) の一様最強力不偏検定が存在する。



**Proposition**

確率モデルが単調尤度比を持つとし、\\( \alpha \\) を \\( 0 < \alpha < 1 \\) を満たす実数とする。
このとき、以下の条件を満たす検定統計量 \\( T(x) \\) に関する両側検定 \\( \phi \\) が存在する。
\\[ \\begin{aligned}  \\int \\phi(x) f (x; \\theta _ {0}) = \\alpha\, \\\\ \\int \\tilde{\\phi} (x) \\cdot \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) dx = 0.  \\end{aligned} \\]
*Proof*: 確率モデルが指数型分布族であるため、



\\( \Box \\)



**Proposition**

確率モデルが指数型分布族であるとし、\\( \theta _ {1} \\) を \\( \theta _ {1} \neq \theta _ {0} \\) を満たす実数とする。
このとき、検定統計量 \\( T(x) \\) に関する両側検定 \\( \phi \\) に対して、ある実数 \\( k _ {0}\, k _ {1} \\) が存在して、\\( \mathbb{R}^{N} \\) 上の関数
\\[ \\begin{aligned}  g(x) := f (x; \\theta _ {1}) - k _ {0} f (x; \\theta _ {0}) - k _ {1} \\frac{\\partial} {\\partial \\theta} f (x; \\theta _ {0})  \\end{aligned} \\]
が以下の条件を満たすようにできる。
\\[ \\begin{aligned}  T(x) < a\, b < T(x) & \\Longrightarrow & g (x) > 0\, \\\\ T(x) = a\, b & \\Longrightarrow & g (x) = 0\, \\\\ a < T(x) < b & \\Longrightarrow & g (x) < 0. \\\\  \\end{aligned} \\]


**Proposition（Neyman–Pearson の定理 2）**

\\( f _ {0}\, f _ {1} \\) を \\( \mathbb{R}^{N} \\) 上の可積分関数とする。実数 \\( k _ {0} \geq 0\, k _ {1} \geq 0 \\)、\\( 0 \leq \gamma \leq 1 \\) に対して、検定関数 \\( \phi \\) を
\\[ \\begin{aligned}  \\phi (x; k _ {0}\, k _ {1}\, \\gamma) :=  \\begin{cases}     1      & f (x; \\theta _ {1}) > k _ {0} f (x; \\theta _ {0}) + k _ {1} \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) \\\\     \\gamma & f (x; \\theta _ {1}) = k _ {0} f (x; \\theta _ {0}) + k _ {1} \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) \\\\     0      & f (x; \\theta _ {1}) < k _ {0} f (x; \\theta _ {0}) + k _ {1} \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) \\end{cases}  \\end{aligned} \\]
と定義する。\\( \tilde{\phi} \\) を以下を満たす検定関数とする。
\\[ \\begin{aligned}  \\int \\tilde{\\phi} (x) f (x; \\theta _ {0}) dx \\leq \\int \\phi (x; k _ {0}\, k _ {1}\, \\gamma) f (x; \\theta _ {0}) dx\, \\\\ \\int \\tilde{\\phi} (x) \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) dx \\leq \\int \\phi (x; k _ {0}\, k _ {1}\, \\gamma) \\frac {\\partial} {\\partial \\theta} f (x; \\theta _ {0}) dx.  \\end{aligned} \\]
このとき、以下の不等式が成り立つ。
\\[ \\begin{aligned}  \\int \\tilde{\\phi} (x) f (x; \\theta _ {1}) dx \\leq \\int \\phi (x; k _ {0}\, k _ {1}\, \\gamma) f (x; \\theta _ {1}) dx.  \\end{aligned} \\]




## Appendix: 用語の定義



本記事では、\\( 1 \\) 次元の実数値ハイパーパラメータ \\( \theta \in \mathbb{R} \\) に対する \\( \mathbb{R}^{N} \\) 上の確率分布の族 \\( \mathcal{M} _ {\theta} \\) であり、\\( \mathcal{M} _ {\theta} \\) が \\( \mathbb{R}^{N} \\) 上の確率密度関数 \\( f (x; \theta) \\) を持つ確率モデルを考える。



**Definition（単調尤度比）**

任意の \\(\theta _ {0} < \theta _ {1} \\) に対して、ある \\( \mathbb{R} \\) 上の（狭義）単調増加関数 \\( R (t; \theta _ {0}\, \theta _ {1}) \\) が存在して、尤度比 \\( L(x; \theta _ {0}\, \theta _ {1} ) := \frac { f (x | \theta _ {1} ) } { f (x | \theta _ {0} )} \\) に対して \\( R(t; \theta _ {0}\, \theta _ {1}) = L(x; \theta _ {0}\, \theta _ {1}) \\) と書けるとき、\\( \mathcal{M} \\) は単調尤度比を持つという。



**Definition（指数型分布族）**

確率密度関数が \\( f (x | \theta ) := h(x) \exp \left( \theta \cdot T(x) - A(\theta) \right) \\) と書けるとき、\\( \mathcal{M} _ {\theta} \\) を（正準型の）指数型分布族であるという。

（※）本記事では指数型分布族を正準型に限定する



**Definition（仮説検定）**

- 可測関数 \\( \phi: \mathbb{R}^{N} \rightarrow [0\, 1] \subseteq \mathbb{R} \\) を検定関数という。**以降、仮説検定 \\(\phi \\) と書くとき、仮説検定に付随する検定関数のことを指すとする。**
- 可測関数 \\( T: \mathbb{R}^{N} \rightarrow \mathbb{R} \\) としたとき \\( T(x) \\) を検定統計量という。
- \\(\gamma \\) は \\( 0 \leq \gamma \leq 1 \\) を満たす定数とする。以下の検定関数を用いる仮説検定を（検定統計量 \\( T(x) \\) に関する）片側検定という。

\\[ \\begin{aligned}  \\phi (x) :=  \\begin{cases}     1      & T(x) > a \\\\     \\gamma & T(x) = a \\\\     0      & T(x) < a \\end{cases}  \\end{aligned} \\]

- \\(\gamma \\) は \\( 0 \leq \gamma \leq 1 \\) を満たす定数とする。以下の検定関数を用いる仮説検定を（検定統計量 \\( T(x) \\) に関する）両側検定という。

\\[ \\begin{aligned}  \\phi (x) :=  \\begin{cases}     1      & T(x) > a\, b < T(x) \\\\     \\gamma & T(x) = a\, b \\\\     0      & a < T(x) < b \\end{cases}  \\end{aligned} \\]

- 検定関数に対して、\\( \beta (\theta; \phi) := \int \phi (x) f (x; \theta) dx \\) を \\( \phi \\) に対する検出力関数という。
- 帰無仮説 \\( \Theta _ {0} \\) の元 \\( \theta _ {0} \in \Theta _ {0} \\) に対する検出力関数 \\( \beta (\theta _ {0}; \phi) \\) の値を \\( p \\) 値と呼ぶ。



**Definition（有意水準 \\( \alpha \\) の検定）**

確率モデルがパラメータ空間 \\( \Theta \\) を持ち、帰無仮説を \\( \Theta _ {0} \\) とする。さらに、\\( \alpha \\) を \\( 0 < \alpha < 1 \\) を満たす実数とする。

仮説検定 \\( \phi \\) が以下を満たすとき、検定は有意水準 \\( \alpha \\) の検定であるという。
\\[ \\begin{aligned}  \\beta (\\theta _ {0}; \\phi) \\leq \\alpha \\\,\\\, (\\forall \\theta _ {0} \\in \\Theta _ {0})  \\end{aligned} \\]
（※）対立仮説 \\( \Theta _ {1} \\) は定義上必要がないことに注意する。



**Definition（有意水準 \\( \alpha \\) の不偏検定）**

確率モデルがパラメータ空間 \\( \Theta \\) を持ち、帰無仮説を \\( \Theta _ {0} \\)、対立仮説を \\( \Theta _ {1} \\) とする。さらに、\\( \alpha \\) を \\( 0 < \alpha < 1 \\) を満たす実数とする。

仮説検定 \\( \phi \\) が以下を満たすとき、検定は有意水準 \\( \alpha \\) の不偏検定であるという。
\\[ \\begin{aligned}  \\beta (\\theta _ {0}; \\phi) \\leq \\alpha \\\,\\\, (\\forall \\theta _ {0} \\in \\Theta _ {0})\,\\\\ \\beta (\\theta _ {1}; \\phi) \\geq \\alpha \\\,\\\, (\\forall \\theta _ {1} \\in \\Theta _ {1})  \\end{aligned} \\]


**Definition（有意水準 \\( \alpha \\) の一様最強力検定）**

仮説検定 \\( \phi \\) が次の条件を満たすとき、有意水準 \\( \alpha \\) の一様最強力検定であるという。

- 仮説検定が有意水準 \\( \alpha \\) の検定である。
- 任意の有意水準 \\( \alpha \\) の仮説検定 \\( \tilde{\phi} \\) に対して、\\( \beta (\theta _ {1}; \tilde{\phi}) \leq \beta (\theta _ {1}; \phi) \\,\\, (\forall \theta _ {1} \in \Theta _ {1}) \\) が成り立つ。



**Definition（有意水準 \\( \alpha \\) の一様最強力不偏検定）**

仮説検定 \\( \phi \\) が次の条件を満たすとき、有意水準 \\( \alpha \\) の一様最強力不偏検定であるという。

- 仮説検定が有意水準 \\( \alpha \\) の不偏検定である。
- 任意の有意水準 \\( \alpha \\) の不偏検定 \\( \tilde{\phi} \\) に対して、\\( \beta (\theta _ {1}; \tilde{\phi}) \leq \beta (\theta _ {1}; \phi) \\,\\, (\forall \theta _ {1} \in \Theta _ {1}) \\) が成り立つ。





