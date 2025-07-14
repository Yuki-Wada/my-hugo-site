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


\\[ \\begin{aligned}  dS(t) = \\alpha (t) S(t) dt + \\sigma (t) S(t) dW(t)  \\end{aligned} \\]

\\[ \\begin{aligned}  S(t) = S(0) \\exp \\left( \\int _ {0}^{t} \\sigma(s) dW(s) + \\int _ {0}^{t} \\left( \\alpha(s) - \\frac{1}{2} \\sigma^{2} (s) \\right) ds \\right)  \\end{aligned} \\]

金利仮定
\\[ \\begin{aligned}  D(t) = \\exp \\left( - \\int _ {0}^{t} R(s) ds \\right)  \\end{aligned} \\]

\\[ \\begin{aligned}  D(t) S(t)  \\end{aligned} \\]

\\[ \\begin{align} d \\left(D(t) S(t) \\right) & = D(t) dS(t) + S(t) dD(t) + dD(t) dS(t) \\\\ & = D(t) \\left( \\alpha (t) S(t) dt + \\sigma (t) S(t) dW(t) \\right) + S(t) \\cdot (- R(t) D(t) dt) \\\\ & = \\sigma(t) D(t) S(t) \\left( \\frac{ \\alpha (t) - D(t) }{ \\sigma(t) } dt + dW(t) \\right)  \\end{align} \\]
以下を満たす測度をリスク中立確率測度という。
\\[ \\begin{aligned}  d (D(t) S(t)) = \\sigma (t) D(t) S(t) d \\tilde{W}(t)  \\end{aligned} \\]
**ギルザノフの定理**



例えば、ギルザノフの定理で

\\( \widetilde {\mathbb{P}} \\) は金融商品セット \\( \{ D(t) S(t) \} \\) に対するリスク中立確率測度である。



**マルチンゲールの表現定理**
