# ============================================================
# Módulo de guardado de archivos.
# ============================================================


def guardar_usuarios(nombre_archivo, usuarios):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for rut in usuarios:
        u = usuarios[rut]
        archivo.write(u["rut"] + ";" + u["nombre"] + ";" + u["rol"] + ";" + u["password"] + ";" + u["correo"] + "\n")

    archivo.close()


def guardar_pacientes(nombre_archivo, pacientes):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for rut in pacientes:
        p = pacientes[rut]
        archivo.write(str(p["rut"]) + ";" + str(p["nombre"]) + ";" + str(p["edad"]) + ";" + str(p["direccion"]) + ";" + str(p["telefono"]) + "\n")

    archivo.close()


def guardar_diagnosticos(nombre_archivo, diagnosticos):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for d in diagnosticos:
        archivo.write(d["rut_paciente"] + ";" + d["fecha"] + ";" + d["diagnostico"] + ";" + d["tratamiento"] + ";" + d["rut_doctor"] + "\n")

    archivo.close()
