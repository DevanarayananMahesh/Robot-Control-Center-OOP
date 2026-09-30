from Robot import Robot
from InitBattle import Battle


def main():

    fleet = [
        AggressiveRobot("Titan", 100, 100),
        DefensiveRobot("Gibby", 100, 100),
        AggressiveRobot("Crusher", 100, 100)
    ]

    while True:

        print("\n===== ROBOT CONTROL CENTER =====")
        print("1. View Fleet")
        print("2. Check Sensors")
        print("3. Start Battle")
        print("4. Add Robot")
        print("5. Search Robot")
        print("6. Update Robot")
        print("7. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                ...
            elif choice == 2:
                ...
            elif choice == 3:
                ...
            elif choice == 4:
                ...
            elif choice == 5:
                ...
            elif choice == 6:
                ...
            elif choice == 7:
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()