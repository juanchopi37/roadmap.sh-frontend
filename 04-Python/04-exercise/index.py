# #Definir clase
# class Usuario:
#     #Definimos funcion de inicializacion de la clase
#     def __init__(self, nombre="", edad=0, email=""):
#         self.data = {
#             "nombre":nombre,
#             "edad":edad,
#             "email":email
#         }
#     #Definimos funcion para imprimir las propiedades de la clase
#     def imprimir_propiedades(self):
#         print(self.data)
    
#     def cumple(self):
#         self.data["edad"] +=1
    

# #Definimos una variable de tipo de la clase
# primer_usuario = Usuario(nombre="Andres", email="test@test.co", edad=25)
# segundo_usuario = Usuario(nombre="Felipe", email="test@test.co", edad=25)
# #Ejecutamos una funcion de la clase
# primer_usuario.imprimir_propiedades()

# primer_usuario.cumple()
# primer_usuario.imprimir_propiedades()



# segundo_usuario.imprimir_propiedades()
# segundo_usuario.imprimir_propiedades()

from Formulario import Formulario

f = Formulario()

f.run()