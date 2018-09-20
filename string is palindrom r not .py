S = raw_input()
string2 = ""
 
i = len(S)-1
 
while(i>=0):
   string2 = string2 +S[i]
   i = i-1
if(string2==S):
      print('yes')
else:
      print('no')    

