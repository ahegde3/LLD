from models.internal_dispatcher import InternalDispatcher

class InternalButton:

    def __init__(self):
        self.dispather =  InternalDispatcher()
        self.available_buttons = [1,2,3,4,5,6,7,8,9,10]
        self.button_selected= None

    
    def press_button(self,destination,elevator_car):

        if destination in self.available_buttons:
            self.button_selected = destination
            self.dispather.submit_internal_request(elevator_car,destination)
        else:
            print("Invalid floor number")
