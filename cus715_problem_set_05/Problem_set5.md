#####Question 1
Supposed that
$$T(n)<cn$$
(1) for $n=1,c=2$ :
$$T(1)=1<2*1$$
(2) for $n=k$ :
$$T(k)\leq ck$$
Since
$$T(n)=2*T(\cfrac n2)+1000n$$
$$T(n)=2*c*\cfrac n2+1000n$$
$$T(n)=c*n+1000n$$
$$T(n)=n*(c+1000)<cn$$
$$T(n) \in O(n)$$


#####Question2
Supposed that
$$T(n)<cn^2$$
(1) for $n=1,c=2$ :
$$T(1)=1<2*1$$
(2) for $n=k$ :
$$T(k)\leq ck^2$$
Since
$$T(n)=7*T(\cfrac n2)+18n^2$$
$$T(n)=7*c*(\cfrac n2)^2+18n^2$$
$$T(n)=7*c*(\cfrac {n^2}{4})+18n^2$$
$$T(n)=(\cfrac {7c}{4})n^2+18n^2$$
$$T(n)=(\cfrac {7c}{4}+18)n^2$$
$$T(n)=(\cfrac {7c}{4}+18)n^2<cn^2$$
$$T(n) \in O(n^2)$$

#####Question3
$$T(1)=5$$
$$T(n)=T(\cfrac n2)+2n+3$$

Supposed that
$$T(n)<cn$$
(1) for $n=1,c=6$ :
$$T(1)=5<6*1$$
(2) for $n=k$ :
$$T(k)\leq ck$$
Since
$$T(n)=T(\cfrac n2)+2n+3$$
$$T(n)=c*\cfrac n2+2n+3$$
$$T(n)=\cfrac c2n+2n+3$$
$$T(n)=n(\cfrac c2+2)+3<cn$$
$$T(n) \in O(n)$$
