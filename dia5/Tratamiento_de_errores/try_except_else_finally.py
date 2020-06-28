# introduce en consola datos no permitidos lo cual nos arroja errores
# Pero no queremos que nuestro programa colapse pues utilizamos (try)

try:
    num1 = 5
    num2 = 1
    result = num1 / num2
    print(result)

except (ZeroDivisionError):
    print('Ocurrió un error')
else:
    print('operación exitosa')
finally:
    print('El proceso termino')
