# Definir clase 
class Usuario:
    def __init__(self, nombre, edad, email):
        self.data = {
            "nombre": nombre,
            "edad": edad,
            "email": email
        }

    #Imprimir propiedades 

    def imprimir_propiedades(self):
        print()

primer_usuario = Usuario("Juan", 28)