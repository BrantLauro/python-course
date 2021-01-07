name = input('What`s your \033[3;30mname\033[m? ')

print(f'Nice to meet you \033[3;30m{name:=^20}\033[m!')

# :=^20 cetraliza em 2o espaços com o símbolo de =