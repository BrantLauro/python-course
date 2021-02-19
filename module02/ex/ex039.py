from datetime import date

birth = int(input('What is your year of birth: '))
genre = int(input('What is your genre? (type 1 for male and 2 for female): '))
year =  date.today().year
age = year - birth
under = 18-age
over = age-18
 
if genre == 1:
    
    if age < 18:
        print(f'You will enlist in {under} years. In {year+under}')
    elif age == 18:
        print('Is time to enlist')
    else:
        print(f'Enlistment time has passed {over} years ago. In {year-over}')
elif genre == 2:
    if age < 18:
        print(f'Woman do not need to enlist but you can do it in {year+under} if you want to.')
    elif age == 18:
        print('Woman do not need to enlist but you can do it if you want to.')
    else:
        print(f'Woman do not need to enlist and Enlistment time has passed {over} years ago. In {year-over}')
else:
    print('[ERROR] Verify the input and try again.')