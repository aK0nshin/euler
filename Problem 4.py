#Largest palindrome product
#
#Problem 4

result = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        temp = i * j
        tempStr = str(temp)
        if tempStr == tempStr[ : : -1]:
            if result < temp:
                result = temp
print(result)
