
multiplo = 2

for i in range (1, 11):
    resultado = multiplo * i 
    print(multiplo, "x", i, "=", resultado)

cadena = " Hola Mundo"

for letra in cadena:
    print(letra)

# Array 

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento) 

# Imprimitr tablas de multiplicar del 1 al 10

for i in range(1, 11):
    print("Tabla de multiplicar del ", i)
    for j in range(1, 11):
        print( i, "x", j, "=", i * j)
    print("-----------------------------")

# Extraer numeros pares 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0 

for numero in numeros:
    if numero % 2 == 0:
        print("Los numeros pares de la lista", numeros, "son: ", numero)
        pares += 1
print("\n")
print("El total de los numeros pares es: ", pares)

# Contar a partir de una cadena cuantas vocales hay en ella 

cadena = "Esta es una cadena"
numvocales = 0 

for letra in cadena: 
    if letra in "AaEeIiOoUu":
        numvocales += 1 
print("La cadena tiene un total de", numvocales, "vocales")
print

lista = [11, 12, 13, 14, 15 ,16]

print(lista)

# Añadir numero a la lista

lista.append(19)

print(lista)

#Remover numero de la lista

lista.remove(13)

print(lista)

# Inverir orden de la lista

lista.reverse()
print(lista)

# Ordenar lista  de menor a mayor

lista.sort()
print(lista)

#Ordenar de mayor a menor 

lista.sort(reverse=True)

print(lista )

#limpiar lista 

lista.clear()

print(lista)

dic = {
    "nombre": "Juan",
    "edad": 18
}

print(dic)

print(dic["nombre"])
print(dic["edad"])

#Obtener valor de el diccionario

print(dic.get("edad"))

# Obtener las keys del diccionario

print(dic.keys())

def saludar():
    print("Hola mundo")

saludar()
def doble (num):
    num = num * 2
    return num

print(doble(5))