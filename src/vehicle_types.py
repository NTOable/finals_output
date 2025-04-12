class Vehicle :
    def __init__(self, name : str, wheels : str, type : str) :
        self.name = name
        self.wheels = wheels
        self.type = type
        self.vehicle = []

    def add_vehicle(self, vehicle) :
        self.vehicle.append(vehicle)

    @staticmethod
    def description() :
        return ("Buses are particularly long, large, and heavy vehicles "
                "that can carry dozens of passengers at the same time.")

class SchoolBus(Vehicle) :
    def info(self) :
        return (f"A {self.name} is a {self.wheels} {self.type}, usually sponsored by or paid by "
                f"their respective schools to drive students to school and back home.")
class HomeBus(Vehicle) :
    def info(self) :
        return (f"A {self.name} is a {self.wheels} {self.type} that has been converted to offer the "
                f"comfort and basic necessities that can be found in common houses whilst on the road.")
class TourBus(Vehicle) :
    def info(self) :
        return (f"A {self.name} is a {self.wheels} {self.type} which serves as the main mode of "
                f"transportation for city tour guides to provide a unique viewing experience while they move around.")

#calling static method
description = Vehicle.description()

#instances
vehicle1 = SchoolBus("School Bus", "6-wheeler", "exclusive-use bus")
vehicle2 = HomeBus("Home Bus", "6-wheeler", "on the road living space bus")
vehicle3 = TourBus("City Bus", "10-wheeler", "double-decker bus")

print(description)

print("Here are some examples: \n")
for vehicle in vehicle1, vehicle2, vehicle3 :
    print(vehicle.info(), "\n")

#Instance checker
print(isinstance(vehicle1, Vehicle)) #True