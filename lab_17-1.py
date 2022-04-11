# Author: ATN 4/11/22

# importing math for later use
import math

# defining the class
class Circle:
    """ Circle class represents a circle """

    # setting the default values for the circle
    def __init__(self):
        """ Create a new circle with radius 1 """
        self.radius = 1


    # area = πr^2
    def get_area(self):
        return (math.pi * (math.sqrt(self.radius)))


# defining my object and calling the functions
my_circle = Circle()
my_circle.radius = 3
print(my_circle.get_area())
