---
date: '2025-05-06'
title: '伊藤の公式を用いた、マルチンゲールのモーメント不等式の証明'
description: '確率解析における基本的かつ重要な不等式の一つであるマルチンゲールのモーメント不等式に関する具体的な証明を取り上げます。'
slug: 'ito-integral-moment-inequality'
weight: 999
math: true
categories:
    - 金融工学
    - 確率過程論
    - メモ
draft: true
---



## 導入

----

本記事では、確率解析における基本的かつ重要な不等式の一つであるマルチンゲールのモーメント不等式に関する具体的な証明を取り上げます。特に Karatzas and Shreve の教科書 [1] に登場する練習問題を題材に、伊藤の公式をどのように応用すればよいかを詳細に解説します。

<br><br>


## 概要 (abstract or point)

----

#### この記事で伝えたいこと



#### 記事の対象者

- 伊藤の公式を実際の証明にどのように応用するかを具体的に学びたい方
- Exercise 3.3.25 of Karatzas and Shreve の該当練習問題を自力で完結できなかった方

<br><br>

## 本文1 ― 詳細 (reason)

----

#### 証明したい命題

$ W={Wt,Ft;0≤t<∞} $ を標準的な一次元ブラウン運動、$ X_{t} $ を可測で適合的な確率過程で
$$
E \int_{0}^{T} |X_{t}|^{2m} \, dt < \infty
$$
をある実数 $ T > 0 $、$ m \geq 1 $ のときに満たすとする。このとき、以下の不等式が成り立つ。
$$
\mathbb{E} \left| \int_{0}^{T} X_{t} dW_{t} \right|^{2m}
\leq \left( m(2m−1) \right)^{m} \cdot T^{m−1} \cdot \mathbb{E} \int_{0}^{T} |X_{t}|^{2m} \, dt
$$


#### 課題の背景

上記の問題はマルチンゲールのモーメント不等式

マルチンゲールのモーメント不等式（martingale moment inequality）は、確率論においてマルチンゲールの最大値や変動の大きさを制御するための強力な道具です。特に、マルチンゲールが「どれくらい大きくなりうるか」をモーメント（平均値のべき乗）で評価します。

マルチンゲールとは、未来の期待値が現在の値に等しいという性質をもつ確率過程。

Karatzas and Shreve の問題に



#### 課題を解決する技術・手法の概要

今回は



#### 技術・手法の効果、課題がどう解決されるか

##### 伊藤の公式を適用

元ネタである [1] の Exercise 3.3.25 のヒントには「マルチンゲール $ \{ M_{t} = ∫t0XsdWs,Ft;0≤t≤T\} \{Mt=∫0tXsdWs,Ft;0≤t≤T \} $ と $ f(x) = |x|^{2m} $ に対して、伊藤の公式を適用すればよい」とあります。

ですが、そのまま $ f(x) = |x|^{2m} \,\, (x \in \mathbb{R}) $ に対して伊藤の公式を適用するのは $ f'' $ が連続でないという懸念点があるので、[1] の Proposition 3.3.26 の証明を援用してみます。

$ Y_{t} = \delta + M_{t}^{2} \,\, (\delta > 0) $ に対して、$ g(x) = x^{m} \,\, (x > 0) $ は値を代入でき、さらに $ g', g'' $ も連続です。よって、問題なく伊藤の公式が適用できます。$ \delta > 0 $ の場合に対して最終的に $ \delta \rightarrow +0 $ とすることによって、$ | M_{t} | ^{2m} $ の結果を得ることができそうです。

実際に計算してみます。伊藤の公式を使うことで、
$$
Y_{t}
= \delta + M_{t}^{2}
= \delta + 2 \int_{0}^{t} M_{t} \, d M_{t} + \langle M \rangle_{t}
= \delta + 2 \int_{0}^{t} M_{t} \, d M_{t} + \int_{0}^{t} X_{t}^{2} \, dt
$$
であり、$ Y_{t} $ のマルチンゲール部分 $ 2 \int_{0}^{t} M_{t} \, d M_{t} $ の二次変分は $ 4 M_{t}^{2} \, d\langle M\rangle_{t} = 4 M_{t}^{2} X_{t}^{2} \, dt $ とかけます。よって、さらに伊藤の公式を適用することで、
$$
\begin{aligned}
Y_{T}^{m} = g(Y_{T}) & = g(Y_{0})
+ \int_{0}^{T} g'(Y_{t}) \, dY_{t}
+ \frac{1}{2} \int_{0}^{T} g''(Y_{t}) \, d\langle Y \rangle_{t} \\
& = \delta^{m} + m \cdot \int_{0}^{T} Y_{t}^{m - 1} \, dY_{t}
+ \frac{m (m - 1)}{2} \int_{0}^{T} (Y_{t})^{m - 2} \cdot 4 M_{t}^{2} X_{t}^{2} \, dt \\
& = \delta^{m} + 2m \cdot \int_{0}^{T} Y_{t}^{m - 1} M_{t} \, dM_{t}
+ m \cdot \int_{0}^{T} Y_{t}^{m - 1} X_{t}^{2} \, dt
+ 2m \cdot (m - 1) \cdot \mathbb{E} \left( \int_{0}^{T} Y_{t}^{m - 2} M_{t}^{2} X_{t}^{2} \, dt \right) \\
\end{aligned}
$$
とかけます。両辺の期待値を取ると、$ \int_{0}^{T} Y_{t}^{m - 1} M_{t} \, dM_{t} $ がマルチンゲールですので、 
$$
\begin{aligned}
\mathbb{E}(Y_{T}^{m})
= m \cdot \mathbb{E} \left( \int_{0}^{T} Y_{t}^{m - 1} X_{t}^{2} \, dt \right)
+ 2m \cdot (m - 1) \cdot \mathbb{E} \left( \int_{0}^{T} Y_{t}^{m - 2} M_{t}^{2} X_{t}^{2} \, dt \right) \\
\end{aligned}
$$
となり、さらに $ \delta \rightarrow +0 $ とすることでルベーグの優収束定理より、
$$
\begin{aligned}
\mathbb{E}( |M_{T}|^{2m} )
& = m \cdot (2m - 1) \cdot \mathbb{E} \left( \int_{0}^{T} |M_{t}|^{2m - 2} X_{t}^{2} \, dt \right) \\
\end{aligned}
$$
という等式が成立することがいえます。



##### 積分項を整理

ここまで伊藤の公式を使って式変形をしてきました。$ \mathbb{E} \left( \int_{0}^{T} M_{t}^{2m - 2} X_{t}^{2} \, dt \right) $ という項が出てきていますが、これを $ \mathbb{E} \int_{0}^{T} |X_{t}|^{2m} \, dt$ とどう結びつけるかが次の問題になります。

$ m = 1 $ なら問題ないので、ここから $ m > 1 $ とします。

まず、$ p= \frac{m} {m−1}, \,\, q = m $ に対して、$ \frac{1}{p} + \frac{1}{q} = 1 $ を満たすことからヘルダーの不等式を適用することで、

$$
\begin{aligned}
\mathbb{E} \left( \int_{0}^{T} | M_{t} |^{2m - 2} X_{t}^{2} \, dt \right)
\leq \left( \mathbb{E} \left( \int_{0}^{T} | M_{t} |^{2m} \, dt \right) \right)^{\frac{m - 1}{m}} \cdot
\left( \mathbb{E} \left( \int_{0}^{T} |X_{t}|^{2m} \, dt \right) \right) ^{\frac{1}{m}}
\end{aligned}
$$
という不等式が成立し、$ M_{t} $ に関する積分と $ X_{t} $ に関する積分の積に分離できます。

次に、$ M_{t} $ がマルチンゲールで $ h(x) = |x|^{2m} $ が凸関数であるため、$ |M_{t}|^{2m} $　が劣マルチンゲールであることから、$ |M_{t}|^{2m} \leq \mathbb{E} \left( |M_{T}|^{2m} | \mathcal{F}_{t} \right) $ であることがわかります。両辺の期待値を取って、
$$
\mathbb{E} |M_{t}|^{2m} \leq \mathbb{E} \left( |M_{T}|^{2m} \right)
$$
という不等式が成立することがわかります。よって、フビニの定理を適用することで、
$$
\mathbb{E} \left( \int_{0}^{T} | M_{t} |^{2m} \, dt \right)
= \int_{0}^{T} \mathbb{E} \left( | M_{t} |^{2m} \right) \, dt
\leq \int_{0}^{T} \mathbb{E} \left( | M_{T} |^{2m} \right) \, dt
= T \cdot \mathbb{E} \left( | M_{T} |^{2m} \right)
$$
という不等式が成立し、$ t $ に関する積分を追い出した項で上から抑えることができます。

上記二つの不等式を使って元の式を整理すると、
$$
\begin{aligned}
\mathbb{E}( |M_{T}|^{2m} )
= & m \cdot (2m - 1) \cdot \mathbb{E} \left( \int_{0}^{T} | M_{t} |^{2m - 2} |X_{t}|^{2} \, dt \right) \\
\leq & m \cdot (2m - 1) \cdot \left( \mathbb{E} \left( \int_{0}^{T} | M_{t} |^{2m} \, dt \right) \right)^{\frac{m - 1}{m}} \cdot
\left( \mathbb{E} \left( \int_{0}^{T} |X_{t}|^{2m} \, dt \right) \right) ^{\frac{1}{m}} \\
\leq & m \cdot (2m - 1) \cdot \left( T \cdot \mathbb{E} \left( | M_{T} |^{2m} \right) \right)^{\frac{m - 1}{m}} \cdot
\left( \mathbb{E} \left( \int_{0}^{T} |X_{t}|^{2m} \, dt \right) \right) ^{\frac{1}{m}}
\end{aligned}
$$
とかけますので、$ \mathbb{E}( |M_{T}|^{2m} )^{ \frac{m-1}{m} } $ で両辺を割った後、$ m $ 乗すれば、
$$
\begin{aligned}
\mathbb{E}( |M_{T}|^{2m} )
\leq & \left( m \cdot (2m - 1) \right)^{m} \cdot T ^{m - 1} \cdot
\mathbb{E} \left( \int_{0}^{T} |X_{t}|^{2m} \, dt \right)
\end{aligned}
$$
となり、所望の不等式が成立することを示せました。



#### 留意点、デメリット



<br><br>

## 結論

----

伊藤の公式とヘルダーの不等式、マルチンゲールの性質を組み合わせることで、[1] の Exercise 3.3.25 に登場するモーメント不等式を導出することができました。本手法は、他の確率微分方程式や不等式評価にも応用可能であり、伊藤解析の基礎を深める良い練習になります。

<br><br>

## 参考文献

----

[1] Ioannis Karatzas, Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed.

