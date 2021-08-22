import re
exp = "(a+b*c*)|(a*b+c*)|(a*b*c+)"
user_input = input()
if (re.search(exp, user_input)):
    print("Expresión válida")
else:
    print("Expresión inválida")
    