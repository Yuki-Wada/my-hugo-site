---
title: '最尤推定量の漸近正規性'
description: '最尤推定量の漸近正規性'
date: '2025-01-19'
categories: []
weight: 999
math: true
draft: true
---



[フィッシャー情報量](/wiki/%E6%95%B0%E7%90%86%E3%83%A2%E3%83%87%E3%83%AB/%E3%83%95%E3%82%A3%E3%83%83%E3%82%B7%E3%83%A3%E3%83%BC%E6%83%85%E5%A0%B1%E9%87%8F/)

**(C1)** $ f( x | \theta ) $ のサポートが $\theta $ に依存しない。

**(C2)** 

$ (C6) $ $ f( x | \theta ) $ が $ \theta $ に関して $ 3 $ 回連続微分可能とする。



**Definition** パラメータ $ \theta $ に対する推定量 $ (\hat {\theta_{n} }) $ に対して、$ \sqrt{n} ( \hat{\theta_{n}} - \theta) $ がある平均 $ 0 $ の正規分布に分布収束するとき、$ (\hat{\theta_{n}}) $ は $\theta $ に関して漸近正規的であるという。
$$
\sqrt{n} ( \hat{\theta_{n}} - \theta) \rightarrow_{d} \mathcal{N} (0, c)
$$



**Theorem** 

真の母数 $ \theta_{0} $ に確率収束する最尤推定量 $ ( \theta_{n} ) $ の列が存在する。



**Theorem** 

真の母数 $ \theta_{0} $ に確率収束する最尤推定量 $ ( \theta_{n} ) $ の列が存在する。このとき、以下が成立する。
$$
\sqrt{n} ( \hat{\theta_{n}} - \theta) \rightarrow_{d} \mathcal{N} (0, c)
$$
とくに $ ( \theta_{n} ) $ は漸近正規的である。

*Proof*: 対数尤度関数 $ l (\theta) $ に対して、最尤推定量 $ \hat{\theta} $ は
$$
\ell' ( \hat{\theta} ) = 
\ell' ( \hat { \theta_{0} } ) + \ell'' ( \hat { \theta_{0} } ) ( \hat{\theta} - \theta_{0} ) +
\frac {1} {2} \ell''' ( \theta^{*} ) ( \hat{\theta} - \theta_{0} )^{2}
$$
 と近似できる。ここで $ \theta^{*} $ は $\theta_{0} $ と $ \hat{\theta} $ の間の点である。$ \ell ' (\hat{\theta}) $ は
$$
\sqrt {n} (\hat{\theta} - \theta_{0} ) =
\frac { \frac{1}{\sqrt{n}} \ell ' (\theta_{0})' } { -\frac{1} {n} \ell '' (\theta_{0}) - \frac{1}{2n} }
$$
と書ける。$ S_{1} (\theta, X_{i}) := \frac{d} {d \theta} \log f (X_{i} | \theta) $ とおくと、 



大数の法則より、
$$
- \frac{1} {n} \ell '' (\theta_{0}) \rightarrow_{p} I_{1} (\theta_{0})
$$
となる。最後に、

以上よりスラツキーの定理を用いると、

















