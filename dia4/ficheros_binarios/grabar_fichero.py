import pickle

camiones_mineros = ['797F','797D','794AC','785D','789D','793D']

fichero = open('camiones.pckl','wb')

pickle.dump(camiones_mineros,fichero)

fichero.close()