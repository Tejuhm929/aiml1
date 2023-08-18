
a=[1,1,1]
b=[2,2,2]
c=[3,3,3]
l=list(map(lambda x,y,z:x+y+z,a,b,c))
print(l)


fruits=["mango","orange","apple","kiwi"]
l=list(filter(lambda x:"g"in x,fruits))
print(l)
