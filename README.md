# Python Course
 Python Course of **Curso em Vídeo**
 
 I done the first module of the python course of the brazilian teacher __*Gustavo Guanabara*__. I had **11 classes** and **35 exercises**.
 
 Some of the exercises are in english and are stylized, I am working to traslate all the exercises to english and paint all of them.
 
 If you want to see my exercises go to the **ex folder**, please open it on PyCharm because I tried to organize the styles that Guanabara asked for. He asked us to put color in the terminal for all the exercises using the escape sequence ANSI, so I created a document named **style.py** then created some variables with the ANSI code and import this document into all my exercises and put the variables of **style.py** in my code to make it more readable, but that didn't work in VSCode, only in PyCharm, then if you want to see that working, play it on PyCharm.
 
 ## Here some examples
 
 **Without style.py**
 
```print('\033[7mHello World!\033[m')``
 
 **With style.py**
 ``
 from ex.stile import none, blue

name = input('What is your name? ')
age = int(input('How old are you? '))
weight = float(input('What is your weight? '))

print(f'Hi, {blue}{name}{none} you are {blue}{age}{none} and weighs {blue}{weight}{none} Kg')
``
 
 I really enjoy taking this course. Python is a delicious language.
 
 Coding is my passion than I want to study more and more.
 
 ## Here the link for the course
 
 [Click Here](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)
