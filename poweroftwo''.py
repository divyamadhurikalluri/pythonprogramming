n=int(input())
p=round(pow(n,0.5))
q=pow(2,p)
if n==1:
  print('yes')
elif n==q:
  print("yes")
else:
  print("no")
