N=int(raw_input())
s=1
while(N>0):
  a=N%10
  s*=a
  N/=10
print s  

