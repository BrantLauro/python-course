from style import blue, none

name = input(f'What`s your {blue}name{none}? ')

print(f'Nice to meet you {blue}{name:=^20}{none}!')
