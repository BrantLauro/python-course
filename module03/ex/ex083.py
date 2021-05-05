expression = input('Type a expression: ').upper()
parenteses_l = expression.count('(')
parenteses_r = expression.count(')')
if parenteses_l == parenteses_r:
    print('Correct expression')
else:
    print('Incorrect expression')
