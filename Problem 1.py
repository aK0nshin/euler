#Multiples of 3 and 5
#
#Problem 1

limit = int(input('Enter limit: '))
result = 0

for x in range(limit-1):
    y = x+1;
    if y % 3 == 0 or y % 5 == 0:
        result += y

print(result)
