"""
This file has some classes related to the implementation of an Abstract Factory Pattern Design..

Author: Carlos Sierra - cavirguez@udistrital.edu.co
"""

from abc import ABC, abstractmethod

from .engines import ElectricEngine, GasEngine,HybridEngine 


class AbstractEngineFactory(ABC):
    """
    This class is an abstract factory to create both gas and electric engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an electric engine.
        create_gas_engine -> GasEngine: This method create a gas engine.
    """

    @abstractmethod
    def create_electric_engine(self) -> ElectricEngine:
        """
        This method create an electric engine.

        Returns:
            An electric engine object.
        """

    @abstractmethod
    def create_gas_engine(self) -> GasEngine:
        """
        This method create a gas engine.

        Returns:
            A gas engine object.
        """

    @abstractmethod
    def create_hybrid_engine(self) -> HybridEngine:
        """
        This method create a hybrid engine.

        Returns:
            A hybrid engine object.
        """

class HighEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create expensive versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an expensive electric engine.
        create_gas_engine -> GasEngine: This method create an expensive gas engine.
        create_hybride_engine -> HybridEngine: This method create an expensive hybride engine.

    """

    def create_electric_engine(self) -> ElectricEngine:
        return ElectricEngine(
            torque=180,
            maximum_speed=300,
            dimenssions="200x200x200",
            power=200,
            stability="high",
            weight=100.9,
        )

    def create_gas_engine(self) -> GasEngine:
        return GasEngine(
            torque=210,
            maximum_speed=400,
            dimenssions="210x200x250",
            power=250,
            stability="medium",
            weight=120.5,
        )
    def create_hybrid_engine(self) -> HybridEngine:
        return HybridEngine(
            torque=210,
            maximum_speed=400,
            dimenssions="200x150x250",
            power=250,
            stability="medium",
            weight=120.5,
            electric_power=110.3
        )

class LowEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create cheap versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create a cheap electric engine.
        create_gas_engine -> GasEngine: This method create a cheap gas engine.
    """

    def create_electric_engine(self) -> ElectricEngine:
        return ElectricEngine(
            torque=90,
            maximum_speed=100,
            dimenssions="100x100x100",
            power=50,
            stability="low",
            weight=63.4,
        )

    def create_gas_engine(self) -> GasEngine:
        return GasEngine(
            torque=100,
            maximum_speed=150,
            dimenssions="110x100x150",
            power=100,
            stability="low",
            weight=80.5,
        )
    def create_hybrid_engine(self) -> HybridEngine:
        return HybridEngine(
            torque=110,
            maximum_speed=130,
            dimenssions="50x100x50",
            power=140,
            stability="low",
            weight=70.5,
            electric_power=80.5
        )