def avg(num):
  s=0
  for x in num:
    s+=x
  return (s/len(num))
N=int(raw_input())
a=list(map(int,raw_input().split()))
for x in range(1,N):
  s1=avg(a[:x])
  s2=avg(a[x:])
  if s1==s2:
    print('yes')
    break
else:
  print('no')
