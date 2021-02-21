print(f"{'='*12} BRANT'STORE {'='*12}")
price = float(input('How much the product costs? $'))
print('''Choose the form of payment:
[1] Cash/check
[2] Credit Card''')
payment = int(input('What is the payment method? '))

if payment == 1:
    price -= price * 0.1
    print(f'The price will be ${price:.2f}')
elif payment == 2:
    print('''Choose the installment:
    [1] In Cash 
    [2] Up to 2x
    [3] Up to 3x or more''')
    installment = int(input('Installment: '))
    if installment == 1:
        price -= price * 0.05
        print(f'The price will be ${price:.2f}')
    elif installment == 2:
        print(f'The price will be ${price:.2f} (${price / 2:.2f} per month)')
    elif installment == 3:
        price += price * 0.2
        time = int(input('For how many months? '))
        if time > 2:
            print(f'The price will be ${price:.2f} (${price / time:.2f} per month during {time} months)')
        else:
            print('[ERROR] Verify the data and try again!')
    else:
        print('[ERROR] Verify the data and try again!')
else:
    print('[ERROR] Verify the date and try again!')
