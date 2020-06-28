#Funcion definicion

def presentar(name):
  print('Hola mi nombre es: {}'.format(name))

presentar('Kevin')

def sumar(num1,num2):
    return num1 + num2

#print(sumar(8,5))

lista_alumnos = ['Kevin','Luis','Nilton']

def agregarAlumnos(lista_alumnos,alumno):
    lista_alumnos.append(alumno)

n = int(input('Introduce el numero de Alumnos: '))

'''A qui pueden  eliminar el while y borrar los espacios y el codigo seguirá
    corriendo igual , una demostracion de que con while tambien se puede hacer el autoincremento
    sin embargo si no lo ponemos da exactamente lo mismo y ahorramos recursos del computador '''
m = 1

for alumno in range(n):
    while (m <= n):
        alumno = input('Introduce al alumno Nª {} '.format(m))
        m += 1
        agregarAlumnos(lista_alumnos, alumno)


print('El numero de alumnos que introdujo es {}'.format(n))

for i in lista_alumnos:
    if( i == 'Kevin'):
        print('Kevin es un buen alumno')
    elif( i == 'Luis'):
        print('Luis sabe programar')
    elif(i == 'Nilton'):
        print('Nilton sabe sobre python')

print(lista_alumnos)
