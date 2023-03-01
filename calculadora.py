import tkinter as tk
import math

class Calculadora:

    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Creamos la pantalla
        self.pantalla = tk.Entry(master, width=25, font=('Arial', 16))
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=5)
        self.pantalla.focus_set()

        # Creamos los botones
        boton1 = tk.Button(master, text="1", command=lambda: self.agregar_valor("1"))
        boton1.grid(row=1, column=0, padx=5, pady=5)
        boton2 = tk.Button(master, text="2", command=lambda: self.agregar_valor("2"))
        boton2.grid(row=1, column=1, padx=5, pady=5)
        boton3 = tk.Button(master, text="3", command=lambda: self.agregar_valor("3"))
        boton3.grid(row=1, column=2, padx=5, pady=5)
        boton4 = tk.Button(master, text="4", command=lambda: self.agregar_valor("4"))
        boton4.grid(row=2, column=0, padx=5, pady=5)
        boton5 = tk.Button(master, text="5", command=lambda: self.agregar_valor("5"))
        boton5.grid(row=2, column=1, padx=5, pady=5)
        boton6 = tk.Button(master, text="6", command=lambda: self.agregar_valor("6"))
        boton6.grid(row=2, column=2, padx=5, pady=5)
        boton7 = tk.Button(master, text="7", command=lambda: self.agregar_valor("7"))
        boton7.grid(row=3, column=0, padx=5, pady=5)
        boton8 = tk.Button(master, text="8", command=lambda: self.agregar_valor("8"))
        boton8.grid(row=3, column=1, padx=5, pady=5)
        boton9 = tk.Button(master, text="9", command=lambda: self.agregar_valor("9"))
        boton9.grid(row=3, column=2, padx=5, pady=5)
        boton0 = tk.Button(master, text="0", command=lambda: self.agregar_valor("0"))
        boton0.grid(row=4, column=0, padx=5, pady=5)

        boton_suma = tk.Button(master, text="+", command=lambda: self.agregar_valor("+"))
        boton_suma.grid(row=1, column=3, padx=5, pady=5)
        boton_resta = tk.Button(master, text="-", command=lambda: self.agregar_valor("-"))
        boton_resta.grid(row=2, column=3, padx=5, pady=5)
        boton_multiplica = tk.Button(master, text="*", command=lambda: self.agregar_valor("*"))
        boton_multiplica.grid(row=3, column=3, padx=5, pady=5)
        boton_divide = tk.Button(master, text="/", command=lambda: self.agregar_valor("/"))
        boton_divide.grid(row=4, column=3, padx=5, pady=5)

        boton_limpiar = tk.Button(master, text="C", command=self.limpiar_pantalla)
        boton_limpiar.grid(row=4, column=1, padx=5, pady=5)
        boton_igual = tk.Button(master, text="=", command=self.calcular)
        boton_igual.grid(row=4, column=2, padx=5, pady=5)

        boton_raiz = tk.Button(master, text="√", command=self.calcular_raiz)
        boton_raiz.grid(row=5, column=0, padx=5, pady=5)
        boton_potencia = tk.Button(master, text="x²", command=self.calcular_potencia)
        boton_potencia.grid(row=5, column=1, padx=5, pady=5)
        boton_sin = tk.Button(master, text="sin", command=self.calcular_sin)
        boton_sin.grid(row=5, column=2, padx=5, pady=5)
        boton_cos = tk.Button(master, text="cos", command=self.calcular_cos)
        boton_cos.grid(row=5, column=3, padx=5, pady=5)

    def agregar_valor(self, valor):
        self.pantalla.insert(tk.END, valor)

    def limpiar_pantalla(self):
        self.pantalla.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = eval(self.pantalla.get())
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")

    def calcular_raiz(self):
        try:
            resultado = math.sqrt(float(self.pantalla.get()))
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")

    def calcular_potencia(self):
        try:
            resultado = float(self.pantalla.get()) ** 2
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")

    def calcular_sin(self):
        try:
            resultado = math.sin(float(self.pantalla.get()))
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")

    def calcular_cos(self):
        try:
            resultado = math.cos(float(self.pantalla.get()))
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()