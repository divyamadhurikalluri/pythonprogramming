N=int(raw_input())
s=list(map(int,raw_input().split()))
a=0
for x in range(0,N):
  for y in range(0,x):
    if(s[x]>s[y]):
      a+=s[y]
print(a)



'''


N=int(raw_input())
s=list(map(int,raw_input().split()))
a=[]
for x in range(1,N):
  b=0
  for y in range(x):
    if(s[x]>s[y]):
      b+=s[y]
  a.append(b)
print(sum(a))


'''

