a = str(input('Digite uma frase: ')).strip().upper()

print(f'Nesta frase existem {a.count("A")} letras "A" \n'
      f'O Primeiro "A" está na posição {a.find("A") + 1} \n'
      f'O último "A" está na posição {a.rfind("A") + 1}')
