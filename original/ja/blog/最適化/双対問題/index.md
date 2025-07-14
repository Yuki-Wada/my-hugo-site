---
title: '双対問題'
description: '双対問題'
slug: 'dual-problem'
date: '2025-07-13'
weight: 999
categories:
  - 最適化
math: true
draft: true
---

## 概要

#### この記事で伝えたいこと
今まで双対問題について勉強してきたのですが、そのたびに忘れてしまったので、
メモとして記載しております。  
双対問題がどのように導出されているのか、何が本質的に重要なのか、どのような条件の下で成り立つのかといった点は、一箇所に整理されている資料は意外と少ないように思います。
そこでこの記事では、これらのポイントについて概略的に整理し、理解の助けとなるようにまとめてみたいと思います。

#### この記事の対象者
- 双対問題の定義をしっかり
- 双対問題の重要性をしっかり理解したい方
- 強双対定理が成り立つための条件をしっかりと理解したい方

#### 参考記事
- 凸関数の定義・性質は[この記事](/convex-function/#section2)も参考にしてください。
- 不等式制約付き最適化問題については[この記事](/inequality-constrained-optimization/)も参考にしてください。



<br><br>



## 双対問題
### Definition (双対問題)
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> ラグランジュ緩和関数
> $$
  L(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \lambda_i g_i(x) + \sum_{j=1}^{p} \mu_j h_j(x)
> $$
> に対して、
> $$
  g(\mu, \lambda) := \inf_{x} L(x, \lambda, \mu)
> $$
> とおきます。
> このとき、以下の最適化問題を元の問題の双対問題と定義します: 
> $$
  \text{supremum} \,\, g(\mu, \lambda) .
> $$
> また、元の問題を主問題といいます。

### Propositon (双対問題の凸性)
> $g(\mu, \lambda)$ は凸関数です。

### 弱双対定理

双対問題の定義の仕方から、
主問題の最適値が双対関数の最適値で下から抑えられることがわかります。

**Propositon (弱双対定理)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> 実行可能解の集合を $F$ とします。
> このとき、以下の不等式が成り立ちます。
> $$ \inf_{x \in F} f(x) \geq \sup_{\mu, \lambda} g(\mu, \lambda) $$
> <details><summary>(Proof)</summary><div>
> 
> $$ \min_{x} f(x) \geq \min_{x} \max_{\mu, \lambda} L(x, \lambda, \mu) \geq \max_{\mu, \lambda} \min_{x} L(x, \lambda, \mu) \geq \max_{\mu, \lambda} g(\mu, \lambda) $$
> となるため。
> 
> </div></details>

### 強双対定理
弱双対定理によって、主問題の最適値と双対問題の最適値の差（双対ギャップ）は常に 0 以上になることがわかります。
特に、主問題と双対問題の最適値が一致する（すなわち dual gap = 0）場合には、双対問題を解くことで主問題の最適値を求めることができます。
この場合は、双対問題を解くことの意義が明確になります。

この dual gap が 0 になるためには、ある条件が満たされている必要があります。
こうした条件のもとで 双対ギャップが 0 になることを保証する定理を、一般に強双対定理（strong duality theorem） と呼びます。
中でも代表的な十分条件として知られているのが、次節で説明するスレーター条件です。
ここでは、強双対定理の主張を簡単にまとめておきます。

**Statement (強双対定理)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> 実行可能解の集合を $F$ とします。
> 以下の等式が成り立つとき、この最適化問題は強双対定理が成り立つといいます。
> $$
  \inf_{x \in F} f(x) = \sup_{\mu, \lambda} g(\mu, \lambda)
  $$



<br><br>



## 強双対定理の成立条件

#### スレーター条件



**Definition (スレーター条件)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。
> このとき、この問題が凸最適化問題で、$h_{j}$ がアフィン関数であり、さらに、以下の条件
> $$ g_i(x_0) < 0 \quad (\forall \, i), \quad h_j(x_0) = 0 \quad (\forall \, j) $$
> を満たす $x_{0}$ が存在するとき、この最適化問題はスレーター条件を満たすと定義します。


実際に最適化問題がスレーター条件を満たすならば、強双対定理が成り立つことを示すことができます。このことを Proposition の形でまとめておきます。


**Propositon (スレーター条件が満たされるならば強双対定理が成り立つ)**
> 不等式制約付きの**凸最適化問題** $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ がスレーター条件を満たすならば、強双対定理が成り立ちます。
> <details><summary>(Proof)</summary><div>
> 
> (1) 文献にある通り、最初は $\tilde{x}$ が内点であり、行列 $A$ の階数がfull であるケースを考えます。
> 次の集合を考えます。
> $$ \mathcal{A} = \{ (u, v, t) | ∃x ∈ D, fi(x) ≤ ui, i = 1, . . . , m, hi(x) = vi, i = 1, . . . , p, f0(x) ≤ t\}, \\
  \mathcal{B} = {(0, 0, s) ∈ Rm × Rp × R | s < p⋆} $$
> まず、この問題が凸最適化問題であるため $\mathcal{A}$ は凸集合です。
> 次に $\mathcal{A} \cap \mathcal{B} = \empty$ であることがわかります。
> よって、凸集合の分離定理から、以下の条件を満たす $\lambda, \mu, \nu \in \mathbb{R}^{n}$ が存在します:
> $$ \langle \lambda, u \rangle + \langle \nu, b \rangle + \mu \cdot t \geq \alpha \quad 
  \left( (u, v, t)\in \mathcal{A} \right), \\
  \langle \lambda, u \rangle + \langle \mu, b \rangle + \nu \cdot t \leq \alpha \quad
  \left( (u, v, t)\in \mathcal{B} \right). $$  
>   
> $\mu > 0$ を示しましょう。一旦 $\mu = 0$ が正しいと仮定します。
> $$ \sum_{i=} \lambda_{i} g_{i}(x)  + ν^{T} (Ax − b) \geq 0. $$
> $A \tilde{x} − b = 0$ なので、$ \sum_{i=1} \lambda_{i} g_{i}(\tilde{x}) \geq 0$ とならなければなりません。
> 一方で、$g_{i}(\tilde{x}) < 0$ となることから $\lambda_{i} \geq 0$ と合わせて、$\lambda_{i} g_{i}(\tilde{x}) \leq 0$ も成り立つ必要があります。
> よって、各不等号は等号で成立する必要があり、$g_{i}(\tilde{x}) \neq 0$ より $\lambda_{i} = 0$ が示せます.
> 
> $\lambda_{i} = 0$ から $ν^{T} (A x − b) \geq 0$ とならなければなりません。
> 一方で $ν^{T} (A \tilde{x} − b) = 0$ であるから、$ν^{T} A (x - \tilde{x}) \geq 0$ が成り立つ必要があります。
> これは $\tilde{x}$ が内点であること、 $A$ のランクがfullであることと矛盾します。
> 
> (2) 行列 $A$ の階数が行数と一致しないケースを考えます。  
> 実行可能解 $\tilde{x}$ が存在することから、一次従属になる行を取り除いてしまっても制約条件が変わらないことがわかります。
> よって、一次従属になる行を取り除いてしまえば (1) に帰着可能です。
> 
> (3) $\tilde{x}$ が $\mathbb{R}^{N}$ 自身の内点ではないケースを考えます。  
> この場合、ある部分アフィン空間 $A$ が存在して、$\tilde{x}$ は $A$ において内点となっています。
> よって、アフィン空間 $A$ 上に制限すれば、(2) に帰着可能です。
> 
> 以上より、示すことができました。
> 
> </div></details>


#### 緩和されたスレーター条件
強双対定理が成り立つことは双対問題を解くモチベーションを出す上で重要でした。十分条件の一つがスレーター条件であることからスレーター条件の重要性が理解できます。
一方で、スレーター条件は条件として少し厳しすぎるようにも見えます。
例えば、線形計画法の問題を考える場合に、不等式制約に対して不等号が成り立っているもの


**Definition (緩和されたスレーター条件)**
> 不等式制約付き**凸最適化問題** $\left( f, \{g_{i}\} \cup \{g'_{i'}\}, \{h_{j}\} \right)$ を考えます。
> このとき、この問題が凸最適問題で、$g'_{i'}, h_{j}$ がアフィン関数であり、さらに、以下の条件
> $$ g_i(x_0) < 0 \quad (\forall \, i), \quad g'_{i'} (x_0) \leq 0 \quad (\forall \, i'), \quad h_j(x_0) = 0 \quad (\forall \, j) $$
> を満たす $x_{0}$ が存在するとき、この最適化問題は緩和されたスレーター条件を満たすと定義します。

### Propositon (スレーター条件を緩和しても強双対定理が成り立つ)  
> 不等式制約付き**凸最適化問題** $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ が緩和されたスレーター条件を満たすならば、強双対定理が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> $I'$ を $\{1, \dots, i' \}$ の任意の部分集合とします。 
> $$F(I)$$  
> このとき、実行可能解は $\cup F(I)$と一致します。
> 各 $F(I)$においてはスレーター条件が成立していることを示せます。
> よって成立が言えました。
> </div></details>



<br><br>



## 双対問題と KKT 条件

**Propositon (主・双対問題に最適解が存在するならば KKT 条件が成り立つ)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。このとき、主問題の最適解 $ x^{\ast\ast}$、双対問題の最適解 $(\mu^{\ast}, \lambda^{\ast})$ が存在し、かつ、強双対定理が成立するならば、$(x, \mu^{\ast}, \lambda^{\ast})$ において KKT 条件が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> (1) Primal feasibility（実行可能性）と feasibility（双対実行可能性）は前提条件から成り立つことがわかります。  
> (2) Complementary slackness（相補性条件）が成り立つことを示します。
> 最適化問題の実行可能解の集合を $F$ とします。
> ラグランジュ緩和関数 に対して、
> $$ \begin{align}
  1
  \end{align} $$
> と式変形できる。ここで、強双対定理が成り立つことから、$f(x^{\ast}) = g(\mu^{\ast}, \lambda^{\ast})$ となるため、上記の不等号は全て等号になることがわかります。
> よって、
> $$
>   \sum_{i=1}^{m} \lambda_{i}^{a} g_{i}(x^{a}) + \sum_{j=1}^{p} \mu_{j}^{a} h_{j}(x^{\ast}) = 0
> $$
> となることがわかります。
> $$ 
>   L(x^{\ast}, \mu^{\ast}, \lambda^{\ast}) = \inf_{x} L(x, \mu^{\ast}, \lambda^{\ast})
> $$
> であることから、$L(x, \mu^{*}, \lambda^{*})$ を $x$ の関数としてみたときに $x = x^{*}$ で極小となることがわかるため、Stationarity（停留条件）が成り立つこともわかる。
> 
> </div></details>

**Propositon (KKT 条件が成り立つならば主・双対問題に最適解が存在する)**
> 不等式制約付き最適化問題 $\left( f, \{g_{i}\}, \{h_{j}\} \right)$ を考えます。さらに、この問題が凸最適化問題であるとします。
> このとき、$(x, \mu^{\ast}, \lambda^{\ast})$ において KKT 条件を満たすならば、強双対定理が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> Complementary slackness（相補性条件）が成り立つことから、
> $$
  f(x^{\ast}) = f(x^{\ast}) + \sum_{i=1}^{m} \lambda_i^{\ast} g_i(x^{\ast}) + \sum_{j=1}^{p} \mu_j^{\ast} h_j(x^{\ast})
> $$
> が成り立ちます。  
> 次に、この不等式制約付き最適化問題が凸最適化問題であることから、ラグランジュ緩和関数 $L(x, \mu^{\ast}, \lambda^{\ast})$ は $x$ の関数とみたときに凸関数であることがわかります。一般に、凸関数が $x=x^{\ast}$ で停留条件を満たすならば $x=x^{\ast}$ で最小値をとるため、
> $$ 
>   L(x^\ast, \mu^\ast, \lambda^\ast) = \min_{x} L(x, \mu^{\ast}, \lambda^{\ast})
> $$
> が成り立ちます。
> よって、
> $$
>   \begin{align}
>   & f(x^{\ast}) \nonumber \\
>   = & f(x^{\ast}) + \sum_{i=1}^{m} \lambda_i^{\ast} g_i(x^{\ast}) + \sum_{j=1}^{p} \mu_j^{\ast} h_j(x^{\ast}) \nonumber \\
>   = & L(x^{\ast}, \mu^{\ast}, \lambda^{\ast}) \nonumber \\
>   = & \min_{x} L(x, \mu^{\ast}, \lambda^{\ast}) \nonumber \\
>   = & g(\mu^{\ast}, \lambda^{\ast}) \nonumber \\ 
>   \end{align}
> $$
>   と式変形できます。このことから、強双対定理が成り立つことがわかります。$ \Box $
> </div></details>



<br><br>



## フェンシェル双対性















<br><br>



## 結論



<br><br>



## 参考文献
- <a id="kanamaori"></a>金森敬文（2015）『統計的学習理論』共立出版（機械学習プロフェッショナルシリーズ）


