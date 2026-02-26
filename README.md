# 💳 Cajero Automático

Un sistema de Cajero Automático (ATM) implementado en Python que permite a los usuarios autenticarse, consultar saldos, realizar depósitos y retiros de dinero con una interfaz en línea de comandos.

## 📋 Descripción

Este proyecto simula el funcionamiento de un cajero automático tradicional, presentando un menú interactivo donde los usuarios pueden:
- Registrarse en el sistema
- Iniciar sesión
- Consultar su saldo actual
- Retirar dinero
- Depositar dinero
- Salir de la aplicación

## ✨ Características

- **Autenticación de usuarios**: Sistema de login y registro
- **Validación de credenciales**: Verificación de email y contraseña
- **Gestión de saldo**: Consulta, depósito y retiro de dinero
- **Validación de entrada**: Manejo de errores para entradas inválidas
- **Interfaz interactiva**: Menús claros y organizados
- **Compatibilidad multiplataforma**: Soporta Windows, Linux y macOS
- **Limpeza de pantalla automática**: La pantalla se limpia entre transacciones

## 🛠️ Requisitos

- Python 3.6 o superior
- No requiere instalación de paquetes externos

## 📦 Instalación

1. Clona o descarga el repositorio
```bash
git clone https://github.com/LFDIAZDEV2209/cajero-automatico.git
cd cajero-automatico
```

2. Ejecuta el programa
```bash
python main.py
```

## 📁 Estructura del Proyecto

```
cajero-automatico/
│
├── main.py                          # Punto de entrada principal
├── data.py                          # Base de datos de usuarios
│
└── modules/
    ├── auth/                        # Módulo de autenticación
    │   ├── login.py                 # Funcionalidad de login
    │   ├── register.py              # Funcionalidad de registro
    │   └── __pycache__/
    │
    ├── ATM/                         # Módulo principal del cajero
    │   ├── module.py                # Menú principal del ATM
    │   ├── depositAmount.py         # Función de depósito
    │   ├── whithdrawAmount.py       # Función de retiro
    │   ├── listAmount.py            # Consulta de saldo
    │   └── __pycache__/
    │
    ├── utils/                       # Módulo de utilidades
    │   ├── msg.py                   # Mensajes y menús
    │   ├── screenController.py      # Control de pantalla
    │   └── __pycache__/
    │
    └── __pycache__/
```

## 🚀 Uso

### Menú Principal

Al ejecutar el programa, se muestra el menú de bienvenida:

```
--------------------
Bienvenido al cajero automático
--------------------
1. Iniciar sesión
2. Registrarse
3. Salir
```

### Opción 1: Iniciar Sesión

Ingresa tus credenciales (email y contraseña) para acceder a tu cuenta.

```
Iniciar sesión
Ingrese su email: juan.perez@example.com
Ingrese su contraseña: 123456
```

### Opción 2: Registrarse

Crea una nueva cuenta proporcionando tu nombre, email y contraseña.

```
Registrarse
Ingrese su nombre: Carlos Lopez
Ingrese su email: carlos.lopez@example.com
Ingrese su contraseña: micontraseña
```

### Menú del Cajero Automático

Una vez autenticado, accederás al menú principal del ATM:

```
-----------------
Cajero Automatico
-----------------
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir
```

#### Consultar Saldo (Opción 1)
Muestra tu saldo actual en la cuenta.

#### Retirar Dinero (Opción 2)
Permite retirar una cantidad de dinero de tu cuenta.
- Valida que la cantidad sea positiva
- Verifica que tengas fondos suficientes
- Actualiza tu saldo

#### Depositar Dinero (Opción 3)
Permite depositar una cantidad de dinero en tu cuenta.
- Valida que la cantidad sea positiva
- Actualiza tu saldo

#### Salir (Opción 4)
Cierra la sesión y regresa al menú principal.

## 👥 Usuarios de Prueba

El sistema viene con dos usuarios predefinidos para pruebas:

| Email | Contraseña | Saldo Inicial |
|-------|-----------|---------------|
| john.doe@example.com | 123456 | $1000 |
| juan.perez@example.com | 123456 | $1000 |

## 📚 Descripción de Módulos

### `main.py`
- Punto de entrada de la aplicación
- Maneja el menú principal de bienvenida
- Orquesta el flujo entre autenticación y funcionalidades del ATM

### `data.py`
- Almacena la información de usuarios (actualmente en memoria)
- Cada usuario tiene: id, nombre, email, contraseña y saldo

### `modules/auth/`

**`login.py`**
- Valida credenciales del usuario
- Busca el usuario en la base de datos
- Verifica email y contraseña

**`register.py`**
- Permite crear nuevos usuarios
- Valida que el email no esté registrado
- Genera un nuevo ID automáticamente

### `modules/ATM/`

**`module.py`**
- Menú principal del cajero automático
- Orquesta las operaciones disponibles
- Gestiona el flujo de transacciones

**`listAmount.py`**
- Muestra el saldo actual del usuario

**`whithdrawAmount.py`**
- Solicita cantidad a retirar
- Valida entrada y fondos disponibles
- Retorna la cantidad y nuevo saldo

**`depositAmount.py`**
- Solicita cantidad a depositar
- Valida entrada
- Retorna la cantidad y nuevo saldo

### `modules/utils/`

**`msg.py`**
- Define los menús de la aplicación
- Contiene constantes de mensajes

**`screenController.py`**
- Limpia la pantalla según el sistema operativo
- Pausa la pantalla para permitir lectura
- Compatible con Windows, Linux y macOS

## ⚙️ Flujo de Ejecución

```
Inicio
  ↓
Menú Principal (Login/Registro/Salir)
  ├─→ Login exitoso → Menú ATM
  │     ├─→ Consultar Saldo
  │     ├─→ Retirar Dinero
  │     ├─→ Depositar Dinero
  │     └─→ Salir → Regresa a Menú Principal
  │
  ├─→ Registro exitoso → Menú Principal
  │
  └─→ Salir → Fin de la aplicación
```

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 👨‍💻 Autor

Proyecto desarrollado como parte del curso de programación en Python - Clan 9 RIWI - Luis Felipe Diaz

---

**¡Gracias por usar el Cajero Automático!** 😊
