import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

class Clima:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = None
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            if not os.path.exists(self.archivo_csv):
                raise FileNotFoundError(f"El archivo '{self.archivo_csv}' no existe")
            
            self.datos = pd.read_csv(self.archivo_csv)
            
            columnas_requeridas = ['fecha', 'temperatura']
            for columna in columnas_requeridas:
                if columna not in self.datos.columns:
                    raise ValueError(f"El archivo debe contener la columna '{columna}'")
            
            self.datos['fecha'] = pd.to_datetime(self.datos['fecha'])
            
            if self.datos['temperatura'].isna().any():
                self.datos['temperatura'].fillna(self.datos['temperatura'].mean(), inplace=True)
            
            print(f"Datos cargados exitosamente: {len(self.datos)} registros")
            
        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.datos = pd.DataFrame()
        except pd.errors.EmptyDataError:
            print("Error: El archivo está vacío")
            self.datos = pd.DataFrame()
        except pd.errors.ParserError:
            print("Error: El archivo tiene formato incorrecto o datos corruptos")
            self.datos = pd.DataFrame()
        except Exception as e:
            print(f"Error inesperado al cargar datos: {e}")
            self.datos = pd.DataFrame()
    
    def calcular_temperatura_media(self):
        try:
            if self.datos.empty:
                raise ValueError("No hay datos climáticos cargados")
            
            temperatura_media = np.mean(self.datos['temperatura'])
            return temperatura_media
            
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    def calcular_desviacion_estandar(self):
        try:
            if self.datos.empty:
                raise ValueError("No hay datos climáticos cargados")
            
            desviacion = np.std(self.datos['temperatura'])
            return desviacion
            
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    def detectar_valores_atipicos(self, metodo='iqr'):
        try:
            if self.datos.empty:
                raise ValueError("No hay datos climáticos cargados")
            
            temperaturas = self.datos['temperatura']
            atipicos = []
            
            if metodo == 'iqr':
                Q1 = np.percentile(temperaturas, 25)
                Q3 = np.percentile(temperaturas, 75)
                IQR = Q3 - Q1
                limite_inferior = Q1 - 1.5 * IQR
                limite_superior = Q3 + 1.5 * IQR
                
                atipicos = self.datos[
                    (temperaturas < limite_inferior) | (temperaturas > limite_superior)
                ]
                
            elif metodo == 'zscore':
                z_scores = np.abs((temperaturas - np.mean(temperaturas)) / np.std(temperaturas))
                atipicos = self.datos[z_scores > 3]
            
            return atipicos
            
        except ValueError as e:
            print(f"Error: {e}")
            return pd.DataFrame()
    
    def graficar_temperaturas_tiempo(self):
        try:
            if self.datos.empty:
                raise ValueError("No hay datos para graficar")
            
            plt.figure(figsize=(14, 8))
            
            plt.subplot(2, 1, 1)
            plt.plot(self.datos['fecha'], self.datos['temperatura'], 
                    color='red', alpha=0.7, linewidth=1, label='Temperatura diaria')
            
            temp_media = self.calcular_temperatura_media()
            if temp_media is not None:
                plt.axhline(y=temp_media, color='blue', linestyle='--', 
                           label=f'Temperatura media: {temp_media:.2f}°C')
            
            atipicos = self.detectar_valores_atipicos()
            if not atipicos.empty:
                plt.scatter(atipicos['fecha'], atipicos['temperatura'], 
                           color='red', s=50, zorder=5, label='Valores atípicos')
            
            plt.title(f'Evolución de Temperaturas - {os.path.basename(self.archivo_csv)}')
            plt.ylabel('Temperatura (°C)')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            
            plt.subplot(2, 1, 2)
            plt.hist(self.datos['temperatura'], bins=30, alpha=0.7, 
                    color='lightblue', edgecolor='black')
            
            desviacion = self.calcular_desviacion_estandar()
            if desviacion is not None:
                plt.axvline(x=temp_media, color='red', linestyle='--', 
                           label=f'Media: {temp_media:.2f}°C')
                plt.axvline(x=temp_media + desviacion, color='orange', linestyle=':', 
                           label=f'+1σ: {temp_media + desviacion:.2f}°C')
                plt.axvline(x=temp_media - desviacion, color='orange', linestyle=':', 
                           label=f'-1σ: {temp_media - desviacion:.2f}°C')
            
            plt.title('Distribución de Temperaturas')
            plt.xlabel('Temperatura (°C)')
            plt.ylabel('Frecuencia')
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.show()
            
        except ValueError as e:
            print(f"Error al graficar: {e}")
    
    def mostrar_estadisticas(self):
        print(f"\n=== ESTADÍSTICAS CLIMÁTICAS ===")
        
        try:
            if self.datos.empty:
                raise ValueError("No hay datos climáticos cargados")
            
            temp_media = self.calcular_temperatura_media()
            desviacion = self.calcular_desviacion_estandar()
            atipicos = self.detectar_valores_atipicos()
            
            print(f"Período analizado: {self.datos['fecha'].min().date()} a {self.datos['fecha'].max().date()}")
            print(f"Total de registros: {len(self.datos)}")
            print(f"Temperatura media: {temp_media:.2f}°C")
            print(f"Desviación estándar: {desviacion:.2f}°C")
            print(f"Temperatura máxima: {self.datos['temperatura'].max():.2f}°C")
            print(f"Temperatura mínima: {self.datos['temperatura'].min():.2f}°C")
            print(f"Valores atípicos detectados: {len(atipicos)}")
            
            if not atipicos.empty:
                print("\nValores atípicos:")
                for idx, fila in atipicos.iterrows():
                    print(f"  {fila['fecha'].date()}: {fila['temperatura']:.2f}°C")
                    
        except ValueError as e:
            print(f"Error: {e}")

def crear_csv():
    fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    np.random.seed(42)
    
    base_temp = 15 + 10 * np.sin(2 * np.pi * np.arange(len(fechas)) / 365)
    variacion = np.random.normal(0, 5, len(fechas))
    temperaturas = base_temp + variacion
    
    indices_atipicos = np.random.choice(len(fechas), 10, replace=False)
    temperaturas[indices_atipicos] += np.random.choice([-15, 15], 10)
    
    datos = pd.DataFrame({
        'fecha': fechas,
        'temperatura': temperaturas,
        'humedad': np.random.randint(30, 90, len(fechas))
    })
    
    datos.to_csv('datos_climaticos.csv', index=False)
    print("Archivo de creado: 'datos_climaticos.csv'")
    return 'datos_climaticos.csv'

def main():
    archivo = 'datos_climaticos.csv'
    
    if not os.path.exists(archivo):
        print("Creando archivo...")
        archivo = crear_csv()
    
    clima = Clima(archivo)
    
    if not clima.datos.empty:
        clima.mostrar_estadisticas()
        clima.graficar_temperaturas_tiempo()

if __name__ == "__main__":
    main()