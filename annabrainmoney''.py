n,k=map(int,raw_input().split())
s=list(map(int,raw_input().split()))
w=(sum(s)-s[k])//2
c=int(raw_input())
if c==w:
  print('Bon Appetit')
else:
  print(c-w)
