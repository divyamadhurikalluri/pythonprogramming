N=int(raw_input())
a=list(map(int,raw_input().split()))
x=0
for i in range(0,N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if(a[i]+a[j]==a[k]):
        x=x+1
print x        
