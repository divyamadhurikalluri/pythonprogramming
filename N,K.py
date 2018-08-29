N=int(raw_input())
K=int(raw_input())
c=[]
for x in range(0,N):
    c.append(int(input()))
print(sum(c[:K]))
