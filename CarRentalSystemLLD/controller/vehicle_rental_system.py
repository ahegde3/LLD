from controller.store import Store
class VehicleRentalSystem:
    def __init__(self, stores, users):
        self.store_list = stores
        self.user_list = users

    def get_store(self, location) -> Store:
        # based on location, we will filter out the Store from store_list.
        return self.store_list[0]

    # add_users

    # remove_users

    # add_stores

    # remove_stores