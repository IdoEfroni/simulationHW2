import pedestrians
import simulation
class Equation:
    def __init__(self, num_of_pedestrians, room):
        self.num_of_pedestrians = num_of_pedestrians
        self.room = room
        simula = simulation(num_of_pedestrians,room)
        simula.place_pedestrians()
