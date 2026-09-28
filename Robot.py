class Robot:

    robot_fleet = {}

    def __init__(self, name, battery, weapons, weight_class):
        self._name = name
        self._battery = battery
        self._weapons = weapons
        self._weight_class = weight_class

        Robot.robot_fleet[self._name] = [self._battery, self._weapons, self._weight_class]



    def add_robot(self, name, battery, weapons, weight_class):

        self._name = name
        
        if battery > 100 or battery < 0:
            return f"{battery} is not a valid battery level"
        else:
            self._battery = battery

        self._weapons = weapons

        if weight_class.strip().lower() not in ["flyweight", "lightweight", "welterweight", "heavyweight"]:
            return f"{weight_class} is not a valid weight class"
        else:
            self._weight_class = weight_class

        Robot.robot_fleet[self._name] = [self._battery, self._weapons, self._weight_class]



    def init_battle(self, opponent):
        if opponent[1] < 20:
            return f"{opponent[0]} does not have enough battery to fight"
        elif self._battery < 20:
            return f"{self._battery} does not have enough battery to fight"

        print(f"{self._name} goes first!")
        
        while self._battery >= 20 or opponent[1] >= 20:

            
            

def main():
    robot1 = Robot("Joh", 13, "Phone", 100)
    print(Robot.robot_fleet)

main()
