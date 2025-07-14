---
title: '凸集合の性質'
description: '凸集合の性質'
slug: 'convex-set'
date: '2025-07-13'
weight: 999
categories:
  - 最適化
aliases: 
  - "/convex-set/"
math: true
draft: true
---

## 概要

#### この記事で伝えたいこと
- この記事で伝えたいこと ← ★重要★
- 記事の対象者

#### 記事の対象者
- 凸集合で使う定義をまとめて確認したい人
- 凸集合の分離定理について知りたい人



<br><br>



## 凸集合の定義

#### Definition (凸集合)
> ベクトル空間 $V$ の部分集合 $C$ を考えます。
> 任意の $x, y \in C$ と任意の $0 \leq \lambda \leq 1$ に対して、
> $$ \lambda x + (1 - \lambda) y \in C $$
> が成り立つとき、$C$ を凸集合と定義します。


#### Propositon（凸集合の共通部分は凸集合）
> 凸集合の集合族 $(C_{\lambda})_{\lambda \in \Lambda}$ の共通部分 $\cap C_{\lambda}$ も凸集合です。
> <details><summary>(Proof)</summary><div>
> 
> 証明略。
> 
> </div></details>

#### Definition (凸包)
> 集合 $A$ を含む最小の凸集合を $A$ の凸包と定義し、$\text{conv}A$ と表記します。


凸包の定義を見る限り、具体的にどのような元が凸包に含まれるかが明記されていません。
ですが、集合 $A$ の凸包が $A$ を含む最小の凸集合であるという性質から、有限個の点 $x_1, \ldots, x_k \in A$ の凸結合（convex combination）全体の集合が凸包と一致することがわかります。


#### Proposition (凸包の具体的な表現)
> 集合 $A$ の凸包 $\text{conv}(A)$ は次のように書き下すことができます:
> $$ \mathrm{conv}(A) = \left\{ \sum_{i=1}^k \lambda_i x_i \;\middle|\; k \in \mathbb{N},\; x_i \in A,\; \lambda_i \geq 0,\; \sum_{i=1}^k \lambda_i = 1 \right\} $$
> 
> <details><summary>(Proof)</summary><div>
> 
> 証明略。
> 
> </div></details>

**Propositon（凸集合の閉包は凸集合）**  
> 凸集合の閉包は凸集合です。
> <details><summary>(Proof)</summary><div>
> 
> $C$を凸集合、$\overline{C}$ を $C$ の閉包とします。任意に $x, y \in \overline{C}$、および $\lambda \in [0,1]$ をとります。
> $x \in \overline{C}$, $y \in \overline{C}$ なので、それぞれ以下の条件を満たす $C$ 内の点列 $\{x_n\} \subset C$, $\{y_n\} \subset C$ が存在します:
> $$ x_n \to x,\quad y_n \to y \quad (n \to \infty). $$
> $C$ が凸集合であるため、各 $n$ に対して $ z_n := \lambda x_n + (1 - \lambda) y_n$ と定義すると $z_{n} \in C$ です。
> $\overline{C}$ が閉集合なので $n \to \infty$ のときに $z_{n}$ の収束先が存在するならばその収束先は $\overline{C}$ の元です。  
> また $x_{n}, y_{n}$ の取り方から、$(n \to \infty)$ のときに $z_n$ は $\lambda x + (1 - \lambda) y \quad (n \to \infty)$ に収束します。 
> 
> よって、$ \lambda x + (1 - \lambda) y \in \overline{C} $であることが示せました。
> 
> </div></details>


一方で、閉集合の凸包は閉集合とは限りません（最初私は閉集合の凸包は閉集合となると思い込んでいましたが反例がありました）。


**Propositon（閉集合の凸包は閉集合とは限らない）**  
> 閉集合の凸包が閉集合とならない反例が存在します。
> 
> <details><summary>(Proof)</summary><div>
> 
> $$ A := \{ (x, y) | xy \geq 1, x > 0, y > 0 \} \cup {(0, 0)} $$
> とおく。このとき、以下が成り立ちます。
> - $A$ が閉集合です。（理由: $(x, y) \to xy$ が連続なので $\{ (x, y) | xy < 1, x > 0, y > 0 \}$ が開集合となるため。）
> - $ \text{conv}(A) = \{ (x, y) | x > 0, y > 0 \} \cup {(0, 0)}$。（理由: $x > 0, y > 0, xy < 1$ を満たす $x, y$ に対して $\lambda = (x_{0}y_{0})^{-\frac{1}{2}} > 1$ とおくと $(\lambda x)\cdot(\lambda y) = 1$ となるため。）
> - $ \text{conv}(A)$ が閉集合ではありません。 
>
> よって、反例が存在することを示せました。
> 
> </div></details>


閉集合の凸包が閉集合になるとは限らないため、閉集合を考える場合においては単なる凸包では捉えたい対象を十分にとらえきれない可能性があります。
幸いにも、凸集合の共通部分が凸集合となるのと同じく、閉集合の共通部分も閉集合となることから、$A$ を含む最小の閉凸集合が存在することがわかります。


#### Definition (閉凸包)
> 集合 $A$ を含む最小の閉凸集合を $A$ の閉凸包と定義します。



<br><br>



## 凸集合の分離定理

**Propositon（凸集合の分離定理 1）**  
> $C \in \mathbb{R}^n$ を凸集合とします。任意の $x_{0} \notin Cl(C)$ を固定します。
> このとき、以下の条件を満たす $a, b \in \mathbb{R}^n$ が存在します。
> $$ \langle a, c\rangle \geq b \quad (\forall c \in C), \\
  \langle a, x_{0}\rangle < b $$
> 
> <details><summary>(Proof)</summary><div>
> 
> [統計的学習理論](#kanamori)の補題 B.2 を参照。
> 
> </div></details>


**Corollary（凸集合の分離定理 1）**  
> $C \in \mathbb{R}^n$ を凸集合とします。任意の $x_{0} \notin Cl(C)$ を固定します。
> このとき、以下の条件を満たす $a, b \in \mathbb{R}^n$ が存在します。
> $$ \langle a, c\rangle \geq b \quad (\forall c \in C), \\
  \langle a, x_{0}\rangle < b $$
> 
> <details><summary>(Proof)</summary><div>
> 
> 証明は文献を参照。
> 
> </div></details>

<h2 id="section2">セクション2</h2>


#### Propositon（凸集合の分離定理 2）
> $X, Y \in \mathbb{R}^n$ を凸集合と、さらに $ X \cap Y = \empty$ を満たすとします。
> このとき、以下の条件を満たす $a, b \in \mathbb{R}^n$ が存在します:
> $$ \langle a, x \rangle \geq b \quad (\forall x \in X), \\
  \langle a, y \rangle \leq b \quad (\forall y \in Y). $$
> 
> <details><summary>(Proof)</summary><div>
> 
> 「凸集合の分離定理 1」と同様に
> 
> </div></details>

#### 補足説明
凸集合の分離定理は有限次元実ベクトル空間 $\mathbb{R}^{N}$ の場合にだけ成立するのではなく、Banach 空間の場合であっても成立することが知られており、
関数解析学における Hahn-Banach の分離定理がそれに該当します。

**Theorem（Hahn-Banach の分離定理）**  
> $V$ を、K (= ℝ または ℂ) に対する位相ベクトル空間とし、$A$ および $B$ を、$V$ の空でない凸な部分集合とし、A ∩ B = ∅ とする。このとき、次が成立する:
> - A が開ならば、ある連続線型作用素 λ: V → K および実数 t ∈ R が存在して、Re λ(a) < t ≤ Re λ(b) がすべての a ∈ A, b ∈ B に対して成立する。
> - $V$ が局所凸、$A$ がコンパクトで、$B$ が閉ならば、ある連続線型作用素 $\lambda: V \rightarrow K$ および実数 $s, t \in \mathbb{R}$ が存在して、$Re \lambda(a) < t < s < Re \lambda(b)$ がすべての $a ∈ A$, $b ∈ B$ に対して成立する。

定理の主張を見てみると、凸集合の分離定理と全く同じことを述べていることがわかります。
とはいえ、この定理を有限次元の場合に具体的に示すことで、凸集合の持つ性質がより理解しやすくなったのではないかと思います。



<br><br>



## 結論 (conclusion or point)



<br><br>



## 参考文献
- <a id="kanamaori"></a>金森敬文（2015）『統計的学習理論』共立出版（機械学習プロフェッショナルシリーズ）


