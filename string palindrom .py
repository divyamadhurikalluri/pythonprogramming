string1 = raw_input()
string2 = ""
i = len(string1)-1
while(i>=0):
    string2 = string2 + string1[i]
    i = i-1
if(string2==string1):
    print('yes')
else:
    print('no')    

