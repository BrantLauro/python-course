print(f'''{22*"="}
= Fibonacci Sequence =
{22*"="}''')
n = int(input('Type a number to stop: '))
stop = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')

while stop != n:
    t = t1 + t2
    print(f' → {t}', end='')
    t1 = t2
    t2 = t
    stop += 1