numbers = []
for c in range(0, 5):
    number = (int(input('Type a number: ')))
    if c == 0 or number > numbers[-1]:
        numbers.append(number)
    else:
        pos = 0
        while pos < len(number):
            if number <= numbers[pos]:
                numbers.insert(pos, number)
                break
            pos += 1
print(numbers)
#this program is cool 