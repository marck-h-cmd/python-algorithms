#Ingresar una lista con la información de n libros 
# donde cada elemento es una tupla
#que contiene (título, autor, año de publicación).
# Obtener una nueva lista de libros
# publicados después de 2000.

def ingresar_libros():
    libros = []
    n = int(input("¿Cuántos libros desea ingresar? "))
    
    for i in range(n):
        titulo = input(f"\nTitulo del libro {i + 1}: ").title()
        autor = input("Autor del libro: ")
        year_publicacion = int(input('Ingrese el año de publicación'))
        libros.append((titulo, autor,year_publicacion))
    
    return libros

def obtener_nueva_lista(libros):
    nueva_lista=[]
    for libro in libros:
        if libro[2]>2000:
            nueva_lista.append(libro)
    return nueva_lista

def main():
    libros = ingresar_libros()
    
    nueva_lista = obtener_nueva_lista(libros)
    
    print("La nueva lista de libros publicados después de 2000 es: ",nueva_lista[:])
main()