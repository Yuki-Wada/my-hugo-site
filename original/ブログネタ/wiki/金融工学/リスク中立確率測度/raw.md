---
title: 'リスク中立確率測度'
description: 'リスク中立確率測度'
date: '2025-01-03'
slug: '/risk-neutral-probability'
categories:
    - mathematical-model
weight: 30
math: true
draft: true
---


$$
dS(t) = \alpha (t) S(t) dt + \sigma (t) S(t) dW(t)
$$

$$
S(t) = S(0) \exp \left( \int_{0}^{t} \sigma(s) dW(s)
+ \int_{0}^{t} \left( \alpha(s) - \frac{1}{2} \sigma^{2} (s) \right) ds \right)
$$

金利仮定
$$
D(t) = \exp \left( - \int_{0}^{t} R(s) ds \right)
$$

$$
D(t) S(t)
$$

$$
\begin{align}
d \left(D(t) S(t) \right) & = D(t) dS(t) + S(t) dD(t) + dD(t) dS(t) \\
& = D(t) \left( \alpha (t) S(t) dt + \sigma (t) S(t) dW(t) \right) + S(t) \cdot (- R(t) D(t) dt) \\
& = \sigma(t) D(t) S(t) \left( \frac{ \alpha (t) - D(t) }{ \sigma(t) } dt + dW(t) \right) 
\end{align}
$$
以下を満たす測度をリスク中立確率測度という。
$$
d (D(t) S(t)) = \sigma (t) D(t) S(t) d \tilde{W}(t)
$$
**ギルザノフの定理**



例えば、ギルザノフの定理で

$ \widetilde {\mathbb{P}} $ は金融商品セット $ \{ D(t) S(t) \} $ に対するリスク中立確率測度である。



**マルチンゲールの表現定理**
