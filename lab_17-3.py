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


# calling the functions
my_remote = tv_remote()
my_remote.on = True
print(my_remote)
