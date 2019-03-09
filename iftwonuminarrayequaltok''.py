N,K=map(int,raw_input().split())
A=list(map(int,raw_input().split()))
p=0
for i in range(0,N):
  for j in range(i,N):
    if(A[i]+A[j]==K):
      p+=1
if(p>1):
  print("YES")
else:
  print("NO")
