#definimos funciones que vamos a usar

def pedir_nota(prompt):
    """Pide una nota por consola y valida que sea un número entre 0 y 10."""
    while True:
        entrada = input(prompt).strip()
        # Permitir coma decimal y convertir a float
        entrada = entrada.replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("  -> Entrada inválida. Escribe un número (ej. 7 o 7.5).")
            continue
        if 0 <= nota <= 10:
            return nota
        else:
            print("  -> La nota debe estar entre 0 y 10.")

def calcular_promedio_materias(materias):
    """Recibe la lista de materias (cada una con su nota final) y devuelve el promedio general."""
    finales = [m[3] for m in materias if m[3] is not None]
    if not finales:
        return 0.0
    return sum(finales) / len(finales)

def cargar_notas_alumno(nombre, materias_template):
    """
    Crea una copia de la plantilla de materias y solicita 2 notas por materia.
    Devuelve la lista de materias con notas cargadas.
    """
    # Hacemos copia para no modificar la plantilla original
    materias = [row.copy() for row in materias_template]
    print("\n" + "="*50)
    print(f"Cargando notas para: {nombre}")
    for i, materia in enumerate(materias):
        print(f"\nMateria: {materia[0]}")
        n1 = pedir_nota("  Nota 1: ")
        n2 = pedir_nota("  Nota 2: ")
        final = (n1 + n2) / 2
        materias[i][1] = n1
        materias[i][2] = n2
        materias[i][3] = round(final, 2)
        print(f"  Nota Final: {materias[i][3]}")
    return materias

def mostrar_materias(materias):
    """Imprime la tabla de materias con sus notas (formato simple)."""
    print("\nLista de materias y notas:")
    print(f"{'Materia':15} {'Nota1':>6} {'Nota2':>6} {'Final':>6}")
    print("-"*40)
    for m in materias:
        print(f"{m[0]:15} {m[1]:6.2f} {m[2]:6.2f} {m[3]:6.2f}")

def materia_con_mayor_calificacion(materias):
    """Devuelve la materia con la nota final más alta."""
    # Asumimos que todas las materias tienen nota final ya cargada
    mejor = max(materias, key=lambda x: x[3])
    return mejor  # devuelve la fila: [nombre_materia, nota1, nota2, final]

def main():
    # Diccionario de alumnos: legajo -> "Apellido Nombre"
    alumnos = {
        60902: "Rodolfo Fernandez",
        61654: "Luis Gomez",
        61852: "Andrea Pereira",
        61754: "Juan Cruz Gonzales",
    }

    # Plantilla de materias (col: Materia, Nota1, Nota2, NotaFinal)
    materias_template = [
        ["Ciencias", None, None, None],
        ["Historia", None, None, None],
        ["Geografia", None, None, None],
        ["Matematicas", None, None, None],
        ["Fisica", None, None, None],
    ]

    # Lista donde guardaremos [nombre_alumno, promedio_general]
    notasFinales = []

    # Proceso principal: para cada alumno pedir notas, calcular y guardar
    for legajo, nombre in alumnos.items():
        materias = cargar_notas_alumno(nombre, materias_template)
        mostrar_materias(materias)

        mejor = materia_con_mayor_calificacion(materias)
        print(f"\n-> Materia con la calificación más alta para {nombre}: {mejor[0]} ({mejor[3]})")

        promedio_general = calcular_promedio_materias(materias)
        promedio_general = round(promedio_general, 2)
        notasFinales.append([nombre, promedio_general])
        print(f"Promedio general de {nombre}: {promedio_general}")
        print("="*50 + "\n")

    # Al finalizar todos los alumnos: determinar quién tiene mejor promedio
    mejor_alumno = max(notasFinales, key=lambda x: x[1])
    print("Resultados finales (promedios generales):")
    for fila in notasFinales:
        print(f"  {fila[0]:25} => {fila[1]}")
    print(f"\nEl alumno con mejor promedio es: {mejor_alumno[0]} con {mejor_alumno[1]}")

if __name__ == "__main__":
    main()
