N,S=list(map(int,raw_input().split()))
a=sorted(list(map(int,raw_input().split())))
a=a[::-1]
s=0
for i in range(len(a)):
  if(S>=a[i]):
    s+=int(S/a[i])
    S%=a[i]
if(S==0):
  print(s)
else:
  print("not possible")
