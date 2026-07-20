# MEDICONTROL - EVA4

## Descripción

MEDICONTROL es un sistema de gestión médica desarrollado en Python como proyecto final de la asignatura **Programación Segura** de INACAP.

El objetivo del proyecto fue analizar el sistema entregado por el profesor, identificar vulnerabilidades de seguridad, aplicar buenas prácticas de programación segura y documentar el proceso de desarrollo utilizando la metodología Scrum y herramientas de control de versiones.

---

## Objetivo General

Fortalecer la seguridad del sistema MEDICONTROL mediante el análisis, corrección y documentación de las vulnerabilidades presentes en el código fuente.

## Objetivos Específicos

- Analizar el código fuente proporcionado.
- Identificar vulnerabilidades de seguridad.
- Implementar controles de seguridad para proteger la información sensible.
- Aplicar buenas prácticas de programación segura.
- Gestionar el desarrollo utilizando Git y GitHub.
- Organizar el trabajo mediante la metodología Scrum.
- Documentar todas las mejoras implementadas.

---

# Equipo de Desarrollo

| Integrante | Rol |
|------------|-----|
| Leonardo Bolívar | Scrum Master |
| Alejandra Espinoza | Developer |
| Daniel Ramírez | Developer |

---

# Tecnologías Utilizadas

- Python 3
- Git
- GitHub
- Jira
- Visual Studio Code
- bcrypt
- cryptography (Fernet)
- Bandit (análisis estático de seguridad del código)
---

# Sistemas Operativos

- Ubuntu Linux
- macOS
- Windows

---

# Mejoras de Seguridad Implementadas

Durante el desarrollo del proyecto se incorporaron distintas medidas para fortalecer la seguridad del sistema:

- Validación de RUT.
- Validación de correos electrónicos.
- Validación de datos ingresados por el usuario.
- Manejo de excepciones.
- Ocultamiento de contraseñas mediante `getpass`.
- Almacenamiento seguro de contraseñas utilizando `bcrypt`.
- Cifrado de información sensible mediante `Fernet` (`cryptography`).

---

# Estructura del Proyecto

```text
medicontrol_eval/

├── main.py
├── usuarios.py
├── pacientes.py
├── diagnosticos.py
├── archivos.py
├── seguridad.py
├── utilidades.py
│
├── usuarios.txt
├── pacientes.txt
├── diagnosticos.txt
├── logs.txt
├── clave.key
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Instalación

Clonar el repositorio:

```bash
git clone git@github.com:LeonardoDev26/medicontrol-desarrollo-seguro.git
```

Ingresar al directorio del proyecto:

```bash
cd medicontrol_eval
```

Crear un entorno virtual (opcional pero recomendado):

```bash
python3 -m venv venv
```

Activar el entorno virtual:

Linux:

```bash
source venv/bin/activate
```

Windows:

```cmd
venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecución

```bash
python3 main.py
```

---

# Flujo de Trabajo con Git

Para el desarrollo del proyecto se utilizó una estrategia basada en ramas.

Ramas principales:

- main
- integration

Ramas de desarrollo:

- feature/leonardo-seguridad
- feature/ale-pacientes
- feature/daniel-diagnosticos

Cada integrante desarrolló sus funcionalidades en una rama independiente, las cuales posteriormente fueron integradas en la rama `integration` y finalmente fusionadas con `main`.

---

# Metodología de Trabajo

El desarrollo del proyecto se realizó utilizando la metodología Scrum.

Durante el proceso se llevaron a cabo reuniones de planificación, seguimiento e integración, registrando actas y evidencias del avance de cada sprint.

---

# Estado del Proyecto

**Versión:** 1.0

**Estado:** Finalizado.

---

# Historial de Versiones

| Versión | Descripción |
|----------|-------------|
| 1.0 | Versión final del proyecto con mejoras de seguridad implementadas. |

---

# Asignatura

Programación Segura

Instituto Profesional INACAP

---

# Licencia

Proyecto desarrollado exclusivamente con fines académicos.