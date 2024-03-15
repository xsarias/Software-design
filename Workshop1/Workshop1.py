"""
this file contains the first workshop for the software design I course
Author: Xiomara Arias
Date: Mar-15th-2024
"""
class Vehicle:
  """
  this class represents the structure of a vehicle
  """
  #constructor
  def __init__(self, engine:str, chasis:str, model:str, year:str, GasConsumption:float):
    self.engine=engine
    self.chasis=chasis
    self.model=model
    self.year=year
    self.GasConsumption=GasConsumption
  
  def CreateVehicles():
    print("Insert the type of vehicle that you want to create:")
    MessageVehicles="""
    1). Car.
    2). Truck.
    3). Yacht.
    4). Motorcycle.
    5). Regresar.
    """
    print(MessageVehicles)
    op=int(input("Select an option:"))
    while op !=5:
      if op==1:
        
        break
      elif op==2:
        print("gg")
        break
      elif op==3:
        print("gg")
        break
      elif op==4:
        print("gg")
        break
      elif op==5:
        Menu()

class Engine():
  """
  this class can create Engines
  """

  #constructor
  def init(self, EngineName:str, EngineType:int, EnginePotency:int, EngineWeight:int):
    self.EngineName=EngineName
    self.EngineType=EngineType
    self.EnginePotency=EnginePotency
    self.EngineWeight=EngineWeight

  def CreateEngine():
    print("Insert the characteristic of the new Engine")
    EngineName=input("Insert Engine Name: ")
    print("Select the Engine Type: A or B")
    EngineType=input("Insert Engine Type")
    EnginePotency=input("Insert Engine Potency")
    EngineWeight=iput("Insert Engine Weight")
    Engine.CalculateVehicleGas( EngineType, EnginePotency,EngineWeight);
    EngineNew=Engine(EngineName, EngineType, EnginePotency,EngineWeight)
  def CalculateVehicleGas(EngineType, EnginePotency,EngineWeight):
    VehicleGas=1.1*EnginePotency+0.2*EngineWeight

class Car(Vehicle):
  """
  this class represent the car structure
  """
  #constructor
  def init(self, engine:str, chasis:str, model:str, year:str, GasConsumption:float):
    super().__init__(engine, chasis, model, year, GasConsumption)
  def CreateCar():
    print("Insert the characteristic of the new Car")
    

class Truck(Vehicle):
  """
  this class represent the truck structure
  """
  #constructor
  def init(self, engine:str, chasis:str, model:str, year:str, GasConsumption:float):
    super().__init__(engine, chasis, model, year, GasConsumption)


class Yacht(Vehicle):
  """
  this class represent the yacht structure
  """
  #constructor
  def init(self, engine:str, chasis:str, model:str, year:str, GasConsumption:float):
    super().__init__(engine, chasis, model, year, GasConsumption)


class Motorcycle(Vehicle):
  """
  this class represent the car structure
  """
  #constructor
  def init(self, engine:str, chasis:str, model:str, year:str, GasConsumption:float):
    super().__init__(engine, chasis, model, year, GasConsumption)




def Menu():
  MESSAGE="""
  >>>> Vehicles Constructor Company <<<<

  1). Create vehicle.
  2). Create engine.
  3). Show Vehicles Registered.
  4). Find Vehicle.
  5). Exit.
  """

  print(MESSAGE)
  op=int(input("Select an option:"))
  while op !=5:
    if op==1:
      Vehicle.CreateVehicles()
    elif op==2:
      Engine.CreateEngine()
    elif op==3:
      Vehicle.
    elif op==4:
      print("gg")
    print(MESSAGE)
    op=int(input("Select an option:"))


Menu()