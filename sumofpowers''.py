N=raw_input()
a=list(N)
p=0
for x in range(0,len(a)):
  p=p+(int(a[x])**x)
print p 
