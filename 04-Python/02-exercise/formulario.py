import tkinter as tk 
from tkinter import messagebox

class Formulario():
    def __init__(self):
        self.lista_usuarios = []
        self.ventana = tk.Tk()
        self.construir_formulario()

    def construir_formulario(self):
        tk.Label(self.ventana, text="Nombre").grid(row=0, column=0, padx=25, pady=20)
        self.inputNombre = tk.Entry(self.ventana)
        self.inputNombre.grid(row=0, column=1, padx=25, pady=20)


        self.buttonListar = tk.Button(self.ventana, text="Listar", fg="white", bg="Blue", command=self.listar_datos)
        self.buttonListar.grid(row=1, column=0, padx=25, pady=20)

        self.buttonEnviar = tk.Button(self.ventana, text="Enviar", fg="white", bg="Blue", command=self.enviar_formulario)
        self.buttonEnviar.grid(row=1, column=1, columnspan=2, padx=25, pady=20)


    def enviar_formulario(self):
        nombre = self.inputNombre.get()
        self.lista_usuarios.append(nombre)
        print(self.lista_usuarios)


    def listar_datos(self):
        messagebox.showinfo("Usuarios", self.lista_usuarios)

    def run(self):
        self.ventana.mainloop()

    function Formulario()


# Agregarle los campos anteriormente creados y la tabla 
# Index una clase llamada login y verificar es correcta cerrar ventana login y abrir formulario 