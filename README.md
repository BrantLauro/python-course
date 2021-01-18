# Python Course
 Python Course of **Curso em Vídeo**
 
 A **free** Python course of **Gustavo Guanabara**
 
 Some of the exercises are in english and are stylized, I am working to traslate all the exercises to english.
 
 If you want to see my exercises go to the **ex folder**, please open it on PyCharm because I tried to organize the styles that Guanabara asked for. He asked us to put color in the terminal for all the exercises using the escape sequence ANSI, so I created a document named **style.py** then created some variables with the ANSI code and import this document into some of my exercises (i will not do this for all the exercises becouse I don't think thats beautiful) and put the variables of **style.py** in my code to make it more readable, but that didn't work in VSCode, only in PyCharm, then if you want to see that working, play it on PyCharm.
 
 Obs: I used 2 external modules: emoji and playsound so make sure you have instaled it on the venv
 
 ## Here some examples
 
 **Without style.py**
 
`print('\033[7mHello World!\033[m')`
 
 **With style.py**
 ```
 from ex.style import none, blue

name = input('What is your name? ')
age = int(input('How old are you? '))
weight = float(input('What is your weight? '))

print(f'Hi, {blue}{name}{none} you are {blue}{age}{none} and weighs {blue}{weight}{none} Kg')
```
 
 I really enjoy taking this course. Python is a delicious language.
 
 Coding is my passion than I want to study more and more.
 
 ## Here the link for the course
 
 [Click Here](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)
 
 ![Python](https://camo.githubusercontent.com/888e388801f947dec7c3d843942c277af25fe2b1aed1821542c4e711f210312a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67)
