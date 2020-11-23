import numpy as np
import pedestrians
class Simulation:
    def __init__(self, room, num_of_pedestrians):
        self.room = room
        self.num_of_pedestrians = num_of_pedestrians
        self.list_pedestrians = list()

    def place_pedestrians(self):
        room_length = self.room.get_length()
        room_width = self.room.get_width()
        place_list  =list();
        for i in range(self.num_of_pedestrians):
            r = np.random.uniform(0.5, 0.7) / 2
            flag = True
            while (flag):
                place_x = np.randint(0 + r,room_width-r)
                place_y = np.randint(0+ r, room_length-r)
                flag2 =
                for p in self.list_pedestrians:
                    if abs(p.place[0]-place_x)<p.get_radii or abs(p.place[1]-place_y)<p.get_radii:
                        continue




            self.list_pedestrians.append(pedestrians(1.5,,r),np.randint(60,100),0)
