from abc import ABC, abstractmethod
from datetime import datetime

class ClientRequest(ABC):
    """This class represents a client request interface."""

    @abstractmethod
    def get_vehicles_info(self):
        """This method gets vehicle information."""
        pass

class RealClientRequest(ClientRequest):
    def __init__(self, name_engine, type_engine, potency_engine, weight_engine):
        """Constructor of ProxyClientRequest Class"""
        self.name_engine = name_engine
        self.type_engine = type_engine
        self.potency_engine = potency_engine
        self.weight_engine = weight_engine
    """This class represents a real client request."""

    def get_vehicles_info(self):
        """This method gets vehicle information."""
        try:
            with open("vehicles.txt", 'r') as file:
                for line in file:
                    print(line.strip()) 
        except FileNotFoundError:
            print(f"file 'vehicles.txt' doesn't exist.")

class ProxyClientRequest(ClientRequest):
    """This class represents a proxy client request."""
    
    def __init__(self, name_engine, type_engine, potency_engine, weight_engine):
        """Constructor of ProxyClientRequest Class"""
        self.name_engine = name_engine
        self.type_engine = type_engine
        self.potency_engine = potency_engine
        self.weight_engine = weight_engine
    
    def create(self):
        """This method creates a vehicle entry in the catalog."""
        try:
            with open("vehicles.txt", "a") as file:
                file.write(f"Name Engine: {self.name_engine}, Type Engine: {self.type_engine}, "
                           f"Potency Engine: {self.potency_engine}, Weight Engine: {self.weight_engine}\n")
            print("Vehicle information successfully saved.")
        except (IOError, PermissionError) as e:
            print(f"Error writing to vehicles.txt: {e}")
    
    def get_vehicles_info(self):
        """This method gets vehicle information."""
        try:
            with open("vehicles.txt", 'r') as file:
                for line in file:
                    print(line.strip())  
        except FileNotFoundError:
            print(f"file 'vehicles.txt' doesn't exist.")

    def __monitor_start(self):
        """This method logs the start of the monitoring."""
        print(f"== Monitoring started at: {datetime.now()}")

    def __monitor_end(self):
        """This method logs the end of the monitoring."""
        print(f"== Monitoring ended at: {datetime.now()}\n")
