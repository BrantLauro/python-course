number = int(input('Type a number to see the factorial: '))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)
