N = int(input())
a = []
for val in range(0,N):
   p = int(input())
   a.append(p)
a.sort()
b = sorted(set(a))
c = []
if a==b:
   print "unique"

else: 
    for i in range(len(b)):
        if(a.count(b[i]) > 1 ):
           c.append(b[i])
    print (' '.join (str(k) for k in c))
