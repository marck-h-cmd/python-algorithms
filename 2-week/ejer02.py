import pandas as pd
import matplotlib.pyplot as plt
from ejer01 import Estudiante, ingresar_estudiante

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        
    def exportar_datos(self, filename):
        try:
            if len(self.estudiantes) == 0:
                raise ValueError("No hay estudiantes en el curso.")
            
            data = {
                "Nombre": [est.nombre for est in self.estudiantes],
                "Promedio": [est.calcular_promedio() for est in self.estudiantes]
            }
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Datos exportados a {filename}")
            return df
            
        except ValueError as e:
            print(f"Error: {e}")
            return pd.DataFrame()  
    
    def graficar_histograma_promedios(self, df):
        try:
            if df.empty:
                raise ValueError("El DataFrame está vacío.")
            
            plt.figure(figsize=(10, 6))
            plt.hist(df['Promedio'], bins=10, alpha=0.7, edgecolor='black')
            plt.title(f"Histograma de promedios - {self.nombre}")
            plt.xlabel("Promedio")
            plt.ylabel("Número de estudiantes")
            plt.grid(True)
            plt.show()
            
        except ValueError as e:
            print(f"Error al graficar: {e}")
    
            
def main():
    curso_nombre = input("Ingrese el nombre del curso: ")
    curso = Curso(curso_nombre)
    
    while True:
        estudiante = ingresar_estudiante()
        curso.agregar_estudiante(estudiante)
        
        otro = input("¿Desea agregar otro estudiante? (s/n): ").lower()
        if otro != 's':
            break
    
   
    df = curso.exportar_datos("estudiantes.csv")
    
    if not df.empty:
        curso.graficar_histograma_promedios(df) 
         

if __name__ == "__main__":
    main()