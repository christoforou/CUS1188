#####Question1
$$T(1) = 1$$
$$T(n) = 2T(\frac n2)+1000n$$

$$T(\frac n2) = 2T(\frac {n}{2^2})+1000\frac n2$$
$$T(n) = 2(2T(\frac {n}{2^2})+1000\frac n2)+1000n$$
$$T(n) = 2^2T(\frac {n}{2^2})+1000n+1000n$$
$$T(\frac {n}{2^2}) = 2T(\frac {n}{2^3})+1000\frac {n}{2^2}$$
$$T(n) = 2^2(2T(\frac {n}{2^3})+1000\frac {n}{2^2})+1000n+1000n$$
$$T(n) = 2^3T(\frac {n}{2^3})+1000n+1000n+1000n$$
$$T(n) = 2^kT(\frac {n}{2^k})+k*1000n$$
Since
$$T(1) = 1$$
So when
$$\frac {n}{2^k}=1$$
$$T(\frac {n}{2^k})=1$$
So
$$n=2^k$$
$$k=\log_2n$$
So
$$T(n) = n*1+\log_2n*1000n$$
$$T(n) = n+\log_2n*1000n \in O(n\log_2 n)$$

#####Question2
$$T(1) = 1$$
$$T(n) = 7T(\frac n2)+18n^2$$

$$T(\frac n2) = 7T(\frac {n}{2^2})+18(\frac {n}{2})^2$$
$$T(n) = 7(7T(\frac {n}{2^2})+18(\frac {n}{2})^2)+18n^2$$
$$T(n) = 7^2T(\frac {n}{2^2})+7*18(\frac {n}{2})^2+18n^2$$
$$T(\frac {n}{2^2}) = 7T(\frac {n}{2^3})+18(\frac {n}{2^2})^2$$
$$T(n) = 7^2(7T(\frac {n}{2^3})+18(\frac {n}{2^2})^2)+7*18(\frac {n}{2})^2+18n^2$$
$$T(n) = 7^3T(\frac {n}{2^3})+7^2*18(\frac {n}{2^2})^2+7^1*18(\frac {n}{2^1})^2+7^0*18(\frac n{2^0})^2$$
$$T(n) = 7^3T(\frac {n}{2^3})+18n^2*\frac {7^2}{2^{2*2}}+18n^2*\frac {7^1}{2^{1*2}}+18n^2*\frac {7^0}{2^{0*2}}$$
$$T(n) = 7^3T(\frac {n}{2^3})+18n^2*(\frac {7}{2^{2}})^2+18n^2*(\frac {7}{2^{2}})^1+18n^2*(\frac {7}{2^{2}})^0$$
$$T(n) = 7^kT(\frac {n}{2^k})+18n^2*\sum_{i=0}^{k-1}(\frac {7}{2^{2}})^i$$
Since
$$T(1) = 1$$
So when
$$\frac {n}{2^k}=1$$
$$T(\frac {n}{2^k})=1$$
So
$$n=2^k$$
$$k=\log_2n$$
$$7^{\log_2n}=n^{\log_27}$$
So
$$T(n) = n^{\log_27}+18n^2*\sum_{i=0}^{\log_2n-1}(\frac {7}{2^{2}})^i$$
$$T(n) = n^{\log_27}+18n^2*\frac {(\frac {7}{2^{2}})^{\log_2n-1+1}-1}{\frac {7}{2^{2}}-1} $$
$$T(n) = n^{\log_27}+18n^2*\frac {(\frac {7^{\log_2n}-n^2}{n^{2}})}{\frac {3}{4}}$$
$$T(n) = n^{\log_27}+24*(7^{\log_2n}-n^2)$$
$$T(n) = n^{\log_27}+24n^{\log_27}-24n^2$$
$$T(n) = 25n^{\log_27}-24n^2 \in O(n^{\log_27})$$

#####Question3
$$T(1)=5$$
$$T(n)=T(\cfrac n2)+2n+3$$


$$T(\frac n2) = T(\frac {n}{2^2})+2*\frac n2+3$$
$$T(n) = T(\frac {n}{2^2})+2*\frac n2+3+2n+3$$
$$T(\frac {n}{2^2}) = T(\frac {n}{2^3})+2*\frac {n}{2^2}+3$$
$$T(n) = T(\frac {n}{2^3})+2*\frac {n}{2^2}+3+2*\frac n2+3+2n+3$$
$$T(n) = T(\frac {n}{2^k})+2n*\sum_{i=0}^{k-1}2^{-i}+3k$$
Since
$$T(1) = 5$$
So when
$$\frac {n}{2^k}=1$$
$$T(\frac {n}{2^k})=5$$
So
$$n=2^k$$
$$k=\log_2n$$
So
$$T(n) = 5+2n*\sum_{i=0}^{\log_2n-1}2^{-i}+3\log_2n$$
Since
$$\sum_{i=0}^{\log_2n-1}2^{-i} \in [1,2]$$
So
$$T(n) = 5+2n*\sum_{i=0}^{\log_2n-1}2^{-i}+3\log_2n \in O(n)$$
