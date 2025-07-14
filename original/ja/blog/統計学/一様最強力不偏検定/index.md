---
title: '一様最強力不偏検定'
description: '一様最強力不偏検定'
slug: 'uniformly-most-powerful-unbiased-test'
date: '2025-01-19'
weight: 999
categories:
  - 統計学
math: true
draft: true
---





**Definition（有意水準 $ \alpha $ の一様最強力不偏検定）**

仮説検定 $ \phi $ が次の条件を満たすとき、有意水準 $ \alpha $ の一様最強力不偏検定であるという。

- 仮説検定が有意水準 $ \alpha $ の不偏検定である。
- 任意の有意水準 $ \alpha $ の不偏検定 $ \tilde{\phi} $ に対して、$ \beta (\theta_{1}; \tilde{\phi}) \leq \beta (\theta_{1}; \phi) \,\, (\forall \theta_{1} \in \Theta_{1}) $ が成り立つ。



<br><br>

## Appendix: 主張（一様最強力不偏検定が存在すること）の証明

----

**Proposition**

指数型分布族は単調尤度比を持つ。

*Proof*: 確率モデルが指数型分布族であるため、
$$
f (x; \theta_{1}) = \exp \left( (\theta_{1} - \theta_{0}) T(x) - (A(\theta_{1}) - A(\theta_{0}) \right) f (x; \theta_{0})
$$
であるため、$ R(t) := \exp \left( (\theta_{1} - \theta_{0}) t - (A(\theta_{1}) - A(\theta_{0}) \right) $ とおけば、確率モデルが単調尤度比を持つことが示せた。

$ \Box $



**Proposition**

確率モデルが指数型分布族であるとし、$ \theta_{1} $ を $ \theta_{1} \neq \theta_{0} $ を満たす実数とする。
このとき、検定統計量 $ T(x) $ に関する両側検定 $ \phi $ に対して、ある実数 $ k_{0}, k_{1} $ が存在して、$ \mathbb{R}^{N} $ 上の関数
$$
g(x) := f (x; \theta_{1}) - k_{0} f (x; \theta_{0}) - k_{1} \frac{\partial} {\partial \theta} f (x; \theta_{0})
$$
が以下の条件を満たすようにできる。
$$
T(x) < a, b < T(x) & \Longrightarrow & g (x) > 0, \\
T(x) = a, b & \Longrightarrow & g (x) = 0, \\
a < T(x) < b & \Longrightarrow & g (x) < 0. \\
$$
*Proof*: 確率モデルが指数型分布族であるため、確率密度関数 $ f (x | \theta) $ が存在して $ f (x | \theta) := h(x) \exp \left( \theta \cdot T(x) - A(\theta) \right) $ と書ける。
$$
f (x; \theta_{1}) = \exp \left( (\theta_{1} - \theta_{0}) T(x) - (A(\theta_{1}) - A(\theta_{0}) \right) f (x; \theta_{0}), \\
\frac{\partial} {\partial \theta} f (x; \theta_{0}) = (T(x) - A'(\theta_{0})) f (x; \theta_{0})
$$
であるため、
$$
g(x) =
\left( \exp \left( (\theta_{1} - \theta_{0}) T(x) - (A(\theta_{1}) - A(\theta_{0}) \right)
- k_{0} - k_{1} (T(x) - A'(\theta_{0})) \right) f (x; \theta_{0})
$$
となることから、
$$
\begin{aligned}
& g(x) f (x; \theta_{0})^{-1} \exp \left(A(\theta_{1}) - A(\theta_{0}) \right) \\
= & \exp \left( C_{1} T(x) \right) - k_{0} C_{0} - k_{1} C_{0} (T(x) - A'(\theta_{0})) \\
= & \exp \left( C_{1} T(x) \right) - K_{0} - K_{1} T(x)\\
\end{aligned}
$$
と式変形できる。このとき、$ C_{0} := \exp \left(A(\theta_{1}) - A(\theta_{0}) \right), C_{1} := \theta_{1} - \theta_{0}, K_{0} := k_{0} C_{0} - k_{1} C_{0} A'(\theta_{0}), K_{1} := k_{1}C_{0} $ と置いた。

直線 $ y = K_{0} x + K_{1} $ が点 $ (a, \exp(C_{1} a)), (b, \exp(C_{1} b))$ を通るように $ K_{0}, K_{1} $ を定めると、指数関数の凸性から、 
$$
T(x) < a, b < T(x) & \Longrightarrow & g (x) > 0, \\
T(x) = a, b & \Longrightarrow & g (x) = 0, \\
a < T(x) < b & \Longrightarrow & g (x) < 0 \\
$$
であることがわかる。$ K_{0}, K_{1} $ が決まれば $ k_{0}, k_{1} $ が定まるため、示すことができた。

$ \Box $



**Theorem（指数型分布族に対して両側検定実施時に有意水準 $ \alpha $ の一様最強力不偏検定が存在する）**

確率モデルが指数型分布族であるとし、$ \alpha $ を $ 0 < \alpha < 1 $ を満たす実数とする。
このとき、「帰無仮説:  $ \theta = \theta_{0} $、対立仮説: $ \theta \neq \theta_{0} $」となる仮説検定に対して、有意水準 $ \alpha $ の一様最強力不偏検定が存在する。

*Proof*: 

(1) 確率モデルが指数型分布族であるため、Proposition から以下の条件を満たす検定統計量 $ T(x) $に関する両側検定 $ \phi $ が存在する。
$$
\int \phi(x) f (x; \theta_{0}) = \alpha, \\
\int \phi (x) \cdot \frac {\partial} {\partial \theta} f (x; \theta_{0}) dx = 0.
$$
確率モデルが指数型分布族であるため、Proposition から任意の $ \theta_{1} \neq \theta_{0} $ に対して、$ \theta_{0}, \theta_{1} $ に依存する実数 $ k_{0}(\theta_{0}, \theta_{1}), k_{1}(\theta_{0}, \theta_{1}) $ が存在して、
$$
g(x) := f (x; \theta_{1}) - k_{0} f (x; \theta_{0}) - k_{1} \frac{\partial} {\partial \theta} f (x; \theta_{0})
$$
が両側検定 $ \phi $ と整合的にとることができる。

(2) 両側検定 $ \phi $ が一様最強力不偏検定であることを示そう。任意の有意水準 $ \alpha $ の不偏検定 $ \tilde{\phi} $ をとる。

まず、$ \tilde{\phi} $ が有意水準 $ \alpha $ の検定であることから、$ \int \tilde{\phi} (x) f (x; \theta_{0}) dx \leq \alpha $ である。

次に、$ \tilde{\phi} $ が不偏検定であることから、 $ \theta \neq \theta_{0} $ は $ \int \tilde{\phi} (x) f (x; \theta) dx \geq \alpha $ なので、$ \int \tilde{\phi} (x) f (x; \theta) dx $ は $ \theta = \theta_{0} $ で最小値を取るため、
$$
\int \tilde{\phi} (x) \cdot \frac {\partial} {\partial \theta} f (x; \theta_{0}) dx
= \frac {\partial} {\partial \theta} \int \tilde{\phi} (x) f (x; \theta_{0})
= 0
$$
とならなければならない。

よって、Neyman–Pearson の定理 2 を適用することで、
$$
\int \tilde{\phi} (x) f (x; \theta_{1}) dx \leq \int \phi (x) f (x; \theta_{1}) dx
$$
であることがわかる。

(3) 最後に両側検定 $ \phi $ が不偏検定であることを示そう。これは検定関数 $ \tilde{\phi} $ として $ \tilde{\phi} \equiv \alpha $ の定数関数をとることで、$ \alpha = \int \tilde{\phi} (x) f (x; \theta_{1}) dx \leq \int \phi (x) f (x; \theta_{1}) dx $ となることからわかる。

(4) 以上より、両側検定 $ \phi $ が一様最強力不偏検定であることが示せた。

$ \Box $



