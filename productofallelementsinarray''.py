N=int(raw_input())
A=list(map(int,raw_input().split()))
b,c=[],[]
p=1
for i in range (0,N):
  b.append(A[i])
for i in range (0,N):
  for j in range (0,N):
    if(j!=i):
      p=p*b[j]
  c.append(p)
  p=1
print(" ".join(str(i) for i in c))  

'''
N=int(input())
A=list(map(int,input().split()))
b=[]
p=1
for i in range (0,N):
  b.append(A[i])
for i in range (0,N):
  for j in range (0,N):
    if(j!=i):
      p=p*b[j]
  print(p,end=' ')
  p=1
'''
