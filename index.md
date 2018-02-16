# Abramson Notes

# Sine Reduction Formula

$$\int \sin^{n}x dx=-\frac{1}{n}\sin^{n-1}x\cos x+\left(\frac{n-1}{n}\right)\int\sin^{n-2}x dx$$

**Proof.**
$$\begin{align}\text{Let }n\in\mathbb{Z}^{+},\ \text{Given }\int \sin^{n}x dx \\
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
**Theorem:**

$$\prod_{n \mathop = 1}^\infty \frac {2 n} {2 n - 1} \cdot \frac {2 n} {2 n + 1} = \frac 2 1 \cdot \frac 2 3 \cdot \frac 4 3 \cdot \frac 4 5 \cdot \frac 6 5 \cdot \frac 6 7 \cdot \frac 8 7 \cdot \frac 8 9 \cdots = \frac \pi 2$$

**Proof.**
$$\begin{align}\text{Sine Reduction Formula: } \\
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

$$\text{Plugging in for $I$:}\\1\geq \frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \times\frac 2 \pi \geq 1-\frac{1}{2n+2}$$


$$\frac \pi 2 (1)\geq \frac \pi 2 \left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \times\frac 2 \pi \right)\geq \frac \pi 2 \left(1-\frac{1}{2n+2}\right)\\
\frac \pi 2 \geq \frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1 \geq \frac \pi 2 \left(1-\frac{1}{2n+2}\right)\\
\lim_{n\to\infty}\left(\frac \pi 2\right) \geq \lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) \geq \lim_{n\to\infty}\left(\frac \pi 2 \left(1-\frac{1}{2n+2}\right)\right)\\
\frac \pi 2 \geq \lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) \geq \frac \pi 2\\\\$$

$$\text{By Squeeze Theorem: }\lim_{n\to\infty}\left(\frac{2n}{2n+1}\times\frac{2n}{2n-1}\times \ldots\times\frac 2 3 \times\frac 2 1\right) = \frac \pi 2\ \ \ \ \blacksquare$$

# Factorial Function

$$f(t)=\int_{0}^{\infty}x^t e^{-x}dx=tf(t-1)$$

**Proof.**

$$\begin{align}
\int x^t& e^{-x}dx\\
u&=x^t\\du&=tx^{t-1}dx\\dv&=e^{-x}dx\\v&=-e^{-x}\\
\int x^t e^{-x}dx &=-x^t e^{-x}\Big|^{\infty}_0+t\int_0^{\infty}x^{t-1}e^{-x}dx\\
&=0+t\int_0^{\infty}x^{t-1}e^{-x}dx&&\left(\lim_{x\to\infty}e^{-x}=0\right)\\
&=tf(t-1)\\
f(t)&=tf(t-1)\\\\
\implies f(0)=1,f(1)=1,&f(2)=2,f(3)=6,f(4)=24\\
\implies \forall t\in\mathbb{Z}^+ &\cup\{0\},\ f(t)=t!
\end{align}$$

# Gamma Function

$$\begin{align}
\Gamma(t)&=\int_0^\infty x^{t-1}e^{-x}dx\\
&=f(t-1)\\
\implies \Gamma(1)=1,\ \Gamma(2)&=1,\ \Gamma(3)=2,\ \Gamma(4)=6\\
\implies t\Gamma(t)&=\Gamma(t+1)\end{align}$$

## Applications
1. $$\left(\frac{1}{2}\right)!=\int_0^\infty \sqrt{x}e^{-x}dx\\\\\implies \text{Can compute any fractional factorial as long as you can compute the integral}$$

# Calculating Area Under Bell Curve

$$\begin{align}
\text{Bell Curve: }& e^{-x^2}\\
\text{Area Under Half: }& \int_0^\infty e^{-x^2}dx=\frac{\sqrt{\pi}}{2}
\end{align}$$

**Proof.**

$$\begin{align}
\text{Calculate reduction formula:}&\\
\int&(1-x^2)^ndx\\
u&=(1-x^2)^n\\du&=n(1-x^2)^{n-1}(-2x)dx\\dv&=1dx\\v&=x\\
\int(1-x^2)^ndx &= x(1-x^2)^n+2n\int x^2(1-x^2)^{n-1}dx\\
&=x(1-x^2)^n+2n\int(1-(1-x^2))(1-x^2)^{n-1}dx\\
\int(1-x^2)^ndx &= x(1-x^2)^n+2n\int(1-x^2)^{n-1}dx-2n\int(1-x^2)^ndx\\
(2n+1)\int(1-x^2)^ndx&=x(1-x^2)^n+2n\int(1-x^2)^{n-1}dx\\
\int(1-x^2)^ndx&=\frac{x(1-x^2)^n}{2n+1}+\frac{2n}{2n+1}\int(1-x^2)^{n-1}dx\\\\
\text{Calculate }\ f(n)\ \text{: }&\\
f(n)&=\int_0^1(1-x^2)^ndx\\
&=\left(\frac{x(1-x^2)^n}{2n+1}\right)\Big|_0^1+\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
&=0+\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
&=\frac{2n}{2n+1}\int_0^1(1-x^2)^{n-1}dx\\
f(n)&=\frac{2n}{2n+1}f(n-1)\\\\\end{align}$$

$$\begin{align}
\text{Calculate reduction formula:}&\\
\int\frac{1}{(1+x^2)^n}&=\int\frac{1+x^2}{(1+x^2)^n}-\frac{x^2}{(1+x^2)^n}dx\\
&=\int\frac{1}{(1+x^2)^{n-1}}dx-\int\frac{x^2}{(1+x^2)^n}dx\\
\text{Solving for: }& \int\frac{x^2}{(1+x^2)^n}dx\\
u&=x\\du&=1dx\\dv&=\frac{x}{(1+x^2)^n}\\v&=\int\frac{x}{(1+x^2)^n}dx
=\frac{1}{2-2n}\left(\frac{1}{(1+x^2)^{n-1}}\right)&&\text{(U-Sub)}\\
\int\frac{1}{(1+x^2)^n}=\int\frac{1}{(1+x^2)^{n-1}}dx&-\left(\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)-\frac{1}{2-2n}\int\frac{1}{(1+x^2)^{n-1}}dx\right)\\
&=\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)+\left(1+\frac{1}{2-2n}\right)\int\frac{1}{(1+x^2)^{n-1}}dx\\
&=\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)+\frac{2n-3}{2n-2}\int\frac{1}{(1+x^2)^{n-1}}dx\\\\
\text{Calculate }\ g(n)\ \text{: }&\\
g(n)&=\int_0^\infty\frac{1}{(1+x^2)^n}\\
&=\left(\frac{1}{2-2n}\left(\frac{x}{(1+x^2)^{n-1}}\right)\right)\Big|_0^\infty+\frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
&=0 + \frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
&=\frac{2n-3}{2n-2}\int_0^\infty\frac{1}{(1+x^2)^{n-1}}dx\\
g(n)&=\frac{2n-3}{2n-2}g(n-1)
\end{align}$$

$$\begin{align}
\text{Using Wallis's Theorem:}&\\
\frac \pi 2 &\approx \frac 2 1 \times \frac 2 3 \times \frac 4 3 \times \frac 4 5 \times \times\ldots\times\frac{2n}{2n-1}\times\frac{2n}{2n+1}\\
\implies \pi &\approx\frac{2\times 2\times 4\times 4\times\ldots\times 2n\times 2n}{1\times 1\times 3\times 3\times \ldots\times (2n-1)\times(2n-1)}\times\frac{2n}{2n+1}\\
\implies \sqrt{\pi}&\approx\frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\\
\text{Let}\ k(n) &= \frac{2\times 4\times\ldots\times 2n}{1\times 3\times \ldots\times (2n-1)}\times\frac{1}{\sqrt{n}}\\
&\implies\lim_{n\to\infty}k(n)=\sqrt{\pi}
\end{align}$$

$$\begin{align}
\text{From before:}&\\
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

$$\begin{align}
\text{Proving some} &\text{ intermediate results:}\\
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

$$\begin{align}
\text{Using all} &\text{ previous results:}\\
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
\implies &\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}
\end{align}$$
