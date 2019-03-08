N=int(raw_input())
a=list(map(int,raw_input().split()))
s=[]
for i in range(0,N-1):
  if a[i]>max(a[i+1:]):
    s.append(a[i])
s.append(a[N-1])
print(' '.join(map(str,s)))
print(max(a))
