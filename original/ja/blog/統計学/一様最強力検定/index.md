---
title: '一様最強力検定'
description: '一様最強力検定'
slug: 'uniformly-most-powerful-test'
date: '2025-01-19'
weight: 999
categories:
  - 統計学
math: true
draft: true
---



## Appendix: 主張（一様最強力検定が存在すること）の証明



**Theorem**

確率モデルが単調尤度比を持つとし、$ \alpha $ を $ 0 < \alpha < 1 $ を満たす実数とする。
このとき、「帰無仮説:  $ \theta = \theta_{0} $、対立仮説: $ \theta > \theta_{0} $」となる仮説検定に対して、有意水準 $ \alpha $ の一様最強力検定が存在する。

*Proof*: 

(1) 確率モデルが単調尤度比を持つため、Proposition から任意の $ \theta_{1} > \theta_{0} $ に対して、$ \theta_{0}, \theta_{1} $ に依存する実数 $ k_{0}(\theta_{0}, \theta_{1}) $ が存在して、
$$
g(x) := f (x; \theta_{1}) - k_{0} f (x; \theta_{0})
$$
が片側検定 $ \phi $ と整合的にとることができる。

(2) 検定 $ \phi $ が一様最強力検定であることを示そう。任意の有意水準 $ \alpha $ の検定 $ \tilde{\phi} $ をとる。

まず、$ \tilde{\phi} $ が有意水準 $ \alpha $ の検定であることから、$ \int \tilde{\phi} (x) f (x; \theta_{0}) dx \leq \alpha $ である。

よって、Neyman–Pearson の定理 1 を適用することで、
$$
\int \tilde{\phi} (x) f (x; \theta_{1}) dx \leq \int \phi (x) f (x; \theta_{1}) dx
$$
であることがわかる。

(3) 以上より、片側検定 $ \phi $ が一様最強力不偏検定であることが示せた。

$ \Box $



**Proposition**

確率モデルが単調尤度比も持つとし、$ \theta_{1} $ を $ \theta_{1} > \theta_{0} $ を満たす実数とする。
このとき、検定統計量 $ T(x) $ に関する片側検定 $ \phi $ に対して、ある実数 $ k_{0} $ が存在して、$ \mathbb{R}^{N} $ 上の関数
$$
g(x) := f (x; \theta_{1}) - k_{0} f (x; \theta_{0})
$$
が以下の条件を満たすようにできる。
$$
T(x) > a \Longrightarrow g (x) > 0 \\
T(x) = a \Longrightarrow g (x) = 0 \\
T(x) < a \Longrightarrow g (x) < 0
$$
*Proof*: 確率モデルが単調尤度比を持つため、ある $ \mathbb{R} $ 上の（狭義）単調増加関数 $ R (t) $ が存在して、尤度比 $ L(x) := \frac { f (x | \theta_{1} ) } { f (x | \theta_{0} )} $ に対して $ R(T(x)) = L(x) $ と書ける。

よって、$ k_{0} = R(a) $ とおけば、
$$
T(x) > a & \Longrightarrow & R(T(x)) > k_{0} & \Longleftrightarrow & g (x) > 0, \\
T(x) = a & \Longrightarrow & R(T(x)) = k_{0} & \Longleftrightarrow & g (x) = 0, \\
T(x) < a & \Longrightarrow & R(T(x)) < k_{0} & \Longleftrightarrow & g (x) < 0
$$
となるため、主張が示せた。

$ \Box $



