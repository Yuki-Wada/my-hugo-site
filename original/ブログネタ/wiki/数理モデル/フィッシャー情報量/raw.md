---
title: 'フィッシャー情報量'
description: 'フィッシャー情報量'
date: '2025-01-19'
categories: []
weight: 999
math: true
---



**Definition** （フィッシャー情報量）
$$
I_{n} (\theta) := \mathbb{E} \left[ \bigg( \frac{d} {d \theta} \log f_{n} (\bold{X} | \theta) \bigg)^{2} \right]
$$

$$
I_{n} (\theta) := \mathbb{E} \left[ \frac{ \partial } { \partial \theta_{i} } \log f_{n} (\bold{X} | \theta) \cdot \frac{ \partial } { \partial \theta_{j}} \log f_{n} (\bold{X} | \theta) \right]
$$


**Proposition** フィッシャー情報行列は以下のように書ける。
$$
\begin{align}
I_{n} (\theta) := &
\mathbb{E} \left[ \frac{ \partial } { \partial \theta_{i} } \log f_{n} (\bold{X} | \theta) \cdot \frac{ \partial } { \partial \theta_{j}} \log f_{n} (\bold{X} | \theta) \right] \\
= & - \mathbb{E} \left[ \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } \log f_{n} (\bold{X} | \theta) \right]
\end{align}
$$
*Proof* 以下のように式変形できる。
$$
\begin{align}
& \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } \log f_{n} (\bold{X} | \theta) \\
= & \frac{ \partial } { \partial \theta_{i} } \frac { \frac{ \partial } { \partial \theta_{j} } f_{n} (\bold{X} | \theta)} {f_{n} (\bold{X} | \theta)} \\
= & \frac { \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } f_{n} (\bold{X} | \theta)} {f_{n} (\bold{X} | \theta)} - 
\frac { \frac{ \partial } { \partial \theta_{i} } f_{n} (\bold{X} | \theta)} {f_{n} (\bold{X} | \theta)} \cdot
\frac { \frac{ \partial } { \partial \theta_{j} } f_{n} (\bold{X} | \theta)} {f_{n} (\bold{X} | \theta)} \\
= & \frac { \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } f_{n} (\bold{X} | \theta)} {f_{n} (\bold{X} | \theta)} -
\left( \frac{ \partial } { \partial \theta_{i} } \log f_{n} (\bold{X} | \theta) \right) \cdot \left( \frac{ \partial } { \partial \theta_{j} } \log f_{n} (\bold{X} | \theta) \right)
\end{align}
$$
ここで両辺の期待値を取ると、
$$
\mathbb{E} \left[ \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } f_{n} (\bold{X} | \theta) \right] =
\frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } \mathbb{E} \left[ f_{n} (\bold{X} | \theta) \right] = \frac{ \partial^{2} } { \partial \theta_{i} \partial \theta_{j} } 1 = 0
$$
であることから、所望の等式が示せた。$ \Box $

