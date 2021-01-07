a = 'Hello World!'

print(f'The string \033[3;30mis\033[m \033[7;30m{a} \033[m\n'
      f'The \033[3;30mindex 2nd\033[m is \033[7;30m{a[2]} \033[m\n'
      f'The string \033[3;30muntil the 3rd index\033[m is \033[7;30m{a[:3]} \033[m\n'
      f'The string \033[3;30mstarting in the 3rd index\033[m is \033[7;30m{a[3:]} \033[m\n'
      f'The string \033[3;30mcounted every 2\033[m is \033[7;30m{a[::2]} \033[m\n'
      f'The string has \033[7;30m{len(a)}\033[m characters \n'
      f'The string has \033[7;30m{a.count("o")}\033[m letters "o" \n'
      f'The string has \033[7;30m{a.count("O", 0, 3)}\033[m letters "O" starting on 0 index until the 3rd index\n'
      f'The string has a the word \033[3;30m"World" starting in the index\033[m: \033[7;30m{a.find("World")} \033[m\n'
      f'The string has the word \033[3;30m"Python"\033[m? \033[7;30m{"Python" in a} \033[m\n'
      f'If it substitutes \033[3;30m"World"\033[m to \033[3;30m"Python"\033[m would be: \033[7;30m{a.replace("World", "Python")} \033[m\n')

b = input('Type something: ')

print(f'{b} in \033[3;30muppers\033[m stay: \033[7;30m{b.upper()} \033[m\n'
      f'{b} in \033[3;30mlowers\033[m stay: \033[7;30m{b.lower()} \033[m\n'
      f'{b} \033[3;30mcapitalized\033[m stay: \033[7;30m{b.capitalize()} \033[m\n'
      f'{b} was a \033[3;30mtitle\033[m stay: \033[7;30m{b.title()} \033[m\n'
      f'{b} \033[3;30mwith no spaces in the right\033[m stay: \033[7;30m{b.rstrip()} \033[m\n'
      f'{b} \033[3;30mwith no spaces in the left\033[m stay: \033[7;30m{b.lstrip()} \033[m\n'
      f'{b} \033[3;30mwith no spaces in the right and left\033[m stay: \033[7;30m{b.strip()} \033[m\n'
      f'{b} \033[3;30mcapitalized after taken away the spaces\033[m stay: \033[7;30m{b.strip().capitalize()} \033[m\n'
      f'\033[3;30mSplitting off all words in {b}\033[m would be: \033[7;30m{b.split()} \033[m\n')

# para fazer anotações se  usa # e para escrever textos longos '''
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
