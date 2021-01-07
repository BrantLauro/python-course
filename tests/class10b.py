n1 = float(input('Type a \033[33mfist grade\033[m: '))
n2 = float(input('Type a \033[33msecond grade\033[m: '))

a = (n1+n2)/2

print(f'Your average was \033[3;30m{a:.1f}\033[m')

if a >= 6.0:
    print('\033[3;30mCongratulations!\033[m Your grades are great!')
else:
    print('\033[3;30mStudy more!\033[m Your grades are not so good!')

print('\033[30mHave a good day!')
