class Robot:
    """ Represents a Robot, with Name. """
    # A class variable counts the number of robots
    population = 0

    def __init__(self, name):
        """ Initialize the Data """
        self.name = name
        print("(Initialize {})".format(self.name))

        #When this person is created, the robot adds to the population
        Robot.population += 1
    
    def dies(self):
        """ I am dying """
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one. ".format(self.name))
        else:
            print("There are still {:d} Robots working".format(Robot.population))
    
    def say_hi(self):
        """" Greeting by the Robot
         
          Yeah, they can do that. """
        print("Greeting, My masters call me {}.".format(self.name))
 
    @classmethod
    def how_many(cls):
        #Prints the current population 
        print("We have {:d} robots".format(cls.population))   

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print('\nRobots can do somework here. \n')
print("Robots have finished their work, So lets destroy them. ")

droid1.dies()
droid2.dies()

Robot.how_many()

