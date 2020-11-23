class Pedestrian:
    def __init__(self, desire_velocity, place, radii, mass, real_velocity):
        self.desire_velocity = desire_velocity
        self.place = place
        self.radii = radii
        self.mass = mass
        self.real_velocity = real_velocity

    def get_desire_velocity(self):
        return self.desire_velocity

    def get_place(self):
        return self.place

    def get_radii(self):
        return self.radii

    def get_mass(self):
        return self.mass

    def get_real_velocity(self):
        return self.real_velocity

    def set_desire_velocity(self, desire_velocity):
        self.desire_velocity = desire_velocity

    def set_place(self, place):
        self.place = place

    def set_radii(self, radii):
        self.radii = radii

    def set_mass(self, mass):
        self.mass = mass

    def set_real_velocity(self, real_velocity):
        self.real_velocity = real_velocity
