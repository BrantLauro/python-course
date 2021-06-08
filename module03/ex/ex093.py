def lin():
    print('=' * 30)

lin()
print(f'{"PLAYER REGISTRATION":>24}')
lin()

player = {}

player['name'] = input('PLayer name: ').strip()
games = int(input(f'How many games does {player["name"]} played? '))
player['points'] = []
for c in range(0, games):
    player['points'].append(int(input(f'How many points does {player["name"]} made in the {c+1}° game? ')))
player['total'] = sum(player['points'])

lin()
print(player)

lin()
for k, v in player.items():
    print(f'The key {k} have the value {v}.')

lin()
print(f'{player["name"]} played a total of {games} games.')
for c in range(0, games):
    print(f'In the {c+1}° game, made {player["points"][c]} points')
print(f'The total is {player["total"]}')
lin()
