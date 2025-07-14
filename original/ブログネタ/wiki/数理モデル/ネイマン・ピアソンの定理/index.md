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

\\( \Omega \\)  を任意の測度空間、\\( f _ {0}\, f _ {1} \\) を \\( \Omega \\) 上の可積分関数とする。実数 \\( c > 0 \\)、\\( 0 \leq \gamma \leq 1 \\) に対して、検定関数 \\( \phi: \Omega \rightarrow [0\, 1] \\) を
\\[ \\begin{aligned}  \\phi (\\omega; c\, \\gamma) :=  \\begin{cases}     1      & f _ {1} (\\omega) > c f _ {0} (\\omega) \\\\     \\gamma & f _ {1} (\\omega) = c f _ {0} (\\omega) \\\\     0      & f _ {1} (\\omega) < c f _ {0} (\\omega) \\end{cases}  \\end{aligned} \\]
と定義する。
\\[ \\begin{aligned}  \\alpha := \\mathbb{E} _ {0} ( \\phi (\\omega; c\, \\gamma)) := \\int \\phi (\\omega; c\, \\gamma) f _ {0}(\\omega) d\\Omega  \\end{aligned} \\]
となるように（棄却率に相当する）\\( \alpha \\) となるように定めると、検定関数 \\( \phi \\) は有意水準が \\( \alpha \\) であるような確率化検定の中で検出力が最大となる。

つまり、\\( 0 \leq \psi (\omega) \leq 1\\) かつ
\\[ \\begin{aligned}  \\mathbb{E} _ {0} ( \\psi (\\omega) ) := \\int \\psi (\\omega) f _ {0} (\\omega) d \\Omega \\leq \\alpha  \\end{aligned} \\]
を満たす検定関数 \\( \psi (\omega) \\) に対して以下の不等式が成り立つ。
\\[ \\begin{aligned}  \\int \\phi (\\omega) f _ {1} (\\omega) d \\Omega \\geq \\int \\psi (\\omega) f _ {1} (\\omega) d \\Omega  \\end{aligned} \\]
*Proof*: 単純な式変形で導出できる。
\\[ \\begin{aligned} & \\int \\phi(\\omega) f(\\omega) d\\Omega -\\int \\psi(\\omega) f(\\omega) d\\Omega \\\\ \\geq & \\int \\phi(\\omega) f(\\omega) d\\Omega - \\int \\psi(\\omega) f(\\omega) d\\Omega - \\sum _ {i=1}^{n} k _ {i} \\left( \\alpha _ {i} - \\int \\psi (\\omega) g _ {i} (\\omega) d\\Omega \\right) \\\\ \\geq & \\int \\phi(\\omega) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega - \\int \\psi(\\omega) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega \\\\ \\geq & \\int \\left(\\phi(\\omega) - \\psi(\\omega) \\right) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega \\\\ \\end{aligned} \\]
\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) > 0  \\) のときは \\( \phi(\omega) = 1 \\) なので \\( \phi(\omega) - \psi(\omega) \geq 0 \\) であり、\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) < 0  \\) のときは \\( \phi(\omega) = 0 \\) なので \\( \phi(\omega) - \psi(\omega) \leq 0 \\) であることから、

\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) = 0 \\) のときは上記の積分の値に影響を与えないことと合わせて、上記の積分の値が \\( \geq 0 \\) となることが示せた。\\( \Box \\)



**Proposition** (一般化されたネイマン・ピアソンの補題)

\\( \Omega \\)  を任意の測度空間、\\( f \\), \\( (g _ {i}) _ {i = 1 \dots n}\\) を \\( \Omega \\) 上の可積分関数とし、 非負の定数 \\( (k _ {i}) _ {i = 1 \dots n} \\) に対して、検定関数 \\( \phi: \Omega \rightarrow [0\, 1] \\) を
\\[ \\begin{aligned}  \\phi (\\omega; (k _ {i}) _ {i = 1 \\dots n}) :=  \\begin{cases}     1    & f(\\omega) > \\sum _ {i = 1}^{n} k _ {i} g _ {i} (\\omega) \\\\     0    & f(\\omega) < \\sum _ {i = 1}^{n} k _ {i} g _ {i} (\\omega) \\end{cases}  \\end{aligned} \\]
と定義する。（棄却率に相当する）\\( (\alpha _ {i}) _ {i = 1 \dots n} \\) を
\\[ \\begin{aligned}  \\alpha _ {i} ((k _ {i'}) _ {i' = 1 \\dots n}) := \\int \\phi (\\omega; (k _ {i'}) _ {i' = 1 \\dots n}) g _ {i} (\\omega) d \\Omega  \\end{aligned} \\]
と定義し、（レベル \\( \alpha _ {i} \\) の検定に相当する）\\( \psi (\omega) \\) を \\( 0 \leq \psi (\omega) \leq 1\\) かつ
\\[ \\begin{aligned}  \\int \\psi (\\omega) g _ {i} (\\omega) d \\Omega \\leq \\alpha _ {i}  \\end{aligned} \\]
を満たす検定関数とする。このとき、以下の不等式が成り立つ。
\\[ \\begin{aligned}  \\int \\phi (\\omega) f (\\omega) d \\Omega \\geq \\int \\psi (\\omega) f (\\omega) d \\Omega  \\end{aligned} \\]
*Proof*: 単純な式変形で導出できる。
\\[ \\begin{aligned} & \\int \\phi(\\omega) f(\\omega) d\\Omega -\\int \\psi(\\omega) f(\\omega) d\\Omega \\\\ \\geq & \\int \\phi(\\omega) f(\\omega) d\\Omega - \\int \\psi(\\omega) f(\\omega) d\\Omega - \\sum _ {i=1}^{n} k _ {i} \\left( \\alpha _ {i} - \\int \\psi (\\omega) g _ {i} (\\omega) d\\Omega \\right) \\\\ \\geq & \\int \\phi(\\omega) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega - \\int \\psi(\\omega) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega \\\\ \\geq & \\int \\left(\\phi(\\omega) - \\psi(\\omega) \\right) \\left( f(\\omega) - \\sum _ {i=1}^{n} k _ {i} g _ {i} (\\omega) \\right) d\\Omega \\\\ \\end{aligned} \\]
\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) > 0  \\) のときは \\( \phi(\omega) = 1 \\) なので \\( \phi(\omega) - \psi(\omega) \geq 0 \\) であり、\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) < 0  \\) のときは \\( \phi(\omega) = 0 \\) なので \\( \phi(\omega) - \psi(\omega) \leq 0 \\) であることから、

\\( f(\omega) - \sum _ {i=1}^{n} k _ {i} g _ {i} (\omega) = 0 \\) のときは上記の積分の値に影響を与えないことと合わせて、上記の積分の値が \\( \geq 0 \\) となることが示せた。\\( \Box \\)


