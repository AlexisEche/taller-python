import pickle

valor = open('camiones.pckl','rb')

valores = pickle.load(valor)


print(valores)