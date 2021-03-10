from random import randint
numbers = []
while len(numbers) < 5:
    numbers.append(randint(0, 10))

print(numbers)
print(f'The better is {max(numbers)}')
print(f'The lower is {min(numbers)}')
