matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair = []

for width in range(0, 3):
    for length in range(0, 3):
        number = int(input('Type a number: '))
        matrix[width][length] = number
        if number % 2 == 0:
            pair.append(number) 

for width in range(0, 3):
    for length in range(0, 3):
        print(f'[{matrix[width][length]:^5}]', end=' ')
    print()
print('=' * 30)
print(f'The sum of all pair numbers is: {sum(pair)}')
print(f'The sum of all numbers in third column is: {matrix[0][2] + matrix[1][2] + matrix[2][2]}')
print(f'The best number in the second line is: {max(matrix[1])}')
