gender = input('What is your gender [M/F]? ').upper()[0].strip()

while gender != 'M' and gender != 'F':
    print('[ERROR] Verify tha data and try again!')
    gender = input('What is your gender [M/F]? ').upper()[0].strip()
print(gender)
