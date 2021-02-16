from style import blue, red, purple, none

a = 'Hello World!'

print(f'The string {blue}is{none} {purple}{a} {none}\n'
      f'The {blue}index 2nd{none} is {purple}{a[2]} {none}\n'
      f'The string {blue}until the 3rd index{none} is {purple}{a[:3]} {none}\n'
      f'The string {blue}starting in the 3rd index{none} is {purple}{a[3:]} {none}\n'
      f'The string {blue}counted every 2{none} is {purple}{a[::2]} {none}\n'
      f'The string has {blue}{len(a)}{none} characters \n'
      f'The string has {blue}{a.count("o")}{none} letters "o" \n'
      f'The string has {blue}{a.count("O", 0, 3)}{none} letters "O" starting on 0 index until the 3rd index\n'
      f'The string has a the word {blue}"World" starting in the index{none}: {purple}{a.find("World")} {none}\n'
      f'The string has the word {blue}"Python"{none}? {purple}{"Python" in a} {none}\n'
      f'If it substitutes {blue}"World"{none} to {blue}"Python"{none} would be: {purple}{a.replace("World", "Python")} {none}\n')

b = input('Type something: ')

print(f'{b} in {blue}uppers{none} stay: {purple}{b.upper()} {none}\n'
      f'{b} in {blue}lowers{none} stay: {purple}{b.lower()} {none}\n'
      f'{b} {blue}capitalized{none} stay: {purple}{b.capitalize()} {none}\n'
      f'{b} was a {blue}title{none} stay: {purple}{b.title()} {none}\n'
      f'{b} {blue}with no spaces in the right{none} stay: {purple}{b.rstrip()} {none}\n'
      f'{b} {blue}with no spaces in the left{none} stay: {purple}{b.lstrip()} {none}\n'
      f'{b} {blue}with no spaces in the right and left{none} stay: {purple}{b.strip()} {none}\n'
      f'{b} {blue}capitalized after taken away the spaces{none} stay: {purple}{b.strip().capitalize()} {none}\n'
      f'{blue}Splitting off all words in {b}{none} would be: {purple}{b.split()} {none}\n')

print('''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')
