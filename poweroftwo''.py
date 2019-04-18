N=int(raw_input())
p=round(pow(N,0.5))
q=pow(2,p)
if N==1:
  print('yes')
elif N==q:
  print("yes")
else:
  print("no")
