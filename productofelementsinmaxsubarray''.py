N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[]
for i in range(N):
  c= 1
  for j in range(i,N):
    c*=a[j]
  b.append(c)
for i in range(N):
  c=1
  for j in range(i+1):
    c*=a[j]
  b.append(c)
print(max(b))
