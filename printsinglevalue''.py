N=raw_input() 
n=list(map(int,raw_input().split()))

'''
a=[]
for i in range(0,len(n)):
    e=n.count(n[i])
    if(e<2):
      a.append(n[i])
print(' '.join(map(str,a)))
'''

for i in range(0,len(n)):
  e=n.count(n[i])
  if(e<2):
    print(n[i])
