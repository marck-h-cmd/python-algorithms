def mostrar_menu():
    print("\n" + "="*40)
    print("AGENDA TELEFÓNICA")
    print("="*40)
    print("1. Añadir/Modificar contacto")
    print("2. Buscar contactos")
    print("3. Borrar contacto")
    print("4. Listar todos los contactos")
    print("5. Salir")
    print("="*40)

def añadir_modificar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ").strip().title()
    
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - Teléfono: {agenda[nombre]}")
        modificar = input("¿Desea modificar el teléfono? (s/n): ").lower()
        if modificar == 's':
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ").strip()
            agenda[nombre] = nuevo_telefono
            print("Teléfono actualizado correctamente.")
    else:
        telefono = input("Ingrese el número de teléfono: ").strip()
        agenda[nombre] = telefono
        print("Contacto añadido correctamente.")

def buscar_contactos(agenda):
    cadena = input("Ingrese la cadena de búsqueda: ").strip().title()
    encontrados = False
    
    print(f"Contactos que comienzan con '{cadena}':")
    for nombre, telefono in agenda.items():
        if nombre.startswith(cadena):
            print(f"  {nombre}: {telefono}")
            encontrados = True
    
    if not encontrados:
        print("No se encontraron contactos con ese criterio.")

def borrar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a borrar: ").strip().title()
    
    if nombre in agenda:
        confirmar = input(f"¿Está seguro de borrar a {nombre}? (s/n): ").lower()
        if confirmar == 's':
            del agenda[nombre]
            print("Contacto borrado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Contacto no encontrado.")

def listar_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return
    
    print("\n" + "="*30)
    print("LISTA DE CONTACTOS")
    print("="*30)
    
    for i, (nombre, telefono) in enumerate(agenda.items(), 1):
        print(f"{i:2d}. {nombre:<20} : {telefono}")

def main():
    agenda = {}
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        if opcion == 1:
            añadir_modificar_contacto(agenda)
        elif opcion == 2:
            buscar_contactos(agenda)
        elif opcion == 3:
            borrar_contacto(agenda)
        elif opcion == 4:
            listar_contactos(agenda)
        elif opcion == 5:
            print("Fin del menu")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()