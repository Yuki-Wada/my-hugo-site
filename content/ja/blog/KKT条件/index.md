---
aliases: []
author: Yuki Wada
categories:
- 最適化
date: '2025-07-13'
description: KKT条件
draft: true
math: true
slug: kkt-condition
title: KKT条件
weight: 999
---

概要（修正案）
本記事では、不等式制約付き最適化問題の基本的な構造を定式化したうえで、ラグランジュ緩和関数や KKT 条件（Karush-Kuhn-Tucker 条件）といった重要概念について紹介します。特に、最適化問題における実行可能性・凸性・滑らかさといった性質が、どのように解の存在や性質に関係しているのかを明確にします。

また、KKT 条件がどのような前提のもとで最適解の特徴づけに使われるか、その背後にある直観や理論的意義を読み解いていきます。最適化における双対性や制約付き問題の取扱いに関心のある読者に向け、数式だけでなく構造的な視点から理解を深めることを目指します。




## 導入（スレーター条件・強双対を軸に）

制約付き最適化問題を考えるとき、目的関数を最小化するだけでなく、「与えられた制約条件を満たしながら」解を求める必要があります。
このとき、「主問題」と並行して考えられる**双対問題**の存在が、最適化理論の深い構造を形づくっています。

特に**凸最適化問題**においては、「主問題と双対問題の最適値が一致する」こと（**強双対性**）が成り立つかどうかが、理論的にも計算的にも極めて重要です。
この強双対性が成り立つための鍵となるのが、\*\*スレーター条件（Slater's condition）\*\*と呼ばれる実行可能性の仮定です。

本記事では、凸最適化問題の定式化を踏まえたうえで、

* なぜ双対問題を考えるのか
* なぜ強双対性が重要なのか
* スレーター条件がなぜ必要なのか
  といった問いに答えることを目指します。
  最適化の構造的理解に欠かせない「双対性の意味と限界」を、直観と定理の両面から読み解いていきます。

---

## 記事の対象者

* **凸最適化における双対性の本質を理解したい方**
  　→ ラグランジュ双対、強双対性、スレーター条件といった理論的基盤を明確に把握したい方。

* **単なる KKT 条件の丸暗記にとどまらず、適用の前提を押さえておきたい方**
  　→ KKT 条件がなぜ成り立つのか、スレーター条件との関係を明確にしたい方。

* **最適化理論の応用にあたって、主問題と双対問題の関係を正しく理解したい方**
  　→ 統計的学習理論、経済学、制御理論などで、凸最適化を理論的に扱いたい方。

* **凸解析・最適化理論を体系的に学び直したい方**
  　→ 実行可能性・凸性・双対性といった核心的な概念を整理したい方。

## 不等式制約付き最適化問題

**Definition（不等式制約付き最適化問題）**
> (1) 以下の問題を不等式制約付き最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) と定義します。
> \\[ \\begin{align*}   \\text{infimum} \\quad & f(x) \\\\   \\text{subject to} \\quad   & g _ {i}(x) \\leq 0 \\quad (\\forall \\\, i) \\\\   & h _ {j}(x) = 0 \\quad (\\forall \\\, j) \\\\   \\end{align*} \\]
> 
> (2) 制約条件
> \\[ \\begin{gather*}  g _ {i}(x) \\leq 0 \\quad (\\forall \\\, i)\, \\quad  h _ {j}(x) = 0 \\quad (\\forall \\\, j)  \\end{gather*} \\]
> を満たす \\(x\\) を \\(\mathcal{P}\\) の実行可能解（feasible point）と定義する。
> 
> (3) \\(\mathcal{P}\\) の実行可能解の集合を \\(F\\) として、
> \\[ \\begin{gather*}  p^{\\ast} \:= \\inf _ {x \\in F} f(x) \\end{gather*} \\]
> を \\(\mathcal{P}\\) の最適値と表記し、
> \\[ \\begin{gather*} p^{\\ast} = f(x _ {0}) \\end{gather*} \\]
> を満たす \\(x _ {0}\\) を \\(\mathcal{P}\\) の最適解（optimal point）と定義する。

### 不等式制約付き最適化問題についての補足
上記の最適化問題で考えられるケースには以下の 4 通りがあります。
1. 実行可能解が存在しない（この場合を便宜的に \\( \inf _ {x \in F} f(x) = +\infty\\) とみなす）。
1. 実行可能解が存在するが、下限値が存在しない（つまり、実行可能解の集合を \\(F\\) として、\\( \inf _ {x \in F} f(x) = -\infty\\)）。
1. 実行可能解が存在し、下限値が存在するが、最適解が存在しない。
1. 実行可能解が存在し、下限値が存在し、最適解が存在する。

**Definition (凸関数)**
> 不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。  
> 1. \\(f\, g _ {i}\, h _ {j}\\) がいずれも凸関数であるとき、この最適化問題は凸であると定義します。  
> 1. \\(f\, g _ {i}\, h _ {j}\\) がいずれも \\(C^{1}\\) 級関数であるとき、この最適化問題は滑らかであると定義します。


### Definition（ラグランジュ緩和関数）
> 不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> このとき、ラグランジュ緩和関数 \\(L(x\, \lambda\, \nu)\\) を以下の式で定義します。
> \\[ \\begin{gather*}  > L(x\, \\lambda\, \\nu) \:= f(x) + \\sum _ {i=1}^{m} \\lambda _ i g _ i(x) + \\sum _ {j=1}^{p} \\nu _ j h _ j(x) >  \\end{gather*} \\]

### Definition (KKT 条件)
> 滑らかな不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> \\((x^*\, \mu^*\, \lambda^*)\\) が以下の条件を満たすとします。
> 1. 停留点条件:
>    \\[ \\begin{gather*}  >    \\nabla _ x L(x\, \\lambda\, \\nu) = \\nabla f(x) + \\sum _ {i=1}^{m} \\lambda _ i \\nabla g _ i(x) + \\sum _ {j=1}^{p} \\nu _ j \\nabla h _ j(x) = 0 >     \\end{gather*} \\]
> 1. 主問題の実行可能性:
>    \\[ \\begin{gather*}  >    g _ i(x) \\leq 0 \\quad (\\forall \\\, i)\, \\quad h _ j(x) = 0 \\quad (\\forall \\\, j) >     \\end{gather*} \\]
> 
> 1. 双対実行可能性:
> 
>    \\[ \\begin{gather*}  >    \\lambda _ i \\geq 0 \\quad (\\forall \\\, i) >     \\end{gather*} \\]
> 
> 1. 相補性条件:
> 
>    \\[ \\begin{gather*}  >    \\lambda _ i g _ i(x) = 0 \\quad (\\forall \\\, i) >     \\end{gather*} \\]
> 
> このとき、この問題は \\((x^*\, \lambda^*\, \nu^*)\\) において KKT 条件を満たすと定義します。


## 双対問題と KKT 条件

**Propositon (主・双対問題に最適解が存在するならば KKT 条件が成り立つ)**
> 不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。このとき、主問題の最適解 \\( x^{\ast\ast}\\)、双対問題の最適解 \\((\mu^{\ast}\, \lambda^{\ast})\\) が存在し、かつ、強双対定理が成立するならば、\\((x\, \mu^{\ast}\, \lambda^{\ast})\\) において KKT 条件が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> (1) Primal feasibility（実行可能性）と feasibility（双対実行可能性）は前提条件から成り立つことがわかります。  
> (2) Complementary slackness（相補性条件）が成り立つことを示します。
> 最適化問題の実行可能解の集合を \\(F\\) とします。
> ラグランジュ緩和関数 に対して、
> \\[ \\begin{align}   1   \\end{align} \\]
> と式変形できる。ここで、強双対定理が成り立つことから、\\(f(x^{\ast}) = g(\mu^{\ast}\, \lambda^{\ast})\\) となるため、上記の不等号は全て等号になることがわかります。
> よって、
> \\[ \\begin{gather*}  >   \\sum _ {i=1}^{m} \\lambda _ {i}^{a} g _ {i}(x^{a}) + \\sum _ {j=1}^{p} \\mu _ {j}^{a} h _ {j}(x^{\\ast}) = 0 >  \\end{gather*} \\]
> となることがわかります。
> \\[ \\begin{gather*}   >   L(x^{\\ast}\, \\mu^{\\ast}\, \\lambda^{\\ast}) = \\inf _ {x} L(x\, \\mu^{\\ast}\, \\lambda^{\\ast}) >  \\end{gather*} \\]
> であることから、\\(L(x\, \mu^{*}\, \lambda^{*})\\) を \\(x\\) の関数としてみたときに \\(x = x^{*}\\) で極小となることがわかるため、Stationarity（停留条件）が成り立つこともわかる。
> 
> </div></details>

**Propositon (KKT 条件が成り立つならば主・双対問題に最適解が存在する)**
> 不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。さらに、この問題が凸最適化問題であるとします。
> このとき、\\((x\, \mu^{\ast}\, \lambda^{\ast})\\) において KKT 条件を満たすならば、強双対定理が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> Complementary slackness（相補性条件）が成り立つことから、
> \\[ \\begin{gather*}    f(x^{\\ast}) = f(x^{\\ast}) + \\sum _ {i=1}^{m} \\lambda _ i^{\\ast} g _ i(x^{\\ast}) + \\sum _ {j=1}^{p} \\mu _ j^{\\ast} h _ j(x^{\\ast}) >  \\end{gather*} \\]
> が成り立ちます。  
> 次に、この不等式制約付き最適化問題が凸最適化問題であることから、ラグランジュ緩和関数 \\(L(x\, \mu^{\ast}\, \lambda^{\ast})\\) は \\(x\\) の関数とみたときに凸関数であることがわかります。一般に、凸関数が \\(x=x^{\ast}\\) で停留条件を満たすならば \\(x=x^{\ast}\\) で最小値をとるため、
> \\[ \\begin{gather*}   >   L(x^\\ast\, \\mu^\\ast\, \\lambda^\\ast) = \\min _ {x} L(x\, \\mu^{\\ast}\, \\lambda^{\\ast}) >  \\end{gather*} \\]
> が成り立ちます。
> よって、
> \\[ \\begin{gather*}  >   \\begin{align} >   & f(x^{\\ast}) \\nonumber \\\\ >   = & f(x^{\\ast}) + \\sum _ {i=1}^{m} \\lambda _ i^{\\ast} g _ i(x^{\\ast}) + \\sum _ {j=1}^{p} \\mu _ j^{\\ast} h _ j(x^{\\ast}) \\nonumber \\\\ >   = & L(x^{\\ast}\, \\mu^{\\ast}\, \\lambda^{\\ast}) \\nonumber \\\\ >   = & \\min _ {x} L(x\, \\mu^{\\ast}\, \\lambda^{\\ast}) \\nonumber \\\\ >   = & g(\\mu^{\\ast}\, \\lambda^{\\ast}) \\nonumber \\\\  >   \\end{align} >  \\end{gather*} \\]
>   と式変形できます。このことから、強双対定理が成り立つことがわかります。\\( \Box \\)
> </div></details>



<br><br>



## フェンシェル双対性

**Propositon (KKT 条件が成り立つならば主・双対問題に最適解が存在する)**
> 凸関数 \\(f\: \mathbb{R}^{N} \rightarrow \mathbb{R} \cup \\{ + \infty \\}\, g\: \mathbb{R}^{M} \rightarrow \mathbb{R} \cup \\{ + \infty \\}\\) とし、
> \\(A\\) を \\(M \times N\\) 型の行列とする。
> 
> このとき、\\(\text{dom} (f) \cap \text{dom} (g)\\) が内点を持つならば、以下の等式が成り立ちます:
> 
> \\[ \\begin{gather*}  \\inf _ {x \\in \\mathbb{R}^{N}} \\left( f (x) + g(A x) \\right) = \\inf _ {\\lambda \\in \\mathbb{R}^{M}} \\left( - f^{\\ast}(-A^{T} \\lambda) -  g^{\\ast} (\\lambda) \\right) \\end{gather*} \\] 
> 
> <details><summary>(Proof)</summary><div>
> 
> 以下の最適化問題 \\(\mathcal{P}\\) を考える:
> \\[ \\begin{gather*}   \\text{Supremum} \\quad & \\phi(x\, y) \:= f(x) + g(y)\, \\\\   \\text{subject to} \\quad   & \\xi(x\, y) \:= y - Ax = 0.   \\end{gather*} \\]
> 最適化問題 \\(\mathcal{P}\\) のラグランジュ緩和関数 \\(L(x\, y)\\) は
> \\[ \\begin{align*}   L(x\, y)   & \:=f(x) + g(y) + \\langle \\lambda\, y - Ax \\rangle \\\\   & = - \\left(\\langle A^{T} \\lambda\, x \\rangle - f(x) \\right) - \\left(\\langle \\lambda\, y \\rangle - g(y) \\right) \\\\   \\end{align*} \\]
> と変形できるから、双対問題の目的関数 \\(\psi(\lambda)\\) は
> \\[ \\begin{align*}   \\psi(\\lambda)   & = \\inf _ {x\, y} L(x\, y) \\\\   & = - \\sup _ {x\, y} \\left(\\langle A^{T} \\lambda\, x \\rangle - f(x)) -    \\langle \\lambda\, y \\rangle - g(y) \\right) \\\\   & = - \\sup _ {x} \\left(\\langle A^{T} \\lambda\, x \\rangle - f(x) \\right) -    \\sup _ {y} \\left(\\langle \\lambda\, y \\rangle - g(y) \\right) \\\\   & = - f^{\\ast} (A^{T} \\lambda) - g^{\\ast} (\\lambda) \\\\   \\end{align*} \\]
> とかける。
> 
> \\(\text{dom} (f) \cap \text{dom} (g)\\) が内点を持つことから、
> 最適化問題 \\(\mathcal{P}\\) が緩和されたスレーター条件が成リ立つことがわかる。よって、以下の強双対定理
> \\[ \\begin{gather*}   \\inf _ {x\, y\, y - Ax = 0} \\phi(x\, y) = \\sup _ {\\lambda} \\psi(\\lambda)   \\end{gather*} \\]
> が成り立つので、
> 
> \\[ \\begin{gather*}  \\inf _ {x \\in \\mathbb{R}^{N}} \\left( f (x) + g(A x) \\right) = \\inf _ {y \\in \\mathbb{R}^{M}} \\left( - f^{\\ast}(-A^{T} y) -  g^{\\ast} (y) \\right) \\end{gather*} \\] 
> 
> が成り立つことが示せた。
> 
> </div></details>














結論（修正案）

本記事では、凸最適化問題の基本的な構成を確認し、ラグランジュ関数と双対問題の関係性を明らかにしました。
そのうえで、**強双対性が成立する条件**としてのスレーター条件の役割を強調し、最適解の構造や解釈にどのような影響を与えるのかを考察しました。

双対性は最適化の理論的洗練にとどまらず、\*\*アルゴリズム設計（例：内点法、ラグランジュ緩和法）\*\*や、**問題の数値的安定性の分析**にも密接に関わっています。
また、KKT 条件が強双対性のもとで「最適性の必要十分条件」となることも、理論と計算の橋渡しとして重要です。

今後、より一般的な双対理論や数値的最適化手法に進む際に、本記事で示した構造的理解が強固な基盤となるはずです。
「なぜ双対問題を考えるのか」「なぜ制約の仮定が重要なのか」といった問いに向き合う上で、本稿が一助となれば幸いです。
