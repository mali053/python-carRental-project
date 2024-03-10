class Vehicles:
    def __init__(self, name, cost, seat):
        self.carName = name
        self.cost = cost
        self.numOfSeats = seat


class Motorcycle(Vehicles):
    def __init__(self, name, cost, seat, ):
        Vehicles.__init__(self, name, cost, seat)
        self.helmet = 2


class VehiclesMenu:

    def __init__(self):
        self.pricesDict = {}
        with open("carPrices.txt") as carPrices:
            one_car = carPrices.readline().split(",")
            for line in one_car:
                part = line.split(":")
                vehicle = part[0]
                price = part[1]
                self.pricesDict[vehicle] = price
        self.cars = [
            Vehicles(name="car", cost=self.pricesDict["car"], seat=5),
            Vehicles(name="minBus", cost=self.pricesDict["minBus"], seat=20),
            Motorcycle(name="motorcycle", cost=self.pricesDict["motorcycle"], seat=1)
        ]

    def find_car(self, car_name):
        for item in self.cars:
            if item.carName == car_name:
                return item
        return None

    def manager(self, increase):
        self.cars = [Vehicles(car.carName, int(car.cost) * int(increase), car.numOfSeats) for car in self.cars if
                     car.carName != "motorcycle"]
        self.cars.append(Motorcycle(name="motorcycle", cost=int(self.pricesDict["motorcycle"]) * int(increase), seat=1))

    def report(self):
        print("report about price of car and num of seats")
        for car in self.cars:
            print(car.carName + " price: " + str(car.cost) + " num of seats: " + str(car.numOfSeats))
