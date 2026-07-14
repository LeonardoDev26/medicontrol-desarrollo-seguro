from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

def generar_clave():
    clave = Fernet.generate_key()

    with open("clave.key", "wb") as archivo:
        archivo.write(clave)


def cargar_clave():
    with open("clave.key", "rb") as archivo:
        return archivo.read()


def obtener_fernet():
    clave = cargar_clave()
    return Fernet(clave)


def cifrar(texto):
    fernet = obtener_fernet()
    return fernet.encrypt(texto.encode("utf-8")).decode("utf-8")


def descifrar(texto):
    fernet = obtener_fernet()

    try:
        return fernet.decrypt(texto.encode("utf-8")).decode("utf-8")
    except InvalidToken:
        return texto