class Room:
    def __init__(self, room_length, room_width, arr_destination):
        self.room_length = room_length # room length in meters
        self.room_width = room_width # room width in meters
        self.arr_destination = arr_destination # coordinates of the exit [x,y]

    #return the 2D matrix destination of the goal exit point
    def get_dest(self):
        return self.arr_destination

    def get_length(self):
        return self.room_length

    def get_width(self):
        return self.room_width