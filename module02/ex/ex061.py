start = int(input('Type a number for start: '))
reason = int(input('Reason: '))
final = start + (10 - 1) * reason

while start != final+reason:
    print(start)
    start += reason