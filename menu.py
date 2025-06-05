def show_menu():
    print("\n=== MENÚ DE GESTIÓN DE VUELOS ===")
    print("1. Cargar Archivo")
    print("2. Detalle de vuelo específico")
    print("3. Agrupar vuelos por aerolínea")
    print("4. Ordenar por duración (mayor a menor)")
    print("5. Salir")
    return input("Seleccione una opción: ")

def handle_menu_option(option: str, flight_manager):
    if option == "1":
        file_path = input("Ingrese la ruta del archivo XML: ")
        flight_manager.load_file(file_path)
    
    elif option == "2":
        code = input("Ingrese el código del vuelo: ")
        flight_manager.show_flight_details(code)
    
    elif option == "3":
        flight_manager.group_by_airline()
    
    elif option == "4":
        flight_manager.sort_by_duration()
    
    elif option == "5":
        print("¡Hasta luego!")
        return False
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
    
    return True 