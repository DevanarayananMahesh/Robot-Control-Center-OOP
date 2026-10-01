import time
from Robot import Robot

class Battle:

    def __init__(self, robot1, robot2):
        self._robot1 = robot1
        self._robot2 =robot2


    def net_result_(self, move, reaction):

        if reaction in [0, .25, .5, .75, 1]:
            return [move[0], move[1], reaction]

    def start(self):

        while self._robot1.is_alive() and self._robot2.is_alive():


# =============================================================================================================
# 
#                                           ROBOT 1 TURN
# 
# ============================================================================================================= 


            move = self._robot1.choose_move(self._robot2)
            reaction = self._robot2.react_move(move)

            net_result = self.net_result_(move, reaction)

            print(f"{self._robot1._name} uses {move[0]}")
            print(self._robot1._name, "has", self._robot1._health, "health")
            print(f"\n")

            self._robot1.perform_move(net_result, self._robot2)

            if not self._robot2.is_alive():
                break
            
            time.sleep(1.3) 

# =============================================================================================================
# 
#                                           ROBOT 2 TURN
# 
# ============================================================================================================= 


            move = self._robot2.choose_move(self._robot1)
            reaction = self._robot1.react_move(move)

            net_result = self.net_result_(move, reaction)

            
            print(self._robot2._name, "uses", move[0])
            print(self._robot2._name, "has", self._robot2._health, "health")
            print(f"\n")

            self._robot2.perform_move(net_result, self._robot1)

            time.sleep(1.3) 
        


        if self._robot1.is_alive():
            print(self._robot1._name, "wins!")
            self._robot1._record[0]+=1
            self._robot2._record[1]+=1
        else:
            print(self._robot2._name, "wins!")
            self._robot2._record[0]+=1
            self._robot1._record[1]+=1
            