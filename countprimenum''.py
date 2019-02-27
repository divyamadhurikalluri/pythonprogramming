l,r=map(int,raw_input().split())
c=0
for x in range(l,r+1 ):
  if x > 1:
    for y in range(2,x):
      if (x % y) == 0:
        break
    else:
      c+=1
print(c)  
