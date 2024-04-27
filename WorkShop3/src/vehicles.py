from engines import Engine

class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    vehicles = []

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str = None,
        trade: str = None,
        combustible_type: str = None,
        length: float = None,
        weight: float = None,
    ):
        self.engine = engine
        self.chassis = chassis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type
        self.length = length
        self.weight = weight

    def __str__(self):
        return f"Vehicle: {self.model} - {self.year} - {self.price} - \
            {self.consumption} - {self.engine} - {self.chassis}"


def create_vehicle(type_vehicle: str):
    """
    This method lets create a new vehicle and add it to the
    catalog.

    Parameters:
    - type_vehicle (str): The type of the vehicle
    """
    chassis = input("Write the chassis of the vehicle (A or B):")
    if chassis not in ["A", "B"]:
        raise ValueError("Error: Chassis wrote is wrong. Must be A or B.")
    model = input("Write the model of the vehicle: ")
    year_ = int(
        input("Write the year of the vehicle (should be greater or equal than 2000): ")
    )
    if year_ < 2000:
        raise ValueError("Error. Year is not in a valid range.")
    engine_name = input("Write the name of the motor for the vehicle: ")

    try:
        # Aquí deberías crear una instancia de la clase Engine utilizando el nombre del motor
        engine = Engine()  # Reemplaza esto con la forma correcta de crear un objeto Engine
        vehicle_args = {
            "engine": engine,
            "chassis": chassis,
            "model": model,
            "year": year_,
            "consumption": 0,  # Placeholder for consumption calculation
        }

        if type_vehicle == "car":
            transmission = input("Write the transmission of the car: ")
            trade = input("Write the trade of the car: ")
            combustible_type = input("Write the combustible type of the car: ")
            vehicle_args.update({
                "transmission": transmission,
                "trade": trade,
                "combustible_type": combustible_type,
            })
        elif type_vehicle == "truck":
            vehicle_args.update({
                "length": float(input("Write the length of the truck: ")),
                "weight": float(input("Write the weight of the truck: ")),
            })
        elif type_vehicle == "yatch":
            vehicle_args.update({
                "length": float(input("Write the length of the yatch: ")),
                "weight": float(input("Write the weight of the yatch: ")),
                "trade": input("Write the trade of the yatch: "),
            })
        elif type_vehicle == "motorcycle":
            pass  # No additional attributes for motorcycle

        vehicle_obj_new = Vehicle(**vehicle_args)
        Vehicle.vehicles.append(vehicle_obj_new)  # Accede a la lista de vehículos a través de la clase Vehicle
    except Exception as e:
        print(f"Error: {e}.")


def search_by_year(year_: int) -> list:
    """
    This method makes a search of all vehicles of a specific
    year.

    Parameters:
    - year (int): Year to filter
    """
    return [vehicle for vehicle in Vehicle.vehicles if vehicle.year == year_]


def search_by_potency(potency_: float) -> list:
    """
    This method makes a search of vehicles based on the potency
    of the engine of the vehicle.

    Parameters:
    - potency_ (float): Potency to filter
    """
    return [vehicle for vehicle in Vehicle.vehicles if vehicle.engine.power == potency_]
