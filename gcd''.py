N,M=map(int,raw_input().split())
if(M>N):
  p=M
else:
  p=N
for i in range(1,p+1):
  if(M%i==0 and N%i==0):
    q=i
print q    
