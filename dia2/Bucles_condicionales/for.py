lista_frutas = ['fresa','naranja','platano','uva','piña']

'''
for i in lista_frutas:
    print(i)
    

for i in range(0,10,2):
    print(i)

# rango de 3 es 0 1 2
# rango de 2 es 0 1


for i in range(3):
    for f in range(2):
        print(i)
'''


'''
lista = [0]*2
matriz = [lista]*2

matriz[0][0] = 5
matriz[0][1] = 6

print(matriz)

matriz=[]

filas = int(input('Introduce el numero de filas: '))
columnas = int(input('Introduce el numero de columnas: '))

for i in range(filas):
    matriz.append([0]*columnas)


for f in range(filas):
    for g in range(columnas):
        matriz[f][g]=int(input('Introduce un numero en la posición {} , {} : '.format(f,g)))

print(matriz)
'''


for i in range(10):

    if(i == 4):
        continue
    print(i)










