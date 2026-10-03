from Robot import Robot
from InitBattle import Battle
from Counter import CounterFighterBot
from Berserker import Berserker


def main():
    roster = [
        Robot("Big Woof", 100, 100),
        Berserker("Titan", 100, 100),
        CounterFighterBot("Gibby", 100, 100)
    ]

    print("""

====== ROBOT FIGHT CLUB TERMINAL ======

1) View Robot Fleet
2) View Robot Rankings
3) Initiate a Battle
4) Add Robot
5) View Robot Data
6) Exit

    """)


    while True:
        userAction = input("Choose something to do: (choices 1 to 6) ")

        while not userAction.isdigit():
            print("Please choose a number from 1 - 5\n")
            userAction = input("Choose something to do: (choices 1 to 6) ")

# =============================================================================================================
# 
#                                           CHOICE 1
# 
# =============================================================================================================         
        
        if int(userAction) == 1:

            print("\n--- ROBOT FLEET ---")
            for i, robot in enumerate(roster, 1):
                print(f"{i}. {robot}")
            print()

# =============================================================================================================
# 
#                                           CHOICE 2
# 
# ============================================================================================================= 


        elif int(userAction) == 2:

            print("\n--- ROBOT RANKINGS (BY WINS) ---")
            
            sorted_roster = sorted(
                roster, key=lambda bot: bot._record[0], reverse=True
            )
            for rank, bot in enumerate(sorted_roster, 1):
                wins, losses = bot._record[0], bot._record[1]
                print(
                    f"Rank {rank}: {bot._name} ({bot._type}) | Wins: {wins} - Losses: {losses}"
                )
            print()


# =============================================================================================================
# 
#                                           CHOICE 3
# 
# ============================================================================================================= 


        elif int(userAction) == 3:

            if len(roster) < 2:
                print("\nNot enough robots to battle! Add more robots first.\n")
                continue

            print("\n--- SELECT FIGHTERS ---")
            for idx, bot in enumerate(roster, 1):
                print(f"{idx}. {bot._name} ({bot._type})")

            # Get Robot 1 safely
            while True:
                r1_input = input("\nSelect Robot 1 (#): ").strip()
                if r1_input.isdigit():
                    r1_idx = int(r1_input) - 1
                    if 0 <= r1_idx < len(roster):
                        break
                print("Invalid selection. Please enter a valid robot number.")

            # Get Robot 2 safely
            while True:
                r2_input = input("Select Robot 2 (#): ").strip()
                if r2_input.isdigit():
                    r2_idx = int(r2_input) - 1
                    if r2_idx == r1_idx:
                        print("A robot cannot fight itself! Choose a different robot.")
                    elif 0 <= r2_idx < len(roster):
                        break
                    else:
                        print("Invalid selection. Please enter a valid robot number.")
                else:
                    print("Invalid input. Please enter a valid robot number.")

            # Reset health & energy before fight starts
            robot1, robot2 = roster[r1_idx], roster[r2_idx]
            robot1.health, robot1.battery = 100, 100
            robot2.health, robot2.battery = 100, 100

            print(f"\nSTARTING BATTLE: {robot1._name} vs {robot2._name}\n")
            battle = Battle(robot1, robot2)
            battle.start()


# =============================================================================================================
# 
#                                           CHOICE 4
# 
# ============================================================================================================= 


        elif int(userAction) == 4:

            print("\n--- ADD A NEW ROBOT ---")
            name = input("Enter Robot Name: ").strip()

            print("Select Archetype:")
            print("1) Standard (RobotNorm)")
            print("2) Counter Fighter")
            print("3) Berserker")
            archetype = input("Choice (1-3): ").strip()

            if archetype == "2":
                new_bot = CounterFighterBot(name, 100, 100)
            elif archetype == "3":
                new_bot = Berserker(name, 100, 100)
            else:
                new_bot = Robot(name, 100, 100)

            roster.append(new_bot)
            print(f"\nSuccessfully added {name} ({new_bot._type}) to the fleet!\n")


# =============================================================================================================
# 
#                                           CHOICE 5
# 
# ============================================================================================================= 



        elif int(userAction) == 5:

            print("\n--- SELECT A ROBOT TO INSPECT ---")
            for idx, bot in enumerate(roster, 1):
                print(f"{idx}. {bot._name}")

            bot_idx = int(input("\nSelect Robot (#): ")) - 1
            if 0 <= bot_idx < len(roster):
                bot = roster[bot_idx]
                print(f"\n=== DATA SHEET: {bot._name} ===")
                print(f"Type:    {bot._type}")
                print(f"Health:  {bot.health}/100")
                print(f"Battery: {bot.battery}/100")
                print(f"Record:  {bot._record[0]} Wins - {bot._record[1]} Losses\n")
            else:
                print("Invalid robot index!\n")


# =============================================================================================================
# 
#                                           CHOICE 6
# 
# ============================================================================================================= 


        elif int(userAction) == 6:
            print("\nExiting Robot Fight Club Terminal. Goodbye!")
            break


if __name__ == "__main__":
    main()