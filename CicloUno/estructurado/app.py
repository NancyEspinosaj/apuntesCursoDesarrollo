from aplicacion import aplicar_descuento
from aplicacion import aplicar_iva
from aplicacion import aplicar_suma as ap_suma

precio_con_descuento = []
precio_con_iva = []
diccionario_precios = {1000:20, 500:10, 100:1}

for precio, descuento in diccionario_precios.items():
    precio_con_descuento = aplicar_descuento.operar_descuento(precio, descuento)
    precio_con_iva = aplicar_iva.operar_iva(precio, descuento)


print('El precio de la compra tras aplicar los descuentos es: ', precio_con_descuento)
print('El precio de la compra tras aplicar el IVA es: ', precio_con_iva)

total_con_descuento = ap_suma.sumar(precio_con_descuento)
total_con_iva = ap_suma.sumar(precio_con_iva)

print(total_con_descuento)
print(total_con_iva)