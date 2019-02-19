N=int(raw_input())
s=0
while(N!=0):
  p=N%10
  s=s+(p**2)
  N=N/10
print s  
