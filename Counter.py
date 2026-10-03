from Robot import Robot
import random

class CounterFighterBot(Robot):

    def __init__(self, name, health, battery, record=None):

        """
            Initializes a Robot taking from it's Parent class (Robot)
    
            Args:
                name: the name of the bot
                health: the health of the bot
                battery: the battery of the bot
                record: the record of the bot
                
        """

        super().__init__(name, health, battery, record=record)
        self._type = "CounterFighter"



    def choose_move(self, opponent=None):

        """
            Chooses the move, slightly diff to (Robot)

            args:
                opponent: empty attribute defaulted to NONE
        """

        if self.health < 30:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Heal", "Jab"], weights=[90,10], k=1)[0]
            return [move_name, efficiency]

        elif self.health > 70:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Uppercut", "Wait"], weights=random.choice([[50, 50], [60, 40]]), k=1)[0]
            return [move_name, efficiency]
        else:
            efficiency = self.robot_EFF()
            move_name = random.choices(["Hook", "Body Shot"], weights=random.choice([[40, 60], [60, 40]]), k=1)[0]
            return [move_name, efficiency]




    def perform_move(self, move, opponent):
        """
            This method performs the move itself

            args:
                move: a list made up of move name and efficiency
                opponent: the instance storing the characteristics of a robot
        """

        
        if move[0] == "Wait":
            
            opponent.health -=  0
            self.battery -= 0

        elif move[0] == "Uppercut":

            opponent.health -= 7 * move[1]
            self.battery -= 7 * move[1]

        elif move[0] == "Body Shot":

            opponent.health -= 6 * move[1]
            self.battery -= 6 * move[1]

        elif move[0] == "Hook":

            opponent.health -= 9 * move[1]
            self.battery -= 3 * move[1]
    
        elif move[0] == "Jab":

            opponent.health -= 2 * move[1]
            self.battery -= 1 * move[1]

        elif move[0] == "Heal":
        
            self.health += 5 * move[1]
            self.battery -= 3 * move[1]