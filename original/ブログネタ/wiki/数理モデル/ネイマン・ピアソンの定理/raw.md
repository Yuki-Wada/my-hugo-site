---
title: 'ネイマン・ピアソンの定理'
description: 'ネイマン・ピアソンの定理'
date: '2025-01-19'
categories: []
weight: 999
math: true
---



## Appendix: Preliminaries



**Proposition** (ネイマン・ピアソンの定理)

$ \Omega $  を任意の測度空間、$ f_{0}, f_{1} $ を $ \Omega $ 上の可積分関数とする。実数 $ c > 0 $、$ 0 \leq \gamma \leq 1 $ に対して、検定関数 $ \phi: \Omega \rightarrow [0, 1] $ を
$$
\phi (\omega; c, \gamma) := 
\begin{cases}
    1      & f_{1} (\omega) > c f_{0} (\omega) \\
    \gamma & f_{1} (\omega) = c f_{0} (\omega) \\
    0      & f_{1} (\omega) < c f_{0} (\omega)
\end{cases}
$$
と定義する。
$$
\alpha := \mathbb{E}_{0} ( \phi (\omega; c, \gamma)) := \int \phi (\omega; c, \gamma) f_{0}(\omega) d\Omega
$$
となるように（棄却率に相当する）$ \alpha $ となるように定めると、検定関数 $ \phi $ は有意水準が $ \alpha $ であるような確率化検定の中で検出力が最大となる。

つまり、$ 0 \leq \psi (\omega) \leq 1$ かつ
$$
\mathbb{E}_{0} ( \psi (\omega) ) := \int \psi (\omega) f_{0} (\omega) d \Omega \leq \alpha
$$
を満たす検定関数 $ \psi (\omega) $ に対して以下の不等式が成り立つ。
$$
\int \phi (\omega) f_{1} (\omega) d \Omega \geq \int \psi (\omega) f_{1} (\omega) d \Omega
$$
*Proof*: 単純な式変形で導出できる。
$$
\begin{aligned}
& \int \phi(\omega) f(\omega) d\Omega -\int \psi(\omega) f(\omega) d\Omega \\
\geq & \int \phi(\omega) f(\omega) d\Omega - \int \psi(\omega) f(\omega) d\Omega
- \sum_{i=1}^{n} k_{i} \left( \alpha_{i} - \int \psi (\omega) g_{i} (\omega) d\Omega \right) \\
\geq & \int \phi(\omega) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega
- \int \psi(\omega) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega \\
\geq & \int \left(\phi(\omega) - \psi(\omega) \right) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega \\
\end{aligned}
$$
$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) > 0  $ のときは $ \phi(\omega) = 1 $ なので $ \phi(\omega) - \psi(\omega) \geq 0 $ であり、$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) < 0  $ のときは $ \phi(\omega) = 0 $ なので $ \phi(\omega) - \psi(\omega) \leq 0 $ であることから、

$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) = 0 $ のときは上記の積分の値に影響を与えないことと合わせて、上記の積分の値が $ \geq 0 $ となることが示せた。$ \Box $



**Proposition** (一般化されたネイマン・ピアソンの補題)

$ \Omega $  を任意の測度空間、$ f $, $ (g_{i})_{i = 1 \dots n}$ を $ \Omega $ 上の可積分関数とし、 非負の定数 $ (k_{i})_{i = 1 \dots n} $ に対して、検定関数 $ \phi: \Omega \rightarrow [0, 1] $ を
$$
\phi (\omega; (k_{i})_{i = 1 \dots n}) := 
\begin{cases}
    1    & f(\omega) > \sum_{i = 1}^{n} k_{i} g_{i} (\omega) \\
    0    & f(\omega) < \sum_{i = 1}^{n} k_{i} g_{i} (\omega)
\end{cases}
$$
と定義する。（棄却率に相当する）$ (\alpha_{i})_{i = 1 \dots n} $ を
$$
\alpha_{i} ((k_{i'})_{i' = 1 \dots n}) := \int \phi (\omega; (k_{i'})_{i' = 1 \dots n}) g_{i} (\omega) d \Omega
$$
と定義し、（レベル $ \alpha_{i} $ の検定に相当する）$ \psi (\omega) $ を $ 0 \leq \psi (\omega) \leq 1$ かつ
$$
\int \psi (\omega) g_{i} (\omega) d \Omega \leq \alpha_{i}
$$
を満たす検定関数とする。このとき、以下の不等式が成り立つ。
$$
\int \phi (\omega) f (\omega) d \Omega \geq \int \psi (\omega) f (\omega) d \Omega
$$
*Proof*: 単純な式変形で導出できる。
$$
\begin{aligned}
& \int \phi(\omega) f(\omega) d\Omega -\int \psi(\omega) f(\omega) d\Omega \\
\geq & \int \phi(\omega) f(\omega) d\Omega - \int \psi(\omega) f(\omega) d\Omega
- \sum_{i=1}^{n} k_{i} \left( \alpha_{i} - \int \psi (\omega) g_{i} (\omega) d\Omega \right) \\
\geq & \int \phi(\omega) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega
- \int \psi(\omega) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega \\
\geq & \int \left(\phi(\omega) - \psi(\omega) \right) \left( f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) \right) d\Omega \\
\end{aligned}
$$
$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) > 0  $ のときは $ \phi(\omega) = 1 $ なので $ \phi(\omega) - \psi(\omega) \geq 0 $ であり、$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) < 0  $ のときは $ \phi(\omega) = 0 $ なので $ \phi(\omega) - \psi(\omega) \leq 0 $ であることから、

$ f(\omega) - \sum_{i=1}^{n} k_{i} g_{i} (\omega) = 0 $ のときは上記の積分の値に影響を与えないことと合わせて、上記の積分の値が $ \geq 0 $ となることが示せた。$ \Box $


