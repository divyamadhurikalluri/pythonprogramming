N=int(raw_input())
a=list(raw_input().split())
for X in range(0,N):
  a[X]=a[X].lower()
a= sorted(a)
for X in a:
  print X
