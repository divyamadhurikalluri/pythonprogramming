N,K=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
a=0
for x in range(0,len(l)-1):
  for y in range(x+1,len(l)):
    if l[x]+l[y]==K:
      a=1
      break
    else:
      a=0  
  if a==1:
    print('yes')
    break
else:
  print('no')
