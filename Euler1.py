def checkNumbers(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    
sum = 0
for i in range(1,1000):
    print("checking the number", i)
    if checkNumbers(i):
        print(checkNumbers(i))
        sum = sum + i

print("sum of all the multiples of 3 or 5 bellow 10 is: ", sum)