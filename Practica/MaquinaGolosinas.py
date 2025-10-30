# --- 1. DATOS INICIALES (Como constantes globales) ---

GOLOSINAS = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevos Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "MYM'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

EMPLEADOS = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

CLAVES_TECNICO = ("admin", "CCCDDD", 2020)

# --- 2. DATOS DE ESTADO (Variables de sesión) ---

# Usamos un diccionario para un registro de ventas más eficiente: {código: cantidad}
GOLOSINAS_PEDIDAS = {}


# --- 3. FUNCIONES DE UTILIDAD Y BÚSQUEDA ---

def buscar_golosina(codigo):
    """Busca y retorna la sublista de la golosina o None si no se encuentra."""
    for item in GOLOSINAS:
        if item[0] == codigo:
            return item
    return None

def obtener_entero_valido(mensaje):
    """Garantiza que el usuario ingrese un número entero."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("❌ ¡Error! Ingrese solo números enteros, por favor.")

# --- 4. FUNCIONES DEL MENÚ ---

def pedir_golosina():
    """Opción A: Permite a un empleado comprar una golosina."""
    print("\n--- 🛒 Pedir Golosinas ---")
    legajo = obtener_entero_valido("Ingrese su número de legajo: ")

    if legajo not in EMPLEADOS:
        print("❌ ¡Acceso Denegado! El legajo ingresado no es válido.")
        return

    print(f"✅ Legajo verificado. ¡Bienvenido, {EMPLEADOS[legajo]}!")
    
    # Muestra el menú antes de pedir el código
    mostrar_golosinas() 
    
    codigo = obtener_entero_valido("Ingrese el código de la golosina: ")
    item_golosina = buscar_golosina(codigo)

    if not item_golosina:
        print("⚠️ Código de golosina no encontrado. Intente de nuevo.")
        return

    # item_golosina: [código, nombre, stock]
    nombre = item_golosina[1]
    stock_actual = item_golosina[2]

    if stock_actual <= 0:
        print(f"🚫 Lo sentimos, **{nombre}** está agotado. Por favor, seleccione otra.")
        return
    
    # Procesar la venta
    item_golosina[2] -= 1  # Reduce el stock
    
    # Registrar la venta eficientemente (usando diccionario)
    GOLOSINAS_PEDIDAS[codigo] = GOLOSINAS_PEDIDAS.get(codigo, 0) + 1
    
    print(f"🥳 ¡Disfrute su **{nombre}**! Quedan {item_golosina[2]} unidades.")


def mostrar_golosinas():
    """Opción B: Muestra el inventario actual (Stock)."""
    print("\n--- 📋 Stock de Golosinas ---")
    print("Código | Nombre de Producto | Stock")
    print("-" * 35)
    for codigo, nombre, stock in GOLOSINAS:
        # Se resalta el stock bajo
        stock_msg = f"{stock} (¡Bajo!)" if stock <= 5 and stock > 0 else stock
        stock_msg = "AGOTADO" if stock == 0 else stock_msg
        print(f"{codigo:<6} | {nombre:<18} | {stock_msg}")
    print("-" * 35)


def rellenar_golosinas():
    """Opción C: Permite a un técnico reponer stock."""
    print("\n--- 🔧 Rellenar Golosinas (Acceso Técnico) ---")
    
    # --- Verificación de Claves ---
    contrasena1 = input("Paso 1/3 - Ingrese la primer contraseña: ")
    if contrasena1 != CLAVES_TECNICO[0]:
        print("❌ Contraseña incorrecta. Acceso denegado.")
        return
    
    contrasena2 = input("Paso 2/3 - Ingrese la segunda contraseña: ")
    if contrasena2 != CLAVES_TECNICO[1]:
        print("❌ Contraseña incorrecta. Acceso denegado.")
        return
        
    contrasena3 = obtener_entero_valido("Paso 3/3 - Ingrese la tercer contraseña (año): ")
    if contrasena3 != CLAVES_TECNICO[2]:
        print("❌ Contraseña incorrecta. Acceso denegado.")
        return

    print("✅ ¡Acceso técnico concedido!")
    
    # --- Proceso de Recarga ---
    codigo = obtener_entero_valido("Ingrese el código de la golosina a recargar: ")
    item_golosina = buscar_golosina(codigo)

    if not item_golosina:
        print("⚠️ Código de golosina no encontrado. Recarga cancelada.")
        return

    cantidad_a_recargar = obtener_entero_valido(f"Ingrese cuántas unidades desea agregar a '{item_golosina[1]}': ")

    if cantidad_a_recargar <= 0:
        print("❌ La cantidad a recargar debe ser mayor que cero.")
        return

    # Realizar la recarga
    item_golosina[2] += cantidad_a_recargar
    print(f"📦 ¡Recarga exitosa! Se agregaron {cantidad_a_recargar} unidades de **{item_golosina[1]}**.")
    print(f"   Nuevo stock total: {item_golosina[2]}")


def apagar_maquina():
    """Opción D: Muestra el informe de ventas y apaga la máquina."""
    print("\n--- 🛑 APAGANDO LA MÁQUINA ---")
    print("--- INFORME DE VENTAS ---")

    if not GOLOSINAS_PEDIDAS:
        print("⚠️ No se registraron ventas en esta sesión.")
        return True # Devuelve True para apagar

    # Recorremos el diccionario de pedidos para mostrar el informe
    total_vendido = 0
    print("Código | Producto | Cantidad Vendida")
    print("-" * 35)
    
    # Recorre el diccionario GOLOSINAS_PEDIDAS: {código: cantidad}
    for codigo_vendido, cantidad in GOLOSINAS_PEDIDAS.items():
        # Buscamos el nombre usando el código
        item = buscar_golosina(codigo_vendido) 
        nombre = item[1] if item else f"Código {codigo_vendido} (Desconocido)"
        
        print(f"{codigo_vendido:<6} | {nombre:<18} | {cantidad}")
        total_vendido += cantidad

    print("-" * 35)
    print(f"⭐ Venta total de la sesión: {total_vendido} unidades.")
    print("¡Máquina apagada con éxito! ¡Hasta pronto! 👋")
    return True # Devuelve True para apagar

# --- 5. FUNCIÓN PRINCIPAL (Main Loop) ---

def main():
    """Bucle principal de ejecución del programa."""
    apagar = False

    while not apagar:
        menu_opcion = input(
            "\n*** MÁQUINA EXPENDEDORA ***\n"
            "A - Pedir Golosinas | B - Mostrar Golosinas | "
            "C - Rellenar Golosinas | D - Apagar Máquina \n"
            "Seleccione una opción: "
        ).upper()

        if menu_opcion == "A":
            pedir_golosina()
        elif menu_opcion == "B":
            mostrar_golosinas()
        elif menu_opcion == "C":
            rellenar_golosinas()
        elif menu_opcion == "D":
            # Si apagar_maquina retorna True, salimos del bucle.
            apagar = apagar_maquina() 
        else:
            print("❌ Opción no válida. Por favor, elija A, B, C o D.")

# --- 6. PUNTO DE ENTRADA (Usando el 'if __name__ == "__main__":') ---

if __name__ == "__main__":
    main()