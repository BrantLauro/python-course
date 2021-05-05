people = []
data = []
weighs = []
while True:
    data.append(input('What is your name? ').strip())
    weigh = int(input('How much do you weigh? '))
    weighs.append(weigh)
    data.append(weigh)
    people.append(data[:])
    data.clear()
    choice = ' '
    while choice not in 'NY':
        choice = input('Do you want to continue? [Y/N] ').upper().strip()[0]
    if choice == 'N':
        print(30*'-')
        break
    if choice == 'Y':
        print(30*'-')
most_heave_people = []
less_heave_people = []
for p in people:
    if p[1] == max(weighs):
        most_heave_people.append(p[0])
    if p[1] == min(weighs):
        less_heave_people.append(p[0])
print(f'You squared {len(people)} people')
print(f'The biggest weigh is {max(weighs)} that {most_heave_people} has')
print(f'The lowest weigh is {min(weighs)} that {less_heave_people} has')
