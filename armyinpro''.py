N=int(raw_input())
m=list(map(int,raw_input().split()))
c=0
for i in range(len(m)):
	for j in range(i+1,len(m)):
		for k in range(j+1,len(m)):
			if(m[i]>m[j]>m[k]):
				c+=1
print(c)
