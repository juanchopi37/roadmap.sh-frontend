import tkinter as tk
from tkinter import messagebox

class Formulario: 
    def __init__(self):
        self.lista_usuario=[]
        self.ventana = tk.Tk()

        self.construir_formulario()
    
    def construir_formulario(self):
        tk.Label(self.ventana, text="Nombre: ").grid(row=0, column=0, padx=25, pady=20, sticky=tk.W)
        self.input_nombre = tk.Entry(self.ventana)
        self.input_nombre.grid(row=0, column=1, padx=25, pady=20)

        self.button_enviar =  tk.Button(self.ventana,text="Enviar", fg="white", bg="blue", command=self.enviar_datos)
        self.button_enviar.grid(row=1, column=1, pady=15)

        self.button_listar =  tk.Button(self.ventana,text="Listar Usuarios", fg="white", bg="blue", command=self.listar_datos)
        self.button_listar.grid(row=1, column=0, pady=15)

    def enviar_datos(self):
        nombre_text = self.input_nombre.get()
        self.lista_usuario.append(nombre_text)
        self.input_nombre.delete(0,tk.END)
    
    def listar_datos(self):
        messagebox.showinfo("Lista de usuarios",self.lista_usuario)

    def run(self):
        self.ventana.mainloop()
