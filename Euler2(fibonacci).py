fibonacci = [1,2]
#Stage1
def get_fibonacci(n):
    if n > 2:
        a = fibonacci[n-2]
        b = fibonacci[n-3]
        fibonacci.append(a + b)

#Stage2
for steps in range(1,11):
    get_fibonacci(steps)
    
#Stage3
sum_them = 0
for numbers in fibonacci:
    if numbers % 2 != 0:
        sum_them = sum_them + numbers

print(sum_them)