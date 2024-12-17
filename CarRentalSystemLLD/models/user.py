

class User:
    def __init__(self):
        self.userId = None
        self.userName = None
        self.drivingLicense = None

    def set_user_id(self, userId):
        self.userId = userId

    def get_user_id(self):
        return self.userId

    def set_user_name(self, userName):
        self.userName = userName

    def get_user_name(self):
        return self.userName

    def set_driving_license(self, drivingLicense):
        self.drivingLicense = drivingLicense

    def get_driving_license(self):
        return self.drivingLicense
                    