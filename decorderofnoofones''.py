N=int(raw_input())
a=list(map(int,raw_input().split()))
m=max(a)
for x in range(0,N):
  for y in range(x,N):
    if(a[x]<a[y]):
      a[x],a[y]=a[y],a[x]
for p in a:
  print p      
