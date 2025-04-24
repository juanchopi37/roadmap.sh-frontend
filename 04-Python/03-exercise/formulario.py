import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Formulario: 
    def __init__(self):
        self.lista_usuario=[]
        self.ventana = tk.Tk()
        self.ventana.geometry("1000x500")

        self.construir_formulario()
    
    def construir_formulario(self):
        tk.Label(self.ventana, text="Nombre: ").grid(row=0, column=0, padx=25, pady=20, sticky=tk.W)
        self.input_nombre = tk.Entry(self.ventana)
        self.input_nombre.grid(row=0, column=1, padx=25, pady=20)

        tk.Label(self.ventana, text="Edad: ").grid(row=1, column=0, padx=25, pady=20, sticky=tk.W)
        self.input_edad = tk.Entry(self.ventana)
        self.input_edad.grid(row=1, column=1, padx=25, pady=20)

        tk.Label(self.ventana, text="Email: ").grid(row=2, column=0, padx=25, pady=20, sticky=tk.W)
        self.input_email= tk.Entry(self.ventana)
        self.input_email.grid(row=2, column=1, padx=25, pady=20)

        self.button_enviar =  tk.Button(self.ventana,text="Enviar",command=self.enviar_datos)
        self.button_enviar.grid(row=3, column=1, pady=15)

        self.button_modificar = tk.Button(self.ventana,text="Modificar",command=self.mostrar_datos_seleccionados)
        self.button_modificar.grid(row=3, column=0, pady=15)

        self.boton_eliminar = tk.Button(self.ventana,text="Eliminar",command=self.eliminar_datos)
        self.boton_eliminar.grid(row=3, column=2, pady=15)

        self.button_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_cambios)
        self.button_guardar.grid(row=3, column=3, pady=15)
        self.button_guardar.config(state=tk.DISABLED)

        self.lista_usuario.append({
            "Nombre":"Nombre",
            "Edad": "Edad",
            "Email":"Email"
        })
        columns = ("Nombre", "Edad", "Email")
        self.tabla = ttk.Treeview(self.ventana,  columns=columns, show='headings')
        self.tabla.heading('Nombre',text='Nombre')
        self.tabla.heading("Edad", text="Edad")
        self.tabla.heading("Email", text="Email")
        
        self.tabla.grid(row=4, pady=10, padx=20)

    def enviar_datos(self):
        nombre = self.input_nombre.get()
        self.input_nombre.delete(0,tk.END)

        edad = self.input_edad.get()
        self.input_edad.delete(0,tk.END)

        email = self.input_email.get()
        self.input_email.delete(0,tk.END)

        if nombre == "" or edad == "" or email == "":
            messagebox.showerror("Error", "Por favor, rellene todos los campos")
        else:
            self.lista_usuario.append({
            "Nombre":nombre,
            "Edad": edad,
            "Email":email
        })
            
        self.cargar_datos()
    
    def eliminar_datos(self):
        selected_item = self.tabla.selection()
        if selected_item:
            index = self.tabla.index(selected_item)
            self.lista_usuario.pop(index)
            self.cargar_datos()

    def mostrar_datos_seleccionados(self):
        selected_item = self.tabla.selection()
        if selected_item:
            index = self.tabla.index(selected_item)
            usuario = self.lista_usuario[index]
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.insert(0, usuario["Nombre"])
            self.input_edad.delete(0, tk.END)
            self.input_edad.insert(0, usuario["Edad"])
            self.input_email.delete(0, tk.END)
            self.input_email.insert(0, usuario["Email"])
            self.index_a_modificar = index
            self.button_guardar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Seleccione un registro")

    def guardar_cambios(self):
        nombre = self.input_nombre.get()
        edad = self.input_edad.get()
        email = self.input_email.get()

        if nombre == "" or edad == "" or email == "":
            messagebox.showerror("Error", "Por favor, rellene todos los campos")
        else:
            self.lista_usuario[self.index_a_modificar] = {
                "Nombre": nombre,
                "Edad": edad,
                "Email": email
            }
            self.cargar_datos()
            self.input_nombre.delete(0, tk.END)
            self.input_edad.delete(0, tk.END)
            self.input_email.delete(0, tk.END)
            self.button_guardar.config(state=tk.DISABLED)

    def cargar_datos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for row in self.lista_usuario:
            nombre = row["Nombre"]
            edad = row["Edad"]
            email = row["Email"]
            self.tabla.insert('', tk.END, values=(nombre, edad, email))

    def run(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    f = Formulario()
    f.run()