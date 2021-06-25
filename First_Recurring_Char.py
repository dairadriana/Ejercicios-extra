# First recurring character on a given string
# First recurring char = primero que se repite en la cadena

def first_recurring_char(my_string):
    my_string = my_string.upper()
    my_chars = []
    if not my_string:
        print("The given string is empty")
        return
    for c in my_string:
        if c in my_chars:
            print("The first recurring character is {}". format(c))
            return c
        my_chars.append(c)
    print("No recurring character found")
    return

my_string = input()
first_recurring_char(my_string)

# Usando tablas hash
def first_recurring(my_string):
    counts = {}
    for c in my_string:
        if c in counts:
            return c
        counts[c] = 1
    return None

print("First recurring character is {}". format(first_recurring(my_string)))
