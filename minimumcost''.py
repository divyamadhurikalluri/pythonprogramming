X,Y=map(str,raw_input().split())
X,Y=list(X),list(Y)
x,y=len(X),len(Y)
i,j=0,0
Z=[]
while x>0:
  if X[i]==Y[j]:
    Z.append(X[i])
  i+=1
  j+=1
  x-=1
z=len(Z)
print(y-z)
