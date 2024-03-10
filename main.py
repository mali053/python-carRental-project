from rentals import Rentals
from vehicles import VehiclesMenu
from payment import Payment
off = True
rental = Rentals()
vehicle = VehiclesMenu()
profit = Payment()
while off:
    print("welcome to the vehicles rental")
    choose = input("press:\n1 for taking\n2 for returning\n3 for change prices\n4 to see vehicle report\n5 to see stack"
                   " report\n6 to see profit\n7 for exit")
    if choose == '1':
        rental.taking()
    elif choose == '2':
        rental.returning()
    elif choose == '3':
        vehicle.manager(float(input("Enter the price increase percentage (for example 1.1)")))
    elif choose == '4':
        vehicle.report()
    elif choose == '5':
        rental.report()
    elif choose == '6':
        profit.report()
    elif choose == '7':
        off = False
        print("good bye 😴")

