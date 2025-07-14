---
title: 'フィッシャー情報量'
description: 'フィッシャー情報量や情報行列に関連する情報を'
date: '2025-01-19'
categories: []
weight: 999
math: true
draft: true
---



**Definition** （フィッシャー情報量）
\\[ \\begin{aligned}  I _ {n} (\\theta) := \\mathbb{E} \\left[ \\bigg( \\frac{d} {d \\theta} \\log f _ {n} (\\bold{X} | \\theta) \\bigg)^{2} \\right]  \\end{aligned} \\]

\\[ \\begin{aligned}  I _ {n} (\\theta) := \\mathbb{E} \\left[ \\frac{ \\partial } { \\partial \\theta _ {i} } \\log f _ {n} (\\bold{X} | \\theta) \\cdot \\frac{ \\partial } { \\partial \\theta _ {j}} \\log f _ {n} (\\bold{X} | \\theta) \\right]  \\end{aligned} \\]


**Proposition** フィッシャー情報行列は以下のように書ける。
\\[ \\begin{align} I _ {n} (\\theta) := & \\mathbb{E} \\left[ \\frac{ \\partial } { \\partial \\theta _ {i} } \\log f _ {n} (\\bold{X} | \\theta) \\cdot \\frac{ \\partial } { \\partial \\theta _ {j}} \\log f _ {n} (\\bold{X} | \\theta) \\right] \\\\ = & - \\mathbb{E} \\left[ \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } \\log f _ {n} (\\bold{X} | \\theta) \\right] \\end{align} \\]
*Proof* 以下のように式変形できる。
\\[ \\begin{align} & \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } \\log f _ {n} (\\bold{X} | \\theta) \\\\ = & \\frac{ \\partial } { \\partial \\theta _ {i} } \\frac { \\frac{ \\partial } { \\partial \\theta _ {j} } f _ {n} (\\bold{X} | \\theta)} {f _ {n} (\\bold{X} | \\theta)} \\\\ = & \\frac { \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } f _ {n} (\\bold{X} | \\theta)} {f _ {n} (\\bold{X} | \\theta)} -  \\frac { \\frac{ \\partial } { \\partial \\theta _ {i} } f _ {n} (\\bold{X} | \\theta)} {f _ {n} (\\bold{X} | \\theta)} \\cdot \\frac { \\frac{ \\partial } { \\partial \\theta _ {j} } f _ {n} (\\bold{X} | \\theta)} {f _ {n} (\\bold{X} | \\theta)} \\\\ = & \\frac { \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } f _ {n} (\\bold{X} | \\theta)} {f _ {n} (\\bold{X} | \\theta)} - \\left( \\frac{ \\partial } { \\partial \\theta _ {i} } \\log f _ {n} (\\bold{X} | \\theta) \\right) \\cdot \\left( \\frac{ \\partial } { \\partial \\theta _ {j} } \\log f _ {n} (\\bold{X} | \\theta) \\right) \\end{align} \\]
ここで両辺の期待値を取ると、
\\[ \\begin{aligned}  \\mathbb{E} \\left[ \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } f _ {n} (\\bold{X} | \\theta) \\right] = \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } \\mathbb{E} \\left[ f _ {n} (\\bold{X} | \\theta) \\right] = \\frac{ \\partial^{2} } { \\partial \\theta _ {i} \\partial \\theta _ {j} } 1 = 0  \\end{aligned} \\]
であることから、所望の等式が示せた。\\( \Box \\)

