N=input()
A=map(int,raw_input().split())
B=map(int,raw_input().split())
C=[]
for x in range(0,N):
  p=A[x]+B[x]
  C.append(p)
for x in C:  
  k=x
  print ' '.join(str(k))
  

