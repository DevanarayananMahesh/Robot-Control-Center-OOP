import time
import random
from Robot import Robot

class Battle:

    def __init__(self, robot1, robot2):

        """
        Initalized Robot1 and Robot2

        args:
            robot1: the instance of the first robot
            robot2: the instance of the second robot
        """
        self._robot1 = robot1
        self._robot2 =robot2


    def output_text(self, robot, robot2, move):

        """
        A method that returns a custom text output that is used to display the robot's moves

        args:
            robot: the first robot instance
            robot2: the second robot instance
            move: the first robot's move
        """
        move_name, efficiency = move[0], move[1]

        if move_name == "Wait":
            return random.choice(
                [
                    f"{robot._name} pauses, analyzing {robot2._name}'s movement.",
                    f"{robot._name} holds position to conserve energy.",
                    f"{robot._name} bides time, waiting for the right opening.",
                ]
            )

        elif move_name == "Heal":
            return random.choice(
                [
                    f"{robot._name} routes power into repairs, stabilizing systems.",
                    f"{robot._name} diverts energy to recover lost durability.",
                    f"{robot._name} patched up minor damage while out of range.",
                ]
            )

        elif move_name == "Jab":
            if efficiency > 1:
                return random.choice(
                    [
                        f"{robot._name} snaps a crisp jab right through {robot2._name}'s guard!",
                        f"A fast, precise jab from {robot._name} strikes true!",
                        f"{robot._name} lands a sharp jab before {robot2._name} can react.",
                    ]
                )
            else:
                return random.choice(
                    [
                        f"{robot._name} pokes out a light jab at {robot2._name}.",
                        f"{robot._name} tests the distance with a quick jab.",
                        f"A tentative jab from {robot._name} lightly taps {robot2._name}.",
                    ]
                )

        if robot._type == "RobotNorm":
            if efficiency > 1:
                return random.choice(
                    [
                        f"BAM! {robot._name} threw a GREAT {move_name}!",
                        f"{robot._name} shows what he can do by throwing an incredible {move_name}!",
                        f"OUCH! {robot._name} violently hit {robot2._name} with a {move_name}!",
                    ]
                )
            elif efficiency == 1:
                return random.choice(
                    [
                        f"{robot._name} threw a decent {move_name}.",
                        f"{robot2._name} is hit by {robot._name}'s {move_name}.",
                        f"{robot._name} makes a solid hit on {robot2._name} with its {move_name}.",
                    ]
                )
            else:  # efficiency < 1
                return random.choice(
                    [
                        f"{robot._name}'s {move_name} JUST barely connects with {robot2._name}.",
                        f"{robot._name} throws a {move_name}, though it did minimal damage.",
                        f"That was sloppy! {robot._name} throws an awkward {move_name} at {robot2._name}.",
                    ]
                )

        elif robot._type == "CounterFighter":
            if efficiency > 1:
                return random.choice(
                    [
                        f"{robot._name} slips the attack and punishes {robot2._name} with a devastating counter {move_name}!",
                        f"A flawless counter! {robot._name} catches {robot2._name} off-guard with a brutal {move_name}!",
                        f"{robot._name} reads {robot2._name} like a book and answers with a pinpoint {move_name}!",
                    ]
                )
            elif efficiency == 1:
                return random.choice(
                    [
                        f"{robot._name} times {robot2._name}'s movement and connects with a sleek {move_name}.",
                        f"{robot._name} finds an opening and drives home a sharp counter {move_name}.",
                        f"{robot._name} capitalizes on {robot2._name}'s mistiming with a solid {move_name}.",
                    ]
                )
            else:  # efficiency < 1
                return random.choice(
                    [
                        f"{robot._name} tries to counter-strike, but the {move_name} barely grazes {robot2._name}.",
                        f"{robot._name} miscalculated the timing, landing a weak counter {move_name}.",
                        f"{robot2._name} partially blocked {robot._name}'s counter {move_name}.",
                    ]
                )

        elif robot._type == "Berserker":
            if efficiency > 1:
                return random.choice(
                    [
                        f"{robot._name} surges forward in a flurry, crashing a heavy {move_name} into {robot2._name}!",
                        f"Relentless pressure! {robot._name} smashes {robot2._name} with a furious {move_name}!",
                        f"{robot._name} smothers {robot2._name}'s space and drives a explosive {move_name} home!",
                    ]
                )
            elif efficiency == 1:
                return random.choice(
                    [
                        f"{robot._name} stays in {robot2._name}'s face and lands a rapid {move_name}.",
                        f"{robot._name} presses the action, connecting with a quick {move_name}.",
                        f"Continuing the assault, {robot._name} tags {robot2._name} with a {move_name}.",
                    ]
                )
            else:  # efficiency < 1
                return random.choice(
                    [
                        f"{robot._name} rushes in wildly, but the {move_name} lacks power.",
                        f"{robot2._name} absorbs the momentum as {robot._name}'s rushed {move_name} lands lightly.",
                        f"{robot._name} smothers their own strike, delivering an off-balance {move_name}.",
                    ]
                )

    def start(self):
        """
        Initializes battle between 2 robots

        args:
            self: creates an instance
        """
        round_turn = 0
        while self._robot1.is_alive() and self._robot2.is_alive() and self._robot1.is_energized() and self._robot2.is_energized() and round_turn <= 50:


# =============================================================================================================
# 
#                                           ROBOT 1 TURN
# 
# ============================================================================================================= 


            move = self._robot1.choose_move(self._robot2)
            self._robot1.perform_move(move, self._robot2)
            
            text_output = self.output_text(self._robot1, self._robot2, move)

            print(text_output)
            print(f"{self._robot2._name} has {self._robot2.health} health")
            print(f"\n")

            
            if not self._robot2.is_alive():
                break
            
            time.sleep(1.3) 

            round_turn += 1
# =============================================================================================================
# 
#                                           ROBOT 2 TURN
# 
# ============================================================================================================= 


            move = self._robot2.choose_move(self._robot1)
            self._robot2.perform_move(move, self._robot1)

            text_output = self.output_text(self._robot2, self._robot1, move)

            print(text_output)
            print(f"{self._robot1._name} has {self._robot1.health} health")
            print(f"\n")

            time.sleep(1.3) 
        

            round_turn += 1

        if self._robot1.is_alive() and self._robot1.is_energized() or round_turn > 50:
            print(self._robot1._name, "wins!")
            print("Possible reasons include:\nRound Limits, Energy Drain, and Health loss")
            self._robot1._record[0]+=1
            self._robot2._record[1]+=1
        else:
            print(self._robot2._name, "wins!")
            print("Possible reasons include:\nRound Limits, Energy Drain, and Health loss")
            self._robot2._record[0]+=1
            self._robot1._record[1]+=1
            