import math
from math import sqrt as raiz

### Operadores aritmeticos
# + - / * ** %
num1 = 10
num2 = 3

resultado = (num1+num2)
print("El resultado de la operacion {} + {} es {}".format(num1,num2,resultado))


resultado = (num1-num2)
print("El resultado de la operacion {} - {} es {}".format(num1,num2,resultado))

resultado = (num1*num2)
print("El resultado de la operacion {} * {} es {}".format(num1,num2,resultado))

resultado = (num1/num2)
print("El resultado de la operacion {} / {} es {}".format(num1,num2,resultado))

resultado = (num1//num2)
print("El resultado de la operacion {} // {} es {}".format(num1,num2,resultado))

resultado = (num1%num2)
print("El modulo de la operacion {} % {} es {}".format(num1,num2,resultado))

x=16
y=raiz(x)
print(y)

### Operadores de asignacion
# += -= /= *= **=

numero = 4
numero **= 4

print(numero)






### Operadores de comparacion
#==  # >= <= < > !=

num1 = 5
num2 = 6
num3 = 10


if (num1 < num2):
    print('Se cumplio la condicion')


### Operadores Logicos
# and or not

if (not (num3 < num2 )):
    print('La segunta condicion se cumplio')



### Operadores de identidad
#is is not
'''
frutas1 = ['mango','papaya','fresa']
frutas2 = ['mango','papaya','fresa']
frutas1 = frutas2

print(frutas1 is not frutas2)
'''
### Operadores de pertenencia
 # in not in

frutas1 = ['mango','papaya','fresa']
frut1 = 'papa'

print(frut1 not in frutas1)
