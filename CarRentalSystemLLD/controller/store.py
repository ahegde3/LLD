from controller.vehicle_inventory_management import VehicleInventoryManagement
from controller.reservation import Reservation

class Store:
    def __init__(self):
        self.store_id = None
        self.inventory_management = None
        self.location = None
        self.reservations= []

    def get_vehciles(self,vehicle_type):
        #TODO: Pending filtering by vehicle type
        return self.inventory_management.get_vehicle()    
    
    def set_vehicles(self, vehicles):
        self.inventory_management = VehicleInventoryManagement(vehicles)

    def create_reservation(self, user,vehicle):
        reservation = Reservation()
        reservation.createReservation(user,vehicle)
        self.reservations.append(reservation)
        return reservation
    
    def complete_reservation(self, reservation):
        #take out the reservation from the list and call complete the reservation method.
        return True