from math import sqrt


class Pedestrian:
    def __init__(self, desire_velocity, initial_coordinates, radii, mass):
        self.desire_velocity = desire_velocity # v_0 - Constant
        self.radii = radii # Radius of the pedestrian in meters
        self.mass = mass # Mass of the pedestrian in kg
        self.norm_velocities = list()  # # list of the normalized x and y velocities of the simulation
        self.places = list() # The velocities for each k interval [ [v_x1, v_y1] , [v_x2, v_y2] ... ]
        self.add_place(initial_coordinates) # Adding the initial Coordination of the pedestrian [x, y] to the places list
        self.velocities = list() # The Coordination for each k interval [ [x1, y1] , [x2, y2] ... ]
        self.add_velocity([0,0]) # Adding the initial velocity (0) to the velocities list
        self.exited = False
        self.escape_time = 0 # the interval k while escaping

    def get_velocities(self):
        return self.velocities

    def get_places(self):
        return self.places

    def get_radii(self):
        return self.radii

    def get_mass(self):
        return self.mass

    def get_desire_velocity(self):
        return self.desire_velocity

    def get_exited(self):
        return self.exited

    def get_velocities(self):
        return self.velocities

    def get_places(self):
        return self.velocities

    def get_curr_place(self):
        return self.places[-1] #returns the current coordinates of the pedestrian (x, y)

    def get_curr_velocity(self):
        return self.velocities[-1] #returns the current velocity of the pedestrian (v_x, v_y)

    def set_desire_velocity(self, desire_velocity):
        self.desire_velocity = desire_velocity

    def set_radii(self, radii):
        self.radii = radii

    def set_mass(self, mass):
        self.mass = mass

    def set_exited(self, exited):
        self.exited = exited

    def add_place(self, place):
        self.places.append(place)

    def add_velocity(self, velocity):
        self.velocities.append(velocity)
        self.norm_velocities.append(sqrt(velocity[0]**2 + velocity[1]**2))

