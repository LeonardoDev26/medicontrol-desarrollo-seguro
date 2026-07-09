# ============================================================
# Módulo de usuarios - contiene vulnerabilidades intencionales.
# ============================================================

ROLES = ("Administrador", "Doctor")  


def cargar_usuarios(nombre_archivo):
    usuarios = {}

    
    archivo = open(nombre_archivo, "r", encoding="utf-8")

    for linea in archivo:
        datos = linea.strip().split(";")  

        if len(datos) >= 5:
            rut = datos[0]
            usuarios[rut] = {
                "rut": datos[0],
                "nombre": datos[1],
                "rol": datos[2],
                "password": datos[3],  
                "correo": datos[4]
            }

    archivo.close()
    return usuarios


def login(usuarios):
    print("\n--- Inicio de sesión ---")
    rut = input("RUT usuario: ")
    password = input("Contraseña: ")

    if rut in usuarios:
        usuario = usuarios[rut]

        if usuario["password"] == password:
            print("Bienvenido", usuario["nombre"])
            print("Rol:", usuario["rol"])
            return usuario

    return None


def registrar_usuario(usuarios):
    print("\n--- Registrar usuario ---")
    rut = input("RUT: ")
    nombre = input("Nombre: ")
    rol = input("Rol (Administrador/Doctor): ")
    password = input("Contraseña: ")
    correo = input("Correo: ")

    usuarios[rut] = {
        "rut": rut,
        "nombre": nombre,
        "rol": rol,
        "password": password,
        "correo": correo
    }

    print("Usuario registrado correctamente.")


def listar_usuarios(usuarios):
    print("\n--- Listado de usuarios ---")

    for rut in usuarios:
        usuario = usuarios[rut]
        print("RUT:", usuario["rut"])
        print("Nombre:", usuario["nombre"])
        print("Rol:", usuario["rol"])
        print("Contraseña:", usuario["password"])
        print("Correo:", usuario["correo"])
        print("-------------------------")
