S=raw_input()
a=[]
c=0
for i in S:
  if not i in a:
    c+=1
    a.append(i)
  else:
    break
print(c)      
