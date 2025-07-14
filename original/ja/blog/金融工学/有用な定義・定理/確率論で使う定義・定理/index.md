---
date: '2025-07-15'
title: '確率論で使う定義・定理'
linkTitle: '確率論で使う定義・定理'
description: >
  この記事の概要です。
  タイトル名の下に記事の見出しとして表示されます。
slug: 'probability-theory-reference'
author: Yuki Wada
weight: 999
categories:
  - test
aliases: 
  - 'probability-theory-reference'
math: true
draft: true
---



## 導入

----



<br><br>

## 概要 (abstract or point)

----

#### この記事で伝えたいこと

- 
- 

#### 記事の対象者

- 
- 

<br><br>

## Dynkin 族定理

#### 有用性

#### Definition（Dynkin 族）
> 集合 $\Omega$ 上の部分集合族 $\mathcal{D}$ を考えます。
> $\mathcal{D}$ が以下の条件を全て満たすとき、$\mathcal{D}$ は Dynkin 族であると定義します:
> 
> 1. （全体集合を含む）: $\Omega \in \mathcal{D}$
> 1. （補集合を取る操作について閉じている）  
>     $A \in \mathcal{D}$ ならば $A^c \in \mathcal{D}$（補集合に関して閉じている）
> 1. $A_1 \subset A_2 \subset A_3 \subset \cdots$, 各 $A_n \in \mathcal{D}$ のとき
>    $\bigcup_{n=1}^\infty A_n \in \mathcal{D}$（単調増加列に関して加法的）

#### Theorem（Dynkin 族定理）
> 集合 $\Omega$ 上の部分集合族 $\mathcal{D}$ を考えます。
> $\mathcal{D}$ が
集合 $\Omega$ 上の部分集合族 $\mathcal{P} \subset 2^\Omega$ が **π-系（π-system）** であるとする。

また、$\mathcal{D} \subset 2^\Omega$ が **Dynkin 族（λ-系）** であり、$\mathcal{P} \subset \mathcal{D}$ を満たすとする。

このとき、

$$
\sigma(\mathcal{P}) \subset \mathcal{D}
$$

が成り立つ。ただし、$\sigma(\mathcal{P})$ は $\mathcal{P}$ によって生成される **σ-加法族** を表す。


## Borel–Cantelli の補題


----


## 条件付き期待値

#### Definition（条件付き期待値）
> $(\Omega, \mathcal{F}, \mathbb{P})$ を確率空間、$f$ を可測関数、$\mathcal{G} \subseteq \mathcal{F}$ を $\sigma$ 加法族とする。
> このとき、以下の条件を満たす可測関数 $g$ を $\mathcal{G}$ 上における $f$ の条件付き期待値と定義する。
> - $A \in \mathcal{G}$ となる任意の $\Omega$ の部分集合に対して、$\int_{A} f d\mathbb{P} = \int_{A} g d\mathbb{P}$ が成り立つ。
> - $g$ は $\mathcal{G}$-可測関数である。

条件付き期待値で実現したいことは、$\mathcal{F}$ よりも粗い $\mathcal{G}$ 上で関数の値を判別できるように $f$ の値をならしていることがわかる。

#### Theorem（条件付き期待値が存在する）
条件付き期待値が存在する。
> <details><summary>(Proof)</summary><div>
> 
> Radon-Nicodym の定理を使えばよい。
> 
> </div></details>

## 条件付き確率測度


#### Theorem（条件付き確率測度の存在条件）
条件付き期待値が存在する。
> <details><summary>(Proof)</summary><div>
> 
> Radon-Nicodym の定理を使えばよい。
> 
> </div></details>

## 一様可積分性



<br><br>

## 結論 (conclusion or point)

----



<br><br>

## 参考文献

----

[1] Ioannis Karatzas, Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed.