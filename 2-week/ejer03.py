import numpy as np
import matplotlib.pyplot as plt

class SimuladorDados:
    def __init__(self, num_lanzamientos):
        if num_lanzamientos <= 0:
            raise ValueError("El número de lanzamientos debe ser mayor que 0")
        self.num_lanzamientos = num_lanzamientos
        self.resultados = np.array([])
        
    def lanzar_dados(self):
        self.resultados = [np.random.randint(1, 7) + np.random.randint(1, 7) for _ in range(self.num_lanzamientos)]
    
    def calcular_media(self):
        if len(self.resultados) == 0:
            raise ValueError("No se han lanzado los dados aún")
        return np.mean(self.resultados)
    
    def calcular_varianza(self):
        if len(self.resultados) == 0:
            raise ValueError("No se han lanzado los dados aún")
        return np.var(self.resultados)
    
    def calcular_distribucion_frecuencias(self):
        if len(self.resultados) == 0:
            raise ValueError("No se han lanzado los dados aún")
        
        valores_unicos, conteos = np.unique(self.resultados, return_counts=True)
        frecuencias = dict(zip(valores_unicos, conteos))
        
        for i in range(2, 13):
            if i not in frecuencias:
                frecuencias[i] = 0
        
        return frecuencias
    
    def graficar_frecuencias(self):
        if len(self.resultados) == 0:
            raise ValueError("No hay datos para graficar")
        
        frecuencias = self.calcular_distribucion_frecuencias()
        
        resultados_ordenados = sorted(frecuencias.keys())
        conteos_ordenados = [frecuencias[key] for key in resultados_ordenados]
        
        plt.figure(figsize=(10, 6))
        plt.bar(resultados_ordenados, conteos_ordenados, 
                color='lightblue', edgecolor='black', alpha=0.7)
        
        plt.title(f'Distribución de Frecuencias - {self.num_lanzamientos} lanzamientos')
        plt.xlabel('Suma de los dados')
        plt.ylabel('Frecuencia')
        plt.xticks(range(2, 13))
        plt.grid(axis='y', alpha=0.3)
        
        for i, v in enumerate(conteos_ordenados):
            plt.text(resultados_ordenados[i], v + 0.1, str(v), 
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
        
    def mostrar_resultados(self):
        if len(self.resultados) == 0:
            raise ValueError("No se han lanzado los dados aún")
        
        media = self.calcular_media()
        varianza = self.calcular_varianza()
        frecuencias = self.calcular_distribucion_frecuencias()
        
        print(f"\nResultados de la simulación de {self.num_lanzamientos} lanzamientos de dos dados:")
        print(f"Media: {media:.2f}")
        print(f"Varianza: {varianza:.2f}")
        print("Frecuencia de resultados:")
        for resultado in range(2, 13):
            print(f"  {resultado}: {frecuencias.get(resultado, 0)}")

  
def main():
    while True:
        try:
            n = int(input("¿Cuántos lanzamientos de dos dados desea simular? "))
            simulador = SimuladorDados(n)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
    simulador.lanzar_dados()
    
    simulador.mostrar_resultados()
        
    simulador.graficar_frecuencias()
        
if __name__ == "__main__":
    main()