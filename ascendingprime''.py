N=int(raw_input())
k=[]
for i in range(2,N):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
    k.append(i)
for x in range(0,len(k)):
  if(x==(len(k)-1)):
    print(k[x])
  else:
    print(k[x]) 
