N,K=map(int,raw_input().split())
a=0
b=K-1
while(a==0 and b>1):
  if(K%b==0 and N%b==0):
    a+=1
  b-=1
print(b+1)

