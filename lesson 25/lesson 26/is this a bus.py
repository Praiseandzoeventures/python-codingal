class vehicle:
    def __init__(self,name,max_speed,milleage):
        self.name=name
        self.max_speed=max_speed
        self.milleage=milleage
        
class Bus(vehicle):
    pass
school_bus=Bus("school Volvo", i80 ,12)
print("vehicle name:",school_bus.name, "speed:",school_bus.max_speed,"Milleage:",school_bus.milleage)