import re
exp = "(mmm)*"
user_input = input()
res = re.findall(exp, user_input)
if (re.search(exp, user_input)):
    print("Es válido")
else:
    print("No válido")
