from Cuenta import cuenta

# Ejemplo de uso
mi_cuenta = cuenta()
mi_cuenta.titular = "Juan Perez"
mi_cuenta.cantidad = 1000
mi_cuenta.mostrar()
mi_cuenta.ingresarDinero(500.0)  
mi_cuenta.mostrar() 
mi_cuenta.retirarDinero(200.0)  
mi_cuenta.mostrar()  
print("-----")
otra_cuenta = cuenta()
otra_cuenta.titular = "Martin Lopez"
otra_cuenta.cantidad = 1000
otra_cuenta.mostrar()
otra_cuenta.ingresarDinero(200)
otra_cuenta.mostrar()
otra_cuenta.retirarDinero(700)
otra_cuenta.mostrar()
