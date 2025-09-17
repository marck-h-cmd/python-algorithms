def ingresar_estudiantes():
    estudiantes = []
    n = int(input("¿Cuántos estudiantes desea ingresar? "))
    
    for i in range(n):
        nombre = input(f"\nNombre del estudiante {i + 1}: ").title()
        nota = float(input("Nota del estudiante: "))
        estudiantes.append((nombre, nota))
    
    return estudiantes

def buscar_estudiante(estudiantes, nombre):
    nombre = nombre.title()
    for estudiante in estudiantes:
        if estudiante[0] == nombre:
            return estudiante[1]
    return None

def main():
    estudiantes = ingresar_estudiantes()
    
    estudiantes.sort(key=lambda x: x[0])
    
    print("\nLISTA ORDENADA ALFABÉTICAMENTE:")
    for nombre, nota in estudiantes:
        print(f"{nombre}: {nota:.2f}")
    
    nombre_buscar = input("\nIngrese nombre a buscar: ")
    nota = buscar_estudiante(estudiantes, nombre_buscar)
    
    if nota is not None:
        print(f"Nota de {nombre_buscar.title()}: {nota:.2f}")
    else:
        print("Estudiante no encontrado")

main()