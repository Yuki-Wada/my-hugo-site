---
date: '2025-01-03'
title: 'タイトル名'
linkTitle: Announcing Docsy
description: >
  この記事の概要です。
  タイトル名の下に記事の見出しとして表示されます。
slug: 'template'
author: Yuki Wada
weight: 999
categories:
    - test
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

## 本文1 ― 詳細 (reason)

#### Doob-Mayer 分解

#### 二次変分

#### 二乗マルチンゲール空間の完備性



#### 課題の背景



#### 課題を解決する技術・手法の概要



#### 技術・手法の効果、課題がどう解決されるか



#### 留意点、デメリット



<br><br>

## 本文2 ― 具体例 (example) 

#### 単関数の伊藤積分

#### 伊藤積分

#### 伊藤の公式


<br><br>

## 結論 (conclusion or point)









## Appendix: 確率過程の可測性（measurable process）

確率空間 $(\Omega, \mathcal{F}, \mathbb{P})$ と時刻集合 $T \subset \mathbb{R}_+$（離散 or 連続）上の確率過程
$$
X = \{X_t : \Omega \to \mathbb{R} \}_{t \in T}
$$
があるとします。

#### 定義：可測過程（measurable process）

確率過程 $X: \Omega \times T \to \mathbb{R}$ が可測であるとは、
 積集合 $\Omega \times T$ 上の写像として、以下が成立することをいいます：
$$
(\omega, t) \mapsto X_t(\omega) \quad \text{が } \mathcal{F} \otimes \mathcal{B}(T)\text{-可測}
$$
ここで：

- $\mathcal{F}$ は確率空間上の σ-代数（$\omega$ に関する情報）
- $\mathcal{B}(T)$ は $T \subset \mathbb{R}_+$ のボレル集合（時刻に関する σ-代数）
- $\mathcal{F} \otimes \mathcal{B}(T)$ は積集合上の積 σ-代数

つまり、**$X$ は2変数関数 $(\omega, t)$ として可測である**ということです。



------



#### 定義：可測過程（measurable process）

確率過程 $X: \Omega \times T \to \mathbb{R}$ が可測であるとは、
 積集合 $\Omega \times T$ 上の写像として、以下が成立することをいいます：
$$
(\omega, t) \mapsto X_t(\omega) \quad \text{が } \mathcal{F} \otimes \mathcal{B}(T)\text{-可測}
$$
ここで：

- $\mathcal{F}$ は確率空間上の σ-代数（$\omega$ に関する情報）
- $\mathcal{B}(T)$ は $T \subset \mathbb{R}_+$ のボレル集合（時刻に関する σ-代数）
- $\mathcal{F} \otimes \mathcal{B}(T)$ は積集合上の積 σ-代数

つまり、**$X$ は2変数関数 $(\omega, t)$ として可測である**ということです。



#### 定義：適合過程（measurable process）

確率過程 $X: \Omega \times T \to \mathbb{R}$ が適合過程であるとは、
 積集合 $\Omega \times T$ 上の写像として、以下が成立することをいいます：
$$
(\omega, t) \mapsto X_t(\omega) \quad \text{が } \mathcal{F}_{t} \text{-可測}
$$
ここで：



#### 定義: progressively measurable process（適合過程）

確率過程 $X: \Omega \times T \to \mathbb{R}$ が progressively measurable であるとは、
 積集合 $\Omega \times T$ 上の写像として、以下が成立することをいいます：
$$
(\omega, t) \mapsto X_t(\omega) \quad \text{が } \mathcal{F} \otimes \mathcal{B}(T)\text{-可測}
$$
ここで：

- $\mathcal{F}$ は確率空間上の σ-代数（$\omega$ に関する情報）
- $\mathcal{B}(T)$ は $T \subset \mathbb{R}_+$ のボレル集合（時刻に関する σ-代数）
- $\mathcal{F} \otimes \mathcal{B}(T)$ は積集合上の積 σ-代数

つまり、**$X$ は2変数関数 $(\omega, t)$ として可測である**ということです。



### **確率過程における RLCC（càdlàg）過程の定義**

確率過程 $\{X_t\}_{t \geq 0}$ が RLCC（または càdlàg）であるとは、各サンプルパス $\omega \in \Omega$ に対して、
$$
t \mapsto X_t(\omega)
$$
が RLCC 関数（すなわち右連続で左極限を持つ関数）であることを意味します。

------

### **"Closed" について**

RLCC の "Closed" は文脈によりますが、ほとんどの文献では "Right-continuous with Left Limits"（すなわち càdlàg）という意味で "RL" を使い、"Closed" は **ジャンプ点が離散的または閉集合に収まる**という意味合いで加えられることがあります。ただし、この "Closed" の部分は多くの場合、略されるか省略されるため、**RLCC ≒ càdlàg** として理解されるのが一般的です。

------

### **関連用語**

- **càdlàg（右連続左極限）**：RLCC とほぼ同義（フランス語 *continue à droite, limite à gauche* の略）。
- **càglàd（左連続右極限）**：左連続で右極限をもつ関数。

------

### **例**

- ポアソン過程のサンプルパスは RLCC（càdlàg）です。
- 標準ブラウン運動は連続過程なので trivially càdlàg。

------

RLCC の性質は、停止時刻との組み合わせや Doob のマルチンゲール理論、スキームの定理、伊藤積分の定義などで基本的な前提条件となります。必要であれば、それらとの関係も詳しくご説明できます。





## Appendix: 停止時刻（Stopping Time）の定義

----

確率空間 $(\Omega, \mathcal{F}, \mathbb{P})$ と、時間添字付きのフィルトレーション（情報の流れ） $\{\mathcal{F}_t\}_{t \geq 0}$ が与えられているとします。

**定義：**
 実数値確率変数 $\tau: \Omega \to [0, \infty]$ が **停止時刻**（または**停止時間**、stopping time）であるとは、任意の $t \geq 0$ に対して、
$$
\{\omega \in \Omega : \tau(\omega) \leq t\} \in \mathcal{F}_t
$$
が成り立つことをいいます。

------

#### 直感的な意味

時刻 $\tau$ が停止時刻であるとは、「その時刻が来たかどうか」が時刻 $t$ の情報 $\mathcal{F}_t$ を見ただけで判断できる、ということです。

------

### **例**

1. **到達時刻（初めてある集合に達する時刻）**
    ある過程 $X_t$ に対して、ある閾値 $a$ を初めて超える時刻：
   $$
   \tau = \inf \{ t \geq 0 : X_t \geq a \}
   $$
   は自然な停止時刻の例です。

2. **固定時刻 $T$**
    任意の定数 $T$ は停止時刻です（$\{\tau \leq t\} = \emptyset$ または $\Omega$ なので可測）。





## Appendix: 伊藤積分の定義

----

Definition (単関数に対する伊藤積分の定義)



## Appendix: 測度論で使いうる定義

----

Fatou の補題、優収束定理

ラドンにこでぃむの定理

Jensen の不等式



独立性の補題

Dynkin 族定理

ボレルカンテリの補題



条件付き期待値

条件付き期待値に対する Jensen の不等式



<details>   <summary>空行なし(クリックしてください)</summary>
    ### Heading   1. Foo   2. Bar      * Baz      * Qux          ### Some Code   ```js   function logSomething(something) {     console.log('Something', something);   }   ``` </details>



<br><br>

## 参考文献

----

[1] Ioannis Karatzas, Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed.

