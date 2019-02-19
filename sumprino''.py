N=int(raw_input())
s=0
for x in range(2,N):
  if((x%2!=0) and (x%10==3)):
    s=s+x
print s  
