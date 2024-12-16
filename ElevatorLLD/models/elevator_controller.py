import heapq
from models.direction import Direction
# from elevator_car import ElevatorCar 

class ElevatorController:
    def __init__(self, elevator_car):
        self.elevator_car = elevator_car
        self.up_min_pq = []
        self.down_max_pq = []

    def submit_external_request(self, floor, direction):
        if direction == Direction.DOWN:
            heapq.heappush(self.down_max_pq, -floor)  # Use negative values for max-heap
        else:
            heapq.heappush(self.up_min_pq, floor)

    def submit_internal_request(self, floor):
        # Implementation for internal request
        pass

    def control_elevator(self):
        while True:
            if self.elevator_car.elevator_direction == Direction.UP:
                # Implementation for controlling the elevator when moving up
                pass
            elif self.elevator_car.elevator_direction == Direction.DOWN:
                # Implementation for controlling the elevator when moving down
                pass