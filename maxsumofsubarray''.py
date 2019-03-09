N=int(raw_input())
a=list(map(int,raw_input().split()))
b=[]
b.append(sum(a))
for i in range(0,N-1):
  c,d=a[:i+1],a[i+1:]
  if sum(c)>sum(d):
    b.append(sum(c))
  else:
    b.append(sum(d))
print(max(b))
