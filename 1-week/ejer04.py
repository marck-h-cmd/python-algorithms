# Usando diccionarios
# Codifica un programa en python que nos permita guardar 
# los nombres de los alumnos
# de una clase y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad
# de notas. Guarda la información en un diccionario 
# cuyas claves serán los nombres de
# los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos 
# que vamos a introducir, pedirá su nombre e
# irá pidiendo sus notas hasta que introduzcamos
# un número negativo. Al final el
# programa nos mostrará la lista de alumnos
# y la nota media obtenida por cada uno de
# ellos.
# Nota: si se introduce el nombre de un alumno
# que ya existe el programa nos dará un
# error.

def ingresar_estudiantes():
    estudiantes = {}
    n = int(input("¿Cuántos estudiantes desea ingresar? "))
    if n<0:
        print('El número no es valido')
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
            if nota <=20 and nota>0:
                notas.append(nota)
                j+=1
           
        estudiantes[nombre]=nota
    
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