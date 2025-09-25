import numpy as np
import matplotlib.pyplot as plt

class Estudiante:
    def __init__(self, nombre,notas):
        self.nombre = nombre
        self.notas = notas
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Promedio de notas: {self.calcular_promedio():.2f}")
        print(f"Nota Maxima: {self.nota_maxima():.2f}")
        print(f"Nota Minima: {self.nota_minima():.2f}")
        
    def calcular_promedio(self):
        try:
            if len(self.notas) == 0:
                raise ValueError("La lista de notas está vacía.")
            return np.mean(self.notas)
        except ValueError as e:
            print(e)
            return None
    def nota_maxima(self):  
        try:
            if len(self.notas) == 0:
                raise ValueError("La lista de notas está vacía.")
            return max(self.notas)
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    def nota_minima(self):  
        try:
            if len(self.notas) == 0:
                raise ValueError("La lista de notas está vacía.")
            return min(self.notas)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def graficar_notas(self):
        try:
            if len(self.notas) == 0:
                raise ValueError("No hay notas para graficar.")
            
            plt.figure(figsize=(10, 5))
            plt.hist(self.notas, bins=10, alpha=0.7, edgecolor='black')
            plt.title(f"Distribución de notas de {self.nombre}")
            plt.xlabel("Rango de notas")
            plt.ylabel("Frecuencia")
            plt.grid(True)
            plt.show()
        except ValueError as e:
            print(f"Error al graficar: {e}")
        
def ingresar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
    
    while True:
        try:
            n = int(input("¿Cuántas notas desea ingresar? "))
            if n <= 0:
                print("El número debe ser positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    for i in range(n):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} (0-20): "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return Estudiante(nombre, notas)

def main():
    estudiante = ingresar_estudiante()
    estudiante.mostrar_informacion()
    estudiante.graficar_notas()
    
if __name__ == "__main__":
    main()