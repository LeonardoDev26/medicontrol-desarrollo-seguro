# ============================================================
# Módulo de guardado de archivos.
# ============================================================

def guardar_usuarios(nombre_archivo, usuarios):

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for rut in usuarios:
                u = usuarios[rut]

                archivo.write(
                    u["rut"] + ";" +
                    u["nombre"] + ";" +
                    u["rol"] + ";" +
                    u["password"] + ";" +
                    u["correo"] + "\n"
                )

    except Exception as e:
        print(f"Error al guardar usuarios: {e}")

def guardar_pacientes(nombre_archivo, pacientes):

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:

            for rut in pacientes:

                p = pacientes[rut]

                archivo.write(
                    str(p["rut"]) + ";" +
                    str(p["nombre"]) + ";" +
                    str(p["edad"]) + ";" +
                    str(p["direccion"]) + ";" +
                    str(p["telefono"]) + "\n"
                )

    except Exception as e:
        print(f"Error al guardar pacientes: {e}")


def guardar_diagnosticos(nombre_archivo, diagnosticos):

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:

            for d in diagnosticos:

                archivo.write(
                    d["rut_paciente"] + ";" +
                    d["fecha"] + ";" +
                    d["diagnostico"] + ";" +
                    d["tratamiento"] + ";" +
                    d["rut_doctor"] + "\n"
                )

    except Exception as e:
        print(f"Error al guardar diagnósticos: {e}")