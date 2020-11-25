import time

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from Room import Room
from Simulation import Simulation
import pygame
pygame.init()

scale = 33



# Set up the drawing window


running = True


def draw_pedestrians(screen):

    pedestians_to_draw = new_simulation.get_list_pedestrians()
    for p in pedestians_to_draw:
        if p.get_exited() is False:
            pygame.draw.circle(screen, (0, 0, 255), (int(p.get_curr_place()[0] * scale), int(p.get_curr_place()[1] * scale)), int(p.get_radii() * scale))



def show_graph():
    id = 1
    for p in new_simulation.get_list_pedestrians():
        velocities = p.norm_velocities[0::50]
        k = list()
        for i in range(len(velocities)):
            k.append(i * 0.01 * 50)
        plt.plot(k, velocities, color='green', linestyle='dashed', linewidth=0.5,
                 marker='o', markerfacecolor='blue', markersize=5)

        # naming the x axis
        plt.xlabel('Seconds')
        # naming the y axis
        plt.ylabel('Velocity')

        # giving a title to my graph
        plt.title('Pedestrian {} Velocities Until Escape'.format(id))
        id += 1
        # function to show the plot
        #plt.show()

def check_if_all_escaped():
    for p in new_simulation.get_list_pedestrians():
        if not p.get_exited():
            return False
    return True

def get_max_escape_time_in_current_simulation():
    max = 0
    for p in new_simulation.get_list_pedestrians():
        if max < p.escape_time:
            max = p.escape_time
    return max

def ex_1_a(running):
    while running:
        if check_if_all_escaped():
            show_graph()
            running = False

        screen.fill((255, 255, 255))
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white

        pygame.draw.circle(screen, (0, 255, 0), (int(new_room.get_dest()[0] * scale), int(new_room.get_dest()[1] * scale)), int(0.2 * scale))
        # Flip the display
        draw_pedestrians(screen)
        new_simulation.step_pedestians(new_simulation.get_list_pedestrians(),[],new_room.get_dest())
        pygame.display.flip()
        time.sleep(0.01)

def ex_1_b(running):
    while running:
        if check_if_all_escaped():
            show_graph()
            escape_intervals.append(get_max_escape_time_in_current_simulation() * 0.01)
            running = False


        # screen.fill((255, 255, 255))
        # # Did the user click the window close button?
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #
        # # Fill the background with white
        #
        # pygame.draw.circle(screen, (0, 255, 0), (int(new_room.get_dest()[0] * scale), int(new_room.get_dest()[1] * scale)), int(0.2 * scale))
        # # Flip the display
        # draw_pedestrians(screen)
        new_simulation.step_pedestians(new_simulation.get_list_pedestrians(),[],new_room.get_dest())
        # pygame.display.flip()
        # time.sleep(0.00000001)


#new_room = Room(15, 15, [0, 15/ 2])
#new_simulation = Simulation(1,new_room,False)
#screen = pygame.display.set_mode([new_room.get_length() * scale, new_room.get_width() * scale])
#ex_1_a(running)

new_room = Room(15, 15, [0, 15/ 2])
screen = pygame.display.set_mode([new_room.get_length() * scale, new_room.get_width() * scale])
escape_intervals = list() #list that holds all of the times that the last pedestrian escaped in each simulation
for i in range(200):
    new_simulation = Simulation(1, new_room, True)
    ex_1_b(running)
plt.show()
print("The longest time to escape: {} seconds.".format(max(escape_intervals)))
print("The median time to escape: {} ".format(sum(escape_intervals) / len(escape_intervals)))

pygame.quit()

