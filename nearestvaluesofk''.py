N,K=list(map(int,raw_input().split()))
a,b=[],[]
for i in list(map(int,raw_input().split(" "))):
  a.append([abs(i-K),i]) 
a.sort()
a=a[1:]
for i in a[:3]:
  b.append(i[1])
print(' '.join(map(str,b)))

'''

N,K=list(map(int,input().split()))
a=[[abs(i-K),i] for i in list(map(int,input().split(" ")))]
a.sort()
a=a[1:]
b=[i[1] for i in a[:3]]
print(*b)


'''
