n1 = input()
n2 =input()
for num in range(n1,n2+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
        print(num)
