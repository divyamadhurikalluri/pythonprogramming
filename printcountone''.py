S=raw_input()
a=[]
b=[]
for i in S:
    if(i not in a):
        a.append(i)
for i in a:
    if(S.count(i)==1):
      b.append(i)
print "".join(b)      
