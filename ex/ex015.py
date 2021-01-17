days = int(input('For how many days the car has been rented: '))
km = float(input('How many kilometers traveled: '))
p = (days * 60) + (km * 0.15)

print(f'The total to pay is ${p :.2f}')
