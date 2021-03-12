words = 'Learn', 'Coding', 'Language', 'Python', 'For', 'Free', 'Study', 'Practice', 'Work', 'Office', 'Programmer', 'Future'

for word in words:
    print(f' \n In {word} we have:', end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
