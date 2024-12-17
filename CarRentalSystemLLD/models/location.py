

class Location:
    def __init__(self, pincode, city, state, country, address=None):
        self.address = address
        self.pincode = pincode
        self.city = city
        self.state = state
        self.country = country