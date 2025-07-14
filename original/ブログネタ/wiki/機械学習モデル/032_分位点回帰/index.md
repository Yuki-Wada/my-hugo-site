---
title: '分位点回帰'
description: '分位点回帰'
date: '2025-01-03'
categories: []
weight: 32
math: true
---

## 分位点回帰

#### モチベーション

機械学習エンジニアの人は、分類や回帰などの課題に取り組むにあたって、偉い人や導入先の部門から「その予測どれぐらい外れるの？」「学習モデルの予測に対してどうリスク評価をすればいいの？」と尋ねられることはありませんか？
そのような場面で活躍するかもしれないQuantile Regression(分位点回帰)のお話をします。

#### 導入

\\( \tau \\) 分位点回帰モデルを構築するための損失関数は以下である。

\\[ \\begin{align} \\rho _ {\\tau} (t) := & \\left( \\tau I _ { \\{ t \\leq 0 \\} } (t) + (1 - \\tau) I _ { \\{ t > 0 \\} } (t) \\right) \\cdot |t| \\\\ = & \\left( - \\tau I _ { \\{ t \\leq 0 \\} } (t) + (1 - \\tau) I _ { \\{ t > 0 \\} } (t) \\right) \\cdot t \\end{align} \\]
（実例を入れる）

損失関数 \\( \rho _ {\tau}(t) \\)の汎化誤差 \\( \mathbb{E} (\rho _ {\tau} (\hat{y} - y))\\) を最小にする \\( \hat{y} \\) が \\( \tau \\) 分位点回帰の予測値となる。

よって、データセット \\( (x _ {i}\, y _ {i}) _ {i=1 \dots n} \\) が与えられた場合は、予測モデル \\( \hat{y}(x) := f(x) \\) に対して以下の損失関数を最小にするように学習を実行すればよいことがわかる。
\\[ \\begin{aligned}  \\sum _ {i} (\\rho _ {\\tau} (f (x _ {i}) - y _ {i}))  \\end{aligned} \\]






#### （補足）\\( \mathbb{E} (\rho _ {\tau} (\hat{y} - y)) \\) を最小にする \\( \hat{y} \\) が \\( \tau \\) 分位点回帰の予測値となることの証明

\\( \mathbb{E} (\rho _ {\tau} (\hat{y} - y)) \\) を式変形すると下記のようになる（\\( \mathbb{P} (y | x) \\) が確率密度関数 \\( f _ {y|x} (y) \\) を持つとみなした）。
\\[ \\begin{align} & \\mathbb{E} (\\rho _ {\\tau} (\\hat{y} - y)) \\\\ = & \\int \\left( \\int \\rho _ {\\tau} (\\hat{y} - y) d \\mathbb{P} (y | x) \\right) d \\mathbb {P} (x) \\\\  = & \\int \\left( \\int - \\tau I _ { \\{ t \\leq 0 \\} } (\\hat{y} - y) \\cdot ( \\hat{y} - y ) d \\mathbb{P} (y | x) + \\int (1 - \\tau) I _ { \\{ t > 0 \\} } (\\hat{y} - y ) \\cdot ( \\hat{y} - y ) d \\mathbb{P} (y | x) \\right) d \\mathbb {P} (x) \\\\  = & \\int \\left( - \\tau \\int _ {\\hat{y}}^{\\infty} ( \\hat{y} - y ) d \\mathbb{P} (y | x) + (1 - \\tau) \\int _ {-\\infty}^{\\hat{y}} ( \\hat{y} - y ) d \\mathbb{P} (y | x) \\right) d \\mathbb {P} (x) \\\\  = & \\int \\left( -\\tau \\int _ {\\hat{y}}^{\\infty} ( \\hat{y} - y ) f _ {y|x} (y) dy + (1 - \\tau) \\int _ {-\\infty}^{\\hat{y}} ( \\hat{y} - y ) f _ {y|x} (y) dy \\right) d \\mathbb {P} (x) \\end{align} \\]
 一般に \\( \phi (x\, y) \\) が \\( x \\) について \\( C^{1} \\) 級であるならば、
\\[ \\begin{align} & \\frac{d}{dx} \\int _ {C}^{x} \\phi (x\, y) dy \\\\ = & \\lim _ {h \\rightarrow 0} \\frac{\\int _ {C}^{x + h} \\phi (x + h\, y) dy -\\int _ {C}^{x} \\phi (x\, y) dy} {h} \\\\ = & \\lim _ {h \\rightarrow 0} \\int _ {C}^{x + h} \\frac{\\phi (x + h\, y) - \\phi (x\, y) } {h} dy + \\frac{\\int _ {C}^{x + h} \\phi (x\, y) dy -\\int _ {C}^{x} \\phi (x\, y) dy} {h} \\\\ = & \\int _ {C}^{x} \\phi'(x\, y) dy + \\phi(x\, x) \\end{align} \\]
であることから、\\( f _ {y|x} (y) \\) が \\( C^{1} \\) 級であるとみなして、
\\[ \\begin{align} & \\frac{d}{d\\hat{y}} \\left\\{ -\\tau \\int _ {\\hat{y}}^{\\infty} ( \\hat{y} - y ) f _ {y|x} (y) dy + (1 - \\tau) \\int _ {-\\infty}^{\\hat{y}} ( \\hat{y} - y ) f _ {y|x} (y) dy \\right\\} \\\\ = & \\frac{d}{d\\hat{y}} \\left\\{ \\tau \\int _ {\\infty}^{\\hat{y}} ( \\hat{y} - y ) f _ {y|x} (y) dy + (1 - \\tau) \\int _ {-\\infty}^{\\hat{y}} ( \\hat{y} - y ) f _ {y|x} (y) dy \\right\\} \\\\ = & \\tau \\left\\{ \\int _ {\\infty}^{\\hat{y}} f _ {y|x} (y) dy + ( \\hat{y} - \\hat{y} ) f _ {y|x} (y) \\right \\} + (1 - \\tau) \\left\\{ \\int _ {-\\infty}^{\\hat{y}} f _ {y|x} (y) dy + ( \\hat{y} - \\hat{y} ) f _ {y|x} (y) dy \\right \\} \\\\ = & - \\tau \\int _ {\\hat{y}}^{\\infty} f _ {y|x} (y) dy + (1 - \\tau) \\int _ {-\\infty}^{\\hat{y}} f _ {y|x} (y) dy \\\\ = & - \\tau \\left(1 - F _ {y|x} (\\hat{y}) \\right) + (1 - \\tau) F _ {y|x} (\\hat{y}) \\\\ = & F _ {y|x} (\\hat{y}) - \\tau \\end{align} \\]
と式変形できる。\\( \mathbb{E} (\rho _ {\tau} (\hat{y} - y)) \\) が最小となる点は上記の微分が \\( 0 \\) でなければならないので、最終的に
\\[ \\begin{align} F _ {y|x} (\\hat{y}) = \\tau \\end{align} \\]
であることがいえる。上式は \\( \hat{y} \\) が分布 \\( \mathbb{P} (y | x) \\) の \\( \tau \\) 分位数であることを示している。

（今回は \\( f _ {y|x} (y) \\) を \\( C^{1} \\) 級とみなしたので、累積分布関数 \\( F _ {y|x} (\hat{y}) \\) は \\( C^{2} \\) 級でありとくに連続であるとみなした。\\( F _ {y|x} (\hat{y}) \\) が連続であるなら、\\( F _ {y|x} (\hat{y}) = \tau \\) を満たす \\(\hat{y} \\) は必ず存在する。）
