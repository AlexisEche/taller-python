class Celular:
    color = 'Blanco'
    precio = 500
    marca = 'Huawei'


celular1 = Celular()
print(celular1)


celular1.color = 'Negro'
celular1.precio = 200

print(celular1.precio)
print(celular1.color)

class Persona:

    def __init__(self,name,edad):
        self.name=name
        self.edad=edad

    def presentarse(self):
        print('Hola mi nombre es {} y tengo {} años'.format(self.name,self.edad))

    def despedirse(self):
        print(' {} Tengo trabajos por hacer'.format(self.name))



persona1 = Persona('Luis',21)
persona2 = Persona('Kevin',20)
persona3 = Persona('Nilton',21)


persona1.presentarse()
persona2.despedirse()
persona3.presentarse()


#Funcion definicion

def presentar(name):
  print('Hola mi nombre es: {}'.format(name))

presentar('Kevin')

def sumar(num1,num2):
    return num1+num2

#print(sumar(8,5))

lista_alumnos = ['Kevin','Luis','Nilton']

def agregarAlumnos(lista_alumnos,alumno):
    lista_alumnos.append(alumno)

n = int(input('Introduce el numero de Alumnos: '))
m = 1

for i in range(n):
    while (m ==n):
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