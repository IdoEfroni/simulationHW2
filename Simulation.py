import numpy as np
from Pedestrian import Pedestrian
from Equation import Equation

class Simulation:
    def __init__(self, num_of_pedestrians, room, random_places):
        self.room = room
        self.random_places = random_places
        self.num_of_pedestrians = num_of_pedestrians
        self.list_pedestrians = list()
        self.place_pedestrians(self.random_places)

    def exist_place(self, place_x, place_y):
        for p in self.list_pedestrians:
            if abs(p.get_curr_place()[0] - place_x) < p.get_radii() or abs(p.get_curr_place()[1] - place_y) < p.get_radii():
                return True
        return False

    def place_pedestrians(self, random_places):
        room_length = self.room.get_length()
        room_width = self.room.get_width()
        if random_places:
            for i in range(self.num_of_pedestrians):
                r = np.random.uniform(0.5 / 2, 0.7 / 2)
                place_x = np.random.uniform(0 + r, room_width - r)
                place_y = np.random.uniform(0 + r, room_length - r)

                while self.exist_place(place_x, place_y): # Check if the pedestrian is coliding with other pedestrians. If so, generate new coordinates
                    r = np.random.uniform(0.5 / 2, 0.7 / 2)
                    place_x = np.random.randint(0 + r, room_width - r)
                    place_y = np.random.randint(0 + r, room_length - r)
                new_pedestrian = Pedestrian(1.5, [place_x, place_y], r, np.random.uniform(60, 90))  # Create new pedestrian
                self.list_pedestrians.append(new_pedestrian)
        else:
            r = np.random.uniform(0.5 / 2, 0.7 / 2)
            place_x = room_length/2
            place_y = room_width/2
            new_pedestrian = Pedestrian(1.5, [place_x, place_y], r, np.random.uniform(60, 90))  # Create new pedestrian
            self.list_pedestrians.append(new_pedestrian)


    def get_list_pedestrians(self):
        return self.list_pedestrians

    def step_pedestians(self,list_pedestrians,walls,exit):
        e = Equation()
        for p in list_pedestrians:
            if p.get_exited() is False:
                p.add_place(e.r_i(p,list_pedestrians,walls,exit))
                p.escape_time += 1
            if(abs(p.get_curr_place()[0] - exit[0]) < 0.09 and abs(p.get_curr_place()[1] - exit[1]) < 0.09):
                p.set_exited(True)
