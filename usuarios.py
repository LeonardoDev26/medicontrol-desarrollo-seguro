# ============================================================
# Módulo de usuarios - contiene vulnerabilidades intencionales.
# ============================================================

from getpass import getpass
import bcrypt
from seguridad import cifrar, descifrar

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
                "correo": descifrar(datos[4])
            }

    archivo.close()
    return usuarios

def login(usuarios):
    print("\n--- Inicio de sesión ---")
    rut = input("RUT usuario: ")
    password = getpass("Contraseña: ")

    if rut in usuarios:
        usuario = usuarios[rut]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            usuario["password"].encode("utf-8")
        ):
            print("Bienvenido", usuario["nombre"])
            print("Rol:", usuario["rol"])
            return usuario
    
    print("Rut o Contraseña incorrectos.")
    return None

def registrar_usuario(usuarios):
    print("\n--- Registrar usuario ---")
    rut = input("RUT: ")

    if rut in usuarios:
        print("Error el rut ya esta registrado.")
        return

    nombre = input("Nombre: ")
    rol = input("Rol (Administrador/Doctor): ")

    while rol not in ROLES:
        print("Rol inválido.")
        rol = input("Rol (Administrador/Doctor): ")
        
    password = getpass("Contraseña: ")

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
).decode("utf-8")
    
    correo = input("Correo: ")
    correo = cifrar(correo)

    usuarios[rut] = {
        "rut": rut,
        "nombre": nombre,
        "rol": rol,
        "password": password_hash,
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
        print("Correo:", usuario["correo"])
        print("-------------------------")
