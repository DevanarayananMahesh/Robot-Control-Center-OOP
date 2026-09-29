class Robot:

    def __init__(self, name, battery, ability):

        self._name = name
        abilities_list.append(name)
        self._battery = battery
        self._ability = ability


    def add_robot(self, name, battery):
        # name already exists?
        if name in name_list:
            return f"{name} already exists as a Robot"
        # battery validity 
        if battery > 100 or battery < 0:
            return f"Invalid Battery Level"
        # ability in list
        if ability not in abilities_list:
            return f"{ability} is not valid"
        # valid set to self
        self._name = name
        abilities_list.append(name)
        self._battery = battery
        self._ability = ability


name_list = []
abilities_list = [""]