import tkinter as tk
from tkinter import messagebox
from menu import Menu

class Login: 
    def __init__(self):
        self.data={
            "email": "test@test.co",
            "password": "1234"
        }
        self.ventana = tk.Tk()
        self.ui()
    
    def ui(self):
        self.ventana.title("Login")
        self.ventana.geometry("180x150")

        tk.Label(self.ventana, text="Email:").grid(column=1, row=0, sticky=tk.W, padx=20)
        self.input_email = tk.Entry(self.ventana)
        self.input_email.grid(column=1, row=1, padx=20)

        tk.Label(self.ventana, text="Password:").grid(column=1, row=2, sticky=tk.W, padx=20)
        self.input_password = tk.Entry(self.ventana, show="*")
        self.input_password.grid(column=1, row=3, padx=20)

        self.btn_inicio = tk.Button(self.ventana, text="Iniciar", command=self.inicio)
        self.btn_inicio.grid(column=1,row=4, padx=20, pady=10)
    
    def inicio(self):
        email = self.input_email.get()
        password = self.input_password.get()

        if email == self.data["email"] and password==self.data["password"]:
            self.ventana.destroy()
            menu = Menu()
            menu.run()
            
        else:
            messagebox.showerror("Error de credenciales", "Usuario o contraseñas incorrectos")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    login = Login()
    login.run()