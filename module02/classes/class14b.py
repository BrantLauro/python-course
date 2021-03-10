n = 1
impair = odd = 0

while n != 0:
    n = int(input('Type a number: '))
    if n != 0:
        if n % 2 == 0:
            impair += 1
        else:
            odd += 1
print(f'You typed {impair} impair numbers and {odd} odd numbers')
