import tkinter
from tkinter import messagebox, filedialog

#TEXTO BOTONES COMENTARIOS CHECKBUTTONS RADIOBUTTONS VENTANAS EMERGENTES (POPUPS) ASKQUESTION ABRIR UN ARCHIVO

raiz = tkinter.Tk()
raiz.title('Mi aplicación')

frame = tkinter.Frame(raiz)
frame.config(bg='lightblue',width=500,height=500)
frame.pack()

entrada = tkinter.Entry(raiz)
entrada.config(justify='center',bg='lightgreen',show='*')
entrada.pack()

texto = tkinter.Text(raiz)
texto.config(bg='gray', fg='black')
texto.pack()

texto = 'Facultad de Ing de Minas'

texto_etiqueta = tkinter.Label(frame,text=texto)
texto_etiqueta.config(bg='orange',font=('Cortana',30))
texto_etiqueta.pack()


def accion():
    print('Hello word')

boton = tkinter.Button(raiz,text='Click here!', command=accion)
boton.pack()

def seleccionar():
    print('Estas seleccionando la opcion {}'.format(opcion.get()))

opcion = tkinter.IntVar()

radioBoton1 = tkinter.Radiobutton(raiz,text = 'Opcion1', variable = opcion, value=1, command=seleccionar)
radioBoton1.pack()

radioBoton2 = tkinter.Radiobutton(raiz,text='Opcion2', variable=opcion, value=2, command=seleccionar)
radioBoton2.pack()

radioBoton3 = tkinter.Radiobutton(raiz,text='Opcion3', variable=opcion, value=3, command=seleccionar)
radioBoton3.pack()


def verificar():
    valor = chek1.get()
    if(valor ==1 ):
        print('El boton está activado')
    else:
        print('EL boton está desactivado')

chek1 = tkinter.IntVar()

checkBoton = tkinter.Checkbutton(raiz,text='Verdado', variable=chek1, onvalue=1, offvalue=0, command=verificar)
checkBoton.pack()

def avisar():
    tkinter.messagebox.showinfo('Alerta',' ¿Quieres salir del programa?')


botonPopup = tkinter.Button(raiz,text='Pulsa para avisar',command=avisar)
botonPopup.pack()


def preguntar():
    result = tkinter.messagebox.askquestion('Pregunta del día' ,'Te sientes bien')
    if(result == 'yes'):
        print('Si se siente bien dice')
    else:
        print('No se siente bien')

askQuestion = tkinter.Button(raiz,text='Dia',command=preguntar)
askQuestion.pack()

def abrirArchivo():
    filedialog.askopenfilename(title='Abrir este archivo')

botonAbrir = tkinter.Button(raiz,text='Seleccinar Archivo', command=abrirArchivo)
botonAbrir.pack()


raiz.mainloop()

