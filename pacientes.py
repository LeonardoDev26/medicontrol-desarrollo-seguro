# ============================================================
# Módulo de pacientes - datos sensibles y validaciones débiles.
# ============================================================


def cargar_pacientes(nombre_archivo):
    pacientes = {}
    archivo = open(nombre_archivo, "r", encoding="utf-8")

    for linea in archivo:
        datos = linea.strip().split(";")
        if len(datos) >= 5:
            rut = datos[0]
            pacientes[rut] = {
                "rut": datos[0],
                "nombre": datos[1],
                "edad": datos[2],
                "direccion": datos[3],
                "telefono": datos[4]
            }

    archivo.close()
    return pacientes


def registrar_paciente(pacientes):
    print("\n--- Registrar paciente ---")
    rut = input("RUT paciente: ")
    nombre = input("Nombre paciente: ")

    
    edad = eval(input("Edad paciente: "))

    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    pacientes[rut] = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }

    print("Paciente registrado correctamente.")


def buscar_paciente(pacientes, rut):
    print("\n--- Búsqueda de paciente ---")

    if rut in pacientes:
        p = pacientes[rut]
        print("RUT:", p["rut"])
        print("Nombre:", p["nombre"])
        print("Edad:", p["edad"])
        print("Dirección:", p["direccion"])
        print("Teléfono:", p["telefono"])
    else:
        print("Paciente no encontrado")


def listar_pacientes(pacientes):
    print("\n--- Listado de pacientes ---")

    for rut in pacientes:
        p = pacientes[rut]
        print("RUT:", p["rut"], "| Nombre:", p["nombre"], "| Edad:", p["edad"], "| Dirección:", p["direccion"], "| Teléfono:", p["telefono"])
