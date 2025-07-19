---
aliases: []
author: Yuki Wada
categories:
- 最適化
date: '2025-07-14'
description: 凸集合の性質
draft: false
math: true
slug: convex-set
title: 凸集合の性質
weight: 999
---



<script>
var elems = document.getElementsByTagName('details');
var elems2 = document.getElementById('accordion');
function details_open(bool){
  for(elem of elems){
    elem.open = bool;
  }
}
</script>



<button type="button" id="accordion" onclick="details_open(true)">
  証明を開く
</button>
<button type="button" onclick="details_open(false)">証明を閉じる</button>



## 概要

#### この記事で伝えたいこと
本記事では、凸集合に関する基本的な概念と性質を確認したうえで、有限次元実ベクトル空間における凸集合の分離定理を丁寧に解説・証明します。

抽象的な定理を具体的な構成に落とし込むことで、「分離」とは何を意味し、どのように実現されるのかを直観的かつ論理的に理解することを目指します。

特に、閉集合・凸包・閉凸包といった概念の違いが、分離定理にどのように関わるかを具体例とともに明らかにし、単なる定理の理解にとどまらず、それを支える構造や条件の意義にも踏み込みます。

#### 記事の対象者
- 凸集合や凸解析の基礎を体系的に見直したい方  
　→ 凸集合の定義、凸包・閉包・閉凸包といった基本概念をしっかり整理したい方。
- 「凸集合の分離定理」の意味や使い所を具体的に理解したい方  
　→ 抽象的な定理の背景や証明手法を、直感的なレベルで掘り下げたい方。
- 抽象的な定理（Hahn-Banachの定理など）に対して直観的な足場を持ちたい方  
　→ 抽象数学や関数解析における分離定理に接したが、まずは有限次元での具体構成を通して理解したい方。
- 最適化・統計的学習理論・経済学などの分野で凸集合を扱う方  
　→ 現実の問題に現れる「分離可能性」の数学的背景をしっかり理解しておきたい方。



<br><br>



## 凸集合の定義

#### Definition (凸集合)
> ベクトル空間 \\(V\\) の部分集合 \\(C\\) を考えます。
> 任意の \\(x\, y \in C\\) と任意の \\(0 \leq \lambda \leq 1\\) に対して、
> \\[ \\begin{gather*}  \\lambda x + (1 - \\lambda) y \\in C  \\end{gather*} \\]
> が成り立つとき、\\(C\\) を凸集合と定義します。


#### Propositon（凸集合の共通部分は凸集合）
> 凸集合の集合族 \\((C _ {\lambda}) _ {\lambda \in \Lambda}\\) の共通部分 \\(\cap C _ {\lambda}\\) も凸集合です。
> 
> 証明は省略します。

#### Definition (凸包)
> 集合 \\(A\\) を含む最小の凸集合を \\(A\\) の凸包と定義し、\\(\text{conv}A\\) と表記します。


凸包の定義を見る限り、具体的にどのような元が凸包に含まれるかが明記されていません。
ですが、集合 \\(A\\) の凸包が \\(A\\) を含む最小の凸集合であるという性質から、有限個の点 \\(x _ 1\, \ldots\, x _ k \in A\\) の凸結合（convex combination）全体の集合が凸包と一致することがわかります。


#### Proposition (凸包の具体的な表現)
> 集合 \\(A\\) の凸包 \\(\text{conv}(A)\\) は次のように書き下すことができます:
> \\[ \\begin{gather*}  \\mathrm{conv}(A) = \\left\\\{ \\sum _ {i=1}^k \\lambda _ i x _ i \\\;\\middle|\\\; k \\in \\mathbb{N}\,\\\; x _ i \\in A\,\\\; \\lambda _ i \\geq 0\,\\\; \\sum _ {i=1}^k \\lambda _ i = 1 \\right\\\}  \\end{gather*} \\]
> 
> 証明は省略します。

**Propositon（凸集合の閉包は凸集合）**  
> 凸集合の閉包は凸集合です。
> <details><summary>(Proof)</summary><div>
> 
> \\(C\\)を凸集合、\\(\overline{C}\\) を \\(C\\) の閉包とします。任意に \\(x\, y \in \overline{C}\\)、および \\(\lambda \in [0\,1]\\) をとります。
> \\(x \in \overline{C}\\), \\(y \in \overline{C}\\) なので、それぞれ以下の条件を満たす \\(C\\) 内の点列 \\(\\{x _ n\\} \subset C\\), \\(\\{y _ n\\} \subset C\\) が存在します:
> \\[ \\begin{gather*}  x _ n \\to x\,\\quad y _ n \\to y \\quad (n \\to \\infty).  \\end{gather*} \\]
> \\(C\\) が凸集合であるため、各 \\(n\\) に対して \\( z _ n \:= \lambda x _ n + (1 - \lambda) y _ n\\) と定義すると \\(z _ {n} \in C\\) です。
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
> \\[ \\begin{gather*}  A \:= \\\{ (x\, y) | xy \\geq 1\, x > 0\, y > 0 \\\} \\cup {(0\, 0)}  \\end{gather*} \\]
> とおく。このとき、以下が成り立ちます。
> - \\(A\\) が閉集合です。（理由: \\((x\, y) \to xy\\) が連続なので \\(\\{ (x\, y) | xy < 1\, x > 0\, y > 0 \\}\\) が開集合となるため。）
> - \\( \text{conv}(A) = \\{ (x\, y) | x > 0\, y > 0 \\} \cup {(0\, 0)}\\)。（理由: \\(x > 0\, y > 0\, xy < 1\\) を満たす \\(x\, y\\) に対して \\(\lambda = (x _ {0}y _ {0})^{-\frac{1}{2}} > 1\\) とおくと \\((\lambda x)\cdot(\lambda y) = 1\\) となるため。）
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

**Propositon（凸集合と一点の分離）** <a id="separating-hyperplane-lemma"></a>
> \\(C \subseteq \mathbb{R}^n\\) を凸集合とします。
> 
> \\(\inf _ {c \in C} d(c\, x _ {0})\\) > 0 ならば、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{gather*}  \\langle a\, c\\rangle \\geq b \\quad (\\forall c \\in C)\, \\\\   \\langle a\, x _ {0}\\rangle < b.  \\end{gather*} \\]
> 
> \\(\inf _ {c \in C} d(c\, x _ {0})\\) = 0 ならば、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{gather*}  \\langle a\, c\\rangle \\geq b \\quad (\\forall c \\in C)\, \\\\   \\langle a\, x _ {0}\\rangle \\leq b.  \\end{gather*} \\]
> 
> <details><summary>(Proof)</summary><div>
> 
> \\(\inf _ {c \in C} d(c\, x _ {0})\\) > 0 のときは \\(x _ {0} \notin Cl(C)\\) となりますので、
> 証明は[統計的学習理論](#kanamori)の補題 B.2 を参照してください。
> 
> \\(\inf _ {c \in C} d(c\, x _ {0})\\) = 0 のときは \\(x _ {0} \in Bd(C)\\) となりますので、
> 証明は[統計的学習理論](#kanamori)の補題 B.3 を参照してください。
> 
> </div></details>


**Propositon（凸集合の分離定理）** <a id="separating-hyperplane-theorem-1"></a>
> \\(X\, Y \subseteq \mathbb{R}^n\\) を凸集合とし、さらに \\( X \cap Y = \empty\\) を満たすとします。
> 
> このとき、以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{gather*}  \\langle a\, x \\rangle \\geq b \\quad (\\forall x \\in X)\, \\\\   \\langle a\, y \\rangle \\leq b \\quad (\\forall y \\in Y).  \\end{gather*} \\]
> 
> さらに、\\(X\\) が閉集合、\\(Y\\) がコンパクト集合である場合には、
> 以下の条件を満たす \\(a\, b \in \mathbb{R}^n\\) が存在します
> （2 つ目の不等式が真の不等号に変わっていることに注意してください）:
> \\[ \\begin{gather*}  \\langle a\, x \\rangle \\geq b \\quad (\\forall x \\in X)\, \\\\   \\langle a\, y \\rangle < b \\quad (\\forall y \\in Y).  \\end{gather*} \\]
> 
> 
> <details><summary>(Proof)</summary><div>
> 
> \\(Z \:= \\{ x - y \\; | \\; x \in X\, \\; y \in Y \\}\\) とおくと、\\(Z\\) は凸集合、かつ、\\(0 \notin Z\\) を満たします。
> 
> このとき、以下の条件を満たす \\(a _ {0}\, b _ {0} \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{gather*}  \\langle a _ {0}\, c \\rangle \\geq b _ {0} \\quad (\\forall c \\in Z)\, \\quad \\langle a _ {0}\, 0 \\rangle \\leq b _ {0}.  \\end{gather*} \\]
> 
> この式を整理すると以下のようになる:
> 
> \\[ \\begin{gather*}  \\langle a _ {0}\, x \\rangle \\geq b _ {0} + \\langle a _ {0}\, y \\rangle \\quad (\\forall x \\in X\, \\\; \\forall y \\in Y)\, \\quad b _ {0} \\geq 0  \\end{gather*} \\]
> 
> よって、
> 
> \\[ \\begin{gather*}  \\langle a _ {0}\, x \\rangle   \\geq b _ {0} + \\sup _ {y \\in Y} \\langle a _ {0}\, y \\rangle   \\geq b _ {0} + \\langle a _ {0}\, y \\rangle \\geq \\langle a _ {0}\, y \\rangle  \\end{gather*} \\]
> 
> となるため、\\(a \:= a _ {0}\, \\; b \:= b _ {0} + \sup _ {y \in Y} \langle a _ {0}\, y \rangle\\) とおくことで示せました。
> 
> 
> 
> さらに、\\(X\\) を閉集合、\\(Y\\) をコンパクト集合であるとする。
> \\( f\: Y \ni y \rightarrow \inf _ {x \in X} d(x\, y) \in \mathbb{R}\\) とおくと、\\(f\\) は連続であることがわかる。
> さらに、\\(Y\\) がコンパクト集合であるため \\(Y\\) 上で最小値 \\(m\\) が存在することがわかる。つまり、以下を満たす \\(y _ {0} \in Y\\) が存在する:
> 
> \\[ \\begin{gather*}  f(y _ {0}) = \\min _ {y \\in Y} f(y) = m \\end{gather*} \\]
> 
> \\(m = 0\\) と仮定する。
> このとき、\\(\inf _ {x \in X} d(x\, y _ {0}) = 0\\) となるので、\\(x _ {n} \rightarrow y _ {0} \\; (n \rightarrow \infty)\\) を満たす数列 \\((x _ {n})\\) が存在することがわかる。
> ところが、\\(X\\) が閉集合であるため、\\(X\\) の元で構成される数列が収束するならばその収束先も \\(X\\) の元となるため、\\(y _ {0} \in X\\) となってしまうが、これは \\(X \cap Y = \empty\\) に矛盾する。
> よって、\\(m > 0\\) であることが示せた。
> 
> \\(m > 0\\) であることから \\(\inf _ {z \in Z} d(0\, z) > 0\\) となるため、以下の条件を満たす \\(a _ {0}\, b _ {0} \in \mathbb{R}^n\\) が存在します:
> \\[ \\begin{gather*}  \\langle a _ {0}\, c \\rangle \\geq b _ {0} \\quad (\\forall c \\in Z)\, \\quad \\langle a _ {0}\, 0 \\rangle < b _ {0}.  \\end{gather*} \\]
> 
> 前半の議論では \\(b _ {0} \geq 0\\) であることがわかるが、
> 今回は \\(b _ {0} > 0\\) であるため、
> 同様に \\(a \:= a _ {0}\, \\; b \:= b _ {0} + \sup _ {y \in Y} \langle a _ {0}\, y \rangle\\) とおくことで 2 つ目の不等式が真の不等号になることが示せました。
> 
> </div></details>


#### 補足説明
凸集合の分離定理は、有限次元実ベクトル空間 \\(\mathbb{R}^{n}\\) だけではなく、一般の Banach 空間に対しても成り立つことが知られています。
関数解析学における Hahn-Banach の分離定理がそれに該当します。

**Theorem（Hahn-Banach の分離定理）**  
> \\(V\\) を、\\(K \\; (= \mathbb{R} \text{ or }\mathbb{C} )\\) に対する位相ベクトル空間とし、
> \\(X\, Y \subseteq V\\) を凸集合とし、さらに \\( X \cap Y = \empty\\) を満たすとする。
> このとき、次が成立する:
> - A が開集合ならば、ある連続線型作用素 \\(\lambda\: V \rightarrow K\\) と実数 \\(t \in \mathbb{R}\\) が存在して、
> \\(\text{Re} λ(a) < t \leq \text{Re} \lambda(b) \quad ( \forall a \in A\, \\; \forall b \in B )\\) に対して成り立つ。
> - \\(V\\) が局所凸、\\(A\\) がコンパクトで、\\(B\\) が閉ならば、ある連続線型作用素 \\(\lambda\: V \rightarrow K\\) および実数 \\(s\, t \in \mathbb{R}\\) が存在して、
> \\(\text{Re} \lambda(a) < t < s < \text{Re} \lambda(b) \quad ( \forall a \in A\, \\; \forall b \in B )\\) に対して成立する。

Hahn-Banach の分離定理の主張と[凸集合の分離定理](#separating-hyperplane-theorem-1) の主張は少し異なりますが。
Hahn-Banach の分離定理から凸集合の分離定理を導出することも可能です。

とはいえ Hahn-Banach の分離定理は Minkowski 汎関数を上手く取ってきて Hahn-Banach の拡張定理を使うことによって示すことができますが、
凸集合の性質を full に使っているとは言えません。
凸集合の分離定理を有限次元の場合に具体的に証明することによって、凸集合の性質や凸集合の分離定理の持つ意味がより理解しやすくなったのではないかと思います。



<br><br>



## 結論 (conclusion or point)

本記事では、凸集合の基本的な性質を確認したうえで、有限次元空間における凸集合の分離定理を具体的に証明しました。

抽象的な主張だけでは見えにくい「分離の構成」や「幾何的な意味合い」を丁寧に追うことで、定理の内容を直感的に把握できたのではないかと思います。特に、閉集合・凸包・閉凸包といった概念の違いが、定理の成立条件にどのように影響するかを具体例を通じて確認することで、「分離可能性」を支える数学的構造に対する理解が深まったのではないでしょうか。

このような具体的理解は、今後 Hahn-Banach のような一般的な分離定理に進む際の直観的土台となり、また、最適化・機械学習・経済理論など、実問題への応用においても有益です。

本記事が、そうした理論と応用の橋渡しとして、読者の理解を後押しする一助となれば幸いです。

<br><br>



## 参考文献
- 金森敬文（2015）『統計的学習理論』共立出版（機械学習プロフェッショナルシリーズ）<a id="kanamori"></a>


