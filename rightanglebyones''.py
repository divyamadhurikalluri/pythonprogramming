N=int(input())
a=1
for i in range(0,N):
  for j in range(0,N):
    print(a,end=' ')
  print("\r")
  N=N-1
