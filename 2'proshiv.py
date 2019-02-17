N,K=raw_input().split()
c=list(str(N))
K=int(K)
e=K
while(e>0):
  e=e-1
  del(c[e])
print(''.join(c))  
