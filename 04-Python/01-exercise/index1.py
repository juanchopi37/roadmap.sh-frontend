# Variable

variableNum = 113
varibleBool = False
stringVar = "Hola mundo"
print(variableNum, varibleBool, stringVar)

# Operaciones 

num = 4
num2 = 8

sum = num + num2

jerarquia = num + num2 * num

num2 = num -num2 -num
print(sum)

# Condiciones 

"""
igualdad ==
diferencia != 
mayor que > 
menor que <
mayor igual que >=
menor igual que <=
and = and 
not = not
or = or 
"""

num = True
num2 = True


if (num != num2):
    print("Los valores son diferentes")
else:
    print("Los dos valores son iguales")

if (num != num2 and num == num2):
    print('Esto sería el operador and')
elif(num != num2 or num == num2):
    print('Esto sería el operador or')
else:
    print('Ninguna condición se cumplió')


num3 = float(input("Ingrese el valor: "))

print(num3)
