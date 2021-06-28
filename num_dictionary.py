n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        search = input()
        if search in phone_book:
            print("{}={}".format(search, phone_book[search]))
        else:
            print('Not found')
    except:
        break

n = int(input())
tel_dicc={}
for _ in range(n):
    name_telephone = input().split()
    tel_dicc[name_telephone[0]] = name_telephone[1]

while True:
    try:
        search = input()
        if search in tel_dicc:
            print("{}={}".format(search, tel_dicc[search]))
        else:
            print('Not found')
    except:
        break