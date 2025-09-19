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
        print(f"\nEstudiante {i + 1}:")
        nombre = input("Nombre del estudiante: ")
        
        calificaciones = []
        for j in range(3):
            while True:
                    calificacion = float(input(f"Calificación {j + 1}: "))
                    if 0 <= calificacion <= 20:  
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 0 y 20")
        
        estudiantes.append((nombre, calificaciones))
    
    return estudiantes

def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)

def obtener_promedios_estudiantes(estudiantes):
    promedios = []
    
    for estudiante in estudiantes:
        nombre, calificaciones = estudiante
        promedio = calcular_promedio(calificaciones)
        promedios.append((nombre, promedio))
    
    return promedios

def mostrar_resultados(promedios):
    print("\n" + "="*50)
    print("RESULTADOS DE ESTUDIANTES")
    print("="*50)
    
    for i, (nombre, promedio) in enumerate(promedios, 1):
        print(f"{i}. {nombre}: Promedio = {promedio}")

def main():
    estudiantes = ingresar_estudiantes()
    
    promedios_estudiantes = obtener_promedios_estudiantes(estudiantes)
    
    mostrar_resultados(promedios_estudiantes)
    


main()