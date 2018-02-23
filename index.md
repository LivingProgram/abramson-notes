# Abramson Notes

# Sine Reduction Formula
## Main Content

$$\int \sin^{n}x dx=-\frac{1}{n}\sin^{n-1}x\cos x+\left(\frac{n-1}{n}\right)\int\sin^{n-2}x dx$$

### Proof.

$$\text{Let }n\in\mathbb{Z}^{+},\ \text{Given }\int \sin^{n}x dx$$

$$\begin{align}
u&=\sin^{n-1}x\\
du&=(n-1)\sin^{n-2}x\cos xdx\\
dv&=\sin xdx\\
v&=-\cos x\\
\int \sin^{n}x dx&=-\sin^{n-1}x\cos x-\int -\cos x(n-1)\sin^{n-2}x\cos xdx \\
&=-\sin^{n-1}x\cos x+\int (n-1)\sin^{n-2}x\cos^{2} xdx\\
&=-\sin^{n-1}x\cos x+\int (n-1)\sin^{n-2}x(1-\sin^{2}x) xdx\\
\int \sin^{n}x dx&=-\sin^{n-1}x\cos x+(n-1)\int \sin^{n-2}x - (n-1)\int \sin^{n}x dx\\
(1+(n-1))\int \sin^{n}x dx&=-\sin^{n-1}x\cos x+(n-1)\int \sin^{n-2}x \\
\int \sin^{n}x dx&=-\frac{1}{n}\sin^{n-1}x\cos x+\left(\frac{n-1}{n}\right)\int\sin^{n-2}x dx\ \ \ \ \blacksquare\end{align}$$

# Wallis's Theorem

## Main Content
**Theorem:**

$$\prod_{n \mathop = 1}^\infty \frac {2 n} {2 n - 1} \cdot \frac {2 n} {2 n + 1} = \frac 2 1 \cdot \frac 2 3 \cdot \frac 4 3 \cdot \frac 4 5 \cdot \frac 6 5 \cdot \frac 6 7 \cdot \frac 8 7 \cdot \frac 8 9 \cdots = \frac \pi 2$$

### Proof.

$$\text{From Sine Reduction Formula: }$$

$$\begin{align}
\int \sin^{n}x dx&=-\frac{1}{n}\sin^{n-1}x\cos x+\left(\frac{n-1}{n}\right)\int\sin^{n-2}x dx\\
\int_b^a \sin^{n}x dx&=\left(-\frac{1}{n}\sin^{n-1}x\cos x\right)\Big|_b^a+\left(\frac{n-1}{n}\right)\int_b^a\sin^{n-2}x dx\\
\int_0^{\frac{\pi}{2}} \sin^{n}x dx&=\left(-\frac{1}{n}\sin^{n-1}x\cos x\right)\Big|_0^{\frac{\pi}{2}}+\left(\frac{n-1}{n}\right)\int_0^{\frac{\pi}{2}}\sin^{n-2}x dx \\
\int_0^{\frac{\pi}{2}} \sin^{n}x dx&=0+\left(\frac{n-1}{n}\right)\int_0^{\frac{\pi}{2}}\sin^{n-2}x dx \\
\int_0^{\frac{\pi}{2}} \sin^{n}x dx&=\left(\frac{n-1}{n}\right)\int_0^{\frac{\pi}{2}}\sin^{n-2}x dx \\
\\\\
\int_0^{\frac{\pi}{2}} \sin^{2n+1}x dx&=\frac{2n}{2n+1}\times\int_0^{\frac{\pi}{2}}\sin^{2n-1}x dx \\
&=\frac{2n}{2n+1}\times\frac{2n-2}{2n-1}\times\int_0^{\frac{\pi}{2}}\sin^{2n-3}x dx \\
&=\frac{2n}{2n+1}\times\frac{2n-2}{2n-1}\times\ldots\times\int_0^{\frac{\pi}{2}}\sin^{3}x dx \\
&=\frac{2n}{2n+1}\times\frac{2n-2}{2n-1}\times\ldots\times\frac 2 3 \times\int_0^{\frac{\pi}{2}}\sin x dx \\
&=\frac{2n}{2n+1}\times\frac{2n-2}{2n-1}\times\ldots\times\frac 2 3 \times 1\\
\int_0^{\frac{\pi}{2}} \sin^{2n}x dx&=\frac{2n-1}{2n}\times\int_0^{\frac{\pi}{2}}\sin^{2n-2}x dx \\
&=\frac{2n-1}{2n}\times\frac{2n-3}{2n-2}\times\int_0^{\frac{\pi}{2}}\sin^{2n-4}x dx \\
&=\frac{2n-1}{2n}\times\frac{2n-3}{2n-2}\times\ldots\times\int_0^{\frac{\pi}{2}}\sin^{2}x dx \\
&=\frac{2n-1}{2n}\times\frac{2n-3}{2n-2}\times\ldots\times\frac 1 2 \times\int_0^{\frac{\pi}{2}}\sin^{0}x dx \\
&=\frac{2n-1}{2n}\times\frac{2n-3}{2n-2}\times\ldots\times\frac 1 2 \times\frac \pi 2\\
\int_0^{\frac{\pi}{2}} \sin^{2n+2}x dx&=\frac{2n+1}{2n+2}\times\int_0^{\frac{\pi}{2}}\sin^{2n}x dx \\
\\\\\end{align}$$

$$\text{Let }\ I = \frac{\int_0^{\frac{\pi}{2}} \sin^{2n+1}x dx}{\int_0^{\frac{\pi}{2}} \sin^{2n}x dx} = \frac{2n}{2n+1}\times\frac{2n}{2n-1}\times\frac{2n-2}{2n-1}\times\frac{2n-2}{2n-3}\times\ldots\times\frac 2 3 \times\frac 2 1 \times\frac 2 \pi$$

$$\begin{align}\forall x\in\left[0,\frac \pi 2\right],\ &\sin x \leq 1\\&\implies \text{higher powers of } \sin x \text{ yield smaller values}\\&\implies\sin^{2n}x\geq\sin^{2n+1}x\geq\sin^{2n+2}x\end{align}$$

$$\begin{align}\int_0^{\frac{\pi}{2}}\sin^{2n}xdx&\geq\int_0^{\frac{\pi}{2}}\sin^{2n+1}xdx\geq\int_0^{\frac{\pi}{2}}\sin^{2n+2}xdx\\
\frac{\int_0^{\frac{\pi}{2}}\sin^{2n}xdx}{\int_0^{\frac{\pi}{2}}\sin^{2n}xdx}&\geq\frac{\int_0^{\frac{\pi}{2}}\sin^{2n+1}xdx}{\int_0^{\frac{\pi}{2}}\sin^{2n}xdx}\geq\frac{\int_0^{\frac{\pi}{2}}\sin^{2n+2}xdx}{\int_0^{\frac{\pi}{2}}\sin^{2n}xdx}\\
1&\geq I \geq \frac{\frac{2n+1}{2n+2}\times\int_0^{\frac{\pi}{2}}\sin^{2n}x dx }{\int_0^{\frac{\pi}{2}}\sin^{2n}xdx}\tag{Plug in formulas}\\
1&\geq I \geq \frac{2n+1}{2n+2}\\
1&\geq I \geq 1-\frac{1}{2n+2}\\\\\end{align}$$

$$\text{Plugging in for $I$:}$$

$$1\geq \frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \times\frac 2 \pi \geq 1-\frac{1}{2n+2}$$


$$\frac \pi 2 (1)\geq \frac \pi 2 \left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \times\frac 2 \pi \right)\geq \frac \pi 2 \left(1-\frac{1}{2n+2}\right)\\
\frac \pi 2 \geq \frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \geq \frac \pi 2 \left(1-\frac{1}{2n+2}\right)\\
\lim_{n\to\infty}\left(\frac \pi 2\right) \geq \lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) \geq \lim_{n\to\infty}\left(\frac \pi 2 \left(1-\frac{1}{2n+2}\right)\right)\\
\frac \pi 2 \geq \lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) \geq \frac \pi 2\\\\$$

$$\text{By Squeeze Theorem: }$$

$$\lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) = \frac \pi 2\ \ \ \ \blacksquare$$

# Factorial Function
## Main Content

$$f(t)=\int_{0}^{\infty}x^t e^{-x}dx=tf(t-1)$$

### Proof.

$$\begin{align}
\int x^t& e^{-x}dx\\
u&=x^t\\du&=tx^{t-1}dx\\dv&=e^{-x}dx\\v&=-e^{-x}\\
\int x^t e^{-x}dx &=-x^t e^{-x}\Big|^{\infty}_0+t\int_0^{\infty}x^{t-1}e^{-x}dx\\
&=0+t\int_0^{\infty}x^{t-1}e^{-x}dx&&\left(\lim_{x\to\infty}e^{-x}=0\right)\\
&=tf(t-1)\\
f(t)&=tf(t-1)\\\\
\implies f(0)=1,f(1)=1,&f(2)=2,f(3)=6,f(4)=24\\
\implies \forall t\in\mathbb{Z}^+ &\cup\{0\},\ f(t)=t!\ \ \ \ \blacksquare
\end{align}$$

## Applications
* 1.) Find $$\left(\frac{1}{2}\right)!$$
  * Use Factorial Function
  * Answer: $$\int_0^\infty \sqrt{x}e^{-x}dx$$
* 2.) Can you compute fractional factorials?
  * Answer: You can compute any fractional factorial as long as you can compute the integral from plugging in the fraction into the Factorial Function.

# Gamma Function
## Main Content

$$\begin{align}
\Gamma(t)&=\int_0^\infty x^{t-1}e^{-x}dx\\
&=f(t-1)\\
\implies \Gamma(1)=1,\ \Gamma(2)&=1,\ \Gamma(3)=2,\ \Gamma(4)=6\\
\implies t\Gamma(t)&=\Gamma(t+1)\end{align}$$

# Calculating Area Under Bell Curve
## Main Content

$$\begin{align}
\text{Bell Curve: }& e^{-x^2}\\
\text{Area Under Half: }& \int_0^\infty e^{-x^2}dx=\frac{\sqrt{\pi}}{2}
\end{align}$$

### Proof.

$$\text{Calculate reduction formula:}$$

$$\begin{align}
\int&(1-x^2)^ndx\\
u&=(1-x^2)^n\\du&=n(1-x^2)^{n-1}(-2x)dx\\dv&=1dx\\v&=x\\
\int(1-x^2)^ndx &= x(1-x^2)^n+2n\int x^2(1-x^2)^{n-1}dx\\
&=x(1-x^2)^n+2n\int(1-(1-x^2))(1-x^2)^{n-1}dx\\
\int(1-x^2)^ndx &= x(1-x^2)^n+2n\int(1-x^2)^{n-1}dx-2n\int(1-x^2)^ndx\\
(2n+1)\int(1-x^2)^ndx&=x(1-x^2)^n+2n\int(1-x^2)^{n-1}dx\\
\int(1-x^2)^ndx&=\frac{x(1-x^2)^n}{2n+1}+\frac{2n}{2n+1}\int(1-x^2)^{n-1}dx\\\\
\end{align}$$

$$\text{Calculate $f(n)$: }$$

$$\begin{align}
f(n)&=\int_0^1(1-x^2)^ndx\\
&=\left(\frac{x(1-x^2)^n}{2n+1}\right)\Big|_0^1+\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
&=0+\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
&=\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
f(n)&=\frac{2n}{2n+1}f(n-1)\\\\\end{align}$$

$$\text{Calculate reduction formula:}$$

$$\begin{align}
\int\frac{1}{(1+x^2)^n}&=\int\frac{1+x^2}{(1+x^2)^n}-\frac{x^2}{(1+x^2)^n}dx\\
&=\int\frac{1}{(1+x^2)^{n-1}}dx-\int\frac{x^2}{(1+x^2)^n}dx\\
\text{Solving for: }& \int\frac{x^2}{(1+x^2)^n}dx\\
u&=x\\du&=1dx\\dv&=\frac{x}{(1+x^2)^n}\\v&=\int\frac{x}{(1+x^2)^n}dx
=\frac{1}{2-2n}\left(\frac{1}{(1+x^2)^{n-1}}\right)&&\text{(U-Sub)}\\
\int\frac{1}{(1+x^2)^n}=\int\frac{1}{(1+x^2)^{n-1}}dx&-\left(\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)-\frac{1}{2-2n}\int\frac{1}{(1+x^2)^{n-1}}dx\right)\\
&=\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)+\left(1+\frac{1}{2-2n}\right)\int\frac{1}{(1+x^2)^{n-1}}dx\\
&=\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)+\frac{2n-3}{2n-2}\int\frac{1}{(1+x^2)^{n-1}}dx\\\\
\end{align}$$

$$\text{Calculate $g(n)$: }$$

$$\begin{align}
g(n)&=\int_0^\infty\frac{1}{(1+x^2)^n}\\
&=\left(\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)\right)\Big|_0^\infty+\frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
&=0 + \frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
&=\frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
g(n)&=\frac{2n-3}{2n-2}g(n-1)
\end{align}$$

$$\text{Using Wallis's Theorem:}$$

$$\begin{align}
\frac \pi 2 &\approx \frac 2 1 \times \frac 2 3 \times \frac 4 3 \times \frac 4 5 \times \times\ldots\times\frac{2n}{2n-1}\times\frac{2n}{2n+1}\\
\implies \pi &\approx\frac{2\times 2\times 4\times 4\times\ldots\times 2n\times 2n}{1\times 1\times 3\times 3\times \ldots\times (2n-1)\times(2n-1)}\times\frac{2n}{2n+1}\\
\implies \sqrt{\pi}&\approx\frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\\
\text{Let}\ k(n) &= \frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\\
&\implies\lim_{n\to\infty}k(n)=\sqrt{\pi}
\end{align}$$

$$\text{Finding $f(n)$ and $g(n)$ in terms of $k(n)$:}$$

$$\begin{align}
f(n)=\int_0^1(1-x^2)^ndx&=\frac{2n}{2n+1}f(n-1)\\
&=\frac{2n}{2n+1}\times\frac{2n-2}{2n-1}\times\ldots\times\frac 4 5 \times \frac 2 3\\
&=\frac{1}{2n+1}\times\sqrt{n}\times k(n)&&\text{(plug in $k(n)$ to verify)}\\
g(n)=\int_0^\infty\frac{1}{(1+x^2)^n}dx&=\frac{2n-3}{2n-2}g(n-1)\\
&=\frac{2n-3}{2n-2}\times\frac{2n-5}{2n-4}\times\ldots\times\frac 1 2 \times\int_0^\infty\frac{1}{(1+x^2)^1}dx\\
&=\frac{2n-3}{2n-2}\times\frac{2n-5}{2n-4}\times\ldots\times\frac 1 2 \times\frac{\pi}{2}&&\text{($\lim_{x\to\infty}\tan^{-1}x=\frac{\pi}{2}$)}\\
&=\frac{1}{\sqrt{n}\times k(n)}\times\frac{2n}{2n-1}\times\frac{\pi}{2}&&\text{(plug in $k(n)$ to verify)}\\
\end{align}$$

$$\begin{align}
&\text{Absolute min of $e^x-x-1$ is $(0,0)$}\\
&\implies e^x-x-1\geq 0\\&\implies \forall x\ e^x\geq1+x\\
&\implies e^{-x^2}\geq 1-x^2&&\text{(plug in $-x^2$ for $x$)}\\
&\implies e^{x^2}\geq 1+x^2 &&\text{(plug in $x^2$ for $x$)}\\
&\implies e^{-x^2}\leq\frac{1}{1+x^2}&&\text{(take inverse)}\\
&\implies (1-x^2)\leq e^{-x^2}\leq\frac{1}{1+x^2}&&\text{(combine previous)}\\
&\implies(1-x^2)^n\leq e^{-nx^2}\leq\frac{1}{(1+x^2)^n}\\
\end{align}$$

$$\text{Proving some intermediate results:}$$

$$\begin{align}
&\int_0^1 e^{-nx^2}dx\\
y &= x\sqrt{n},\ dy=\sqrt{n}dx\\
\int_0^1 e^{-nx^2}dx&=\frac{1}{\sqrt{n}}\int_0^\sqrt{n}e^{-y^2}dy&&\text{($x=1\implies y=\sqrt{n}$)}\\
&=\frac{1}{\sqrt{n}}\int_0^\sqrt{n}e^{-x^2}dx&&\text{(change $y$ to $x$)}\\\\
&\int_0^\infty e^{-nx^2}dx\\
y &= x\sqrt{n},\ dy=\sqrt{n}dx\\
\int_0^\infty e^{-nx^2}dx&=\frac{1}{\sqrt{n}}\int_0^\infty e^{-y^2}dy&&\text{($x=\infty\implies y=\infty$)}\\
&=\frac{1}{\sqrt{n}}\int_0^\infty e^{-x^2}dx&&\text{(change $y$ to $x$)}\\\\
\frac{1}{\sqrt{n}}\int_0^\sqrt{n}e^{-x^2}dx&\leq\frac{1}{\sqrt{n}}\int_0^\infty e^{-x^2}dx&&\text{(area of $\int_0^\infty >$ area of $\int_0^\sqrt{n}$)}\\\\
\end{align}$$

$$\text{Using all previous results:}$$

$$\begin{align}
(1-x^2)^n\leq &e^{-nx^2}\leq\frac{1}{(1+x^2)^n}\\
\implies\int_0^1(1-x^2)^ndx\leq&\int_0^1 e^{-nx^2}dx = \frac{1}{\sqrt{n}}\int_0^\sqrt{n}e^{-x^2}dx\\
&\leq\frac{1}{\sqrt{n}}\int_0^\infty e^{-x^2}dx=\int_0^\infty e^{-nx^2}dx\leq\int_0^\infty\frac{1}{(1+x^2)^n}dx\\
\implies\int_0^1(1-x^2)^ndx\leq&\frac{1}{\sqrt{n}}\int_0^\sqrt{n} e^{-x^2}dx\leq\int_0^\infty\frac{1}{(1+x^2)^n}dx\\
\implies\frac{1}{2n+1}\times\sqrt{n}\times k(n)\leq&\frac{1}{\sqrt{n}}\int_0^\sqrt{n} e^{-x^2}dx\leq\frac{1}{\sqrt{n}\times k(n)}\times\frac{2n}{2n-1}\times\frac{\pi}{2}\\
\implies\frac{n}{2n+1}\times k(n)\leq&\int_0^\sqrt{n} e^{-x^2}dx\leq\frac{1}{k(n)}\times\frac{2n}{2n-1}\times\frac{\pi}{2}\\
\implies\lim_{n\to\infty}\frac{n}{2n+1}\times k(n)\leq&\lim_{n\to\infty}\int_0^\sqrt{n} e^{-x^2}dx\leq\lim_{n\to\infty}\frac{1}{k(n)}\times\frac{2n}{2n-1}\times\frac{\pi}{2}\\
&\lim_{n\to\infty}\frac{n}{2n+1}\times k(n)=\frac 1 2 \times \sqrt{\pi}=\frac{\sqrt{\pi}}{2}\\
&\lim_{n\to\infty}\frac{1}{k(n)}\times\frac{2n}{2n-1}\times\frac{\pi}{2}=\frac{1}{\sqrt{\pi}}\times 1\times\frac{\pi}{2}=\frac{\sqrt{\pi}}{2}\\
\implies \frac{\sqrt{\pi}}{2}\leq &\lim_{n\to\infty}\int_0^\sqrt{n} e^{-x^2}dx\leq \frac{\sqrt{\pi}}{2}\\
\implies \lim_{n\to\infty}&\int_0^\sqrt{n} e^{-x^2}dx = \frac{\sqrt{\pi}}{2}\\
\implies &\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}\ \ \ \ \blacksquare
\end{align}$$

# Wallis's Applied to Coin Flip
## Main Content
Probability when flipping $$2n$$ coins and getting $$n$$ heads and $$n$$ tails:

$$=\frac{ {2n}\choose{n}}{2^{2n}}\approx\frac{1}{\sqrt{\pi n}}$$

### Proof.

$$\text{Using Wallis's Theorem:}$$

$$\begin{align}
\frac \pi 2 &\approx \frac 2 1 \times \frac 2 3 \times \frac 4 3 \times \frac 4 5 \times \times\ldots\times\frac{2n}{2n-1}\times\frac{2n}{2n+1}\\
\implies \pi &\approx\frac{2\times 2\times 4\times 4\times\ldots\times 2n\times 2n}{1\times 1\times 3\times 3\times \ldots\times (2n-1)\times(2n-1)}\times\frac{2n}{2n+1}\\
\implies \sqrt{\pi}&\approx\frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\\
\implies &\lim_{n\to\infty}\frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}=\sqrt{\pi}\\\\

&\frac{2\times 4\times\ldots\times 2n}{2\times 4\times\ldots\times 2n}\times\left(\frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\right)\\
&=\left(\frac{2^2\times 4^2\times\ldots\times 2n^2}{1\times 3\times \ldots\times (2n-1)\times2\times 4\times\ldots\times 2n}\times\frac{1}{\sqrt{n}}\right)\\
&=\frac{2^{2n}(n!)^2}{(2n)!}\approx \sqrt{\pi}\times\sqrt{n}=\sqrt{\pi n}\\
&\frac{(2n)!}{2^{2n}(n!)^2}\approx\frac{1}{\sqrt{\pi n}}\\
&\frac{ {2n}\choose{n}}{2^{2n}}\approx\frac{1}{\sqrt{\pi n}}\ \ \ \ \blacksquare
\end{align}$$

# Approximating $$\pi$$ Using Wallis's
## Main Content
According to Wallis's Theorem:

$$\begin{align}
&\lim_{n\to\infty}\frac 2 1 \times \frac 2 3 \times \frac 4 3 \times \frac 4 5 \times \times\ldots\times\frac{2n}{2n-1}\times\frac{2n}{2n+1}=\frac{\pi}{2}\\
&\implies \pi = 2\times \lim_{n\to\infty}\frac 2 1 \times \frac 2 3 \times \frac 4 3 \times \frac 4 5 \times \times\ldots\times\frac{2n}{2n-1}\times\frac{2n}{2n+1}
\end{align}$$

To get better and better approximations of $$\pi$$, multiply more of these products together:

$$\begin{align}
&\pi\approx2\times\frac 2 1 = 4\\
&\pi\approx2\times\frac 2 1\times \frac 2 3 = 2.\bar{6}\\
&\pi\approx2\times\frac 2 1\times \frac 2 3 \times \frac 4 3 = 3.\bar{5}\\
&\pi\approx2\times\frac 2 1\times \frac 2 3 \times \frac 4 3 \times \frac 4 5 = 2.8\bar{4}\\
&\pi\approx\ldots
\end{align}$$

# Approximating $$\tan^{-1}a$$
## Main Content
We can approximate $$\tan^{-1}a\ \ (\forall\ |a|\leq 1)$$ to the necessary accuracy, $$z$$, by using the following steps:

* Find $$n$$ such that

$$\frac{a^{2n+3}}{2n+3}\leq z$$

* Find approximation by plugging $$n$$ and $$a$$ into:

$$a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}$$

* To check answer, approximation should be within $$z$$ of actual value of $$\tan^{-1}a$$

### Proof.

$$\begin{align}
\tan^{-1}a&=\int_0^a\frac{1}{1+x^2}dx\\\\
\text{Using long division}&\text{ to find $\frac{1}{1+x^2}$:}\\
\end{align}$$

$$\begin{align}
\require{enclose}
1-x^2+x^4-\ldots \\[-3pt]
1+x^2\phantom{0} \enclose{longdiv}{1\phantom{00000000000000}}\kern-.2ex \\[-3pt]
\underline{1+x^2}\phantom{0000000000} \\[-3pt]
-x^2\phantom{0000000000} \\[-3pt]
\underline{-x^2-x^4}\phantom{00000} \\[-3pt]
x^4\phantom{00000} \\[-3pt]
\underline{x^4+x^6} \\[-3pt]
-x^6 \\[-3pt]
\ldots \\[-3pt]\\
\end{align}$$

$$\begin{align}
\frac{1}{1+x^2}&=1-\frac{x^2}{1+x^2}\\
&=1-x^2+\frac{x^4}{1+x^2}\\
&=1-x^2+x^4-\frac{x^6}{1+x^2}\\
&=1-x^2+x^4-x^6+\ldots+(-1)^nx^{2n}+(-1)^{n+1}\frac{x^{2n+2}}{1+x^2}\\
&\implies \text{$\frac{1}{1+x^2}$ can be expressed as a geometric series}\\
&\phantom{000000}\text{with 1st term 1, ratio $-x^2$, converging to $\frac{1}{1+x^2}$}\\\\
\end{align}$$

$$\text{Integrating previous result:}$$

$$\begin{align}
\int_0^a\frac{1}{1+x^2}dx&=\int_0^a\left(1-x^2+x^4-x^6+\ldots+(-1)^nx^{2n}+(-1)^{n+1}\frac{x^{2n+2}}{1+x^2}\right)dx\\
&=\left(x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\ldots+(-1)^n\frac{x^{2n+1}}{2n+1}\right)\Big|_0^a+\int_0^a(-1)^{n+1}\frac{x^{2n+2}}{1+x^2}dx\\
&=\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right)+(-1)^{n+1}\int_0^a\frac{x^{2n+2}}{1+x^2}dx\\
\implies \tan^{-1}a&=\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right)+(-1)^{n+1}\int_0^a\frac{x^{2n+2}}{1+x^2}dx\\\\
\end{align}$$

$$\begin{align}
\text{Let } E_n(a)=(-1)^{n+1}&\int_0^a\frac{x^{2n+2}}{1+x^2}dx\\
\frac{1}{1+x^2}&\leq 1\\
\implies\frac{x^{2n+2}}{1+x^2}&\leq x^{2n+2}\\
\implies \int_0^a\frac{x^{2n+2}}{1+x^2}dx&\leq\int_0^a x^{2n+2}dx\\
\implies\int_0^a\frac{x^{2n+2}}{1+x^2}dx&\leq\frac{a^{2n+3}}{2n+3}\\
\implies\left|(-1)^{n+1}\int_0^a\frac{x^{2n+2}}{1+x^2}dx\right|&\leq\frac{a^{2n+3}}{2n+3}\\
\implies|E_n(a)|&\leq\frac{a^{2n+3}}{2n+3}\\\\
\end{align}$$

$$\text{Taking limit of previous result:}$$

$$\begin{align}
|a|\leq1&\implies\lim_{n\to\infty}|E_n(a)|\leq\lim_{n\to\infty}\frac{a^{2n+3}}{2n+3}\\
&\implies\lim_{n\to\infty}|E_n(a)|\leq0\\
&\implies\lim_{n\to\infty}|E_n(a)|=0\\
|a|>1&\implies\lim_{n\to\infty}|E_n(a)|\leq\lim_{n\to\infty}\frac{a^{2n+3}}{2n+3}\\
&\implies\lim_{n\to\infty}|E_n(a)|\leq\infty\\
&\implies\lim_{n\to\infty}|E_n(a)|\ \ \text{diverges}\\\\
\end{align}$$

$$\text{Apply results to $\tan^{-1}a$:}$$

$$\begin{align}
E_n(a)&=(-1)^{n+1}\int_0^a\frac{x^{2n+2}}{1+x^2}dx\\
\implies \tan^{-1}a &= \left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right) +E_n(a)\\
\implies \lim_{n\to\infty}\tan^{-1}a &=\lim_{n\to\infty}\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right) +\lim_{n\to\infty}E_n(a)\\
\implies \tan^{-1}a &=\lim_{n\to\infty}\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right) +\lim_{n\to\infty}|E_n(a)|\\
|a|\leq1&\implies\lim_{n\to\infty}|E_n(a)|=0\\
&\implies\tan^{-1}a =\lim_{n\to\infty}\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right) +0\\
&\implies\tan^{-1}a\ \ \text{can be approximated to }\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right)\\
|a|>1&\implies\lim_{n\to\infty}|E_n(a)|\ \ \text{diverges}\\
&\implies\tan^{-1}a \ \ \text{cannot be approximated}\ \ \ \ \blacksquare
\end{align}$$

## Applications
* 1.) $$\tan^{-1}\left(\frac 1 2\right)$$ approximated to $$10^{-3}$$
  * Find $$n$$ such that:
  * $$\begin{align}\frac{\left(\frac 1 2\right)^{2n+3}}{2n+3}&\leq 10^{-3}\\n&=2\end{align}$$
  * Find approximation by plugging $$n=2$$ and $$a=\frac 1 2$$ into:
  * $$a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\\=\frac 1 2 -\frac{\left(\frac 1 2 \right)^3}{3}+\frac{\left(\frac 1 2 \right)^5}{5}\\=0.46458\bar{3}$$
  * To check answer, approximation should be within $$10^{-3}$$ of actual value of $$\tan^{-1}\left(\frac 1 2\right)$$:
  * $$\begin{align}\text{Approximated }\tan^{-1}\left(\frac 1 2\right) &= 0.46458\bar{3}\\\text{Actual }\tan^{-1}\left(\frac 1 2\right) &= 0.463647609\ldots\\\text{Difference between Actual and Approx.} &= 0.00093572433\ldots\\0.00093572433\ldots &< 10^{-3}\end{align}$$
  * Answer: $$0.46458\bar{3}$$
* 2.) Approximate $$\pi$$
  * Plugging $$a=1$$ into $$\tan^{-1}a$$ approximation formula:
  * $$\tan^{-1}(a)=\left(a-\frac{a^3}{3}+\frac{a^5}{5}-\frac{a^7}{7}+\ldots+(-1)^n\frac{a^{2n+1}}{2n+1}\right)\\\tan^{-1}(1)=\left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots+(-1)^n\frac{1}{2n+1}\right)\\\frac \pi 4 = \left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots+(-1)^n\frac{1}{2n+1}\right)\\\pi = 4\left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots+(-1)^n\frac{1}{2n+1}\right)$$
  * Answer: Approximate $$\pi$$ by choosing an $$n$$ and plugging it into $$4\left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\ldots+(-1)^n\frac{1}{2n+1}\right)$$

# "Polynomial Bases"
## Introduction Problems
* 1.) Convert 2018 to base 9
  * $$\begin{align}2018\div9&=224\ R\ 2 \\224\div9&=24\ R\ 8 \\24\div9&=2\ R\ 6 \\\implies 2018 \text{ in base } 9 &= 2682\end{align}$$
  * Answer: 2682
* 2.) Convert $$x^3+x+1$$ to a polynomial in $$(x-2)$$
  * The process is identical to converting numerical bases
  * $$\begin{align}x^3+x+1&=11+(x-2)(x^2+2n+5) \\&=11+(x-2)(13+(x-2)(x+4)) \\&=11+(x-2)(13+(x-2)(6+1(x-2))) \\&=11+13(x-2)+6(x-2)^2+1(x-2)^3\end{align}$$
  * Answer: $$11+13(x-2)+6(x-2)^2+1(x-2)^3$$

## Main Content
A polynomial $$P(x)$$ of degree $$n$$ can be written as a polynomial in $$(x-a)$$:

$$\forall \text{ unique constants } a_0,a_1,\ldots,a_n\\
P(x)=a_0+a_1(x-a)+a_2(x-a)^2+\ldots+a_n(x-a)^n$$

The constants can be calculated using:

$$a_k=\frac{P^{(k)}(a)}{k!}$$

where $$P^{(k)}(x)$$ is the function $$P(x)$$ after taking $$k$$ derivatives.

And the polynomial can be expressed as:

$$P(x)=\sum_{k=0}^n\frac{P^{(k)}(a)}{k!}(x-a)^k$$

### Proof.

$$\text{WWTP: }a_k=\frac{P^{(k)}(a)}{k!}$$

$$\text{Plugging in $x=0$ to $P(x)$:}$$

$$\begin{align}
P(x) &= a_0+a_1(x-a)+a_2(x-a)^2+\ldots+a_n(x-a)^n \\
P(a) &= a_0
\end{align}$$

$$\text{Then use derivatives:}$$

$$\begin{align}
P'(x) &= a_1+2a_2(x-a)+3a_3(x-a)^2+\ldots+na_n(x-a)^{n-1} \\
P'(a) &= a_1 \\
P''(x) &= 2a_2+6a_3(x-a)+12a_4(x-a)^2+\ldots+n(n-1)a_n(x-a)^{n-2} \\
P''(a) &= 2a_2 \\
&\ldots \\
\end{align}$$

$$
\text{After taking $k$ derivatives of $P(x)$,} \\
\text{non-zero values of $P^{(k)}(x)$ start from $a_k(x-a)^k$:} \\
$$

$$P^{(k)}(x)=\left(\frac{d}{dx}\right)^k(a_k(x-a)^k+\ldots)$$

$$\text{and k derivatives of $a_k(x-a)^k$ is $k!a_k$:}$$

$$\begin{align}
P^{(k)}(x) &= k!a_k+\ldots \\
P^{(k)}(a) &= k!a_k \\
a_k &= \frac{P^{(k)}(a)}{k!}\ \ \ \ \blacksquare
\end{align}$$

### Proof.

$$\text{WWTP: }P(x)=\sum_{k=0}^n\frac{P^{(k)}(a)}{k!}(x-a)^k$$

$$\text{Given by previous proof:}$$

$$\begin{align}
a_k &= \frac{P^{(k)}(a)}{k!} \\
P(x) &= a_0+a_1(x-a)+a_2(x-a)^2+\ldots+a_n(x-a)^n \\
&= \frac{P^{(0)}(a)}{0!}(x-a)^0+\frac{P^{(1)}(a)}{1!}(x-a)^1+\ldots+\frac{P^{(n)}(a)}{n!}(x-a)^n \\
&= \sum_{k=0}^n\frac{P^{(k)}(a)}{k!}(x-a)^k\ \ \ \ \blacksquare
\end{align}$$

## Applications
* 1.) Express $$P(x)=x^3+x+1$$ in $$(x-2)$$
  * $$\begin{align}& & P(2)&=11 \\P'(x)&=2x^2+1 & P'(2)&=13\\P''(x)&=6x & P''(2)&=12\\P'''(x)&=6 & P'''(2)&=6\\\end{align}$$
  * $$P(x) = \sum_{k=0}^n\frac{P^{(k)}(a)}{k!}(x-a)^k \\\text{Degree of $P(x)=n$ and $a=2$} \\\implies P(x) = \sum_{k=0}^3\frac{P^{(k)}(2)}{k!}(x-2)^k \\= \frac{P^{(0)}(2)}{0!}(x-2)^0+\frac{P^{(1)}(2)}{1!}(x-2)^1+\frac{P^{(2)}(2)}{2!}(x-2)^2+\frac{P^{(3)}(2)}{3!}(x-2)^3 \\= \frac{11}{1}(x-2)^0+\frac{13}{1}(x-2)^1+\frac{12}{2!}(x-2)^2+\frac{6}{3!}(x-2)^3 \\= 11+13(x-2)+6(x-2)^2+1(x-2)^3 \\$$
  * Answer: $$11+13(x-2)+6(x-2)^2+1(x-2)^3$$
* 2.) Express $$P(x)=x^4$$ in $$(x+3)$$
  * $$\begin{align}& & P(-3)&=81 \\P'(x)&=4x^3 & P'(-3)&=-108\\P''(x)&=12x^2 & P''(-3)&=108\\P'''(x)&=24x & P'''(-3)&=-72\\P''''(x)&=24 & P''''(-3)&=24\\\end{align}$$
  * $$P(x) = \frac{81}{0!}+\frac{-108}{1!}(x+3)+\frac{108}{2!}(x+3)^2+\frac{-72}{3!}(x+3)^3+\frac{24}{4!}(x+3)^4 \\= 81-108(x+3)+54(x+3)^2-12(x+3)^3+1(x+3)^4$$
  * Answer: $$81-108(x+3)+54(x+3)^2-12(x+3)^3+1(x+3)^4$$

# Taylor Polynomials
## Main Content
**Definition:**

A function $$f(x)$$ is $$\underline{\textbf{infinitely differentiable}}$$ if you can keep taking derivative after derivative of $$f(x)$$ and obtain functions that are defined

**Definition:**

Let $$f(x)$$ be infinitely differentiable at $$x=a$$, the $$\underline{n^{\text{th}} \textbf{ order Taylor Polynomial of } f(x) \textbf{ at } x=a}$$ is:

$$T_{(n,f,a)}(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k$$
