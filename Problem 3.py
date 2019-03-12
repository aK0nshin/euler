#Largest prime factor
#
#Problem 3
import math

def isPrime(n):
    if n >= 2:
        for y in range(2, round(math.sqrt(n))):
            if not ( n % y ):
                return False
    else:
        return False
    return True

limit = int(input('Enter limit: '))
result = 0
i = 1

while i < math.sqrt(limit):
    if limit % i == 0 and isPrime(i):
        if result < i:
            result = i;
    i += 1
print(result)
