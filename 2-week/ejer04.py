import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Tienda:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas = pd.DataFrame(columns=["Producto", "Cantidad", "Precio"])
        
    def registrar_venta(self, producto, cantidad, precio):
        try:
            if cantidad <= 0 or precio < 0:
                raise ValueError("Cantidad debe ser mayor que 0 y precio no puede ser negativo.")
            
            nueva_venta = pd.DataFrame({
                "Producto": [producto],
                "Cantidad": [cantidad],
                "Precio": [precio]
            })
            
            if self.ventas.empty:
                self.ventas = nueva_venta
            else:
                self.ventas = pd.concat([self.ventas, nueva_venta], ignore_index=True)
                
            print(f"Venta registrada: {producto}, Cantidad: {cantidad}, Precio: {precio}")
        
        except ValueError as e:
            print(f"Error al registrar venta: {e}")
        
    
    def total_ventas(self):
        try:
            if self.ventas.empty:
                raise ValueError("No hay ventas registradas.")
            total = (self.ventas["Cantidad"] * self.ventas["Precio"]).sum()
            return total
        except ValueError as e:
            print(f"Error al calcular total de ventas: {e}")
            return 0
        
    def producto_mas_vendido(self):
        try:
            if self.ventas.empty:
                raise ValueError("No hay ventas registradas.")
            producto_vendido = self.ventas.groupby("Producto")["Cantidad"].sum()
            producto_mas_vendido = producto_vendido.idxmax()
            cantidad_total = producto_vendido.sum()
            if cantidad_total == 0:
                raise ValueError("No se han vendido productos.")
            return producto_mas_vendido, cantidad_total
        except ValueError as e:
            print(f"Error al determinar el producto más vendido: {e}")
            return None, 0
    def promedio_ventas_por_transaccion(self):
        try:
            if self.ventas.empty:
                raise ValueError("No hay ventas registradas en la tienda")
            
            montos_transacciones = self.ventas['Cantidad'] * self.ventas['Precio']
            
            promedio = np.mean(montos_transacciones)
            return promedio
            
        except ValueError as e:
            print(f"Error: {e}")
            return 0
        
    def generar_grafico_ventas_por_producto(self):
        try:
            if self.ventas.empty:
                raise ValueError("No hay ventas registradas para generar el gráfico")
            
            ventas_por_producto = self.ventas.groupby('Producto').apply(
                lambda x: (x['Cantidad'] * x['Precio']).sum(), include_groups=False
            ).sort_values(ascending=False)
            
            plt.figure(figsize=(12, 6))
            ventas_por_producto.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.7)
            
            plt.title(f'Ventas por Producto - {self.nombre}')
            plt.xlabel('Producto')
            plt.ylabel('Ventas Totales (s/.)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            
            for i, v in enumerate(ventas_por_producto):
                plt.text(i, v + 0.01 * max(ventas_por_producto), f's/.{v:.2f}', 
                        ha='center', va='bottom')
            
            plt.tight_layout()
            plt.show()
            
        except ValueError as e:
            print(f"Error al generar gráfico: {e}")
            
    def mostrar_estadisticas(self):
        print(f"\n=== ESTADÍSTICAS DE {self.nombre.upper()} ===")
        
        try:
            if self.ventas.empty:
                raise ValueError("No hay ventas registradas")
            
            total = self.total_ventas()
            producto_mas, cantidad = self.producto_mas_vendido()
            promedio = self.promedio_ventas_por_transaccion()
            
            print(f"Total vendido: s/.{total:.2f}")
            print(f"Producto más vendido: {producto_mas} ({cantidad} unidades)")
            print(f"Promedio por transacción: s/.{promedio:.2f}")
            print(f"Número total de transacciones: {len(self.ventas)}")
            
        except ValueError as e:
            print(f"Error: {e}")
            
def main():
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    tienda = Tienda(nombre_tienda)
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar venta")
        print("2. Mostrar estadísticas")
        print("3. Generar gráfico de ventas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                producto = input("Nombre del producto: ")
                cantidad = int(input("Cantidad vendida: "))
                precio = float(input("Precio unitario: "))
                
                tienda.registrar_venta(producto, cantidad, precio)
                
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio")
        
        elif opcion == '2':
            tienda.mostrar_estadisticas()
        
        elif opcion == '3':
            tienda.generar_grafico_ventas_por_producto()
        
        elif opcion == '4':
            print("Fin del programa")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()