N=int(raw_input())
k=1
while(k>=1):
  k=k*2
  if(k==N):
    p=0
    break
  if(k>N):
    p=min(abs(k-N),abs(N-int(k/2)))
    break
print(p)
