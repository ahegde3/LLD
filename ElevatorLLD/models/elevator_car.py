from models.elevator_display import ElevatorDisplay
from models.internal_button import InternalButton
from models.elevator_state import ElevatorState
from models.direction import Direction
from models.elevator_door import ElevatorDoor

class ElevatorCar:
    def __init__(self,id):
        self.id = id
        self.display = ElevatorDisplay()
        self.internal_buttons = InternalButton()
        self.elevator_state = ElevatorState.IDLE
        self.current_floor = 0
        self.elevator_direction = Direction.UP
        self.elevator_door =  ElevatorDoor()

    def show_display(self):
        self.display.show_display()

    def press_button(self, destination):
        self.internal_buttons.press_button(destination, self)


    def set_display(self):
        self.display.set_display(self.current_floor, self.elevator_direction)


    def move_elevator(self, dir, destination_floor):
        start_floor = self.current_floor
        if dir == Direction.UP:
            for i in range(start_floor, destination_floor + 1):
                self.current_floor = i
                self.set_display()
                self.show_display()
                if i == destination_floor:
                    return True

        if dir == Direction.DOWN:
            for i in range(start_floor, destination_floor - 1, -1):
                self.current_floor = i
                self.set_display()
                self.show_display()
                if i == destination_floor:
                    return True

        return False    

