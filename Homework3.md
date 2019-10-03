<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
#### Problem Set3

##### Question1
suppose that the inner loop runs x times:
$$j*2^x = n$$
$$2^x=\frac nj$$
$$x=\log_2 \frac nj$$
so the time innerloop need is $2*\log_2 \frac nj$

tthe outter loop runs y times:
$$\frac {i}{2^y} = 1$$
$$i=2^y$$
$$y=\log_2 i$$
so the total time is
$$2+\log_2i+\sum_{i=1}^{\log_2i}(2*\log_2\frac ni)$$
since that $n=2^k$ so $i=n=2^k$
so
$$T(n)=2+k*(+\sum_{i=1}^{k}(2*(k-log_2i)))$$

##### Question2

a.  Error, out of bund, when i=5, there is no A[5]

b. $T(n)=n+n=2n$

c.
```
for(i=1; i<=n; i++){
  j=j+A[i];
  k=k+k;
}
```

#####Question3
$$f(n)=n^2+3n^3$$
Since
$$n>1$ So $n^3>n^2$$

So
$$n^2+3n^3 < 4n^3$$

So
$$f(n) \in O(n^3)$$

Since
$$n^2+3n^3 > 3n^3$$

So
$$f(n) \in \Omega(n^3)$$
