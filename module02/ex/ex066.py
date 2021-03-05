n = s = a = 0
while True:
    n = int(input('Type a number [999 to stop]: '))
    if n == 999:
        break
    s += n
    a +=1
print(f'The sum of the {a} numbers typed is {s}!')
