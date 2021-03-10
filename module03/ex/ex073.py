teams = 'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'
print(f'The places of Brasileirão are: {teams}')
print(f'The First 5 teams are {teams[:5]}')
print(f'The Last 4 teams are {teams[-4:]}')
print(f'Sorted teams: {sorted(teams)}')
print(f'Flamengo are in the position {teams.index("Flamengo")+1}')
