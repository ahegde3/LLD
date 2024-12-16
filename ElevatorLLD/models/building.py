from models.floor import Floor

class Building:

    def __init__(self, floors):
        self.floors = floors

    def add_floor(self, floor):
        self.floors.append(floor)

    def get_floor(self, floor_no):
        return self.floors[floor_no]

    def get_floors(self):
        return self.floors

    def remove_floor(self, floor_no):
        self.floors.pop(floor_no)        

    def __str__(self):
        return f"{self.name} located at {self.address} has {self.floors} floors"