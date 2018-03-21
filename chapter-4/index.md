# Uniform Convergence and Power Series
## Definition
A $$\underline{\textbf{power series}}$$ of $$f(x)$$ is the infinite sum $$\lim_{n\to\infty}T_{(n,f,a)}$$.

## Introduction

$$
  \text{The power series of } e^x \\
  = \lim_{n\to\infty} T_{n,0} = 1+x+\frac{x^2}{2!} +\ldots+\frac{x^n}{n!}+\frac{x^{n+1}}{(n+1)!}\\\\
$$


$$
  \text{Interested in functions of the form:} \\
  f(x) = f_1(x) + f_2(x) + f_3(x) + \ldots \\\\
  \text{In other words, we have a sequence of sums:} \\
  \{f_1(x), f_1(x) + f_2(x), f_1(x) + f_2(x) + f_3(x), \ldots\} \\
  s_n = f_1 + \ldots + f_n \\
  \{s_n\} = \{s_1,s_2,s_3,\ldots\} \\
  f(x) = \lim_{n\to\infty} f_n(x) \\\\
  \text{For such functions, $\lim_{n\to\infty} f_n(x)$,} \\
  \text{nothing we hope to be true, is true, for example:} \\
$$

1. $$f_n(x) \text{ continuous } \nRightarrow \lim_{n\to\infty} f_n(x) \text{ continuous }$$
2. $$\lim_{n\to\infty} \int_0^1 f_n(x)dx \nRightarrow \int_0^1 \lim_{n\to\infty} f_n(x)dx$$
3. $$f_n(x) \text{ differentiable } \nRightarrow \lim_{n\to\infty} f_n(x) \text{ differentiable }$$

$$
  \text{Some counter-examples:} \\\\
  \text{Counter-example for continuity:} \\
  0 \leq x \leq 1,\ f_n(x) = x^n \\
  \implies f_n(x) \text{ continuous } \\
  \lim_{n\to\infty} f_n(x) = f(x) = \begin{cases}
    0, & \text{ if } 0 \leq x < 1 \\
    1, & \text{ if } x = 1
  \end{cases} \\
  \implies \lim_{n\to\infty} f_n(x) \text{ not continuous } \\\\
  \text{Counter-example for integrals:} \\
  0 \leq x \leq 1, \\
  f_n(x) \text{ defined as line connecting $(\frac{1}{2n},2n)$ to $(\frac 1 n, 0)$ to $(1,0)$} \\
  \implies \int_0^1 f_n(x) = \frac 1 2 \cdot \frac 1 n \cdot 2n = 1 \\
  \lim_{n\to\infty} f_n(x) = f(x) = 0 \\
  \implies \int_0^1 \lim_{n\to\infty} f_n(x) = 0 \\
  \implies \lim_{n\to\infty} \int_0^1 f_n(x) \neq \int_0^1 \lim_{n\to\infty} f_n(x) \\\\
  \text{Counter-example for differentiability:} \\
  x\in [-1,1],\ f_n(x) = \sqrt{x^2+\frac 1 n} \\
  \implies f_n(x) \text{ differentiable } \\
  \lim_{n\to\infty} f_n(x) = \left|x\right| \\
  \implies \lim_{n\to\infty} f_n(x) \text{ not differentiable } \\\\
$$

## Definitions

Let $$\{f_n(x)\}$$ be a sequence of functions defined on the set $$A$$ (domain), and let $$f(x)$$ be a function which is also defined $$\forall\ x\in A$$. Then $$f(x)$$ is called the $$\underline{\textbf{uniform limit of } \{f_n(x)\} \textbf{ on } A}$$ if:

$$
  \forall\ \epsilon > 0, \exists N, \text{ s.t. } \forall\ x\in A, n>N \implies \left|f(x) - f_n(x)\right| < \epsilon
$$

We also say that $$\underline{\{f_n(x)\} \textbf{ converges uniformly to } f \textbf{ on } A}$$ or $$\underline{f_n(x) \textbf{ approaches } f(x) \textbf{ uniformly on } A}$$.

$$\underline{\{f_n(x)\} \textbf{ converges pointwise to } f \textbf{ on } A}$$ if:

$$
  \forall\ x, f(x) = \lim_{n\to\infty} f_n(x) \\
  \forall\ \epsilon > 0, \forall\ x\in A, \exists N, \text{ s.t. }  n>N \implies \left|f(x) - f_n(x)\right| < \epsilon
$$

Note) $$\text{uniform convergence }\implies\text{ pointwise convergence }$$, but $$\text{ pointwise convergence }\nRightarrow\text{ uniform convergence }$$ because we cannot necessarily find $$N$$ that works $$\forall\ x$$

Note) $$\text{uniform convergence }\implies \text{ after } n>N$$, all functions will be between $$f(x)-\epsilon$$ and $$f(x)+\epsilon$$

## Applications 1
- 1.) If $$f_n(x) = \frac x n \text{ on } [0,1]$$, what does $$\{f_n(x)\}$$ approach uniformly?
  - $$
      \lim_{n\to\infty} f_n(x) = 0 \\
      \implies \{f_n(x)\} \text{ approaches } f(x) = 0 \text{ uniformly on } [0,1]
    $$
  - Answer: $$\{f_n(x)\} \text{ approaches } f(x) = 0 \text{ uniformly on } [0,1]$$
