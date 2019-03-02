N,K=map(int,raw_input().split())
a=0
while(N!=0):
  x=N%10
  if(x==K):
    a+=1
  N=int(N/10)
print(a)
