from Persona import persona 

# Creamos un objeto

#persona_1 = persona("Matias", 20, "45360660")

persona_1 = persona()


persona_1.nombre = "Matias"
persona_1.edad = 20
persona_1.DNI = "45360660"
persona_1.mostrar()
print(f"Soy mayor de edad? {persona_1.mayor_de_edad()}")
print("-------")
persona_1.nombre = "Lucas"
persona_1.edad = 17
persona_1.DNI = "45347798"
persona_1.mostrar()
print(f"Soy mayor de edad? {persona_1.mayor_de_edad()}")
