import re
exp = "([1-9]|((1|2)[0-9])|3[0-1])\/(1[0-2]|[1-9])\/20[0-9][0-9]"
user_input = input()
res = re.findall(exp, user_input)
if (re.search(exp, user_input)):
    print("Es válido")
else:
    print("No válido")
