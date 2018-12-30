s = raw_input().lower()
p = s.split(" ") 
c =[]
for val in p:
    q = val[0].upper() + val[1:] 
    c.append(q) 
print ' '.join(c) 
