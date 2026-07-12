# MEDICONTROL - Eva4

## Descripción

MEDICONTROL es un sistema de gestión médica desarrollado en Python, utilizado como base para la evaluación final de la asignatura Programación Segura de INACAP.
El proyecto consiste en analizar el sistema entregado por el profesor, identificar vulnerabilidades de seguridad, aplicar buenas prácticas de programación segura y documentar el proceso de desarrollo utilizando la metodología Scrum y herramientas de control de versiones.

---

## Objetivos

### Objetivo General

Fortalecer la seguridad del sistema MEDICONTROL mediante el análisis, corrección y documentación de las vulnerabilidades presentes en el código fuente.

### Objetivos Específicos

- Analizar el código entregado por el profesor.
- Identificar vulnerabilidades de seguridad.
- Aplicar buenas prácticas de programación segura.
- Utilizar Git y GitHub para el control de versiones.
- Gestionar el proyecto utilizando la metodología Scrum.
- Documentar el desarrollo del proyecto.

---

## Equipo de Desarrollo

| Integrante | Rol |
|------------|-----|
| Leonardo Bolívar | Scrum Master |
| Alejandra Espinoza | Developer |
| Daniel Ramirez | Developer |

---

## Tecnologías Utilizadas

- Python 3
- Git
- GitHub
- Jira
- Visual Studio Code

### Sistemas Operativos de los devs

- Ubuntu Linux
- macOS
- Windows

### Herramientas que se incorporarán durante el desarrollo

- Bandit
- SonarQube
- bcrypt

---

## Estructura del Proyecto

```text
medicontrol_eval/

├── archivos.py
├── diagnosticos.py
├── pacientes.py
├── usuarios.py
├── utilidades.py
├── main.py
│
├── usuarios.txt
├── pacientes.txt
├── diagnosticos.txt
├── logs.txt
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
└── evidencias/
```

---

## Instalación

Clonar el repositorio:

```bash
git clone git@github.com:LeonardoDev26/medicontrol-desarrollo-seguro.git
```

Ingresar al directorio del proyecto:

```bash
cd medicontrol_eval
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

```bash
python3 main.py
```

---

## Flujo de Trabajo con Git

El proyecto utilizará una estrategia basada en ramas para facilitar el trabajo colaborativo.

Ramas principales:

- main
- develop

Las ramas de desarrollo se crearán a partir de `develop` según las funcionalidades asignadas a cada integrante.

---

## Metodología de Trabajo

El proyecto será desarrollado utilizando la metodología Scrum.
Durante el desarrollo se planificarán y ejecutarán los sprints necesarios hasta la entrega final de la evaluación.

---

## Estado del Proyecto

Versión 1.0
Estado: En preparación.

---

## Historial de Versiones

| Versión | Descripción |
|----------|-------------|
| 1.0 | Configuración inicial del proyecto y documentación base. |

---
## Asignatura

Programación Segura

Instituto Profesional INACAP
---

## Licencia
Proyecto desarrollado exclusivamente con fines académicos.