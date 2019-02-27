N=int(input())
a=[]
if N==2:
  print(0)
for x in range(2,N):
    for y in range(2,x):
        if(x%y==0):
            break
    else:
        a.append(x)
sorted(a) 
print ' '.join(map(str,a))       
