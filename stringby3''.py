N=raw_input()
a=[]
for x in N:
  if(x=='z' or x=='Z'):
    p=chr(ord(x)-23)
    a.append(p)
  else:  
    p=chr(ord(x)+3)
    a.append(p)
print "".join(a)
