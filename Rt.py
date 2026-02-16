



class Robot:

    
    def __init__(self, name, color, purpose):
        self.name = name
        self.color = color
        self.purpose = purpose

    
    def introduce(self):
        print("Hello! My name is", self.name)
        print("My color is", self.color)
        print("My purpose is to", self.purpose)




print("Create Your Robot")

name = input("Enter robot name: ")
color = input("Enter robot color: ")
purpose = input("Enter robot purpose: ")


my_robot = Robot(name, color, purpose)

print("\nRobot Introduction:")
my_robot.introduce()

