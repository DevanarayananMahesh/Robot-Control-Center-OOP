import random

name_list = []

class Robot:

# =============================================================================================================
# 
#                                        INIT COMPOSITOR
# 
# =============================================================================================================


    def __init__(self, name, health, battery, record=None):

        self._name = name
        name_list.append(name)
        self.health = health
        self.battery = battery
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
        if 0 <= value <= 100:
            self._battery = value
        else:
            raise ValueError("Battery must be between 0 and 100.")


    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if 0 <= value <= 100:
            self._health = value
        else:
            raise ValueError("Health must be between 0 and 100.")


# =============================================================================================================
# 
#                                        ADD A ROBOT METHOD
# 
# =============================================================================================================


    def add_robot(self, name, health, battery):

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


    def choose_move(self, opponent):

        # HOOK: BATTERY DRAIN (EXPENSIVE)
        # UPPERCUT: HEALTH DRAIN (EXPENSIVE)
        # JAB: HEALTH DRAIN (CHEAP)
        # CROSS: BATTERY DRAIN (CHEAP)

        # PERRY: BLOCK JAB (CHEAP)
        # PERRY: BLOCK CROSS (EXPENSIVE) - health drain more
        # ROLL: EVADE HOOK (MEDIUM)
        # ELBOW COVER: BLOCK UPPERCUT (MEDIUM)
        # DODGE: EVADE ALL (RISKY) - NO DAMAGE IF PERFORMED CLEANLY

        # HEAL : FOCUS FULL ENERGY TO HEALTH (1% BATTERY SACRIFICE per 5 health)

        if self.health < 30:
            efficiency = self.robot_EFF()
            return ["Heal", efficiency]

        elif self.health > 70:
            efficiency = self.robot_EFF()
            return ["Uppercut", efficiency]
        else:
            efficiency = self.robot_EFF()
            return ["Hook", efficiency]


# =============================================================================================================
# 
#                                      PERFORM ROBOT ACTION
# 
# =============================================================================================================   

            
    def perform_move(self, net_move, opponent):

        if net_move[0] == "Heal":
            
            self.health += 5 * net_move[1]
            if net_move[1] in [0, 0.25, 0.5]:
                self.battery -= 0
            else:
                self.battery -= 1

        elif net_move[0] == "Uppercut":

            opponent.health -= (10 * net_move[1])*net_move[2]
            self.battery -= 10 * net_move[1]

        else:

            opponent.health -= 5 * net_move[1]
            self.battery -= 1 * net_move[1]


# =============================================================================================================
# 
#                                      CHECK IF ROBOT IS ALIVE
# 
# ============================================================================================================= 


    def is_alive(self):
        return self.health > 0


# =============================================================================================================
# 
#                                      STRING MAGIC METHOD
# 
# ============================================================================================================= 


    def __str__(self):
        return (
            f"Robot: {self._name} | "
            f"Health: {self._health} | "
            f"Battery: {self._battery} | "
            f"Record: {self._record[0]}-{self._record[1]}"
        )