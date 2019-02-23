N,Q=map(int,raw_input().split())
x=list(map(int,raw_input().split()))
a=[]
for i in range(0,Q):
  U,V=map(int,raw_input().split())
  n=0
  for j in range(U-1,V):
    n=n+x[j]
  a.append(n)
print(a[0])
print(a[1])
print(a[2])  
