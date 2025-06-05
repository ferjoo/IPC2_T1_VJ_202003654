from flight_manager import FlightManager
from menu import show_menu, handle_menu_option

def main():
    flight_manager = FlightManager()
    
    while True:
        option = show_menu()
        if not handle_menu_option(option, flight_manager):
            break

if __name__ == "__main__":
    main()
