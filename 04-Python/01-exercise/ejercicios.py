# # # Validar datos para un crédito || Unidireccional

# print("---------------------------------------------------------")
# print("| SISTEMA DE CRÉDITO                                    |")
# print("---------------------------------------------------------")

# edad = int(input('Ingresa tu edad: '))
# ingresos = int(input('Ingresa tus ingresos: '))
# historial = int(input('Ingresa tu puntaje crediticio: '))

# if (edad >= 21 and ingresos > 1600000 and historial > 700):
#     print("Usted puede solicitar un crédito")

# if (edad < 21 or ingresos < 1600000 or historial < 700):
#     print("Usted no puede solicitar un crédito")

# if edad < 21:
#     print("Usted no cumple con la edad mínima")

# if ingresos < 1600000:
#     print ("Usted no cumple con los ingresos mínimos")

# if historial < 700:
#     print("Usted no cumple con el puntaje crediticio mínimo")

# # Calcular temperatura || Bidireccional

# print("----------------------------------------------------------")
# print("| SISTEMA DE TEMPERATURA                                   |")
# print("----------------------------------------------------------")

# temperatura = float(input('Digita la temperatura a calcular (en grados celcius): '))

# if temperatura <= 0:
#     print("Congelación")
# elif 1 <= temperatura <= 30:
#     print("Frio")
# else:
#     print("Calor")

# Fabrica de piezas || Multidimensional

# print("----------------------------------------------------------")
# print("| SISTEMA DE FABRICA DE PIEZAS                           |")
# print("----------------------------------------------------------")

# pieza = int(input('Ingrese el peso de la pieza: '))
# altura = int(input('Ingrese la altura de la pieza: '))
# temperatura1 = int(input('Ingrese la temperatura de la pieza: '))

# peso_ok = 50 <= pieza <= 100
# altura_ok = 10 <= altura <= 20 
# temperatura_ok = temperatura1 < 30

# if peso_ok and altura_ok and temperatura_ok:
#     print('La pieza es aceptada')
# elif not peso_ok or not altura_ok:
#     print('Revisar dimensiones')
# elif not temperatura_ok:
#     print('Fallo en el control de temperatura')
# else:
#     print('Rechazada')

# Calcular impuestos || If Anidado Multidimensional

# print("----------------------------------------------------------")
# print("| SISTEMA DE IMPUESTOS                                    |")
# print("----------------------------------------------------------")

# ingresos1 = int(input('Ingresa tus ingresos: '))
# estadoCivil = input('Ingresa tu estado civil en minusculas: ')

# if ingresos1 > 3000000:
#     if estadoCivil == 'soltero':
#         print('Tu impuesto por ser solter@ es de: ', ingresos1 * 0.3)
#     else:
#         print('Tu impuesto por ser casad@ es de: ', ingresos1 * 0.25)
# elif 1000000 <= ingresos1 <= 3000000:
#     if estadoCivil == 'soltero':
#         print('Tu impuesto por ser solter@ es de: ', ingresos1 * 0.2)
#     else:
#         print('Tu impuesto por ser casad@ es de: ', ingresos1 * 0.15)
# elif ingresos1 < 1000000:
#     if estadoCivil == 'soltero':
#         print('Tu impuesto por ser solter@ es de: ', ingresos1 * 0.1)
#     else:
#         print('Tu impuesto por ser casad@ es de: ', ingresos1 * 0.05)
# else:
#     print('No se puede calcular el impuesto')

# Fallo con priorización If multidireccional con priorización

# print("----------------------------------------------------------")
# print("| SISTEMA DE PRIORIZACIÓN                                |")
# print("----------------------------------------------------------")

# velocidadViento = int(input('Ingrese la velocidad del viento: '))
# temperatura2 = int(input('Ingrese la temperatura: '))
# humedad = float(input('Ingrese la humedad: '))

# if velocidadViento >= 80:
#     print('Alerta Roja')
# elif velocidadViento >= 50 and temperatura2 < 0:
#     print('Alerta Amarilla')
# elif temperatura2 > 35 and humedad > 0.8:
#     print('Alerta ola de calor')
# else:
#     print('Condiciones estables')

# Sistema de control de acceso a áreas seguras If multidireccional con múltiples criterios

print("----------------------------------------------------------")
print("SISTEMA DE CONTROL DE ACCESO")
print("----------------------------------------------------------")

NIVEL_PERMITIDO = 3
HORA_INICIO = 9
HORA_FIN = 17
CODIGO_AUTENTICACION = "1234"

# Entrada de datos

nivel = int(input("Ingrese el nivel de seguridad: "))
hora = int(input("Ingrese la hora actual (en formato de 24 horas): "))
codigo = input("Ingrese el código de autenticación: ")

if nivel < NIVEL_PERMITIDO:
    print("Acceso denegado")
elif hora < HORA_INICIO or hora > HORA_FIN:
    print("Acceso denegado, fuera de horario")
elif codigo != CODIGO_AUTENTICACION:
    print("Acceso denegado, código incorrecto")
else:
    print("Acceso permitido: Bienvenido al área segura")

    