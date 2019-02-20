N,K=map(int,raw_input().split())
a=map(int,raw_input().split())
i=0
for x in range(0,N):
  for y in range(x+1,N):
    if(a[x]-a[y]==K):
      i+=1
    elif(a[y]-a[x]==K):
      i+=1
    else:
      i=i
print i         
