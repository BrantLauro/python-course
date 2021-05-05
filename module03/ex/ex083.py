expression = input('Type a expression: ').upper()
parenteses = []
for c in expression:
    if c == '(':
        parenteses.append(c)
    elif c == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(c)
        
if len(parenteses) == 0:
    print('Correct expression')
else:
    print('Incorrect expression')
