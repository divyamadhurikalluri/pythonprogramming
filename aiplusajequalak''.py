N=int(raw_input())
l=list(map(int,raw_input().split()))
for i in range(0,len(l)-2):
  for j in range(i+1,len(l)-1):
    for k in range(j+1,len(l)):
      if l[i]+l[j]==l[k] and i<j<k:
        a=l[i],l[j],l[k]
        print(' '.join(map(str,a)))
