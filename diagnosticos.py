# ============================================================
# Módulo de diagnósticos - información médica sensible.
# ============================================================


def cargar_diagnosticos(nombre_archivo):
    diagnosticos = []  
    archivo = open(nombre_archivo, "r", encoding="utf-8")

    for linea in archivo:
        datos = linea.strip().split(";")
        if len(datos) >= 5:
            diagnostico = {
                "rut_paciente": datos[0],
                "fecha": datos[1],
                "diagnostico": datos[2],
                "tratamiento": datos[3],
                "rut_doctor": datos[4]
            }
            diagnosticos.append(diagnostico)

    archivo.close()
    return diagnosticos


def registrar_diagnostico(diagnosticos, pacientes, doctor_actual):
    print("\n--- Registrar diagnóstico ---")
    rut_paciente = input("RUT paciente: ")

    fecha = input("Fecha atención (dd/mm/aaaa): ")
    texto_diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento indicado: ")

    nuevo = {
        "rut_paciente": rut_paciente,
        "fecha": fecha,
        "diagnostico": texto_diagnostico,
        "tratamiento": tratamiento,
        "rut_doctor": doctor_actual["rut"]
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
            encontrados = encontrados + 1

    if encontrados == 0:
        print("No existen diagnósticos registrados para este paciente.")
