sum = 0

for c in range (0, 6):
    n = int(input('Type a number: '))
    if n % 2 == 0:
        sum += n
print(sum)
