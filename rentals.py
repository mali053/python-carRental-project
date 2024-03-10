from vehicles import VehiclesMenu
from datetime import datetime
from payment import Payment

pay = Payment()


class Rentals:
    def __init__(self):
        self.carCount = {
            "car": 30,
            "minBus": 10,
            "motorcycle": 40
        }
        self.user_details_by_vehicles = {
            "car": {},
            "minBus": {},
            "motorcycle": {}
        }

    def manager(self):
        self.carCount = {k: v * 2 for k, v in self.carCount.items()}

    def is_available(self, carName):
        """Checking whether the requested vehicle is available"""
        if self.carCount[carName] > 0:
            return True
        return False

    def get_items(self):
        available_items = []
        for item in VehiclesMenu().cars:
            if self.is_available(item.carName):
                available_items.append(item.carName)
        return available_items

    def taking(self):
        items = "/".join(self.get_items())
        selectedCar = input(f"we have now in the stok: {items} what would you like")
        id_number = input("please enter your ID")
        name = input("please enter your name")
        current_time = datetime.now()
        try:
            self.user_details_by_vehicles[selectedCar][id_number] = [name, current_time]
            self.carCount[selectedCar] -= 1
            vehicle = VehiclesMenu().find_car(selectedCar)
            if hasattr(vehicle, "helmet"):
                print(f"Note that the motorcycle comes with {vehicle.helmet} helmets, make sure to return them")
            print("Your order has been accepted, have a nice trip and have a good day!")
        except Exception as e:
            print(f"error: {e}")

    def returning(self):
        selectedCar = input("which car would you like to return(car/ minBus/ motorcycle)")
        id_number = input("please enter your ID")
        vehicle = VehiclesMenu().find_car(selectedCar)
        try:
            user = self.user_details_by_vehicles[selectedCar][id_number]
            print(f"hello {user[0]} Hope you had a safe trip")
            time_difference = int((datetime.now() - user[1]).total_seconds() / 60)
            pay.do_payment(vehicle.cost, time_difference)
            self.user_details_by_vehicles[selectedCar].pop(id_number)
        except:
            print("the car not found")

    def report(self):
        print("report how many cars have now in the stack")
        for k, v in self.carCount.items():
            print(k + ": have " + str(v) + " cars")
