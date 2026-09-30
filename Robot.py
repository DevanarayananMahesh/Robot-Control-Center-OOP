import random

name_list = []
class Robot:

    def __init__(self, name, health, battery, record=[0,0]):

        self._name = name
        name_list.append(name)
        self._health = health
        self._battery = battery
        self._record = record

    def add_robot(self, name, health, battery):

        if name in name_list:
            return f"{name} already exists as a robot"
        if health > 100 or health < 0:
            return f"That is NOT a valid health (must be 0-100)"
        if battery > 100 or battery < 0:
            return f"That is NOT a valid battery level (must be 0-100)"
        
        self._health = health
        self._battery = battery
        self._record = [0,0]


    def robotBooster(self):
        boosters = [.25, .5, 1, 1.5, 2]
        if self._battery > 60:
            if self._battery > 80:
                weights = [5, 5, 10, 30, 50]
            else:
                weights = [5, 10, 10, 50, 25]

        elif self._battery < 40:
            if self._battery > 30:
                weights = [45, 25, 10, 10, 5]
            else:
                weights = [60, 20, 10, 5, 5]    

        else:
            weights = [20, 20, 20, 20, 20]
        return random.choices(boosters, weights=weights, k=1)[0]

    
    def move(self, opponent, self_):
        if self_[1] < 30:
            efficiency = self.robotBooster()
            if opponent[1] < 10:
                return "Uppercut", efficiency
            else:
                return "Heal", efficiency

        elif self_[1] > 65:
            efficiency = self.robotBooster()

            if opponent[1] > self_[1]:

                if opponent[2] >= self_[2]:

                    return "Hook", efficiency

                else:

                    return "Uppercut", efficiency

            return "Heal", efficiency
