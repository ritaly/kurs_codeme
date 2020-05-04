def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


def suma_recursion(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursion(n-1)


print(suma_for(5))
print(suma_recursion(5))