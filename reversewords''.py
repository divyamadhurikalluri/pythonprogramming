S=raw_input().split()
p=[]
for i in S:
  p.append(i[::-1])
print(" ".join(p))  
