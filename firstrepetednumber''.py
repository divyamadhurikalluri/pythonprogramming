N=int(raw_input())
a=list(map(int,raw_input().split()))
for x in a:
  if(a.count(x)!=1):
    print(x)
    break
else:
  print("unique")
