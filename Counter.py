from Robot import Robot
import random

class CounterFighterBot(Robot):

    def __init__(self, name, health, battery, record=[0,0]):

        super().__init__(name, health, battery, record=[0,0])
        self._type = "counterfighter"

    def choose_move(self, opponent):
        # if self.health < 50:
        #     return ["Heal", self.robot_EFF()]

        # return ["Parry", self.robot_EFF()]
        if self.health > 70:

            if opponent.health > 70:


                
            elif opponent.health < 40:
                # BEAT DOWN
            else:
                # Aggressive testing 
                 
                   
        elif self.health <= 70 and self.health >= 40:

            if opponent.health > 70:
                # DEFENSE 70%
            elif opponent.health < 40:
                # CALCULATED AGGRESSION
            else:
                # RYTHM MATCH

        else:

            if opponent.health > 70:
                # HIGH GUARD RED ALERT
            elif opponent.health < 40:
                # CONSERVATION
            else:
                # STANDOFF/HEAL



    def react_move(self, opponent_move):
        efficiency = self.robot_EFF()

        if opponent_move in ["jab", "cross", "hook", "uppercut"]:

            if efficiency == .25:
                return 0
            elif efficiency == .5:
                return random.choice([0,.25])
            elif efficiency == 1:
                return random.choice([.25,5])
            elif efficiency == 1.5:
                return random.choice([.5,.75])
            elif efficiency == 2:
                return 1
        else:
            return None
        