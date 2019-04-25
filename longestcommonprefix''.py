N=int(input())
l=[]
for i in range(0,N):
    l.append(input())
c=[]
for i in zip(*l):
  if i.count(i[0])==len(i):
    c.append(i[0])
  else:
    break
a=''.join(c)
print(a)
