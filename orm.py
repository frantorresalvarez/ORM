import tkinter as tk
import random
import math


personas = []
numeropersonas = 20




class Persona:
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.color = "blue"
        self.entidad = ""
    def dibuja(self):
        self.entidad = lienzo.create_oval(self.posx-self.radio/2,
                           self.posy-self.radio/2,
                           self.posx+self.radio/2,
                           self.posy+self.radio/2,
                           fill=self.color)
    def mueve(self):
        self.colisiona()
        lienzo.move(self.entidad,
                    math.cos(self.direccion),
                    math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def colisiona(self):
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy > 1024:
            self.direccion += math.pi


# CREO UNA VENTANA
raiz = tk.Tk()

#EN LA VENTANA CREO UN LIENZO
lienzo = tk.Canvas(width=1024,height=1024)
lienzo.pack()

#EN LA COLECCION INTRODUZCO INSTANCIAS DE PERSONAS
for i in range(0,numeropersonas):
    personas.append(Persona())
    
#PARA CADA UNA DE LAS PERSONAS DE LA COLECCION LAS PINTA
for persona in personas:
    persona.dibuja()
    
#CREO UN BUCLE REPETITIVO    
def bucle():
    #PARA CADA PERSONA EN LA COLECCION
    for persona in personas:    
        persona.mueve()
    raiz.after(10,bucle)

    
#EJECUTO EL BUCLE
bucle()
raiz.mainloop()
