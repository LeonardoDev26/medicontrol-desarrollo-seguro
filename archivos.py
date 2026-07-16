# ============================================================
# Módulo de guardado de archivos.
# ============================================================

from seguridad import cifrar


def guardar_usuarios(nombre_archivo, usuarios):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for rut in usuarios:
        u = usuarios[rut]
        archivo.write(
            u["rut"] + ";" +
            u["nombre"] + ";" +
            u["rol"] + ";" +
            u["password"] + ";" +
            cifrar(u["correo"]) + "\n"
        )

    archivo.close()


def guardar_pacientes(nombre_archivo, pacientes):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for rut in pacientes:
        p = pacientes[rut]
        archivo.write(
            str(p["rut"]) + ";" +
            cifrar(str(p["nombre"])) + ";" +
            str(p["edad"]) + ";" +
            cifrar(str(p["direccion"])) + ";" +
            cifrar(str(p["telefono"])) + "\n"
        )

    archivo.close()


def guardar_diagnosticos(nombre_archivo, diagnosticos):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    for d in diagnosticos:
        archivo.write(
            d["rut_paciente"] + ";" +
            d["fecha"] + ";" +
            cifrar(d["diagnostico"]) + ";" +
            cifrar(d["tratamiento"]) + ";" +
            d["rut_doctor"] + "\n"
        )

    archivo.close()