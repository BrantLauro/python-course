height = float(input('How tall are you (m)? '))
mass = float(input('how much do you weigh (Kg)? '))
bmi = mass/height**2

print(f'Your BMI is {bmi:.2f}Kg/m²:')

if bmi < 18.5:
    print('Under weight')
elif 18.5 <= bmi < 25:
    print('Ideal weight')
elif 25 <= bmi < 30:
    print('Overweight')
elif 30 <= bmi < 40:
    print('Obesity')
else:
    print('Morbid obesity')