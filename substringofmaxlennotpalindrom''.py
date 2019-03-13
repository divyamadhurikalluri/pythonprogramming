S=raw_input()
s=''
a=list(reversed(S))
b=''.join(a)
if(S==b):
  for a in range(0,len(S)-1):
    s+=S[a]
  print(s)
else:
  print(S)
