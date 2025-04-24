# Función para calcular factura 

def calcularFactura(valorFactura, porcentajeIva = 0.21):
    total = valorFactura * (1 + porcentajeIva / 100)
    return total 

valor = float(input("Introduce la cantidad sin IVA: "))
porcentaIva = input("Introduce el IVA a aplicar (Si no lo escribes apliqueremos un 21%): ")

if porcentaIva: 
    iva = float(porcentaIva)
else:
    iva = 21

total = calcularFactura(valor, iva)

print(f"El total de la factura con IVA es: {total:.0f}")
