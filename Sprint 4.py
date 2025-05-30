import datetime

# --- Definicion de Clases ---

class Dueño:
    """Representa a un dueño de mascota con su informacion de contacto."""
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        """Retorna una representacion legible del objeto Dueño."""
        return f"Dueño: {self.nombre}, Teléfono: {self.telefono}, Direccion: {self.direccion}"

class Mascota:
    """Representa a una mascota con sus detalles y su dueño asociado."""
    def __init__(self, nombre, especie, raza, edad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueño = dueño  # Esto es un objeto Dueño
        self.historial_consultas = [] # Lista para guardar objetos Consulta de esta mascota

    def __str__(self):
        """Retorna una representación legible del objeto Mascota y su dueño."""
        return (f"Mascota: {self.nombre} ({self.especie} - {self.raza}), Edad: {self.edad} años\n"
                f"  {self.dueño}")

class Consulta:
    """Representa una consulta veterinaria con su fecha, motivo, diagnostico y la mascota asociada."""
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota # Esto es un objeto Mascota

    def __str__(self):
        """Retorna una representacion legible del objeto Consulta."""
        return (f"Fecha: {self.fecha}\n"
                f"  Motivo: {self.motivo}\n"
                f"  Diagnostico: {self.diagnostico}")

# --- Listas globales para almacenar los objetos ---
# Aqui guardaremos todos los dueños y mascotas que se registren
mascotas_registradas = []
dueños_registrados = []

# --- Funcionalidades Esenciales ---

def registrar_dueño():
    """
    Registra un nuevo dueño o retorna uno existente si el nombre coincide.
    Esto evita dueños duplicados con el mismo nombre.
    """
    nombre = input("Ingrese el nombre del dueño: ").strip().title()
    for d in dueños_registrados:
        if d.nombre == nombre:
            print(f"El dueño '{nombre}' ya está registrado.")
            return d # Retorna el objeto Dueño existente
    
    telefono = input("Ingrese el teléfono del dueño: ")
    direccion = input("Ingrese la dirección del dueño: ")
    nuevo_dueño = Dueño(nombre, telefono, direccion)
    dueños_registrados.append(nuevo_dueño)
    print(f"Dueño '{nombre}' registrado exitosamente.")
    return nuevo_dueño

def registrar_mascota():
    """Permite registrar una nueva mascota y asignarla a un dueño existente o nuevo."""
    print("\n--- Registrar Nueva Mascota ---")
    dueño_mascota = None

    if not dueños_registrados:
        print("No hay dueños registrados. Por favor, registre un dueño primero para la mascota.")
        dueño_mascota = registrar_dueño()
    else:
        print("Dueños registrados:")
        for i, dueño in enumerate(dueños_registrados):
            print(f"  {i+1}. {dueño.nombre}")
        
        opcion_dueño = input("Seleccione el número del dueño existente o escriba 'nuevo' para registrar uno: ").lower()
        if opcion_dueño == 'nuevo':
            dueño_mascota = registrar_dueño()
        else:
            try:
                indice_dueño = int(opcion_dueño) - 1
                if 0 <= indice_dueño < len(dueños_registrados):
                    dueño_mascota = dueños_registrados[indice_dueño]
                else:
                    print("Opción inválida. Se registrará un nuevo dueño.")
                    dueño_mascota = registrar_dueño()
            except ValueError:
                print("Entrada inválida. Se registrará un nuevo dueño.")
                dueño_mascota = registrar_dueño()

    if not dueño_mascota: # Si por alguna razon no se pudo obtener o registrar un dueño
        print("No se pudo asignar un dueño a la mascota. Registro cancelado.")
        return

    nombre = input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    raza = input("Raza de la mascota: ")
    while True:
        try:
            edad = int(input("Edad de la mascota (años): "))
            break
        except ValueError:
            print("Por favor, ingrese una edad valida (numero entero).")

    nueva_mascota = Mascota(nombre, especie, raza, edad, dueño_mascota)
    mascotas_registradas.append(nueva_mascota)
    print(f"Mascota '{nombre}' registrada exitosamente para {dueño_mascota.nombre}.")

def registrar_consulta():
    """Registra una consulta veterinaria para una mascota especifica."""
    print("\n--- Registrar Consulta Veterinaria ---")
    if not mascotas_registradas:
        print("No hay mascotas registradas para poder añadir una consulta.")
        return

    print("Mascotas registradas:")
    for i, mascota in enumerate(mascotas_registradas):
        print(f"  {i+1}. {mascota.nombre} (Dueño: {mascota.dueño.nombre})")

    mascota_seleccionada = None
    while mascota_seleccionada is None:
        try:
            seleccion = int(input("Seleccione el número de la mascota para la consulta: ")) - 1
            if 0 <= seleccion < len(mascotas_registradas):
                mascota_seleccionada = mascotas_registradas[seleccion]
            else:
                print("Numero de mascota invalido. Intente de nuevo.")
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero.")

    fecha = datetime.date.today().strftime("%Y-%m-%d") # La fecha se registra automáticamente
    motivo = input("Motivo de la consulta: ")
    diagnostico = input("Diagnostico de la consulta: ")

    nueva_consulta = Consulta(fecha, motivo, diagnostico, mascota_seleccionada)
    mascota_seleccionada.historial_consultas.append(nueva_consulta)
    print(f"Consulta registrada para '{mascota_seleccionada.nombre}'.")

def listar_mascotas():
    """Muestra todas las mascotas registradas junto con la informacion de su dueño."""
    print("\n--- Listado de Todas las Mascotas ---")
    if not mascotas_registradas:
        print("No hay mascotas registradas aun.")
        return

    for mascota in mascotas_registradas:
        print(mascota)
        print("-" * 40) # Separador visual para cada mascota

def ver_historial_consultas():
    """Muestra el historial de consultas de una mascota en particular."""
    print("\n--- Historial de Consultas de una Mascota ---")
    if not mascotas_registradas:
        print("No hay mascotas registradas para ver su historial.")
        return

    print("Mascotas registradas:")
    for i, mascota in enumerate(mascotas_registradas):
        print(f"  {i+1}. {mascota.nombre} (Dueño: {mascota.dueño.nombre})")

    mascota_seleccionada = None
    while mascota_seleccionada is None:
        try:
            seleccion = int(input("Seleccione el numero de la mascota para ver su historial: ")) - 1
            if 0 <= seleccion < len(mascotas_registradas):
                mascota_seleccionada = mascotas_registradas[seleccion]
            else:
                print("Numero de mascota invalido. Intente de nuevo.")
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero.")

    print(f"\n--- Historial de Consultas para {mascota_seleccionada.nombre} ---")
    if not mascota_seleccionada.historial_consultas:
        print(f"'{mascota_seleccionada.nombre}' no tiene consultas registradas aun.")
        return

    for i, consulta in enumerate(mascota_seleccionada.historial_consultas):
        print(f"\nConsulta #{i+1}:")
        print(consulta)
        print("---")

# --- Menu Principal y Ejecucion ---

def mostrar_menu():
    """Imprime el menu de opciones para el usuario."""
    print("\n--- Menu Principal Clinica Amigos Peludos ---")
    print("1. Registrar mascota")
    print("2. Registrar consulta")
    print("3. Listar mascotas")
    print("4. Ver historial de consultas de una mascota")
    print("5. Salir")
    print("------------------------------------------")

def main():
    """Funcion principal que ejecuta el menu interactivo."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            registrar_mascota()
        elif opcion == '2':
            registrar_consulta()
        elif opcion == '3':
            listar_mascotas()
        elif opcion == '4':
            ver_historial_consultas()
        elif opcion == '5':
            print("¡Gracias por usar la aplicacion de Amigos Peludos! ¡Hasta pronto!")
            break
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()