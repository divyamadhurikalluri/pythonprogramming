S=raw_input()
a=[]
for i in range(0,len(S)):
  if(S[i].isdigit()):
    a.append(S[i])
print(''.join(map(str,a)))    
