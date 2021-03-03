start = int(input('Type a number for start: '))
reason = int(input('Reason: '))
final_number = 1
final = start + (10 - 1) * reason

while final_number != 0:
    while start != final + reason:
        print(f'{start}', end=" ")
        start += reason
    final_number = int(input('Want to see more numbers? How much? '))
    final = start + (final_number - 1) * reason
