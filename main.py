from tkinter import *
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

    #REDEFINICIÓN CANVAS
    canvas = Canvas(ventana, width=500, height=500, bg="blue")
    canvas.place(x=0, y=0)

    #CARGAR IMAGEN Y PONERLA DE FONDO
    fondo = CargarImagen("fondo2.png")
    canvas.create_image(0,0,image = fondo, anchor = NW)

    imagenB = CargarImagen("Batrs.png")
    atras = Button(canvas,text = "Atrás",image = imagenB,command = VentanaPrincipal)
    atras.place(x=400,y=420)

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


