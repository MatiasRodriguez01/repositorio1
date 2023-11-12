import funciones_clase13 as funciones


buy_list = [
    ("Nuria Costa", 5, 1234.5, "Calle 1 - 456"),
    ("Jorge Russo", 7, 3999, "Calle 2 - 741"),
    ("Nuria Costa", 3, 2758.9, "Calle 1 - 456"),
    ("Ignacio Zapata", 10, 345, "Calle 4 - 329"),
    ("Rodrigo Rodriguez", 23, 3678, "Calle 3 - 745"),
    ("Jorge Russo", 12, 2359, "Calle 2 - 741")
    ]

home_list = funciones.home(buy_list)
print("Los domicilios de las personas que se les debe enviar una factura de compra son: ")
for i in home_list:
    print(i)
