N= int(input())
S= 0
while(N> 0):
    R= N % 10
    S= S+R
    N= N//10
print(S)
