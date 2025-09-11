from abc import ABC, abstractmethod

# 1)
class Veh:
    def __init__(self, plate, owner):
        self.__plate = plate   
        self.__owner = owner   

    def get_plate(self): return self.__plate
    def get_owner(self): return self.__owner
    def show(self): print("Generic Vehicle")
    def fee(self, hrs): return 0

class Bike(Veh):
    def __init__(self, plate, owner, helmet=True):
        super().__init__(plate, owner); self.helmet = helmet
    def show(self): print(f"Bike {self.get_plate()} ({self.get_owner()}), Helmet={self.helmet}")
    def fee(self, hrs): return 20*hrs


class Car(Veh):
    def __init__(self, plate, owner, seats=4):
        super().__init__(plate, owner); self.seats = seats
    def show(self): print(f"Car {self.get_plate()} ({self.get_owner()}), Seats={self.seats}")
    def fee(self, hrs): return 50*hrs

class SUV(Veh):
    def __init__(self, plate, owner, fourwd=True):
        super().__init__(plate, owner); self.fourwd = fourwd
    def show(self): print(f"SUV {self.get_plate()} ({self.get_owner()}), 4WD={self.fourwd}")
    def fee(self, hrs): return 70*hrs

class Truck(Veh):
    def __init__(self, plate, owner, cap=1000):
        super().__init__(plate, owner); self.cap = cap
    def show(self): print(f"Truck {self.get_plate()} ({self.get_owner()}), Cap={self.cap}kg")
    def fee(self, hrs): return 100*hrs



#2)
class Spot:
    def __init__(self, size): self.size, self.__veh = size, None
    def park(self, v):
        fit = {Bike:["S","M","L","XL"], Car:["M","L","XL"], SUV:["L","XL"], Truck:["XL"]}
        if self.__veh: 
            return False
        if type(v) in fit and self.size in fit[type(v)]:
            self.__veh = v; print(f"{v.get_plate()} in {self.size}"); return True
        return False
    def free(self, hrs):
        if not self.__veh: return None
        v, f = self.__veh, self.__veh.fee(hrs); self.__veh=None
        return v,f
    def status(self):
        return f"{self.size}: {self.__veh.get_plate()}" if self.__veh else f"{self.size}: Empty"

class Lot:
    def __init__(self): self.spots=[]
    def add(self, s): self.spots.append(s)
    def show(self): [print(s.status()) for s in self.spots]
    def park(self,v): return any(s.park(v) for s in self.spots)
    def unpark(self,v,hrs):
        for s in self.spots:
            if v.get_plate() in s.status():
                x=s.free(hrs); print(f"Unpark {x[0].get_plate()}, Fee=₹{x[1]}"); return x[1]
        return 0


# 3)
class Pay(ABC):
    @abstractmethod
    def process(self, amt): pass

class Cash(Pay):
    def process(self, amt): print(f"Paid ₹{amt} by Cash")

class Card(Pay):
    def process(self, amt): print(f"Paid ₹{amt} by Card")

class UPI(Pay):
    def process(self, amt): print(f"Paid ₹{amt} by UPI")


if __name__ == "__main__":
    lot=Lot(); [lot.add(Spot(s)) for s in ["S","M","L","XL"]]

    vs=[Bike("B1","A"), Car("C1","B"), SUV("S1","C"), Truck("T1","D")]
    print("\n-- Vehicles --"); [v.show() for v in vs]

    print("\n-- Park --"); [lot.park(v) for v in vs]; lot.show()

    print("\n-- Unpark + Pay --")
    amt=lot.unpark(vs[1],2)  
    if amt: UPI().process(amt)



