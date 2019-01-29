N=int(input())
a=[]
for i in range(0,N):
  p=int(input())
  a.append(p)
q=sorted(a)
r=q[::-1]
print "".join(map(str,r))

