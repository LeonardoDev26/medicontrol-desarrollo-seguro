# ============================================================
# Módulo de diagnósticos - información médica sensible.
# ============================================================

from seguridad import descifrar


def cargar_diagnosticos(nombre_archivo):
    diagnosticos = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) >= 5:
                    diagnostico = {
                        "rut_paciente": datos[0],
                        "fecha": datos[1],
                        "diagnostico": descifrar(datos[2]),
                        "tratamiento": descifrar(datos[3]),
                        "rut_doctor": datos[4]
                    }

                    diagnosticos.append(diagnostico)

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")

    except Exception as e:
        print(f"Error inesperado al cargar el archivo: {e}")

    return diagnosticos


def registrar_diagnostico(diagnosticos, pacientes, doctor_actual):
    print("\n--- Registrar diagnóstico ---")

    rut_paciente = input("RUT paciente: ")

    while rut_paciente not in pacientes:
        print("Error: El paciente no se encuentra registrado.")
        rut_paciente = input("RUT paciente: ")

    fecha = ""

    while fecha == "":
        fecha = input("Fecha atención (dd/mm/aaaa): ").strip()

        if fecha == "":
            print("Error: Debe ingresar la fecha de atención.")

    texto_diagnostico = ""

    while texto_diagnostico == "":
        texto_diagnostico = input("Diagnóstico: ").replace(";", ",").strip()

        if texto_diagnostico == "":
            print("Error: Debe ingresar un diagnóstico.")

    tratamiento = ""

    while tratamiento == "":
        tratamiento = input("Tratamiento indicado: ").replace(";", ",").strip()

        if tratamiento == "":
            print("Error: Debe ingresar un tratamiento.")

    nuevo = {
        "rut_paciente": rut_paciente,
        "fecha": fecha,
        "diagnostico": texto_diagnostico,
        "tratamiento": tratamiento,
        "rut_doctor": doctor_actual["rut"],
    }

    diagnosticos.append(nuevo)

    print("Diagnóstico registrado correctamente.")


def listar_diagnosticos(diagnosticos, pacientes):
    print("\n--- Listado de diagnósticos ---")

    for d in diagnosticos:

        nombre_paciente = "Paciente no registrado"

        if d["rut_paciente"] in pacientes:
            nombre_paciente = pacientes[d["rut_paciente"]]["nombre"]

        print("Paciente:", d["rut_paciente"], "-", nombre_paciente)
        print("Fecha:", d["fecha"])
        print("Diagnóstico:", d["diagnostico"])
        print("Tratamiento:", d["tratamiento"])
        print("Doctor:", d["rut_doctor"])
        print("----------------------------")


def buscar_diagnosticos_paciente(diagnosticos, pacientes, rut_paciente):
    print("\n--- Diagnósticos por paciente ---")

    encontrados = 0

    for d in diagnosticos:

        if d["rut_paciente"] == rut_paciente:
            print("Fecha:", d["fecha"])
            print("Diagnóstico:", d["diagnostico"])
            print("Tratamiento:", d["tratamiento"])
            print("Doctor:", d["rut_doctor"])
            print("----------------------------")
            encontrados += 1

    if encontrados == 0:
        print("No existen diagnósticos registrados para este paciente.")