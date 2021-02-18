from random import shuffle

s1 = input('Student 1: ')
s2 = input('Student 2: ')
s3 = input('Student 3: ')
s4 = input('Student 4: ')
slist = [s1, s2, s3, s4]
shuffle(slist)

print(f'The order for presentation is: {slist}')
