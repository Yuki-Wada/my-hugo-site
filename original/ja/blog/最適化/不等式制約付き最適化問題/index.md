---
title: '不等式制約付き最適化問題'
description: '不等式制約付き最適化問題'
slug: 'inequality-constrained-optimization'
date: '2025-07-13'
weight: 999
categories:
  - 最適化
aliases:
  - '/inequality-constrained-optimization/'
math: true
draft: true
---


## 不等式制約付き最適化問題

**Definition（不等式制約付き最適化問題）**
> (1) 以下の問題を不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ と定義します。
> $$
  \begin{align}
  \text{infimum} \,\, & f(x)\\
  \text{subject to} \,\,
  & g_{i}(x) \leq 0 \,\, (\forall \, i) \\
  & h_{j}(x) = 0 \,\, (\forall \, j) \\
  \end{align}
  $$
> 
> (2) 制約条件
> $$
  g_{i}(x) \leq 0 \,\, (\forall \, i), \,\,  h_{j}(x) = 0 \,\, (\forall \, j)
  $$
> を満たす $x$ を実行可能解（feasible point）と定義する。
> 
> (3) 実行可能解の集合を $F$ として、
> $ f(x_{0}) = \inf_{x \in F} f(x) $
> を満たす $x$ を最適解（optimal point）と定義する。

### 不等式制約付き最適化問題についての補足
上記の最適化問題で考えられるケースには以下の 4 通りがあります。
1. 実行可能解が存在しない（この場合を便宜的に $ \inf_{x \in F} f(x) = +\infty$ とみなす）。
1. 実行可能解が存在するが、下限値が存在しない（つまり、実行可能解の集合を $F$ として、$ \inf_{x \in F} f(x) = -\infty$）。
1. 実行可能解が存在し、下限値が存在するが、最適解が存在しない。
1. 実行可能解が存在し、下限値が存在し、最適解が存在する。

**Definition (凸関数)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。  
> 1. $f, g_{i}, h_{j}$ がいずれも凸関数であるとき、この最適化問題は凸であると定義します。  
> 1. $f, g_{i}, h_{j}$ がいずれも $C^{1}$ 級関数であるとき、この最適化問題は滑らかであると定義します。


### Definition（ラグランジュ緩和関数）
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> このとき、ラグランジュ緩和関数 $L(x, \lambda, \nu)$ を以下の式で定義します。
> $$
> L(x, \lambda, \nu) := f(x) + \sum_{i=1}^{m} \lambda_i g_i(x) + \sum_{j=1}^{p} \nu_j h_j(x)
> $$

### Definition (KKT 条件)
> 滑らかな不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> $(x^*, \mu^*, \lambda^*)$ が以下の条件を満たすとします。
> 1. 停留点条件:
>    $$
>    \nabla_x L(x, \lambda, \nu) = \nabla f(x) + \sum_{i=1}^{m} \lambda_i \nabla g_i(x) + \sum_{j=1}^{p} \nu_j \nabla h_j(x) = 0
>    $$
> 1. 主問題の実行可能性:
>    $$
>    g_i(x) \leq 0 \quad (\forall \, i), \quad h_j(x) = 0 \quad (\forall \, j)
>    $$
> 
> 1. 双対実行可能性:
> 
>    $$
>    \lambda_i \geq 0 \quad (\forall \, i)
>    $$
> 
> 1. 相補性条件:
> 
>    $$
>    \lambda_i g_i(x) = 0 \quad (\forall \, i)
>    $$
> 
> このとき、この問題は $(x^*, \lambda^*, \nu^*)$ において KKT 条件を満たすと定義します。

