
class ElevatorDisplay:
    def __init__(self):
        self.floor = None
        self.direction = None

    def set_display(self, floor, direction):
        self.floor = floor
        self.direction = direction   

    def show_display(self):
        print(f'Elevator at floor {self.floor} going {self.direction}')