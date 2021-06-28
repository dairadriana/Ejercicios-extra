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