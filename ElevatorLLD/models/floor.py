from models.external_dispatcher import ExternalDispatcher       

class Floor:
    
    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.external_dispatcher = ExternalDispatcher()
   
    def press_button(self, direction):
        self.external_dispatcher.submit_external_request(self.floor_no, direction)
