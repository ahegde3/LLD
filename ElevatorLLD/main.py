from models.floor import Floor
from models.building import Building
from models.direction import Direction

if __name__ == "__main__":

    floor_list = [Floor(1),Floor(2),Floor(3),Floor(4),Floor(5)]

    Building = Building(floor_list)
    floor_list[0].press_button(Direction.UP)
    floor_list[2].press_button(Direction.UP)
    floor_list[3].press_button(Direction.UP)
