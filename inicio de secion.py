print("Bienvenido a la practica #3 de Inicio de Sesion RhStudio")
input("Presiona algo para avanzar")


nombres_no_permitidos = ["negro","tonto","pendejo","gorda","estupido"]
def base_datos_usurario():
    contraseña = ()
    nombre_usuario = ()
    edad = ()
    
contraseña = input("Coloca tu nueva contraseña aqui: ")
while not any(c.isdigit() for c in contraseña):
    print("Debe haber un numero en la contraseña")
    contraseña = input("Coloca tu nueva contraseña aqui: ")

nombre_usuario = input("Pon tu nombre de usuario: ").lower()
while not nombre_usuario.isalpha() or nombre_usuario in nombres_no_permitidos:
    print("No puede llevar numeros el nombre de usuario tampoco  nombres inapropiados")
    nombre_usuario = input("Pon tu nombre de usuario: ").lower()
    
edad = input("Proporciona tu edad: ")

while not edad.isdigit():
    print("Tienen que ser números ❌")
    edad = input("Proporciona tu edad: ")

edad = int(edad)

while edad < 18:
    print("Tienes que ser mayor de edad para avanzar ❌")
    edad = input("Proporciona tu edad: ")

    while not edad.isdigit():   # 🔁 VALIDAS OTRA VEZ
        print("Tienen que ser números ❌")
        edad = input("Proporciona tu edad: ")

    edad = int(edad)

print("Edad aceptada ✅")
