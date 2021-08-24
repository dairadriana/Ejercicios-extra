import re
exp = "(A|E|I|O|U)((0|1)(0|1))+(Z?)"
user_input = input()
res = re.findall(exp, user_input)
a=re.search(exp, user_input)
if (a) :
    print(a)