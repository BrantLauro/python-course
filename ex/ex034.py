s = float(input('What is the salary of the functionary? $'))

if s > 1250.00:
    t = s + s * 0.10
    print(f'His salary increased by 10% and is now {t:.2f}')
else:
    f = s + s * 0.15
    print(f'His salary increased by 15% and is now {f:.2f}')
