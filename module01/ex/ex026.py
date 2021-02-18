a = str(input('Type a phrase: ')).strip().upper()

print(f'In this phrase we have {a.count("A")} letters "A" \n'
      f'The first "A" is on {a.find("A") + 1} \n'
      f'The last "A" is on {a.rfind("A") + 1}')
