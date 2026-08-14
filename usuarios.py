cantidad = int(input("¿Cuántos usuarios quieres crear? "))

for i in range(cantidad):
    nombre = input(f"Ingresa el nombre del usuario {i + 1}: ")
    print(f"Usuario creado: {nombre}")