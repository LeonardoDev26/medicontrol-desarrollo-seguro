# ============================================================
# Módulo de usuarios - contiene vulnerabilidades intencionales.
# ============================================================

from getpass import getpass
import bcrypt
from seguridad import cifrar, descifrar

ROLES = ("Administrador", "Doctor")


def cargar_usuarios(nombre_archivo):
    usuarios = {}

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

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

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

    except OSError:
        print("Ocurrió un error al leer el archivo de usuarios.")

    return usuarios


def login(usuarios):
    print("\n--- Inicio de sesión ---")

    while True:

        rut = input("RUT usuario: ").strip()

        while rut == "":
            print("El RUT no puede estar vacío.")
            rut = input("RUT usuario: ").strip()

        password = getpass("Contraseña: ").strip()

        while password == "":
            print("La contraseña no puede estar vacía.")
            password = getpass("Contraseña: ").strip()

        if rut in usuarios:
            usuario = usuarios[rut]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                usuario["password"].encode("utf-8")
            ):
                print("Bienvenido", usuario["nombre"])
                print("Rol:", usuario["rol"])
                return usuario

        print("Credenciales incorrectas. Intente nuevamente.")


def registrar_usuario(usuarios):
    print("\n--- Registrar usuario ---")

    rut = input("RUT: ").strip()

    while rut == "" or rut in usuarios:

        if rut == "":
            print("El RUT no puede estar vacío.")
        else:
            print("El RUT ya está registrado.")

        rut = input("RUT: ").strip()

    nombre = input("Nombre: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre: ").strip()

    rol = input("Rol (Administrador/Doctor): ").strip()

    while rol not in ROLES:
        print("Rol inválido.")
        rol = input("Rol (Administrador/Doctor): ").strip()

    password = getpass("Contraseña: ").strip()

    while password == "":
        print("La contraseña no puede estar vacía.")
        password = getpass("Contraseña: ").strip()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    correo = input("Correo: ").strip()

    while correo == "":
        print("El correo no puede estar vacío.")
        correo = input("Correo: ").strip()

    while "@" not in correo or "." not in correo:
        print("Formato de correo inválido.")
        correo = input("Correo: ").strip()

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