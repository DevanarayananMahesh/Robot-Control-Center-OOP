from Robot import Robot

class TricksterBot(Robot):

    def __init__(self, name, health, battery, record=[0,0]):

        super().__init__(name, health, battery, record=[0,0])
        self._type = "trickster"

    def choose_move(self, opponent):
        # if self.health < 50:
        #     return ["Heal", self.robot_EFF()]

        # return ["Parry", self.robot_EFF()]

