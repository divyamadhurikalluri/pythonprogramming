
N=int(raw_input())
a=[]
for i in range(0,N):
  a.append(input())
for y in range(0,len(a)):
    for z in range(0,len(a)):
      if(a[y]!=a[z]):
        break
print (a[z])        
