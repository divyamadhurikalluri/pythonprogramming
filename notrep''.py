N=int(raw_input())
n=map(int,raw_input().split())
for x in n:
  if(n.count(x)==1):
    print(x)
