diccionario_colores = {'red':'rojo','yellow':'amarillo','green':'verde','white':'blanco'}

diccionario_colores['black'] = 'negro'
'''print(diccionario_colores.items())

for i in diccionario_colores:
    print(i)'''

for clave,valor in diccionario_colores.items():
    print("El color en ingles es {} y en español es {}".format(clave,valor))




#print(diccionario_colores)