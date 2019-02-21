def sp(N,K,n):
  for x in range(N):
    for y in range(x+1,N):
      if((n[x]+n[y])==K):
        return('yes')
  return('no')
p=map(int,raw_input().split())        
p=list(p)        
q=map(int,raw_input().split())        
q=list(q)
print(sp(p[0],p[1],q))

