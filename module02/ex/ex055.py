weight_list = []

for c in range(0, 5):
    weight = float(input('What is your weight? '))
    weight_list.append(weight)
print(f'The heaviest is = {max(weight_list)}')
print(f'The Lightest is = {min(weight_list)}')
    