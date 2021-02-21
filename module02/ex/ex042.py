print('*'*23)
print('*  Triangle Analyzer  *')
print('*'*23)

a = float(input('First straight: '))
b = float(input('Second straight: '))
c = float(input('Third straight: '))

if a + b > c and b + c > a and a + c > b:
    print('The above segments MAY form a triangle!')
    if a == b == c:
        print('It will be equilateral')
    elif a == b or a == c or b == c:
        print('It will be isosceles')
    elif a != b and a != c and b != c:
        print('It will be scalene')
else:
    print('The above segments CANNOT FORM a triangle!')
