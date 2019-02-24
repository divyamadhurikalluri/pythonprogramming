S=raw_input()
p=[]
for x in S:
  if(x not in p):
    p.append(x)
print("".join(map(str,p[::-1])))    
