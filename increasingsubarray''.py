N=int(raw_input())
a=list(map(int,raw_input().split()))
m,n=1,0
for i in range(0,len(a)-1):
  if a[i]<a[i+1]:
    m+=1
  else:
    m=1
  if n<m:
    n=m
print(n)
