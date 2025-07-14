---
aliases:
- /convex-function/
author: Yuki Wada
categories:
- 最適化
date: '2025-07-13'
description: 凸関数の性質
draft: true
math: true
slug: convex-function
title: 凸関数の性質
weight: 999
---



## 凸集合の定義

#### Definition (凸集合)
> ベクトル空間 \\(V\\) の部分集合 \\(C\\) を考えます。
> 任意の \\(x\, y \in C\\) と任意の \\(0 \leq \lambda \leq 1\\) に対して、
> \\[ \\begin{aligned}  \\lambda x + (1 - \\lambda) y \\in C  \\end{aligned} \\]
> が成り立つとき、\\(C\\) を凸集合と定義します。


#### Propositon（凸集合の共通部分は凸集合）
> 凸集合の集合族 \\((C _ {\lambda}) _ {\lambda \in \Lambda}\\) の共通部分 \\(\cap C _ {\lambda}\\) も凸集合です。
> <details><summary>(Proof)</summary><div>
> 
> 証明略。
> 
> </div></details>

#### Definition (凸包)
> 集合 \\(A\\) を含む最小の凸集合を \\(A\\) の凸包と定義し、\\(\text{conv}A\\) と表記します。


凸包の定義を見る限り、具体的にどのような元が凸包に含まれるかが明記されていません。
ですが、集合 \\(A\\) の凸包が \\(A\\) を含む最小の凸集合であるという性質から、有限個の点 \\(x _ 1\, \ldots\, x _ k \in A\\) の凸結合（convex combination）全体の集合が凸包と一致することがわかります。


#### Proposition (凸包の具体的な表現)
> 集合 \\(A\\) の凸包 \\(\text{conv}(A)\\) は次のように書き下すことができます:
> \\[ \\begin{aligned}  \\mathrm{conv}(A) = \\left\\{ \\sum _ {i=1}^k \\lambda _ i x _ i \\;\\middle|\\; k \\in \\mathbb{N}\,\\; x _ i \\in A\,\\; \\lambda _ i \\geq 0\,\\; \\sum _ {i=1}^k \\lambda _ i = 1 \\right\\}  \\end{aligned} \\]
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
> \\(C\\)を凸集合、\\(\overline{C}\\) を \\(C\\) の閉包とします。任意に \\(x\, y \in \overline{C}\\)、および \\(\lambda \in [0\,1]\\) をとります。
> \\(x \in \overline{C}\\), \\(y \in \overline{C}\\) なので、それぞれ以下の条件を満たす \\(C\\) 内の点列 \\(\{x _ n\} \subset C\\), \\(\{y _ n\} \subset C\\) が存在します:
> \\[ \\begin{aligned}  x _ n \\to x\,\\quad y _ n \\to y \\quad (n \\to \\infty).  \\end{aligned} \\]
> \\(C\\) が凸集合であるため、各 \\(n\\) に対して \\( z _ n := \lambda x _ n + (1 - \lambda) y _ n\\) と定義すると \\(z _ {n} \in C\\) です。
> \\(\overline{C}\\) が閉集合なので \\(n \to \infty\\) のときに \\(z _ {n}\\) の収束先が存在するならばその収束先は \\(\overline{C}\\) の元です。  
> また \\(x _ {n}\, y _ {n}\\) の取り方から、\\((n \to \infty)\\) のときに \\(z _ n\\) は \\(\lambda x + (1 - \lambda) y \quad (n \to \infty)\\) に収束します。 
> 
> よって、\\( \lambda x + (1 - \lambda) y \in \overline{C} \\)であることが示せました。
> 
> </div></details>


一方で、閉集合の凸包は閉集合とは限りません（最初私は閉集合の凸包は閉集合となると思い込んでいましたが反例がありました）。


**Propositon（閉集合の凸包は閉集合とは限らない）**  
> 閉集合の凸包が閉集合とならない反例が存在します。
> 
> <details><summary>(Proof)</summary><div>
> 
> \\[ \\begin{aligned}  A := \\{ (x\, y) | xy \\geq 1\, x > 0\, y > 0 \\} \\cup {(0\, 0)}  \\end{aligned} \\]
> とおく。このとき、以下が成り立ちます。
> - \\(A\\) が閉集合です。（理由: \\((x\, y) \to xy\\) が連続なので \\(\{ (x\, y) | xy < 1\, x > 0\, y > 0 \}\\) が開集合となるため。）
> - \\( \text{conv}(A) = \{ (x\, y) | x > 0\, y > 0 \} \cup {(0\, 0)}\\)。（理由: \\(x > 0\, y > 0\, xy < 1\\) を満たす \\(x\, y\\) に対して \\(\lambda = (x _ {0}y _ {0})^{-\frac{1}{2}} > 1\\) とおくと \\((\lambda x)\cdot(\lambda y) = 1\\) となるため。）
> - \\( \text{conv}(A)\\) が閉集合ではありません。 
>
> よって、反例が存在することを示せました。
> 
> </div></details>


閉集合の凸包が閉集合になるとは限らないため、閉集合を考える場合においては単なる凸包では捉えたい対象を十分にとらえきれない可能性があります。
幸いにも、凸集合の共通部分が凸集合となるのと同じく、閉集合の共通部分も閉集合となることから、\\(A\\) を含む最小の閉凸集合が存在することがわかります。


#### Definition (閉凸包)
> 集合 \\(A\\) を含む最小の閉凸集合を \\(A\\) の閉凸包と定義します。



<br><br>



## 凸集合の分離定理

**Propositon（凸集合の分離定理 1）**  
> \\(C \in \mathbb{R}^n\\) を凸集合とします。任意の \\(x _ {0} \notin Cl(C)\\) を固定します。
> このとき、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します。
> \\[ \\begin{aligned}  \\langle a\, c\\rangle \\geq b \\quad (\\forall c \\in C)\, \\\\   \\langle a\, x _ {0}\\rangle < b  \\end{aligned} \\]
> 
> <details><summary>(Proof)</summary><div>
> 
> [統計的学習理論](#reference1)の補題 B.2 を参照。
> 
> </div></details>


**Corollary（凸集合の分離定理 1）**  
> \\(C \in \mathbb{R}^n\\) を凸集合とします。任意の \\(x _ {0} \notin Cl(C)\\) を固定します。
> このとき、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します。
> \\[ \\begin{aligned}  \\langle a\, c\\rangle \\geq b \\quad (\\forall c \\in C)\, \\\\   \\langle a\, x _ {0}\\rangle < b  \\end{aligned} \\]
> 
> <details><summary>(Proof)</summary><div>
> 
> 証明は文献を参照。
> 
> </div></details>

<h2 id="section2">セクション2</h2>


#### Propositon（凸集合の分離定理 2）
> \\(X\, Y \in \mathbb{R}^n\\) を凸集合と、さらに \\( X \cap Y = \empty\\) を満たすとします。
> このとき、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{aligned}  \\langle a\, x \\rangle \\geq b \\quad (\\forall x \\in X)\, \\\\   \\langle a\, y \\rangle \\leq b \\quad (\\forall y \\in Y).  \\end{aligned} \\]
> 
> <details><summary>(Proof)</summary><div>
> 
> 「凸集合の分離定理 1」と同様に
> 
> </div></details>

#### 補足説明
凸集合の分離定理は有限次元実ベクトル空間 \\(\mathbb{R}^{N}\\) の場合にだけ成立するのではなく、Banach 空間の場合であっても成立することが知られており、
関数解析学における Hahn-Banach の分離定理がそれに該当します。

**Theorem（Hahn-Banach の分離定理）**  
> \\(V\\) を、K (= ℝ または ℂ) に対する位相ベクトル空間とし、\\(A\\) および \\(B\\) を、\\(V\\) の空でない凸な部分集合とし、A ∩ B = ∅ とする。このとき、次が成立する:
> - A が開ならば、ある連続線型作用素 λ: V → K および実数 t ∈ R が存在して、Re λ(a) < t ≤ Re λ(b) がすべての a ∈ A, b ∈ B に対して成立する。
> - \\(V\\) が局所凸、\\(A\\) がコンパクトで、\\(B\\) が閉ならば、ある連続線型作用素 \\(\lambda: V \rightarrow K\\) および実数 \\(s\, t \in \mathbb{R}\\) が存在して、\\(Re \lambda(a) < t < s < Re \lambda(b)\\) がすべての \\(a ∈ A\\), \\(b ∈ B\\) に対して成立する。

定理の主張を見てみると、凸集合の分離定理と全く同じことを述べていることがわかります。
とはいえ、この定理を有限次元の場合に具体的に示すことで、凸集合の持つ性質がより理解しやすくなったのではないかと思います。

----

## 凸関数の定義

関数のグラフ上の2点を結ぶ線分が必ずグラフの**上に位置する**性質を持つ関数を凸関数といいます。  

### Definition (凸関数)

> (1) 集合 \\(C \subset \mathbb{R}^n\\) を凸集合とし、関数 \\(f: C \to \mathbb{R}\\) を \\(C\\) 上の関数とします。
> 任意の \\(x\, y \in C\\)、\\(0 \leq \lambda \leq 1\\) に対して以下の不等式が成り立つとき、\\(f\\) を凸関数と定義します。  
> \\[ \\begin{aligned}  > f(\\lambda x + (1 - \\lambda)y) \\leq \\lambda f(x) + (1 - \\lambda)f(y) >  \\end{aligned} \\]
> 
> (2) 関数 \\(f: \mathbb{R}^n \to \mathbb{R} \cup \{ +\infty \}\\) を \\(\mathbb{R}^n\\) 上の関数とします。
> 任意の \\(x\, y \in \mathbb{R}^n\, 0 \leq \lambda \leq 1\\) に対して以下の不等式が成り立つとき、\\(f\\) を凸関数と定義します。
> \\[ \\begin{aligned}  > f(\\lambda x + (1 - \\lambda)y) \\leq \\lambda f(x) + (1 - \\lambda)f(y) >  \\end{aligned} \\]
> \\(f\\) が実数値を取る領域を \\(\text{dom} (f) := \{x \\,\\, | \\,\\, f(x) < +\infty\}\\) と定義します。不等式が成り立つことから、\\(\text{dom} (f)\\) は凸集合になることがわかります。

### 凸関数の例

* \\(f(x) = \|x\|^2 = x _ 1^2 + x _ 2^2 + \cdots + x _ n^2\\)：凸（ヘッセ行列は単位行列 × 2）
* \\(f(x) = \log(\sum _ {i=1}^n e^{x _ i})\\)：凸（機械学習でよく登場）
* \\(f(x) = -\log \det X\\)（対象正定値行列 \\(X\\) 上の関数）：凸


### 幾何的な意味
* グラフ上の2点を結ぶ線分が、関数のグラフの**上に位置する**という意味です（スカラー値の関数で）。
* 実質的には1変数の場合と全く同じ構造ですが、点 \\(x\, y\\) は \\(\mathbb{R}^n\\) のベクトルになります。

### 凸関数の連続性
関数のグラフ上の2点を結ぶ線分が必ずグラフの**上に位置する**性質から、凸関数 \\(f\\) の値が大きく変動し発散することはないように思えます。
実際、\\(x\\)の周りで関数 \\(f\\) の値が定義されているならば凸関数 \\(f\\) は \\(x\\) で連続であることが示せます。

### Propositon（凸関数の連続性）
> \\(f\\) を凸関数とします。\\(\text{dom} (f)\\) が \\(x\\) の内点を含むなら、\\(f\\) は \\(x\\) で連続です。
> 
> <details><summary>(Proof)</summary><div>
> 
> 証明は文献を参照。
> 
> </div></details>

### 凸関数の性質
凸関数であることは、ある超平面で分離できることと同値です（要イメージ図）。

### Propositon (凸関数と同値な条件)  
> \\(f\\) を凸関数とします。以下は同値です。
> - \\(f\\) が凸関数。
> - 任意の \\( x \in \text{dom}(f) \\) に対して、ある \\( v _ {x} \in \mathbb{R}^n \\) が存在して次が成り立つ:  
>   任意の \\( y \in \mathbb{R}^n \\) に対して、\\(f(y) - f(x) \geq v _ {x}^{T} \cdot (y - x)\\) が成り立つ。

関数が一変数の場合を考えると、凸関数であることとある点を基点としたときに線分の傾きが増加していくことと同値です（要イメージ図）。

### Propositon (一変数凸関数と同値な条件)
> \\(f\\) を凸関数とします。以下は同値です。  
> (1) \\(f\\) が凸関数。  
> (2) 任意の \\( x \in \text{dom}(f) \\) に対して、\\( \phi _ {x} (y) := \frac{f(y) - f(x)}{y - x} \\,\\, (y \neq x)\\) が広義単調増加。
> <details><summary>(Proof)</summary><div>
> 
> はじめに (1) \\(\Rightarrow\\) (2) を示します。  
> \\( x \in \text{dom}(f) \\) を固定し、\\(y _ {1} < x < y _ {2}\\) を任意にとります。
> このとき、\\( \phi _ {x} (y _ {1}) \leq \phi _ {x} (y _ {2})\\) が成立することを示しましょう。
> 
> 最後に (3) \\(\Rightarrow\\) (1) を示します。  
> \\(x\, y \in \text{dom} (f)\\) かつ \\(x < y\\) となる \\(x\, y\\) を考えます。さらに、\\(0 \leq \lambda \leq 1\\) をとり、\\(z := (1 - \lambda) x + \lambda y\\) とおきます。このとき \\(x < y < z\\) となるため、
> \\(\phi _ {x}(z) < \phi _ {x}(y)\\)
> \\[ \\begin{aligned}  \\frac{f(z) - f(x)}{z - x} \\leq \\frac{f(y) - f(x)}{y - x}  \\end{aligned} \\]
> \\(z - x = \lambda (y - x)\\) であることに注意すれば、上記の不等式は \\( f(z) - f(x) \leq \lambda (f(y) - f(x)) \\) と同値であり、
> \\[ \\begin{aligned}  f(z) \\leq (1 - \\lambda) f(x) + \\lambda f(y)  \\end{aligned} \\]
> が成り立つことがわかります。よって示せました。
> </div></details>

### Propositon (凸関数ならば停留点ならば最適解)
> <details><summary>(Proof)</summary><div>
> 
> 証明は文献を参照。
> 
> </div></details>


## 参考文献
- <a id="kanamori"></a>金森敬文（2015）『統計的学習理論』共立出版（機械学習プロフェッショナルシリーズ）
