def ingresar_estudiantes():
    estudiantes = []
    while True:
        n = int(input("¿Cuántos estudiantes desea ingresar? "))
        if n<=0:
            print('El número no es valido')
            continue
        else:
            break
    for i in range(n):
        nombre = input(f"\nNombre del estudiante {i + 1}: ").title()
        while True:
            nota = float(input("Nota del estudiante: "))
            if 0 <= nota <= 20:  
                break
            else:
                print('Ingrese calificación valida')
            continue
        estudiantes.append((nombre, nota))
    
    return estudiantes

def buscar_estudiante(estudiantes, nombre):
    nombre = nombre.title()
    for estudiante in estudiantes:
        if estudiante[0] == nombre:
            return estudiante[1]
    return None

def ordenar_alfabeticamente(estudiantes):
    for i in range(len(estudiantes)):
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[i][0] > estudiantes[j][0]:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]
    return estudiantes

def mostrar_resultado(estudiantes):
    print("\nLISTA ORDENADA ALFABÉTICAMENTE:")
    for nombre, nota in estudiantes:
        print(f"{nombre}: {nota:.2f}")
    
    nombre_buscar = input("\nIngrese nombre a buscar: ")
    nota = buscar_estudiante(estudiantes, nombre_buscar)
    
    if nota is not None:
        print(f"Nota de {nombre_buscar.title()}: {nota:.2f}")
    else:
        print("Estudiante no encontrado")

def main():
    estudiantes = ingresar_estudiantes()
    
    estudiantes = ordenar_alfabeticamente(estudiantes)
    
    mostrar_resultado(estudiantes)

main()