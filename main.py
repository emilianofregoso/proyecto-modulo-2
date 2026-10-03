print("===================================")
print("     CALCULADORA DE COMPRA")
print("===================================")

# Entrada de datos
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: $"))
cantidad = int(input("Ingresa la cantidad de productos: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Operaciones
subtotal = precio * cantidad
monto_descuento = subtotal * (descuento / 100)
subtotal_descuento = subtotal - monto_descuento
iva = subtotal_descuento * 0.16
total = subtotal_descuento + iva

# Salida de datos
print("\n===================================")
print("          RESUMEN DE COMPRA")
print("===================================")

print(f"Producto: {producto}")
print(f"Precio por unidad: ${precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${monto_descuento:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")

print("===================================")
print("Gracias por tu compra.")
