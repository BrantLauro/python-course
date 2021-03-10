lunch = 'hamburger', 'pizza', 'fries', 'milkshake'

#for c in lunch:
#    print(f'I will eat {c}!')

#for c in range(0, len(lunch)):
#    print(f'I will eat {lunch[c]} in the position {c}!')

for pos, c in enumerate(lunch):
    print(f'I will eat {c} in the position {pos}')