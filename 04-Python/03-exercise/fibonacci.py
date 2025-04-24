import tkinter as tk
from tkinter import ttk

class Fibonacci:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Fibonacci")
        self.ventana.geometry("560x400")
        self.n = 0
        self.secuencia = []
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.ventana, text="Ingrese el numero de dígitos de la secuencia de Fibonacci a mostrar:").grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
        self.input_n = ttk.Entry(self.ventana)
        self.input_n.grid(row=0, column=1, padx=20, pady=20, sticky=tk.W)

        self.button = ttk.Button(self.ventana, text="Calcular", command=self.mostrar_secuencia)
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky=tk.W)

        self.resultado = tk.Text(self.ventana, height=10, width=40)
        self.resultado.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky=tk.W)

    def calcular_fibonacci(self, n):
        secuencia = []
        for i in range(n):
            if i == 0:
                secuencia.append(0)
            elif i == 1:
                secuencia.append(1)
            else:  
                secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia

    def mostrar_secuencia(self):
        try: 
            n = int(self.input_n.get())
            self.secuencia = self.calcular_fibonacci(n)
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, f"La secuencia de Fibonacci hasta {n} es: {self.secuencia}")
        except ValueError:
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, "Ingrese un número válido")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    fib = Fibonacci()
    fib.run()