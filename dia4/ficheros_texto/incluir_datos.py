#append
for i in range(3):
    print(i)

file = open('ficherotexto.txt','at')

file_add ='\nEsta es la linea agregada'

file.write(file_add)

file.close()