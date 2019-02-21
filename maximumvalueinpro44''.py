N,P,Q,R=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
a.sort()
for i in range(N):
  for j in range(N):
    for k in range(N):
      s=((P*a[i])+(Q*a[j])+(R*a[k]))
print(s)        
      
