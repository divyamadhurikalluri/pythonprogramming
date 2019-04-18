N,K=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
c=0
for i in range(0,N):
  if(l[i]==K):
    c+=1
print c    
