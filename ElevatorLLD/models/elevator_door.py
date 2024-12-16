class ElevatorDoor:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True
        print("Opening the elevator door")

    def close(self):
        self.is_open = False
        print("Closing the elevator door")