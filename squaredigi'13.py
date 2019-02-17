N=int(raw_input())
s=0
while(N>0):
  x=N%10
  s=(x**2)+s
  N=N//10
print s  
