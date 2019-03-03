N=int(raw_input())
a=list(map(int,raw_input().split()))
b=0
for i in range(0,N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if(a[i]<a[j]<a[k]):
        b+=1
print(b)
