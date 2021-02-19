house_price = float(input('How is the house price? $'))
wage = float(input('How is your wage? $'))
years = float(input('For how many years you will pay? '))
payment = house_price / (years*12)

if payment < (wage*0.3):
    print(f'The mensal payment is: {payment}')
else:
    print(f'Unfortunately, with your wage, in this period of time, you can not buy this house. ')