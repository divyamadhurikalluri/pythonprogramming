a,b=raw_input().split()
c=list(str(a))
b=int(b)
e=b
while(e>0):
  e=e-1
  del(c[e])
print(''.join(c))  
