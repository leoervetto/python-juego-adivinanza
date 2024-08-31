import random
import tkinter as tk
from tkinter import font



# Generar numero aleatorio
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

def adivinanza():   
        global intentos
        intentos += 1
        if pantalla.get().isdigit():
                          
            adivinanza = int(pantalla.get())  # pasando de string a number

            
            if adivinanza < numero_secreto:
                instrucciones.config(text=f"el numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                instrucciones.config(text=f"el numero secreto es menor a {adivinanza}")
            else:
                instrucciones.config(
                    text=f"Felicitaciones el numero secreto era {adivinanza} y lo haz logrado en {intentos} intentos"
                )
        else:
            instrucciones.config(text="Por favor ingresa un numero del 1 al 100")
def nuevoNumero():
     global intentos
     intentos = 0
     global numero_secreto
     numero_secreto = random.randint(1, 100)   
     instrucciones.config(text="Introduce un numero del 1 al 100")




# Configuración de ventana
ventana = tk.Tk()
ventana.title("Adivinanza de número")
ventana.geometry("600x400")


# Entrada de numero
instrucciones = tk.Label(text="introduce un numero del 1 al 100: ", font=('Arial', 12), padx=20, pady=20)
instrucciones.pack()
pantalla = tk.Entry(ventana, font=('Arial', 18), bd=20, insertwidth=2, width=4, borderwidth=4)
pantalla.pack()


# Boton que ingresa el número
boton_ingreso = tk.Button(ventana, text="Ingresar Numero", font=('Arial', 12), padx=20, pady=20, command=adivinanza)
boton_ingreso.pack()
boton_nuevoJuego = tk.Button(ventana, text="Nuevo Juego", font=('Arial', 12), padx=20, pady=20, command=nuevoNumero)
boton_nuevoJuego.pack()


ventana.mainloop()




