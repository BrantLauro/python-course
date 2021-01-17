from ex.style import bold, whiteblack, none
rea = float(input(f'How much {whiteblack}money{none} do you have in your {bold}wallet{none}? R$'))
dol = float(input(f'What is the {whiteblack}current price{none} of the {bold}dollar{none}? R$'))
eur = float(input(f'What is the {whiteblack}current price{none} of the {bold}euro{none}? R$'))
yen = float(input(f'What is the {whiteblack}current price{none} of the {bold}yen{none}? R$'))
lib = float(input(f'What is the {whiteblack}current price{none} of the {bold}libra{none}? R$'))

print(f'You can buy USD${rea / dol :.2f} with R${rea} with the USD at R${dol} \n'
      f'You can buy EUR${rea / eur :.2f} with R${rea} with the EUR at R${eur} \n'
      f'You can buy JPY${rea / yen :.2f} with R${rea} with the JPY at R${yen} \n'
      f'You can buy GBP${rea / lib :.2f} with R${rea} with the GBP at R${lib} \n')
