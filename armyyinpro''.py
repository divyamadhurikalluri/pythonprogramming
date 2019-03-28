N=int(raw_input())
m=list(map(int,raw_input().split()))
n=len(m)
c=0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if(m[i]>m[j]>m[k]):
        c+=1
print(c)

