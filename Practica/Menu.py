# --- Clases de Demostración (asumidas) ---
class Ingrediente:
    def __init__(self, nombre, cantidad, unidadDeMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadDeMedida = unidadDeMedida

class Plato:
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.lista_de_ingredientes = []

    def agregar_ingredientes(self, ingrediente):
        self.lista_de_ingredientes.append(ingrediente)

# ------------------------------------------

class MenuRestaurant:

    def __init__(self):
        self.platos = []

    def agregar_platos(self, dato):
        self.platos.append(dato)

    def validar_plato(self, plato_nombre):
        """Verifica si un plato ya existe en el menú."""
        for ob in self.platos:
            if plato_nombre.upper() == ob.nombreCompleto.upper():
                return True
        return False
    
    def validar_ingrediente(self, ingrediente_nombre, instancia_plato):
        """Verifica si un ingrediente ya está en el plato actual."""
        for ob in instancia_plato.lista_de_ingredientes:
            if ingrediente_nombre.upper() == ob.nombre.upper():
                return True
        return False

    # --- NUEVAS FUNCIONES AUXILIARES ---

    def _obtener_entrada_no_vacia(self, prompt, mensaje_error="Error, valor vacío. Intente de nuevo."):
        """Garantiza que la entrada del usuario no esté vacía."""
        while True:
            valor = input(prompt).strip()
            if valor:
                return valor
            print(f"❌ {mensaje_error}")

    def _obtener_flotante_valido(self, prompt):
        """Garantiza que la entrada sea un número flotante (precio/cantidad)."""
        while True:
            temp = self._obtener_entrada_no_vacia(prompt)
            try:
                return float(temp)
            except ValueError:
                print("❌ Error, ingrese un valor numérico válido.")

    def _obtener_si_no_valido(self, prompt):
        """Garantiza que la entrada sea SI o NO."""
        while True:
            opcion = self._obtener_entrada_no_vacia(prompt).upper()
            if opcion in ["SI", "NO"]:
                return opcion
            print("❌ Error, solo se permite SI/NO.")

    def _solicitar_datos_plato(self):
        """Solicita y valida los datos base de un nuevo plato."""
        print("\n--- 📝 Carga de Nuevo Plato ---")

        # 1. Nombre del Plato
        while True:
            nombrecompleto = self._obtener_entrada_no_vacia("Ingrese el nombre del plato: ")
            if self.validar_plato(nombrecompleto):
                print("❌ Error, el plato ya se encuentra en el menú.")
            else:
                break
        
        # 2. Precio
        precio = self._obtener_flotante_valido("Ingrese el precio: $")
        
        # 3. ¿Es bebida?
        es_bebida_str = self._obtener_si_no_valido("¿Es bebida? SI/NO ")
        esbebida = (es_bebida_str == "SI")
        
        return nombrecompleto, precio, esbebida

    def _solicitar_ingredientes(self, plato_instancia):
        """Solicita los ingredientes para un plato (si no es bebida)."""
        
        while True:
            print(f"\n--- 🥕 Ingredientes para {plato_instancia.nombreCompleto} ---")
            
            # 1. Nombre del Ingrediente
            while True:
                nombre = self._obtener_entrada_no_vacia("Ingrese el nombre del Ingrediente: ")
                if self.validar_ingrediente(nombre, plato_instancia):
                    print("❌ Error, el plato ya tiene ese ingrediente.")
                else:
                    break
            
            # 2. Cantidad y Unidad de Medida
            cantidad = self._obtener_flotante_valido("Ingrese la cantidad: ")
            unidadmedida = self._obtener_entrada_no_vacia("Ingrese la unidad de medida (ej. 'gr', 'ml', 'unid'): ")

            # Crear y agregar instancia de Ingrediente
            instancia_ingrediente = Ingrediente(nombre, cantidad, unidadmedida)
            plato_instancia.agregar_ingredientes(instancia_ingrediente)
            print(f"✅ Ingrediente '{nombre}' agregado.")

            # Preguntar por otro ingrediente
            opcion1 = self._obtener_si_no_valido("¿Desea cargar otro ingrediente? SI/NO ")
            if opcion1 == "NO":
                break

    def _mostrar_menu(self):
        """Imprime la estructura final del menú."""
        print("\n" + "="*30)
        print("------- 📋 MENÚ FINAL DEL RESTAURANTE 📋-------") 
        print("="*30) 
        
        if not self.platos:
            print("El menú está vacío.")
            return

        for o in self.platos:
            print(f"""\n**{o.nombreCompleto.upper()}**
Precio: $ {o.precio:.2f}""")
            
            if not o.esBebida:
                print("Ingredientes:")
                print(f"{'Nombre':<15} {'Cantidad':<10} {'Unidad de Medida':<20}")
                print("-" * 45)
                for p in o.lista_de_ingredientes:
                    print(f" {p.nombre:<14} {p.cantidad:<10} {p.unidadDeMedida:<20} ")
            print("-" * 30)

    # --- MÉTODO PRINCIPAL REFACTORIZADO ---

    def Main(self):
        """Bucle principal para la carga de platos."""
        while True:
            # 1. Solicitar y validar datos del plato
            nombrecompleto, precio, esbebida = self._solicitar_datos_plato()
            
            # 2. Crear instancia y agregar al menú
            instancia_plato = Plato(nombrecompleto, precio, esbebida)
            self.agregar_platos(instancia_plato)
            print(f"🎉 Plato '{nombrecompleto}' agregado al menú.")

            # 3. Solicitar ingredientes (si no es bebida)
            if not esbebida:
                self._solicitar_ingredientes(instancia_plato)
            
            # 4. Preguntar por otro plato
            opcion2 = self._obtener_si_no_valido("\n¿Desea cargar otro plato? SI/NO ")
            if opcion2 == "NO":
                break

        # 5. Mostrar el menú final
        self._mostrar_menu()
    
# --- Ejecución ---
if __name__ == "__main__":
    instanciaMain = MenuRestaurant()
    instanciaMain.Main()