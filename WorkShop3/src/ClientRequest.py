from abc import ABC, abstractmethod
from datetime import datetime

class ClientRequest(ABC):
    """This class represents a client request interface."""

    @abstractmethod
    def get_vehicles_info(self):
        """This method gets vehicle information."""
        pass

class RealClientRequest(ClientRequest):
    """This class represents a real client request."""

    def __init__(self, name_engine, type_engine, potency_engine, weight_engine):
        """Constructor of RealClientRequest Class"""
        self.name_engine = name_engine
        self.type_engine = type_engine
        self.potency_engine = potency_engine
        self.weight_engine = weight_engine

    def get_vehicles_info(self):
        """This method gets vehicle information."""
        try:
            with open("vehicles.txt", 'r') as file:
                for line in file:
                    print(line.strip()) 
        except FileNotFoundError:
            print(f"file 'vehicles.txt' doesn't exist.")

class ProxyClientRequest(ClientRequest):
    
    def __init__(self, name_engine, type_engine, potency_engine, weight_engine):
        """Constructor of VehicleProxy Class"""
        self._real_client_request = RealClientRequest(name_engine, type_engine, potency_engine, weight_engine)

    def get_vehicles_info(self):
        """This method gets vehicle information."""
        self.__monitor_start()
        self._real_client_request.get_vehicles_info()
        self.__monitor_end()

    def create(self):
        """This method creates a vehicle entry in the catalog."""
        self.__monitor_start()
        self._real_client_request.create()
        self.__monitor_end()

    
    