# ============================================================
# Módulo de pacientes.
# ============================================================

from seguridad import descifrar


def cargar_pacientes(nombre_archivo):
    pacientes = {}

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) >= 5:
                    rut = datos[0]

                    pacientes[rut] = {
                        "rut": datos[0],
                        "nombre": descifrar(datos[1]),
                        "edad": int(datos[2]),
                        "direccion": descifrar(datos[3]),
                        "telefono": descifrar(datos[4])
                    }

    except FileNotFoundError:
        print("No se encontró el archivo de pacientes.")

    except OSError:
        print("Ocurrió un error al leer el archivo de pacientes.")

    return pacientes


def validar_rut(rut):
    rut = rut.strip().upper()

    if rut == "":
        print("Error: Debe ingresar un RUT.")
        return False

    rut = rut.replace(".", "")

    if "-" not in rut:
        print("Error: El RUT debe contener un guion (-).")
        return False

    partes = rut.split("-")

    if len(partes) != 2:
        print("Error: Formato de RUT incorrecto.")
        return False

    numero = partes[0]
    dv = partes[1]

    if len(numero) < 7 or len(numero) > 8:
        print("Error: El RUT debe tener entre 7 y 8 dígitos.")
        return False

    if not numero.isdigit():
        print("Error: La parte numérica del RUT solo puede contener números.")
        return False

    if len(dv) != 1 or not (dv.isdigit() or dv == "K"):
        print("Error: Dígito verificador inválido.")
        return False

    suma = 0
    multiplicador = 2

    for digito in reversed(numero):
        suma += int(digito) * multiplicador
        multiplicador += 1

        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)

    if dv != dv_calculado:
        print("Error: El dígito verificador no corresponde al RUT ingresado.")
        return False

    return True


def registrar_paciente(pacientes):
    print("\n--- Registrar paciente ---")

    rut_valido = False

    while not rut_valido:
        rut = input("RUT paciente: ").strip().upper()
        rut_valido = validar_rut(rut)

    while rut in pacientes:
        print("Error: El RUT ya está registrado.")
        rut_valido = False

        while not rut_valido:
            rut = input("RUT paciente: ").strip().upper()
            rut_valido = validar_rut(rut)

    nombre_valido = False

    while not nombre_valido:

        nombre = input("Nombre paciente: ").strip()

        if nombre == "":
            print("Error: Debe ingresar un nombre.")

        elif len(nombre) < 3:
            print("Error: El nombre debe tener al menos 3 caracteres.")

        else:
            valido = True

            for letra in nombre:
                if not letra.isalpha() and letra != " ":
                    valido = False

            if valido:
                nombre_valido = True
            else:
                print("Error: El nombre solo puede contener letras y espacios.")

    edad_valida = False

    while not edad_valida:

        try:
            edad = int(input("Edad paciente: "))

            if 0 <= edad <= 130:
                edad_valida = True
            else:
                print("Error: La edad debe estar entre 0 y 130 años.")

        except ValueError:
            print("Error: Debe ingresar un número entero.")

    direccion_valida = False

    while not direccion_valida:

        direccion = input("Dirección: ").strip()

        if direccion == "":
            print("Error: Debe ingresar una dirección.")

        elif len(direccion) < 5:
            print("Error: La dirección es demasiado corta.")

        else:
            direccion_valida = True

    telefono_valido = False

    while not telefono_valido:

        telefono = input("Teléfono: ").strip()

        if telefono == "":
            print("Error: Debe ingresar un teléfono.")

        elif not telefono.isdigit():
            print("Error: El teléfono solo puede contener números.")

        elif len(telefono) != 9:
            print("Error: El teléfono debe tener 9 dígitos.")

        else:
            telefono_valido = True

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

        print("RUT:", p["rut"])
        print("Nombre:", p["nombre"])
        print("Edad:", p["edad"])
        print("Dirección:", p["direccion"])
        print("Teléfono:", p["telefono"])
        print("-------------------------")