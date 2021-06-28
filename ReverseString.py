def reverseStr(s, k):
        # Se convierte la cadena en una lista para poder modificarla
        a = list(s)
        # Usando el método range, se accede por medio de i a la lista,
        # desde 0 hasta el último caractér, yendo de 2 bloques de k
        for i in range(0, len(a), 2*k):
            # Se modifica el segmento de lista, desde i hasta i+k
            a[i:i+k] = reversed(a[i:i+k])
        # Se regresa la cadena modificada
        return "".join(a)

first_s = "SiNoSiNo"
print(reverseStr(first_s, 2))
second_s = "Mi nombre es Daira, saludos"
print(reverseStr(second_s, 4))