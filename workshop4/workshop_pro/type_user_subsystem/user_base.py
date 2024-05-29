from abc import ABC, abstractmethod

class UserBase(ABC):
    """This class represents a user."""

    @abstractmethod
    def get_all_vehicles(self):
        pass

    @abstractmethod
    def get_by_speed(self):
        pass

    @abstractmethod
    def get_price_by_range(self, min, max):
        pass

    @abstractmethod
    def search_vehicle(self, search):
        pass

class ConcreteUser(UserBase):
    """This class represents a concrete user."""

    def get_all_vehicles(self):
        print("User: Getting all vehicles")

    def get_by_speed(self):
        print("User: Getting vehicles by speed")

    def get_price_by_range(self, min, max):
        print(f"User: Getting vehicles with price range {min} - {max}")

    def search_vehicle(self, search):
        print(f"User: Searching for vehicle {search}")
