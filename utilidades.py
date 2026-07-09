# ============================================================
# Funciones utilitarias.
# ============================================================


def pausar():
    input("\nPresione ENTER para continuar...")


def registrar_log_inseguro(mensaje):
    archivo = open("logs.txt", "a", encoding="utf-8")
    archivo.write(mensaje + "\n")
    archivo.close()
