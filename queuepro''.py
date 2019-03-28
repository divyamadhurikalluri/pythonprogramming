N=int(raw_input())
T=sorted(list(map(int,raw_input().split())))
A=1
for i in range(1,N):
  if sum(T[:i])<=T[i]:
    A+=1
print(A)
