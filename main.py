from tkinter import *
from tkinter import ttk
import os

#FUNCIÓN PARA CARGAR IMAGEN
def CargarImagen(nombre):

    root = os.path.join('Imagenes',nombre)
    image = PhotoImage(file=root)
    return image

def VentanaPrincipal():

    #CREACIÓN DE CANVAS
    canvas = Canvas(ventana,width = 500,height = 500,bg="white")
    canvas.place(x=0,y=0)

    #CARGAR IMAGEN Y PONERLA DE FONDO
    fondo = CargarImagen("fondo.png")
    canvas.create_image(0,0,image = fondo, anchor = NW)

    #TEXTO EN PANTALLA
    canvas.create_text((500 / 2), 20, fill="white", font="Times 20 italic bold",text="TALLER TKINTER")  # TEXTO FIN FONDO
    canvas.create_text((500 / 2), 150, fill="white", font="Times 20 italic bold",text="Digite su nombre")  # TEXTO FIN FONDO
    textoNombre =  canvas.create_text((500 / 2), 250, fill="white", font="Times 20 italic bold",text="")  # TEXTO FIN FONDO

    #ETIQUETA

    labelPalabra = Label(canvas,text = "Esto es un label y se ve feo")
    labelPalabra.place(x = 500/3 + 10, y = 400)

    #ENTRADA DE TEXTO
    entryBox = Entry(canvas)
    entryBox.place(x=190, y=200)

    #BOTON
    bVentana2 = Button(canvas,text = "Cambio ventana",command = Ventana3)
    bVentana2.place(x=500*0.2,y=300)

    #BOTON
    bVentana3 = Button(canvas,text = "Cambio contenido",command = lambda : Ventana2(canvas))
    bVentana3.place(x=300,y=300)

    #BOTON
    imprimir = Button(canvas,text = "Imprimir Nombre",command = lambda : ImprimirNombre(canvas,entryBox.get(),textoNombre))
    imprimir.place(x=200,y=350)

    ventana.mainloop() #ACTUALIZACION

def ImprimirNombre(canvas, text1,textoNombre):

    canvas.itemconfigure(textoNombre, text = text1)

def Ventana2(canvas):

    def ActualizarItem():

        #OBTENER SELECCIONADO
        seleccionado = VistaLista.focus()
        #CAMBIAR VALORES
        VistaLista.item(seleccionado,values = ['0', '0', 'El cielo','100'])

        #OBTENER VALORES DEL SELECCIONADO
        temporal = VistaLista.item(seleccionado,"values")
        print(temporal)

    #REDEFINICIÓN CANVAS
    canvas = Canvas(ventana, width=500, height=500, bg="blue")
    canvas.place(x=0, y=0)

    #CARGAR IMAGEN Y PONERLA DE FONDO
    fondo = CargarImagen("fondo2.png")
    canvas.create_image(0,0,image = fondo, anchor = NW)

    #Listas en tree view
    VistaLista = ttk.Treeview(canvas)
    VistaLista["columns"] = ("País","Hotel","Nombre","Cantidad Estrellas")

    #CREAR COLUMNAS
    VistaLista.column('#0', width=0, stretch=NO)
    VistaLista.column("País", anchor = CENTER, width = 80)
    VistaLista.column("Hotel", anchor=CENTER, width=80)
    VistaLista.column("Nombre", anchor=CENTER, width=80)
    VistaLista.column("Cantidad Estrellas", anchor=CENTER, width=80)

    #CONFIGUAR COLUMAAS
    VistaLista.heading('#0', text='', anchor=CENTER)
    VistaLista.heading('País', text='País', anchor=CENTER)
    VistaLista.heading('Hotel', text='Hotel', anchor=CENTER)
    VistaLista.heading('Nombre', text='Nombre', anchor=CENTER)
    VistaLista.heading('Cantidad Estrellas', text='CE', anchor=CENTER)

    #INSERTAR FILAS
    VistaLista.insert(parent='', index=0, iid=0, text='', values=['1', '1', 'Panchita','5'])
    VistaLista.insert(parent='', index=1, iid=1, text='', values=['1', '2', 'Rio', '5'])
    VistaLista.insert(parent='', index=2, iid=2, text='', values=['3', '3', 'Tamarindo', '5'])
    VistaLista.insert(parent='', index=3, iid=3, text='', values=['14', '4', 'Lonche', '5'])
    VistaLista.insert(parent='', index=4, iid=4, text='', values=['1', '6', 'TEC residencia', '-5'])


    # INSERTAR AUTOMATICAMENTE
    listaAInsertar = [['1', '1', 'Panchita','5'],['1', '1', 'Panchita','5'],['1', '1', 'Panchita','5'],['1', '1', 'Panchita','5']] #lista a insertar

    index = 5 #indice de fila, en este caso empieza en 5 por los cienco elementos anteriores, generalmente empieza en 0
    for i in listaAInsertar: #for para recorrer la lista que queremos insertar
        VistaLista.insert(parent='', index=index, iid=index, text='', values=i)
        index+=1 # aumentamos indice

    VistaLista.place(x=90,y=50)

    cambiar = Button(canvas,text = "Actualizar",command = ActualizarItem)
    cambiar.place(x=300,y=420)


    imagenB = CargarImagen("Batrs.png")
    atras = Button(canvas,text = "Atrás",image = imagenB,command = VentanaPrincipal)
    atras.place(x=400,y=420)

    siguiente = Button(canvas,text = "Siguiente",command = lambda : Ventana4(canvas))
    siguiente.place(x=200,y=420)

    ventana.mainloop()


def Ventana4(canvas):

    def ObtenerItem():

        nombre = listaDesplegable.get()
        indice = listaDesplegable.current()

        print(nombre,indice)

    #REDEFINICIÓN CANVAS
    canvas = Canvas(ventana, width=500, height=500, bg="blue")
    canvas.place(x=0, y=0)

    #CARGAR IMAGEN Y PONERLA DE FONDO
    fondo = CargarImagen("fondo2.png")
    canvas.create_image(0,0,image = fondo, anchor = NW)

    #LISTA DESPLEGABLE

    opciones = ["teletica","movistar","kolbi","pasar intro"] #lista de opciones

    listaDesplegable = ttk.Combobox(canvas,width=20,state = "reandoly") #genero lista desplegable con combbox
    listaDesplegable.place(x=100,y=100)

    listaDesplegable["values"] = opciones #Lo doy los valores
    listaDesplegable.set("Elige una opcion") #eligo el estado inicial

    cambiar = Button(canvas,text = "Obtener",command = ObtenerItem)
    cambiar.place(x=300,y=420)


    ventana.mainloop()





def Ventana3():

    #ESCONDER
    ventana.withdraw()

    #VENTANA EMERGENTE
    ventana3 = Toplevel()
    ventana3.title("Así es incomodo")
    ventana3.minsize(500,500)
    ventana3.resizable(width=NO,height=NO)
    ventana3.config( bg= "black")

    atras = Button(ventana3,text = "Atrás",command = lambda : AtrasAux(ventana3))
    atras.place(x=100,y=150)

    ventana3.mainloop()

def AtrasAux(ventana3):

    ventana3.destroy()
    ventana.deiconify()
    VentanaPrincipal()

if __name__ == '__main__':
    ventana = Tk()  # CREAR LA VENTANA PRINCIPAL
    ventana.title("Taller computación")  # TITULO
    ventana.minsize(500, 500)  # TAMAÑO
    ventana.resizable(width=NO, height=NO)  # MODIFICAR TAMAÑO
    ventana.config(bg="blue")  # CONFIGURACIÓN, COLOR
    VentanaPrincipal()


