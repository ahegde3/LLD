from models.car import Car
from models.vehicle_type import VehicleType
from models.user import User
from models.location import Location
from models.bill import Bill
from controller.store import Store
from controller.vehicle_rental_system import VehicleRentalSystem
from controller.payment import Payment


def add_vehicles():
    vehicles = []

    vehicle1 = Car()
    vehicle1.set_vehicle_id(1)
    vehicle1.set_vehicle_type(VehicleType.CAR)

    vehicle2 = Car()
    vehicle2.set_vehicle_id(2)
    vehicle2.set_vehicle_type(VehicleType.CAR)

    vehicles.append(vehicle1)
    vehicles.append(vehicle2)

    return vehicles

def add_users():
    users = []

    user1 = User()
    user1.set_user_id(1)

    users.append(user1)
    return users

def add_stores(vehicles):
    stores = []

    store1 = Store()
    store1.store_id = 1
    store1.set_vehicles(vehicles)

    stores.append(store1)
    return stores

if __name__ == '__main__':
    users = add_users()
    vehicles = add_vehicles()
    stores = add_stores(vehicles)

    rental_system = VehicleRentalSystem(stores, users)

    # 0. User comes
    user = users[0]

    # 1. user search store based on location
    location = Location(403012, "Bangalore", "Karnataka", "India")
    store = rental_system.get_store(location)

    # 2. get All vehicles you are interested in (based upon different filters)
    store_vehicles = store.get_vehicles(VehicleType.CAR)

    # 3. reserving the particular vehicle
    reservation = store.create_reservation(store_vehicles[0], users[0])

    # 4. generate the bill
    bill = Bill(reservation)

    # 5. make payment
    payment = Payment()
    payment.pay_bill(bill)

    # 6. trip completed, submit the vehicle and close the reservation
    store.complete_reservation(reservation.reservation_id)

