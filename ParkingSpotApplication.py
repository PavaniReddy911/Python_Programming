from abc import ABC, abstractmethod
#1)
class Vehicle:
    def __init__(self,license_plate,owner_name):
        self.__license_plate = license_plate   
        self.__owner_name = owner_name         
    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print("Generic Vehicle")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=1000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Capacity: {self.max_load_capacity}kg")

    def calculate_parking_fee(self, hours):
        return 100 * hours


#2)
class ParkingSpot:
    def __init__(self, size):
        self.__size = size
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        if self.__vehicle is not None:
            print("Spot already occupied")
            return False

        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            self.__vehicle = vehicle
        elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            self.__vehicle = vehicle
        elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            self.__vehicle = vehicle
        elif isinstance(vehicle, Truck) and self.__size == "XL":
            self.__vehicle = vehicle
        else:
            print("Vehicle does not fit this spot")
            return False

        print(f"Vehicle {vehicle.get_license_plate()} parked in spot {self.__size}")
        return True

    def remove_vehicle(self, hours):
        if self.__vehicle is None:
            print("No vehicle in this spot")
            return None
        fee = self.__vehicle.calculate_parking_fee(hours)
        v = self.__vehicle
        self.__vehicle = None
        return v, fee

    def show_status(self):
        if self.__vehicle:
            return f"Spot {self.__size}: Occupied by {self.__vehicle.get_license_plate()}"
        return f"Spot {self.__size}: Empty"

#3)
class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(spot.show_status())

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return True
        print("No suitable spot found")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.show_status().endswith(vehicle.get_license_plate()):
                v, fee = spot.remove_vehicle(hours)
                print(f"Unparked {v.get_license_plate()} | Fee = ₹{fee}")
                return fee
        print("Vehicle not found in lot")
        return 0

#4)
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")


#5)
if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot("S"))
    lot.add_spot(ParkingSpot("M"))
    lot.add_spot(ParkingSpot("L"))
    lot.add_spot(ParkingSpot("XL"))

    vehicles = [
        Bike("B123", "Alice"),
        Car("C456", "Bob"),
        SUV("S789", "Charlie"),
        Truck("T999", "David")
    ]

    print("\n--- Vehicle Display ---")
    for v in vehicles:
        v.display()

    print("\n--- Parking Vehicles ---")
    for v in vehicles:
        lot.park_vehicle(v)

    lot.show_spots()

    print("\n--- Unparking & Payments ---")
    fee = lot.unpark_vehicle(vehicles[1], 2) 
    if fee:
        pay = UPIPayment()
        pay.process_payment(fee)
