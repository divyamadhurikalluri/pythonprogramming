s=raw_input()
f,f2=0,0
for i in s:
  if i.isalpha():
    f=1
  if i.isdigit():
    f2=1
if f==1 and f2==1:
  print("Yes")
else:
  print("No")
