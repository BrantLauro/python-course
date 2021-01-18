s = float(input('What is the salary? $'))
i = float(input('What percentage of increase? '))
ns = s + s * (i / 100)

print(f'The salary {s:.2f} with the promotion of {i}% will be {ns :.2f}')
