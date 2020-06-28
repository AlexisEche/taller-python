# search findall , split, sub

import re

cadena1 = 'Facultad de ingenieria de minas'
buscar = re.search('de.*ingenieria',cadena1)

if (buscar):
    print('Se encontro la palabra')
else:
    print('No se encontró la palabra')



print(buscar)

cadena2 = '''
el automovil de Nilton es de color rojo
el automovil de luis es de color azul
el automovil de kevin es de color negro


# punto (.) = espacios en blanco
# * = numeros


cadena_modificada = re.findall('automovil.*rojo',cadena2)
print(cadena_modificada)


cadena4 = 'El estudio de impacto ambiental se aprobó'

cadena_sub = re.sub('se','no se',cadena4)

print(cadena_sub)'''

cadena3 = 'Facultad,de,ingenieria,de,minas'

cadena_split = re.split(',',cadena3)
print(cadena_split)
