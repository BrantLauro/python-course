from time import sleep
from style import red, green, blue, none

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(f'''{red}BOOOOM!
{green}BOOOOM!
{blue}BOOOOM! {none}''')