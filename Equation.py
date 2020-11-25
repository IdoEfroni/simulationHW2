import Pedestrian
import Simulation
class Equation:

    tau = 0.5

    def __init__(self):
        self.tau = 0.5

    def e_i(self, pedestrian, exit):
        res = list()
        if(exit[0] - pedestrian.get_curr_place()[0] != 0):
            x_curr = (exit[0] - pedestrian.get_curr_place()[0]) / abs(exit[0] - pedestrian.get_curr_place()[0])
        else:
            x_curr = 0
        if (exit[1] - pedestrian.get_curr_place()[1] != 0):
            y_curr = (exit[1] - pedestrian.get_curr_place()[1]) / abs(exit[1] - pedestrian.get_curr_place()[1])
        else:
            y_curr = 0
        res.append(x_curr)
        res.append(y_curr)
        return res # returns the normal direction of movement of the pedestrian [e_i_x, e_i_y]

    # Calculate the force between two pedestrians
    def f_ij(self, pedestrian_1, pedestrian_2):
        return 0 # Relevant for question 2

    # Calculate the force between a pedestrians and a wall
    def f_iw(self, wall, pedestrian):
        return 0 #Relevant for question 2


    def v_i(self, pedestrian,pedestrians,walls,exit):
        res = list()
        res.append(self.calculate_v(pedestrian,pedestrians,walls, pedestrian.get_mass(), pedestrian.get_curr_velocity()[0], pedestrian.get_desire_velocity(),self.e_i(pedestrian,exit)[0]))
        res.append(self.calculate_v(pedestrian, pedestrians, walls, pedestrian.get_mass(), pedestrian.get_curr_velocity()[1],pedestrian.get_desire_velocity(), self.e_i(pedestrian,exit)[1]))
        return res # return the v_i of the interval k of the pedestrian in format of [v_i_x, v_i_y]

    def calculate_v(self,pedestrian, pedestrians, walls, mass, pre_v_i, v_i_0, e_i_0):
        num1 = mass * (pre_v_i * self.tau + 0.01 * v_i_0 * e_i_0)
        sigma_f_ij = 0
        sigma_f_iw = 0
        for p in pedestrians:
            if p != pedestrian:
                sigma_f_ij += self.f_ij(p,pedestrian)

        for w in walls:
                sigma_f_iw += self.f_iw(p,w)

        num2 = 0.01 * self.tau * (sigma_f_ij + sigma_f_iw)
        num3 = mass * (self.tau + 0.01)
        return (num1 + num2) / num3 # returns the v of the pedestrian in one coordinate (v_x OR v_y)


    def r_i(self,pedestrian, pedestrians, walls, exit):
        res = list()
        pre_r_i = pedestrian.get_curr_place() #r_i(k-1)
        v_k = self.v_i(pedestrian, pedestrians, walls, exit)
        pedestrian.add_velocity(v_k)
        res.append(pre_r_i[0] + v_k[0] * 0.01)
        res.append(pre_r_i[1] + v_k[1] * 0.01)
        return res # returns the new coordinates for pedestrian in interval k [x, y]