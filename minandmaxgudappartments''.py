n,k=map(int,input().split())
'''
if k*2<=n:
  print(1,k)
else:
  print(1,n-k)
  
'''
'''

print(min(1,k,n-k),min(n-k,2*k))
'''
print(1,n-k)
