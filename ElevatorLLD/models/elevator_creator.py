from models.elevator_controller import ElevatorController
from models.elevator_car import ElevatorCar

class ElevatorCreator:
    elevator_controller_list = []

    @staticmethod
    def initialize():
        elevator_car1 = ElevatorCar(1)
        controller1 = ElevatorController(elevator_car1)

        elevator_car2 = ElevatorCar(2)
        controller2 = ElevatorController(elevator_car2)

        ElevatorCreator.elevator_controller_list.append(controller1)
        ElevatorCreator.elevator_controller_list.append(controller2)


 # Initialize the static list
ElevatorCreator.initialize()