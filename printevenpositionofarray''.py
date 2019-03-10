N=int(raw_input())
a=list(map(int,raw_input().split()))
if N%2==0:
  print(N//2)
else:
  print(N-2)
