print('='*18)
print('LAURO_BRANT_S BANK')
print('='*18)

money = int(input('How many you want to withdraw? $'))
total = money
paper = 50
total_paper = 0 
while True:
    if total >= paper:
        total -= paper
        total_paper += 1
    else:
        if total_paper != 0:
            print(f'{total_paper} notes of {paper}')
        if paper == 50:   
            paper = 20
        elif paper == 20:
            paper = 10
        elif paper == 10:
            paper = 1
        total_paper = 0
        if total == 0:
            break
