n,l=map(int,input().split())
c=0
for i in range(n,l):
  p=i**(1/2)
  if p==int(p):
    c+=1
print(c)
'''
for i in range(l+1):
  k = i*i
  if k in range(n,l):
    c+=1
print(c)
'''
