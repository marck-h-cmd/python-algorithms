def ingresar_estudiantes():
    estudiantes = {}
    while True:
        n = int(input("¿Cuántos estudiantes desea ingresar? "))
        if n<=0:
            print('El número no es valido')
            continue
        else:
            break
    for i in range(n):
        nombre = input(f"\nNombre del estudiante {i + 1}: ").title()
        
        if nombre in estudiantes:
            print('Este alumno ya existe')
            continue
        notas=[]
        j=1
        while True:
            nota = float(input(f'Ingrese la nota {j}: '))
            
            if nota < 0:
                break
            if 0 <= nota <= 20:  
                notas.append(nota)
                j+=1
           
        estudiantes[nombre]=notas
    
    return estudiantes

def calcular_promedio(notas):
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)

def mostrar_resultados(estudiantes):
    print("\n" + "="*50)
    print("RESULTADOS DE ALUMNOS")
    print("="*50)
    
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        print(f"{nombre}: {len(notas)} notas - Promedio: {promedio:.2f}")
        
        
def main():
    estudiantes=ingresar_estudiantes()  
    mostrar_resultados(estudiantes)
    
main()