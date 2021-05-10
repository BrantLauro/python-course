from random import randint as rd
from operator import itemgetter as ig
players = {}
ranking = []

for c in range(0, 4):
    players[f'player {c}'] = rd(1, 6)

ranking = sorted(players.items(), key = ig(1), reverse=True)

print('=' * 27)
print(f'{"RANKING":>17}')
print('=' * 27)

for i, v in enumerate(ranking):
    print(f'{i+1}° = {v[0]} = {v[1]}')