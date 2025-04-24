import tkinter as tk
from formulario import Formulario
from fibonacci import Fibonacci

class Menu:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menu")
        self.boton_formulario()
        self.boton_fibonacci()
        self.ventana.geometry("350x150")

    def boton_formulario(self):
        tk.Label(self.ventana, text="Iniciar formulario").grid(row=0, column=0, padx=25, pady=20, sticky=tk.W)

        self.button_enviar =  tk.Button(self.ventana,text="Formulario",command=self.login)
        self.button_enviar.grid(row=0, column=1, pady=15)

    def boton_fibonacci(self):
        tk.Label(self.ventana, text="Calcular secuencia de Fibonacci").grid(row=1, column=0, padx=25, pady=20, sticky=tk.W)

        self.button_enviar =  tk.Button(self.ventana,text="Fibonacci",command=self.fibonacci)
        self.button_enviar.grid(row=1, column=1, pady=15)
    
    def fibonacci(self):
        fib = Fibonacci()
        fib.run()

    def login(self):
        formulario = Formulario()

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    menu = Menu()

