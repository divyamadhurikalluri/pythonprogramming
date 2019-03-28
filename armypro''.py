N=int(input())
m=list(map(int,input().split()))
c=0
for x in range(0,len(m)-2):
  for y in range(x+1,len(m)-1):
    for z in range(y+1,len(m)):
      if(m[x]>m[y]>m[z]):
        c+=1
print(c)


