d = float(input('Whats the distance in kms fo the trip? '))

if d <= 200:
    print(f'The ticket will be ${d * 0.50:.2f}')
else:
    print(f'The ticket will be ${d * 0.45:.2f}')
