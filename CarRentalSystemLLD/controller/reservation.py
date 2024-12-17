from models.reservation_type import ReservationType
from models.reservation_status import ReservationStatus

class Reservation:
    def __init__(self):
        self.reservation_id = None
        self.user = None
        self.vehicle = None
        self.booking_date = None
        self.date_booked_from = None
        self.date_booked_to = None
        self.from_timestamp = None
        self.to_timestamp = None
        self.pick_up_location = None
        self.drop_location = None
        self.reservation_type = None
        self.reservation_status = None
        self.location = None

    def create_reserve(self, user, vehicle):
        # generate new id
        self.reservation_id = 12232
        self.user = user
        self.vehicle = vehicle
        self.reservation_type = ReservationType.DAILY
        self.reservation_status = ReservationStatus.SCHEDULED

        return self.reservation_id