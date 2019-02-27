s=raw_input()
p=list(s)
for x in range (0,len(s)):
  if(x%2==0):
    p[x],p[x+1]=p[x+1],p[x]
print ''.join(p)
