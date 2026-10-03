import random

name_list = []

class Robot:

    """
    This Class: Robot, is the parent class to 2 other classes. It sets the base methods, which chooses the moves, and performs them.
    """
# =============================================================================================================
# 
#                                        INIT COMPOSITOR
# 
# =============================================================================================================


    def __init__(self, name, health, battery, record=None):
        """
        Initializes a Robot

        Args:
            name: the name of the bot
            health: the health of the bot
            battery: the battery of the bot
            record: the record of the bot
        
        """
        self._name = name
        name_list.append(name)
        self.health = health
        self.battery = battery
        self._type = "RobotNorm"
        self._record = record if record is not None else [0, 0]


# =============================================================================================================
# 
#                                        GETTERS AND SETTERS
# 
# =============================================================================================================


    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = max(0, min(100, value))


    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = max(0, min(100, value))


# =============================================================================================================
# 
#                                        ADD A ROBOT METHOD
# 
# =============================================================================================================


    def add_robot(self, name, health, battery):

        """
            Adds a Robot to the Fleet

            Args:
                name: name of the robot
                health: health of the robot
                battery: battery of the robot
        """
        if name in name_list:
            return f"{name} already exists as a robot"
        if health > 100 or health < 0:
            return f"That is NOT a valid health (must be 0-100)"
        if battery > 100 or battery < 0:
            return f"That is NOT a valid battery level (must be 0-100)"
        
        self._name = name
        name_list.append(name)
        self.health = health
        self.battery = battery
        self._record = [0,0]


# =============================================================================================================
# 
#                                    ROBOT EFFICIENCY CALCULATION
# 
# =============================================================================================================


    def robot_EFF(self):

        """
            Adds efficiency to the robot move's making them more or less harmful

            args:
                self: specific instance of class
        """
        boosters = [.25, .5, 1, 1.5, 2]
        if self.battery > 60:
            if self.battery > 80:
                weights = [5, 5, 10, 30, 50]
            else:
                weights = [5, 10, 10, 50, 25]

        elif self.battery < 40:
            if self.battery > 30:
                weights = [45, 25, 10, 10, 5]
            else:
                weights = [60, 20, 10, 5, 5]    

        else:
            weights = [20, 20, 20, 20, 20]
        return random.choices(boosters, weights=weights, k=1)[0]


# =============================================================================================================
# 
#                                      ROBOT ACTION DECISION
# 
# =============================================================================================================


    def choose_move(self, opponent=None):

        """
            The Logic behind what moves are chosen

            args:
                opponent: empty argument and defaults to NONE
        """
        if self.health < 30:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Heal", "Jab"], weights=random.choice([[90, 10], [70, 30]]), k=1)[0]
            return [move_name, efficiency]

        elif self.health > 70:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Uppercut", "Knee"], weights=random.choice([[90, 10], [70, 30]]), k=1)[0]
            return [move_name, efficiency]
        else:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Hook", "Body Shot"], weights=random.choice([[90, 10], [70, 30]]), k=1)[0]
            return [move_name, efficiency]
        

# =============================================================================================================
# 
#                                      PERFORM ROBOT ACTION
# 
# =============================================================================================================   

            
    def perform_move(self, move, opponent):

        """
            This method performs the move itself

            args:
                move: a list made up of move name and efficiency
                opponent: the instance storing the characteristics of a robot
        """
        if move[0] == "Knee":
            
            opponent.health -= 15 * move[1]
            self.battery -= 10 * move[1]

        elif move[0] == "Uppercut":

            opponent.health -= 10 * move[1]
            self.battery -= 7 * move[1]

        elif move[0] == "Body Shot":

            opponent.health -= 8 * move[1]
            self.battery -= 6 * move[1]

        elif move[0] == "Hook":

            opponent.health -= 5 * move[1]
            self.battery -= 3 * move[1]
    
        elif move[0] == "Jab":

            opponent.health -= 3 * move[1]
            self.battery -= 1 * move[1]

        elif move[0] == "Heal":
        
            self.health += 5 * move[1]
            self.battery -= 3 * move[1]
        


        
# =============================================================================================================
# 
#                                      CHECK IF ROBOT IS ALIVE
# 
# ============================================================================================================= 


    def is_alive(self):
        return self.health > 0

    def is_energized(self):
        return self.battery > 0

# =============================================================================================================
# 
#                                      STRING MAGIC METHOD
# 
# ============================================================================================================= 


    def __str__(self):

        """
        Returns Robot Stats Such as attributes defined in constructor
        """
        return (
            f"Robot: {self._name} | "
            f"Health: {self._health} | "
            f"Battery: {self._battery} | "
            f"Record: {self._record[0]}-{self._record[1]}"
        )