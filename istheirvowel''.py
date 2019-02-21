S=raw_input()
v=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(S)):
  if(S[i] in v):
    print("yes")
    break
else:
  print("no")    
