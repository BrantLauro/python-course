start = int(input('Type a number for start: '))
reason = int(input('Reason: '))
final = start + (10 - 1) * reason

for c in range(start, final+reason, reason):
    print(c)
