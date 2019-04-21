N,K=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
a=[]
for i in l:
	if i%2==1:
		a.append(i)
print a
print(a[K-1])
