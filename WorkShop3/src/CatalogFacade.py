from datetime import datetime
from abc import ABC
from typing import List
from ClientRequest import ClientRequest, ProxyClientRequest
from vehicles import Vehicle

# Base class for applications
class CatalogFacade(ABC):
    """This class represents an catalog facade"""
    
    def run(self):
        """This method runs the application."""


# Concrete application classes
class User(CatalogFacade):
    """This class represents an application catalog for users."""
    def __init__(self, user_name, vehicles):
        super().__init__()
        self.user_name = user_name
        self.vehicles = vehicles

    # override
    def run(self):
        '''this method runs the aplication for users'''
         # ==================================== MENU
        MESSAGE = f"""
            >>> '{self.user_name}' WELCOME TO CATALOG OF VEHICLES<<
            1). See vehicles.
            2). Search vehicles.
            """
        print(MESSAGE)
        option = int(input("->Please, choise an option: "))
        while option != 3:
            if option == 1:
                break
            elif option == 2:
                break    


class Admin(CatalogFacade):
    """This class represents an application catalog for admins."""
    # ==================================== MENU
    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name
        self.client_request = ClientRequest()
        self.proxy_client_request = ProxyClientRequest()
        self.vehicles = []

    def get_all_vehicles(self) -> List[Vehicle]:
        return self.vehicles

    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        return [vehicle for vehicle in self.vehicles if min_price <= vehicle.price <= max_price]

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    # override
    def run(self):
        '''this method runs the aplication for users'''
        MESSAGE = f"""
            >>> '{self.user_name}' WELCOME TO CATALOG OF VEHICLES<<
            1). See vehicles.
            2) Search vehicles.
            3). Create vehicles.
            4). Update vehicles.
            5). Delete vehicles.
            6). Exit.
            """
        print(MESSAGE)
        option = int(input("->Please, choise an option: "))
        while option != 6:
            if option == 1:
                print("All vehicles:")
                for vehicle in self.vehicles:
                    print(vehicle)
            elif option == 2:
                pass
            elif option == 3:
                # Create vehicles
                self.proxy_client_request.create()
                
            elif option == 4:
                # Update vehicles
                pass
            elif option == 5:
                # Delete vehicles
                pass

# Decorator class for monitoring
class CatalogDecorator(CatalogFacade):
    """This class represents a catalog decorator for each type of user"""

    def __init__(self, catalog: CatalogFacade):
        """
        Constructor of the CatalogDecorator class.

        Args:
            catalog(CatalogFacade): A catalog to decorate.
        """
        self.wrapped = catalog

    # override
    def run(self):
        # Here the decorator wraps original application 
        #self.__monitor_start()
        self.wrapped.run()
        
    def __monitor_start(self):
        """This method logs the start of the monitoring."""
        print(f"== Monitoring started at: {datetime.now()}")

    def __monitor_end(self):
        """This method logs the end of the monitoring."""
        print(f"== Monitoring ended at: {datetime.now()}\n")
