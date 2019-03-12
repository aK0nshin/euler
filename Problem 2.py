#Even Fibonacci numbers
#
#Problem 2

limit = int(input('Enter limit: '))
result = 0
x = 1
y = 1

while x < limit:
    if x % 2 == 0:
        result += x
    x, y = x+y, x
    
print(result)
