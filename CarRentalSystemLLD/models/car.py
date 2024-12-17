class Car:
    def __init__(self):
        self.vehicle_id = None
        self.vehicle_type = None

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_vehicle_type(self):
        return self.vehicle_type