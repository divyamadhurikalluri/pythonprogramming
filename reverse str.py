S=raw_input()
N=len(S)
n=S.split(" ")
m=[i[::-1]for i in n]
l= " ".join(m)
print(l)    
