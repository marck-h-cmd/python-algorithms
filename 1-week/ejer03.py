def ingresar_libros():
    libros = []
    while True:
        n = int(input("¿Cuántos libros desea ingresar? "))
        if n<=0:
            print('El número no es valido')
            continue
        else:
            break
    for i in range(n):
        titulo = input(f"\nTitulo del libro {i + 1}: ").title()
        autor = input("Autor del libro: ")
        while True:
                year_publicacion = int(input("Año de publicación: "))
                if year_publicacion > 0: 
                    break
                else:
                    print("El año debe ser un número positivo.")
        libros.append((titulo, autor,year_publicacion))
    
    return libros

def obtener_nueva_lista(libros):
    nueva_lista=[]
    for libro in libros:
        if libro[2]>2000:
            nueva_lista.append(libro)
    return nueva_lista

def mostrar_libros(libros):
    print("La nueva lista de libros publicados después de 2000 es: ")
    print("=" * 80)
    print(f"{'No.':<4} {'Título':<25} {'Autor':<25} {'Año':<6}")
    print("-" * 80)
    
    if not libros:
        print("No hay libros para mostrar.")
        return
    
    for i, (titulo, autor, year_publicacion) in enumerate(libros, 1):
        print(f"{i:<4} {titulo:<25} {autor:<25} {year_publicacion:<6}")
        
def main():
    libros = ingresar_libros()
    
    nueva_lista = obtener_nueva_lista(libros)
    
    mostrar_libros(nueva_lista)
    
    
   
main()