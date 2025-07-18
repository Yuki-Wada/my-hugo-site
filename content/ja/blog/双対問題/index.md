---
aliases: []
author: Yuki Wada
categories:
- 最適化
date: '2025-07-13'
description: 双対問題
draft: false
math: true
slug: dual-problem
title: 双対問題
weight: 999
---

## 概要

#### この記事で伝えたいこと
今まで双対問題について勉強してきたのですが、そのたびに忘れてしまったので、メモとして記載しております。  
双対問題がどのように導出されているのか、何が本質的に重要なのか、どのような条件の下で成り立つのかといった点は、一箇所に整理されている資料は意外と少ないように思います。
そこでこの記事では、これらのポイントについて概略的に整理し、理解の助けとなるようにまとめてみたいと思います。

#### この記事の対象者
- 双対問題の定義をしっかり
- 双対問題の重要性をしっかり理解したい方
- 強双対定理が成り立つための条件をしっかりと理解したい方

#### 参考記事
- 凸関数の定義・性質は[この記事]({{< ref "blog/凸関数の性質" >}}#section2)も参考にしてください。
- 不等式制約付き最適化問題については[この記事]({{< ref "blog/不等式制約付き最適化問題" >}})も参考にしてください。



<br><br>

<script>
var elems = document.getElementsByTagName('details');
function details_open(bool){
for(elem of elems){
elem.open = bool;
}
}
</script>

<button type="button" onclick="details_open(true)">開く</button>
<button type="button" onclick="details_open(false)">閉じる</button>


## 双対問題

**Definition（双対問題）**
> (1) 不等式制約付き最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> ラグランジュ緩和関数
> \\[ \\begin{gather*}  L(x\, \\lambda\, \\mu) = f(x) + \\sum _ {i=1}^{m} \\lambda _ i g _ i(x) + \\sum _ {j=1}^{p} \\mu _ j h _ j(x)  \\end{gather*} \\]
> に対して、
> \\[ \\begin{gather*}  g(\\mu\, \\lambda) \:= \\inf _ {x} L(x\, \\lambda\, \\mu)  \\end{gather*} \\]
> とおきます。
> このとき、以下の最適化問題を元の問題の双対問題と定義します: 
> \\[ \\begin{gather*}  \\text{supremum} \\quad g(\\mu\, \\lambda).  \\end{gather*} \\]
> また、元の問題を主問題といいます。  
> (2) 主問題の最適値を \\(p^{\ast}\\)、双対問題の最適値は \\(d^{\ast}\\) と表記する。また、双対ギャップを \\(p^{\ast} - d^{\ast}\\) と定義する。

**Propositon（双対問題の凸性）**
> \\(g(\mu\, \lambda)\\) は凸関数です。



## 弱双対定理

双対問題の定義の仕方から、
主問題の最適値が双対関数の最適値で下から抑えられることがわかります。

**Propositon (弱双対定理)**
> 不等式制約付き最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考える。
> \\[ \\begin{gather*}  p^{\\ast} \\geq d^{\\ast}  \\end{gather*} \\]
> <details><summary>(Proof)</summary><div>
> 
> 実行可能解の集合を \\(F\\) とする。このとき、
> \\[ \\begin{align}   p^{\\ast} & = \\inf _ {x \\in F} f(x) \\nonumber \\\\   & \\geq \\inf _ {x} \\sup _ {\\mu\, \\lambda} L(x\, \\lambda\, \\mu) \\nonumber \\\\   & \\geq \\sup _ {\\mu\, \\lambda} \\inf _ {x} L(x\, \\lambda\, \\mu) \\nonumber \\\\   & \\geq \\sup _ {\\mu\, \\lambda} g(\\mu\, \\lambda) \\nonumber \\\\   & = d^{\\ast} \\nonumber   \\end{align} \\]
> となるため、示せた。
> 
> </div></details>



## 強双対定理
弱双対定理によって、双対ギャップは常に 0 以上になることがわかります。
特に、主問題と双対問題の最適値が一致する（すなわち dual gap = 0）場合には、双対問題を解くことで主問題の最適値を求めることができます。
この場合は、双対問題を解くことの意義が明確になります。

この dual gap が 0 になるためには、ある条件が満たされている必要があります。
こうした条件のもとで 双対ギャップが 0 になることを保証する定理を、一般に強双対定理（strong duality theorem） と呼びます。
中でも代表的な十分条件として知られているのが、次節で説明するスレーター条件です。
ここでは、強双対定理の主張を簡単にまとめておきます。

**Statement (強双対定理)**
> 不等式制約付き最適化問題 \\(\left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> 実行可能解の集合を \\(F\\) とします。
> 以下の等式が成り立つとき、この最適化問題は強双対定理が成り立つといいます。
> \\[ \\begin{gather*}  p^{\\ast} = d^{\\ast}  \\end{gather*} \\]



<br><br>



## 強双対定理の成立条件

### スレーター条件

**Definition (スレーター条件)**
> 不等式制約付き最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> さらに \\(\mathcal{P}\\) が凸最適化問題であるとします。
> \\(h _ {j}\\) がアフィン関数であり、さらに、以下の条件
> \\[ \\begin{gather*}  g _ i(x _ 0) < 0 \\quad (\\forall \\\, i)\, \\quad h _ j(x _ 0) = 0 \\quad (\\forall \\\, j)  \\end{gather*} \\]
> を満たす \\(x _ {0}\\) が存在するとき、この最適化問題はスレーター条件を満たすと定義します。


最適化問題がスレーター条件を満たすならば、強双対定理が成り立つことを実際に示すことができます。このことを Proposition の形でまとめておきます。


**Propositon（スレーター条件が満たされるならば強双対定理が成り立つ）** <a id="slater-condition-proposition"></a>
> 不等式制約付きの**凸最適化問題** \\(\mathcal{P} \left( f\, \\{g _ {i}\\}\, \\{h _ {j}\\} \right)\\) がスレーター条件を満たすならば、強双対定理が成り立ちます。
> <details><summary>(Proof)</summary><div>
> 
> (1) [文献](#boyd)の手法に沿って証明を進める。
> 
> 最初に、\\(\tilde{x}\\) が \\(\text{dom} (f)\\) の内点であり、行列 \\(A\\) の階数が行数と一致するケースを考えます。
> 次の集合を考えます。
> 
> \\[ \\begin{gather*}  \\mathcal{A} = \\\{ (u\, v\, t) \\\; | \\\;   \\exist x \\in D\, \\quad   \\quad g _ {i}(x) ≤ u _ {i} \\\; ( \\forall i)\, \\quad   h _ {j}(x) = v _ {j} \\\; (\\forall j)\, \\quad   f(x) \\leq t   \\\}\, \\\\   \\mathcal{B} = \\\{ (0\, 0\, s) ∈ \\mathbb{R}^{m} \\times \\mathbb{R}^{p} \\times \\mathbb{R} \\\; | \\\; s < p^{\\ast} \\\}.  \\end{gather*} \\]
> 
> まず、\\(\mathcal{P}\\) が凸最適化問題であるため \\(\mathcal{A}\\) は凸集合です。
> 次に \\(p^{\ast}\\) は \\(\mathcal{P}\\) の最適値であるため、\\(\mathcal{A} \cap \mathcal{B} = \empty\\) であることがわかります。
> よって、[凸集合の分離定理]({{< ref "blog/凸集合の性質" >}}#separating-hyperplane-theorem-1)から、
> 以下の条件を満たす \\(\lambda\, \nu\, \mu \in \mathbb{R}^{n}\\) が存在します:
> 
> \\[ \\begin{gather*}  \\langle \\lambda\, u \\rangle + \\langle \\nu\, v \\rangle + \\mu \\cdot t \\geq \\alpha \\\;    \\left( (u\, v\, t)\\in \\mathcal{A} \\right)\, \\\\   \\langle \\lambda\, u \\rangle + \\langle \\nu\, v \\rangle + \\mu \\cdot t \\leq \\alpha \\\;   \\left( (u\, v\, t)\\in \\mathcal{B} \\right).  \\end{gather*} \\]  
> 
> \\((u\, v\, t)\in \mathcal{B}\\) なら \\(u=0\, \\; v=0\\) なので \\(\mu \cdot t \leq \alpha\\) となるので、
> \\( \langle \lambda\, u \rangle + \langle \nu\, v \rangle \geq 0 \\; \left( (u\, v\, t)\in \mathcal{A} \right) \\)
> がいえる。\\(\lambda < 0\\) と仮定すると、
> \\[ \\begin{gather*}  ( (u\, v\, t) \\in \\mathcal{A}) \\land (u \\leq u') \\Rightarrow (u'\, v\, t) \\in \\mathcal{A}  \\end{gather*} \\]
> となるため、\\(\langle \lambda\, u \rangle + \langle \nu\, v \rangle \geq 0\\) を満たさない \\(\mathcal{A}\\) の元が構成できてしまうため矛盾する。よって、\\(\lambda \geq 0\\) がいえる。
> 
> \\(\mu > 0\\) を示しましょう。一旦 \\(\mu = 0\\) が正しいと仮定します。
> \\[ \\begin{gather*}  \\sum _ {i} \\lambda _ {i} g _ {i}(x) + \\langle ν\, Ax − b \\rangle \\geq 0.  \\end{gather*} \\]
> \\(A \tilde{x} − b = 0\\) なので、\\( \sum _ {i} \lambda _ {i} g _ {i}(\tilde{x}) \geq 0\\) とならなければなりません。
> 一方で、\\(g _ {i}(\tilde{x}) < 0\\) となることから \\(\lambda _ {i} \geq 0\\) と合わせて、\\(\lambda _ {i} g _ {i}(\tilde{x}) \leq 0\\) も成り立つ必要があります。
> よって、各不等号は等号で成立する必要があり、\\(g _ {i}(\tilde{x}) \neq 0\\) より \\(\lambda _ {i} = 0\\) が示せます。
> 
> \\(\lambda _ {i} = 0\\) から \\(\langle ν\, A x − b \rangle \geq 0\\) とならなければなりません。
> 一方で \\(\langle ν\, A \tilde{x} − b \rangle = 0\\) であるから、\\(\langle ν\, A (x - \tilde{x}) \rangle = \langle A^{T} ν\, (x - \tilde{x}) \rangle \geq 0\\) が成り立つ必要があります。
> だが、
> 
> - \\(\tilde{x}\\) が \\(\text{dom} (f)\\) の内点であること
> - 行列 \\(A^{T}\\) の階数が列数と一致するため \\(A^{T}\\) が単射であること
> 
> から、この不等式は成立しえず矛盾が生じます。よって、\\(\mu > 0\\) となることがいえました。
> 
> (2) 行列 \\(A\\) の階数が行数と一致しないケースを考えます。  
> 実行可能解 \\(\tilde{x}\\) が存在することから、一次従属になる行を取り除いても制約条件としては変わらないことがわかります。
> よって、一次従属になる行を取り除いた行列 \\(A\\) を代わりに用いることで (1) に帰着可能です。
> 
> (3) あるアフィン空間 \\(A \subsetneq \mathbb{R}^{N}\\) が存在して、\\(A\\) に制限した場合に \\(\tilde{x}\\) が \\(\text{dom} (f)\\) の内点であるケースを考えます。  
> この場合はアフィン空間 \\(A\\) に制限すれば、(2) に帰着可能です。
> 
> 以上より、示すことができました。
> 
> </div></details>


<br>


### 緩和されたスレーター条件
強双対定理が成り立つことは双対問題を解くモチベーションを出す上で重要でした。十分条件の一つがスレーター条件であることからスレーター条件の重要性が理解できます。
一方で、スレーター条件は条件として少し厳しすぎるようにも見えます。
例えば、線形計画法の問題を考える場合に、不等式制約に対して不等号が成り立っているもの


**Definition (緩和されたスレーター条件)**
> 不等式制約付き最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\} \cup \\{g' _ {i'}\\}\, \\{h _ {j}\\} \right)\\) を考えます。
> さらに \\(\mathcal{P}\\) が凸最適化問題であるとします。
> \\(g' _ {i'}\, h _ {j}\\) がアフィン関数であり、さらに、以下の条件
> \\[ \\begin{gather*}  g _ i(x _ 0) < 0 \\\; (\\forall \\\, i)\, \\quad g' _ {i'} (x _ 0) \\leq 0 \\\; (\\forall \\\, i')\, \\quad h _ j(x _ 0) = 0 \\\; (\\forall \\\, j)  \\end{gather*} \\]
> を満たす \\(x _ {0}\\) が存在するとき、この最適化問題は緩和されたスレーター条件を満たすと定義します。

**Propositon（スレーター条件を緩和しても強双対定理が成り立つ）**
> 不等式制約付き**凸最適化問題** \\(\mathcal{P} \left( f\, \\{g _ {i}\\} \cup \\{g' _ {i'}\\}\, \\{h _ {j}\\} \right)\\) が緩和されたスレーター条件を満たすならば、強双対定理が成り立ちます。
> 
> <details><summary>(Proof)</summary><div>
> 
> [この Proposition](#slater-condition-proposition) の証明と同様に、\\(\tilde{x}\\) が \\(\text{dom} (f)\\) の内点としてよい。
> 
> 以下を満たす \\(\\{1\, \dots\, i' \\}\\) の部分集合 \\(I _ {\max}^{'}\\) が存在することを示せば、\\(\mathcal{P}\\) について強双対定理が成り立つことが示せます。
> - 最適化問題 \\(\mathcal{P} \left( f\, \\{g _ {i}\\} \cup \\{g' _ {i'}\\}\, \\{h _ {j}\\} \right)\\) が
> 最適化問題 \\(\mathcal{P'} \left( f\, \\{g _ {i}\\} \cup \\{g' _ {i'}\\} _ {i' \in I _ {\max}^{'}}\, \\{h _ {j}\\} \cup \\{g' _ {i'}\\} _ {i' \notin I _ {\max}^{'}} \right)\\) と一致する。
> - \\(\mathcal{P'}\\) がスレーター条件を満たす。
> 
> \\(\\{1\, \dots\, i' \\}\\) の任意の部分集合 \\(I _ {0}^{'}\\) に対して、条件（＊）を考える。
>
> 条件（＊）: 以下の条件を満たす \\(\hat{x}\\) が存在する:
> \\[ \\begin{gather*}  g _ {i}(\\hat{x}) \\leq 0\, \\\\   g' _ {i'}(\\hat{x}) < 0 \\\; (i' \\in I _ {0}^{'})\, \\\\   g' _ {i'}(\\hat{x}) = 0 \\\; (i' \\notin I _ {0}^{'})\, \\\\   h _ {j}(\\hat{x}) = 0.  \\end{gather*} \\]
> 
> \\(I _ {1}^{'}\, \\; I _ {2}^{'}\\) が条件（＊）を満たすのならば、\\(I _ {1}^{'} \cup I _ {2}^{'}\\) が条件（＊）を満たすことを示そう。
> これは、\\(I _ {1}^{'}\\) 由来の \\(\hat{x} _ {1}\\) と \\(I _ {2}^{'}\\) 由来の \\(\hat{x} _ {2}\\) がある場合に、
> \\(I _ {1}^{'} \cup I _ {2}^{'}\\) に対して \\(\frac{\hat{x} _ {1} + \hat{x} _ {2}}{2}\\) が条件（＊）を満たすことからわかる。
> 
> このことから、以下の条件を満たす \\(I _ {\max}^{'}\\) が存在する。
> 
> - \\(I _ {\max}^{'}\\) が条件（＊）を満たす。
> - \\(I _ {0}^{'}\\) が条件（＊）を満たすならば、\\(I _ {0}^{'} \subseteq I _ {\max}^{'}\\) を満たす。
> 
> \\(I _ {\max}^{'}\\) の最大性から、最適化問題 \\(\mathcal{P}\\) が \\(\mathcal{P'}\\) と一致することがわかる。
> 
> スレーター条件から以下を満たす \\(\tilde{x}\\) が存在する:
> \\[ \\begin{gather*}  g _ {i}(\\tilde{x}) < 0\, \\\\   g' _ {i'}(\\tilde{x}) \\leq 0 \\\; (\\forall i')\, \\\\   h _ {j}(\\tilde{x}) = 0.  \\end{gather*} \\]
> 
> \\(I _ {\max}^{'}\\) の条件（＊）から以下を満たす \\(\hat{x}\\) が存在する:
> \\[ \\begin{gather*}  g _ {i}(\\hat{x}) \\leq 0\, \\\\   g' _ {i'}(\\hat{x}) < 0 \\\; (i' \\in I _ {\\max}^{'})\, \\\\   g' _ {i'}(\\hat{x}) = 0 \\\; (i' \\notin I _ {\\max}^{'})\, \\\\   h _ {j}(\\hat{x}) = 0.  \\end{gather*} \\]
> 
> \\(\tilde{x}\\) が \\(\text{dom} (f)\\) の内点なので、\\(g _ {i}\\) は \\(\tilde{x}\\) で連続である。
> よって、ある \\(0 < \lambda < 1\\) が存在して、以下の条件を満たす
> \\[ \\begin{gather*}  x _ {0} = (1 - \\lambda) \\tilde{x} + \\lambda \\hat{x}\, \\\\   g _ {i}(\\hat{x}) < 0\, \\\\   g' _ {i'}(\\hat{x}) < 0 \\\; (i' \\in I _ {\\max}^{'})\, \\\\   g' _ {i'}(\\hat{x}) = 0 \\\; (i' \\notin I _ {\\max}^{'})\, \\\\   h _ {j}(\\hat{x}) = 0.  \\end{gather*} \\]
> 
> 以上より、\\(\mathcal{P'}\\) がスレーター条件を満たすことが示せた。
> 
> </div></details>



<br><br>



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















<br><br>



## 結論



<br><br>



## 参考文献
- <a id="kanamaori"></a>金森敬文（2015）『統計的学習理論』共立出版（機械学習プロフェッショナルシリーズ）
- <a id="boyd"></a>Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press.


