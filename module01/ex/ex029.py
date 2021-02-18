s = float(input('What is the speed of the car right now? km/h '))
f = (s - 80) * 7

if s > 80:
    print(f'FINE! You have exceeded the permitted limit of 80km/h \n'
          f'You have to pay a ${f:.2f} fine!')
print('Have a good day! Drive carefully!')
