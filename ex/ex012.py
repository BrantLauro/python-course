p = float(input('What is de price of the product? $'))
dis = float(input('What is the discount? '))
d = p - p * (dis/100)

print(f'The new price with the discount of {dis}% is {d:.2f}')
