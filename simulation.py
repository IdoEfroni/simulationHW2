import numpy as np
import pedestrians


class Simulation:
    def __init__(self, num_of_pedestrians, room):
        self.room = room
        self.num_of_pedestrians = num_of_pedestrians
        self.list_pedestrians = list()

    def exist_place(self, place_x, place_y):
        for p in self.list_pedestrians:
            if abs(p.place[0] - place_x) < p.get_radii or abs(p.place[1] - place_y) < p.get_radii:
                return True
        return False

    def place_pedestrians(self):
        room_length = self.room.get_length()
        room_width = self.room.get_width()

        for i in range(self.num_of_pedestrians):
            place_x = np.randint(0 + r, room_width - r)
            place_y = np.randint(0 + r, room_length - r)
            r = np.random.uniform(0.5, 0.7) / 2

            while self.exist_place(place_x, place_y):
                place_x = np.randint(0 + r, room_width - r)
                place_y = np.randint(0 + r, room_length - r)

            self.list_pedestrians.append(pedestrians(1.5, [place_x, place_y], r), np.randint(60, 90), 0)
