N=int(raw_input())
l=list(map(int,raw_input().split()))
for i in range(0,N):
  if((i+1)!=l[i]):
    print(i)
    break
