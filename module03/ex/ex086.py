matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for width in range(0, 3):
    for length in range(0, 3):
        number = int(input('Type a number: '))
        matrix[width][length] = number

for width in range(0, 3):
    for length in range(0, 3):
        print(f'[{matrix[width][length]:^5}]', end=' ')
    print()
