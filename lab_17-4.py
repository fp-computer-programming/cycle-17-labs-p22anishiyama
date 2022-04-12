# Author: ATN 4/12/22

# defining the class
class tv_remote:

    # setting the default values
    def __init__(self, channel=0, volume_level=0, on=False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    
    # adding the conditions for the information to print
    def __str__(self):
        if self.on == True:
            return "You are watching channel {0} at {1}% volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."


    # defining many functions for various uses
    def turn_on(self):
        self.on = True
    

    def turn_off(self):
        self.on = False
    

    def volume_up(self, value):
        self.volume_level += value
    

    def volume_down(self, value):
        self.volume_level -= value
    

    def channel_up(self, value):
        self.channel += value
    

    def channel_down(self, value):
        self.channel -= value
    

# calling the functions
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.volume_up(2)
my_remote.volume_down(1)
my_remote.channel_up(6)
my_remote.channel_down(2)
my_remote.turn_on()
print(my_remote)
