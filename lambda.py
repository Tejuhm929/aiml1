#lambda
A=lambda x,y:x+y
print(A(2,3))

B=lambda x,y:x if (x>y) else y
print(B(2,3))

C=lambda x:x*x
print(C(3))

#map
lst=[1,2,3,4,5,6,7,8]
l=list(map(lambda x:x+5,lst))
print(l)

#filter
lst=[1,2,3,4,5,6,7,8]
l=list(filter(lambda x:x%2,lst))
print(l)

#reduce
from functools import reduce
lst=[1,2,3,4,5,6,7,8]
l=reduce(lambda x,y:x+y,lst)
print(l)
