# ============================================================
# SISTEMA MEDICONTROL - EVALUACION U4 DESARROLLO SEGURO
# Archivo principal para que estudiantes analicen y mejoren.
# Contiene vulnerabilidades intencionales con fines educativos.
# ============================================================

from usuarios import cargar_usuarios, login, registrar_usuario, listar_usuarios
from pacientes import cargar_pacientes, registrar_paciente, buscar_paciente, listar_pacientes
from diagnosticos import cargar_diagnosticos, registrar_diagnostico, listar_diagnosticos, buscar_diagnosticos_paciente
from archivos import guardar_usuarios, guardar_pacientes, guardar_diagnosticos
from utilidades import pausar, registrar_log_inseguro

ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_PACIENTES = "pacientes.txt"
ARCHIVO_DIAGNOSTICOS = "diagnosticos.txt"


def menu_administrador(usuario_actual, usuarios, pacientes, diagnosticos):
    opcion = ""

    while opcion != "7":
        print("\n==============================")
        print(" MENÚ ADMINISTRADOR")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Registrar paciente")
        print("4. Listar pacientes")
        print("5. Ver todos los diagnósticos")
        print("6. Guardar información")
        print("7. Cerrar sesión")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            listar_usuarios(usuarios)
        elif opcion == "3":
            registrar_paciente(pacientes)
        elif opcion == "4":
            listar_pacientes(pacientes)
        elif opcion == "5":
            listar_diagnosticos(diagnosticos, pacientes)
        elif opcion == "6":
            guardar_usuarios(ARCHIVO_USUARIOS, usuarios)
            guardar_pacientes(ARCHIVO_PACIENTES, pacientes)
            guardar_diagnosticos(ARCHIVO_DIAGNOSTICOS, diagnosticos)
            print("Información guardada correctamente.")
        elif opcion == "7":
            registrar_log_inseguro("Cierre de sesión administrador: " + usuario_actual["rut"])
            print("Cerrando sesión...")
        else:
            print("Opción inválida")

        pausar()


def menu_doctor(usuario_actual, usuarios, pacientes, diagnosticos):
    opcion = ""

    while opcion != "6":
        print("\n==============================")
        print(" MENÚ DOCTOR")
        print("==============================")
        print("1. Buscar paciente")
        print("2. Registrar diagnóstico")
        print("3. Ver todos los diagnósticos")
        print("4. Ver diagnósticos de un paciente")
        print("5. Guardar información")
        print("6. Cerrar sesión")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            rut = input("Ingrese RUT del paciente: ")
            buscar_paciente(pacientes, rut)
        elif opcion == "2":
            registrar_diagnostico(diagnosticos, pacientes, usuario_actual)
        elif opcion == "3":
            listar_diagnosticos(diagnosticos, pacientes)
        elif opcion == "4":
            rut = input("Ingrese RUT del paciente: ")
            buscar_diagnosticos_paciente(diagnosticos, pacientes, rut)
        elif opcion == "5":
            guardar_diagnosticos(ARCHIVO_DIAGNOSTICOS, diagnosticos)
            print("Diagnósticos guardados correctamente.")
        elif opcion == "6":
            registrar_log_inseguro("Cierre de sesión doctor: " + usuario_actual["rut"])
            print("Cerrando sesión...")
        else:
            print("Opción inválida")

        pausar()


def main():
    print("====================================")
    print(" SISTEMA CLÍNICO MEDICONTROL")
    print(" Evaluación de Desarrollo Seguro")
    print("====================================")

    usuarios = cargar_usuarios(ARCHIVO_USUARIOS)
    pacientes = cargar_pacientes(ARCHIVO_PACIENTES)
    diagnosticos = cargar_diagnosticos(ARCHIVO_DIAGNOSTICOS)

    opcion = ""

    while opcion != "2":
        print("\n1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            usuario_actual = login(usuarios)

            if usuario_actual is not None:
                registrar_log_inseguro("Ingreso exitoso: " + usuario_actual["rut"] + " - " + usuario_actual["rol"])
                if usuario_actual["rol"] == "Administrador":
                    menu_administrador(usuario_actual, usuarios, pacientes, diagnosticos)
                elif usuario_actual["rol"] == "Doctor":
                    menu_doctor(usuario_actual, usuarios, pacientes, diagnosticos)
                else:
                    print("Rol no reconocido. Contacte al administrador.")
            else:
                registrar_log_inseguro("Intento fallido de acceso")
                print("Credenciales incorrectas")

        elif opcion == "2":
            print("Finalizando sistema...")
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
