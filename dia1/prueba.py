
#Sucession Fibonacci (0 1 1 2 3 ....)

def fibonacci(n):
    resultado = []
    a, b = 0, 1
    while (a <= n):
        resultado.append(a)
        a, b = b, a + b
    return resultado

print(fibonacci(1000))



