from abc import ABC, abstractmethod
from xml.etree.ElementTree import canonicalize

class Vehicle(ABC):
    
    def __init__(self, maxspeed, mileage, capacity):
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.capacity = capacity


    class vehicle:
        
        pass

class Bus(Vehicle):

    def __init__(self, maxspeed, mileage, capacity):
        super().__init__(maxspeed, mileage, capacity)
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.capacity = capacity

bus1 = Vehicle("75", "10000", "50")

print(getattr(bus1, "capacity"))   