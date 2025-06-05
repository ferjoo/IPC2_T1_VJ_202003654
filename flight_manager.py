import xml.etree.ElementTree as ET
from typing import Dict, List
from flight import Flight

class FlightManager:
    def __init__(self):
        self.flights: Dict[str, Flight] ={}

    def load_file(self, file_path: str) -> bool:
        try:
            self.flights.clear()
            
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            for flight_elem in root.findall('vuelo'):
                code = flight_elem.find('codigo').text
                
                if code in self.flights:
                    print(f"Error: Ya existe un vuelo con el código {code}")
                    return False
                
                flight = Flight(
                    code=code,
                    origin=flight_elem.find('origen').text,
                    destination=flight_elem.find('destino').text,
                    duration=int(flight_elem.find('duracion').text),
                    airline=flight_elem.find('aerolinea').text
                )
                self.flights[code] = flight
            
            print("Archivo cargado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")
            return False

    def show_flight_details(self, code: str):
        if code in self.flights:
            flight = self.flights[code]
            print("\nDetalle del vuelo:")
            print(f"Código: {flight.code}")
            print(f"Origen: {flight.origin}")
            print(f"Destino: {flight.destination}")
            print(f"Duración: {flight.duration} horas")
            print(f"Aerolínea: {flight.airline}")
        else:
            print(f"No se encontró ningún vuelo con el código {code}")

    def group_by_airline(self):
        airlines: Dict[str, List[str]] = {}
        
        for flight in self.flights.values():
            if flight.airline not in airlines:
                airlines[flight.airline] = []
            airlines[flight.airline].append(flight.code)
        
        print("\nVuelos agrupados por aerolínea:")
        for airline, codes in airlines.items():
            print(f"\n{airline}:")
            for code in codes:
                print(f"- {code}")

    def sort_by_duration(self):
        sorted_flights = sorted(
            self.flights.values(),
            key=lambda x: x.duration,
            reverse=True
        )
        
        print("\nVuelos ordenados por duración (mayor a menor):")
        for flight in sorted_flights:
            print(f"Código: {flight.code}, Duración: {flight.duration} horas") 