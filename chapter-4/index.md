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
  \text{Some counter-examples:}
$$
