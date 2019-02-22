N=raw_input()  
b=[]
a=[]
for i in N:
  b.append(i) 
for x in range(0,len(N)):
  if(int(b[x])%2!=0):
    a.append(b[x])
print(' '.join(map(str,a)))
