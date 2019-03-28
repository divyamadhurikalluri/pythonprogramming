a=input()
b=len(a)
c=0
for i in range(1,b):
  j=0
  while j<b and len(a[:j]+a[i+j:])==b-i:
    n=a[:j]+a[j+i:]
    if int(n)%8==0:
      c=1
      print('yes')
      break
    j+=1
  if c==1:
      break
else:
  print('no')
