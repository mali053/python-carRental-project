multiplication = lambda x, y: x * y


class Payment:
    CURRENCY = "₪"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"the profit is: {self.CURRENCY}{self.profit}")

    def do_payment(self, costCar, minutes):
        try:
            cost = int(multiplication(int(costCar), int(minutes))) / 60
            self.make_payment(cost)
            print(f"the amount to be paid is {self.CURRENCY}{cost}")
            self.money_received = 0
            self.money_received = float(input("please insert coins"))
            while float(self.money_received) < float(cost):
                self.money_received += float((input(f"insert more {float(cost) - float(self.money_received)} money👻😒")))
            if float(self.money_received) > float(cost):
                print(f"take change {self.CURRENCY}{float(self.money_received) - float(cost)}")
            else:
                print("thank you and goodbye!! we would love to see you again😘")

        except:
            print(f"There is no need to pay to take the vehicle for at least a minute")

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        if self.money_received >= cost:
            self.profit += cost
            return True
        return False
