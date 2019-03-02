N=int(raw_input())
a=list(map(int,raw_input().split( )))
k=l=0
for i in range(0,len(a)):
  if i%2==0:
    k+=a[i]
  else:
    l+=a[i]
if k>l:
  print(k)
else:
  print(l)

'''

N=int(raw_input())
a=list(map(int,raw_input().split()))
k=a[::2]
l=a[1::2]
m=a[1::3]
if(sum(k)>sum(l) and sum(k)>sum(m)):
  print(sum(k))
elif(sum(m)>sum(k) and sum(m)>sum(l)):
  print(sum(m))
else:
    print(sum(l))


'''
