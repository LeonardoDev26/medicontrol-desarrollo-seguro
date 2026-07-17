# ============================================================
# Funciones utilitarias.
# ============================================================

from datetime import datetime


def pausar():
    input("\nPresione ENTER para continuar...")


def registrar_log_inseguro(mensaje):

    try:
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{fecha}] {mensaje}\n")

    except Exception as e:
        print(f"Error al registrar el log: {e}")
