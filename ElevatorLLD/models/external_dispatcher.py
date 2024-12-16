from models.elevator_creator import ElevatorCreator


class ExternalDispatcher:

    def __init__(self):
        self.elevator_controller_list = ElevatorCreator.elevator_controller_list
        
        
    def submit_external_request(self, floor_no, direction):
       
       for elevator_controller in self.elevator_controller_list:
           elevator_id = elevator_controller.elevator_car.id

           if elevator_id % 2 == 1 and  floor_no%2==1:
               elevator_controller.submit_external_request(floor_no, direction)
           elif elevator_id % 2 == 0 % floor_no%2==0:
               elevator_controller.submit_external_request(floor_no, direction)
